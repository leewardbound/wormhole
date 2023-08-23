import graphene

from wormhole.apps.indexer import models
from wormhole.apps.indexer.filters import ProposalFilterSet, ProposalVoteFilterSet
from wormhole.apps.indexer.schema import types
from wormhole.utils.graphql import FilterInput, define_query


class Queries(object):
    @define_query(graphene.List(types.Proposal, filters=graphene.Argument(FilterInput(ProposalFilterSet))))
    def proposals(self, info, filters=None):
        return ProposalFilterSet(filters, models.Proposal.objects.all()).qs

    @define_query(graphene.List(types.ProposalVote, filters=graphene.Argument(FilterInput(ProposalVoteFilterSet))))
    def votes(self, info, filters=None):
        return ProposalVoteFilterSet(filters, models.ProposalVote.objects.all()).qs
