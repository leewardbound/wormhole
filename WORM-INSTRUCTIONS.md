## mint.fun backend API take home assignment

### Background

At mint.fun, just about everything you see on the site comes from onchain activity. Anyone who has built anything serious that uses onchain data has had experience building an indexer. For this project, you'll build a backend presents onchain data over an API.

### Nouns

[Nouns](https://nouns.wtf) is an on chain DAO that uses modified contracts from Compound Labs for governance and voting. Nouns NFT holders can vote on [proposals](https://nouns.wtf/vote). All governance for Nouns, including proposal submission and voting, happens on chain.

[`0x6f3E62`](https://etherscan.io/address/0x6f3e6272a167e8accb32072d08e0957f9c79223d) is the primary contract where governance occurs. You can read the [Solidity code](https://github.com/nounsDAO/nouns-monorepo/blob/d91eaefb6a7780dc0c9c2ab70d096a85caee0152/packages/nouns-contracts/contracts/governance/NounsDAOLogicV2.sol) for this contract here. Here's the [ABI](https://github.com/nounsDAO/nouns-monorepo/blob/d91eaefb6a7780dc0c9c2ab70d096a85caee0152/packages/nouns-contracts/abi/contracts/governance/NounsDAOLogicV2.sol/NounsDAOLogicV2.json).

### The API you'll build

We'd like you to build an API that returns information about votes that are submitted onchain. When a vote is cast, the [`VoteCast`](https://github.com/nounsDAO/nouns-monorepo/blob/d91eaefb6a7780dc0c9c2ab70d096a85caee0152/packages/nouns-contracts/contracts/governance/NounsDAOInterfaces.sol#L70) event is emitted ([example tx](https://etherscan.io/tx/0xb2ace4b9dba024e83bb9e98ff495d33f6bf2aba9b8a3290376f62571dead97dc#eventlog)). When a proposal is created, the [`ProposalCreated`](https://github.com/nounsDAO/nouns-monorepo/blob/d91eaefb6a7780dc0c9c2ab70d096a85caee0152/packages/nouns-contracts/contracts/governance/NounsDAOInterfaces.sol#L37-L47) event is emitted ([example tx](https://etherscan.io/tx/0xcf1387a5404a8ca9cc5525c1d229d3be87754b1131784757f39b635c86ed797a#eventlog)).

Attached to this gist are two files, `votes.json` and `proposals.json`. These files contain data obtained from the logs for Proposals #197 and #198 – all of the relevant `VoteCast` and `ProposalCreated` events. You can use this data to build the API.

For this API, we'd like a way to:
* query votes for a proposal
* query votes by a voting address
* query a list of indexed proposals
* anything else you think is interesting, time permitting

Hopefully, in doing this, we'd see:

* ability to write code that parses Ethereum logs (events)
* usage of some database or data store for events
* a simple, but sensible API to query the data

Absent from the above list is any discussion of specific technologies or programming languages. We recommend using tools you're most familiar with and think will get the job done most effectively. Use Typescript, Go, Rust, Postgres, MongoDB, GraphQL, REST, or anything else. No matter what you choose, we'll probably be curious why you chose it - so be prepared to chat about that.

## Pay & deliverables

We'll invite you to a private GitHub repo. Please push your implementation there and let us know when you're ready for us to review it. If you have it deployed to a URL somewhere, that would be awesome too. We'll take a look and ask more questions during your onsite interview.

We recommend budgeting about 5-6 hours of time for this task. Do not work more than 10 hours on this task. We will pay $590 regardless of how long it takes you to complete the task. Please include USDC payment address or PayPal information when you submit your code.