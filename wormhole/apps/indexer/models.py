import json
from datetime import datetime

import pytz
from django.db import models

from wormhole.utils.models import MediumIDMixin, TimestampMixin, UUIDMixin


class Proposal(TimestampMixin, MediumIDMixin):
    """Proposal model for indexed proposals on the blockchain."""

    contract_address = models.CharField(
        max_length=42, db_index=True
    )  # This is probably redundant but good to store it incase we add more contracts someday
    from_tx_hash = models.CharField(max_length=66)
    block_number = models.PositiveIntegerField()
    block_timestamp = models.DateTimeField()

    proposal_id = models.PositiveIntegerField(db_index=True)
    description = models.TextField()
    proposer = models.CharField(max_length=42, db_index=True)
    start_block = models.PositiveIntegerField(db_index=True)
    end_block = models.PositiveIntegerField(db_index=True)

    original_event_data = models.JSONField()

    def __str__(self):
        return f"Proposal #{self.proposal_id} @ {self.contract_address}"

    @classmethod
    def from_tx(cls, tx):
        """Create a Proposal from a transaction. Raises KeyError on malformed tx data."""
        return cls(
            contract_address=tx["address"],
            from_tx_hash=tx["transactionHash"],
            block_number=tx["blockNumber"],
            block_timestamp=datetime.utcfromtimestamp(tx["timestamp"]).astimezone(pytz.UTC),
            proposal_id=tx["event"]["id"],
            description=tx["event"]["description"],
            proposer=tx["event"]["proposer"],
            start_block=tx["event"]["startBlock"],
            end_block=tx["event"]["endBlock"],
            original_event_data=tx["event"],
        )

    @classmethod
    def initialize(cls, initialize_votes=False):
        """Initialize the proposal table with all proposals from the blockchain."""
        for tx in json.loads(open("fixtures/proposals.json").read()):
            try:
                instance = cls.from_tx(tx)
                instance.save()
                print("Created Proposal # ", instance.proposal_id)
            except KeyError:
                print("Skipping malformed Proposal tx: ", tx)
            except Exception as e:
                print("Skipping Proposal tx: ", tx, " due to error: ", e)
        if initialize_votes:
            ProposalVote.initialize()

    @classmethod
    def clean_initialize(cls):
        cls.objects.all().delete()
        cls.initialize(initialize_votes=True)


class ProposalVote(TimestampMixin, UUIDMixin):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name="votes")

    from_tx_hash = models.CharField(max_length=66)
    block_number = models.PositiveIntegerField()
    block_timestamp = models.DateTimeField()

    reason = models.TextField()
    support = models.IntegerField(
        db_index=True
    )  # TODO: I was surprised to get some "2" values here - I assumed this was 1-or-0... need to read docs!
    voter = models.CharField(max_length=42, db_index=True)
    votes = (
        models.PositiveIntegerField()
    )  # TODO:  I'm not entirely clear what this is - "votes by this voter" perhaps? I should clarify with Worm

    original_event_data = models.JSONField()

    @classmethod
    def from_tx(cls, tx):
        """Create a ProposalVote from a transaction.
        Raises KeyError on malformed tx data.
        Raises Proposal.DoesNotExist if the proposal does not exist.
        """
        return cls(
            proposal=Proposal.objects.get(proposal_id=tx["event"]["proposalId"], contract_address=tx["address"]),
            from_tx_hash=tx["transactionHash"],
            block_number=tx["blockNumber"],
            block_timestamp=datetime.utcfromtimestamp(tx["timestamp"]).astimezone(pytz.UTC),
            reason=tx["event"]["reason"],
            support=tx["event"]["support"],
            voter=tx["event"]["voter"],
            votes=tx["event"]["votes"],
            original_event_data=tx["event"],
        )

    @classmethod
    def initialize(cls):
        """Initialize the proposal vote table with all proposal votes from the blockchain."""
        for tx in json.loads(open("fixtures/votes.json").read()):
            try:
                instance = cls.from_tx(tx)
                instance.save()
                print("Created ProposalVote # ", instance.id)
            except KeyError:
                print("Skipping malformed ProposalVote tx: ", tx)
            except Proposal.DoesNotExist:
                print("Skipping ProposalVote tx: ", tx, " because the Proposal does not exist")
            except Exception as e:
                print("Skipping ProposalVote tx: ", tx, " due to error: ", e)
