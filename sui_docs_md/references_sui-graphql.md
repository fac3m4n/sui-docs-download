:::info

:::

GraphQL for the Sui RPC is a public service that enables interacting with the Sui [network](https://sui.io/networkinfo).

To get started with GraphQL for the Sui RPC, check out the [Getting Started](/concepts/data-access/graphql-rpc) guide. If you'd like to learn more about the concepts used in the GraphQL service, check out the [GraphQL](/concepts/data-access/graphql-rpc.md) for Sui RPC concepts page. If you'd like to view the reference documentation, check out the [schema](./sui-api/sui-graphql/beta/reference).

:::info

:::

## Key types

All GraphQL API elements are accessible via the left sidebar, the following are good starting points to explore from.

- "Queries" lists all top-level queries for reading the chain state, from reading details about addresses and objects to dryRunTransactionBlock, which has an execution-like interface but does not modify the chain.
- Object is the type representing all on-chain objects (Move values and packages).
- Address corresponds to account addresses (derived from the public keys of signatures that sign transactions) and can be used to query the objects owned by these accounts and the transactions they have signed or been affected by.
Owner represents any entity that can own a MoveObject to handle cases where it is not known whether the owner is an Object or an Address (for example, from the perspective of a Move object looking at its owner).

## Related links