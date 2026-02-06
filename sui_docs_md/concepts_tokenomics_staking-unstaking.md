Sui uses a delegated proof of stake (DPoS) [consensus mechanism](/concepts/sui-architecture/consensus.md) to secure and operate the network, meaning that the voting power of a [validator](/guides/operator/validator-index.md) in the network is determined by the amount of stake delegated to them by SUI token holders. The more stake delegated to a validator, the more voting power they have. In exchange for processing transactions and providing resources to the network, validators earn rewards based on the amount of gas fees collected. These rewards are then shared among stakers as [staking rewards](/guides/operator/validator/validator-rewards.md).

## Staking

Stake SUI tokens by sending a transaction to the network that calls the staking function implemented as part of the system Move package. This transaction wraps the SUI tokens in a self-custodial stake [object](/guides/developer/objects/object-model.md). This stake object contains information including the validator staking pool ID and the activation [epoch](/concepts/sui-architecture/epochs.md) of the stake. With the introduction of [SIP-6](https://blog.sui.io/liquid-staking-coming-sui/), you can participate in liquid staking protocols using your staked objects.

[Sui-compatible crypto wallets](https://slush.app/) typically have functionality to initiate staking and unstaking from your Sui address. See the respective documentation for these tools to begin staking your SUI.

## Unstaking

Similar to staking, a user withdraws stake from a validator by sending a transaction that calls the unstaking function in the system Move package. This transaction unwraps the stake object, and sends both the principal and the accumulated rewards to the user as SUI tokens. You accrue rewards only during epochs where the stake is active for the entire epoch. The rewards withdrawn from the validator's rewards pool are calculated based on the activation epoch and unstaking epoch of the stake.

## Choosing a validator for staking

You must choose a specific validator you would like to stake your SUI in. The choice of validator can potentially impact the amount of staking rewards you receive. The factors determining this amount include, but are not limited to:

- **Validator commission rate**: A validator can choose to set a non-zero commission rate specifying the percentage of staking rewards they are taking from the stakers. For example, if a validator has a commission rate of 10%, then 10% of every staker's staking rewards is given to the validator. 

:::caution 

A validator can choose its commission at a future moment in time without prior notice.

:::

- **Validator performance**: A validator with bad performance might be punished according to the [tallying rule](/concepts/tokenomics/gas-in-sui.md#tallying-rule). Punished validators do not receive any staking rewards for the epoch during which they are punished, and you also do not receive that epoch's rewards when you withdraw your stake from that validator.

Sui-compatible crypto wallets and [explorers](https://suiscan.xyz/mainnet/home) typically provide validator information such as commission and APY. See the respective documentation for these tools for information on how to retrieve this data.