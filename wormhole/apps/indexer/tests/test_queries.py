def test_list_proposals_query(project_fixture_common):
    result = project_fixture_common.query("query { proposals { proposalId }}")
    assert result["data"]["proposals"][0]["proposalId"] == 197
    assert result["data"]["proposals"][1]["proposalId"] == 198


def test_proposal_with_votes_query(project_fixture_common):
    result = project_fixture_common.query('query { proposals(filters: {proposalId: "197"}) { votes { support }}}')
    proposals = result["data"]["proposals"]
    assert len(proposals) == 1, "Should only get one proposal because of filtering"
    votes = proposals[0]["votes"]
    assert len(votes) == 34, "Proposal 197 should have 34 votes"
    assert votes[0]["support"] == 1, "First vote should be in support of proposal 197"

    # Sum up the votes quickly
    totals = {support: len([v for v in votes if v["support"] == support]) for support in [0, 1, 2]}
    assert totals[0] == 2, "Proposal 197 should have 2 votes against"
    assert totals[1] == 30, "Proposal 197 should have 30 votes for"
    assert totals[2] == 2, "Proposal 197 should have 12 abstentions"


def test_votes_by_address(project_fixture_common):
    result = project_fixture_common.query(
        'query { votes(filters: {voter: "0x008c84421dA5527F462886cEc43D2717B686A7e4"}) { support proposal { proposalId }}}'
    )
    proposals = result["data"]["votes"]
    assert len(proposals) == 2
    assert proposals[0]["proposal"]["proposalId"] == 197
    assert proposals[0]["support"] == 1
    assert proposals[1]["proposal"]["proposalId"] == 198
    assert proposals[1]["support"] == 0
