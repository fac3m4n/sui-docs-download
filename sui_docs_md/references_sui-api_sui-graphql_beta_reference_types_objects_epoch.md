export const Bullet = () => <>&nbsp;●&nbsp;</>

export const SpecifiedBy = (props) => <>Specification⎘</>

export const Badge = (props) => <>{props.text}</>

export const Details = ({ dataOpen, dataClose, children, startOpen = false }) => {
  const [open, setOpen] = useState(startOpen);
  return (
    
      <summary
        onClick={(e) => {
          e.preventDefault();
          setOpen((open) => !open);
        }}
        style={{ listStyle:'none' }}
      >
      {open ? dataOpen : dataClose}
      </summary>
      {open && children}
    
  );
};

Activity on Sui is partitioned in time, into epochs.

Epoch changes are opportunities for the network to reconfigure itself (perform protocol or system package upgrades, or change the committee) and distribute staking rewards. The network aims to keep epochs roughly the same duration as each other.

During a particular epoch the following data is fixed:

- protocol version,
- reference gas price,
- system package versions,
- validators in the committee.

```graphql
type Epoch implements Node {
  checkpoints(
    first: Int
    after: String
    last: Int
    before: String
    filter: CheckpointFilter
  ): CheckpointConnection
  coinDenyList: Object
  endTimestamp: DateTime
  epochId: UInt53!
  fundInflow: BigInt
  fundOutflow: BigInt
  fundSize: BigInt
  id: ID!
  liveObjectSetDigest: String
  netInflow: BigInt
  protocolConfigs: ProtocolConfigs
  referenceGasPrice: BigInt
  startTimestamp: DateTime
  systemPackages(
    first: Int
    after: String
    last: Int
    before: String
  ): MovePackageConnection
  systemState: MoveValue
  totalCheckpoints: UInt53
  totalGasFees: BigInt
  totalStakeRewards: BigInt
  totalStakeSubsidies: BigInt
  totalTransactions: UInt53
  transactions(
    first: Int
    after: String
    last: Int
    before: String
    filter: TransactionFilter
  ): TransactionConnection
  validatorSet: ValidatorSet
}
```

### Fields

#### [Epoch.<b>checkpoints</b>](#)[<b>CheckpointConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-connection.md)  
The epoch's corresponding checkpoints.
##### [Epoch.checkpoints.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.checkpoints.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Epoch.checkpoints.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.checkpoints.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Epoch.checkpoints.<b>filter</b>](#)[<b>CheckpointFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/checkpoint-filter.md)  

#### [Epoch.<b>coinDenyList</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
State of the Coin DenyList object (0x403) at the start of this epoch.

The DenyList controls access to Regulated Coins. Writes to the DenyList are accumulated and only take effect on the next epoch boundary. Consequently, it's possible to determine the state of the DenyList for a transaction by reading it at the start of the epoch the transaction is in.

#### [Epoch.<b>endTimestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
The timestamp associated with the last checkpoint in the epoch (or `null` if the epoch has not finished yet).

#### [Epoch.<b>epochId</b>](#)[<b>UInt53!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)   
The epoch's id as a sequence number that starts at 0 and is incremented by one at every epoch change.

#### [Epoch.<b>fundInflow</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The storage fees paid for transactions executed during the epoch (or `null` if the epoch has not finished yet).

#### [Epoch.<b>fundOutflow</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The storage fee rebates paid to users who deleted the data associated with past transactions (or `null` if the epoch has not finished yet).

#### [Epoch.<b>fundSize</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The storage fund available in this epoch (or `null` if the epoch has not finished yet).
This fund is used to redistribute storage fees from past transactions to future validators.

#### [Epoch.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The epoch's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [Epoch.<b>liveObjectSetDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A commitment by the committee at the end of epoch on the contents of the live object set at that time.
This can be used to verify state snapshots.

#### [Epoch.<b>netInflow</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The difference between the fund inflow and outflow, representing the net amount of storage fees accumulated in this epoch (or `null` if the epoch has not finished yet).

#### [Epoch.<b>protocolConfigs</b>](#)[<b>ProtocolConfigs</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)  
The epoch's corresponding protocol configuration, including the feature flags and the configuration options.

#### [Epoch.<b>referenceGasPrice</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The minimum gas price that a quorum of validators are guaranteed to sign a transaction for in this epoch.

#### [Epoch.<b>startTimestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
The timestamp associated with the first checkpoint in the epoch.

#### [Epoch.<b>systemPackages</b>](#)[<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  
The system packages used by all transactions in this epoch.
##### [Epoch.systemPackages.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.systemPackages.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Epoch.systemPackages.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.systemPackages.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [Epoch.<b>systemState</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The contents of the system state inner object at the start of this epoch.

#### [Epoch.<b>totalCheckpoints</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The total number of checkpoints in this epoch.

Returns `None` when no checkpoint is set in scope (e.g. execution scope).

#### [Epoch.<b>totalGasFees</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The total amount of gas fees (in MIST) that were paid in this epoch (or `null` if the epoch has not finished yet).

#### [Epoch.<b>totalStakeRewards</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The total MIST rewarded as stake (or `null` if the epoch has not finished yet).

#### [Epoch.<b>totalStakeSubsidies</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The amount added to total gas fees to make up the total stake rewards (or `null` if the epoch has not finished yet).

#### [Epoch.<b>totalTransactions</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The total number of transaction blocks in this epoch.

If the epoch has not finished yet, this number is computed based on the number of transactions at the latest known checkpoint.

#### [Epoch.<b>transactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions in this epoch, optionally filtered by transaction filters.

Returns `None` when no checkpoint is set in scope (e.g. execution scope).
##### [Epoch.transactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.transactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Epoch.transactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Epoch.transactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Epoch.transactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [Epoch.<b>validatorSet</b>](#)[<b>ValidatorSet</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-set.md)  
Validator-related properties, including the active validators.

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

### Returned By

[`epoch`](/references/sui-api/sui-graphql/beta/reference/operations/queries/epoch.md)  [`multiGetEpochs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-epochs.md)  

### Member Of

[`ActiveJwk`](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk.md)  [`AuthenticatorStateExpireTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-expire-transaction.md)  [`AuthenticatorStateUpdateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-update-transaction.md)  [`ChangeEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  [`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`ConsensusCommitPrologueTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-commit-prologue-transaction.md)  [`EpochConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch-connection.md)  [`EpochEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch-edge.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  [`ValidatorAggregatedSignature`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-aggregated-signature.md)