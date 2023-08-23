from graphene_django import DjangoObjectType

from wormhole.apps.indexer import models


class Proposal(DjangoObjectType):
    class Meta:
        model = models.Proposal
        # All fields by default


class ProposalVote(DjangoObjectType):
    class Meta:
        model = models.ProposalVote
        # All fields by default
