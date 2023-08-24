def test_basic_projects_fixture(project_fixture_common):
    from wormhole.apps.indexer.models import Proposal, ProposalVote

    assert Proposal.objects.all().count() == 2, "There should be 2 proposals from proposals.json"
    assert ProposalVote.objects.all().count() == 88, "There should be 88 votes from votes.json"
