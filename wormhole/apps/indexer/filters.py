import django_filters

from . import models


class ProposalFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.Proposal
        fields = {
            "contract_address": ["exact"],
            "from_tx_hash": ["exact"],
            "block_number": ["exact", "lte", "gte"],
            "block_timestamp": ["exact", "lte", "gte"],
            "proposal_id": ["exact"],
            "description": ["exact", "icontains"],
            "proposer": ["exact"],
            "start_block": ["exact", "lte", "gte"],
            "end_block": ["exact", "lte", "gte"],
        }


class ProposalVoteFilterSet(django_filters.FilterSet):
    class Meta:
        model = models.ProposalVote
        fields = {
            "proposal__proposal_id": ["exact"],
            "voter": ["exact"],
            "support": ["exact"],
        }
