# type: ignore
from django.contrib.admin import ModelAdmin, TabularInline

from wormhole.utils.admin import register

from . import models


@register(models.ProposalVote)
class ProposalVoteAdmin(ModelAdmin):
    list_display = [
        "from_tx_hash",
        "proposal",
        "block_number",
        "block_timestamp",
        "voter",
        "support",
    ]
    list_filter = [
        "voter",
    ]


class InlineProposalVote(TabularInline):
    model = models.ProposalVote
    extra = 0
    show_change_link = True
    fields = [
        "from_tx_hash",
        "block_number",
        "block_timestamp",
        "voter",
        "support",
    ]


@register(models.Proposal)
class ProposalAdmin(ModelAdmin):
    list_display = [
        "proposal_id",
        "description",
        "proposer",
        "start_block",
        "end_block",
    ]
    list_filter = [
        "proposer",
    ]

    inlines = [
        InlineProposalVote,
    ]
