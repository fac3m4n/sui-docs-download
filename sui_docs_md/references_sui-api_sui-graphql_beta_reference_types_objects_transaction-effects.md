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

The results of executing a transaction.

```graphql
type TransactionEffects {
  balanceChanges(
    first: Int
    after: String
    last: Int
    before: String
  ): BalanceChangeConnection
  balanceChangesJson: JSON
  checkpoint: Checkpoint
  dependencies(
    first: Int
    after: String
    last: Int
    before: String
  ): TransactionConnection
  digest: String!
  effectsBcs: Base64
  effectsDigest: String
  effectsJson: JSON
  epoch: Epoch
  events(
    first: Int
    after: String
    last: Int
    before: String
  ): EventConnection
  executionError: ExecutionError
  gasEffects: GasEffects
  lamportVersion: UInt53
  objectChanges(
    first: Int
    after: String
    last: Int
    before: String
  ): ObjectChangeConnection
  status: ExecutionStatus
  timestamp: DateTime
  transaction: Transaction
  unchangedConsensusObjects(
    first: Int
    after: String
    last: Int
    before: String
  ): UnchangedConsensusObjectConnection
}
```

### Fields

#### [TransactionEffects.<b>balanceChanges</b>](#)[<b>BalanceChangeConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change-connection.md)  
The effect this transaction had on the balances (sum of coin values per coin type) of addresses and objects.
##### [TransactionEffects.balanceChanges.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.balanceChanges.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [TransactionEffects.balanceChanges.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.balanceChanges.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [TransactionEffects.<b>balanceChangesJson</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
The balance changes as a JSON array, matching the gRPC proto format.

#### [TransactionEffects.<b>checkpoint</b>](#)[<b>Checkpoint</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  
The checkpoint this transaction was finalized in.

#### [TransactionEffects.<b>dependencies</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
Transactions whose outputs this transaction depends upon.
##### [TransactionEffects.dependencies.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.dependencies.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [TransactionEffects.dependencies.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.dependencies.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [TransactionEffects.<b>digest</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A 32-byte hash that uniquely identifies the transaction contents, encoded in Base58.

Note that this is different from the execution digest, which is the unique hash of the transaction effects.

#### [TransactionEffects.<b>effectsBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of these effects, as `TransactionEffects`.

#### [TransactionEffects.<b>effectsDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A 32-byte hash that uniquely identifies the effects contents, encoded in Base58.

#### [TransactionEffects.<b>effectsJson</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
The effects as a JSON blob, matching the gRPC proto format (excluding BCS).

#### [TransactionEffects.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
The epoch this transaction was finalized in.

#### [TransactionEffects.<b>events</b>](#)[<b>EventConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/event-connection.md)  
Events emitted by this transaction.
##### [TransactionEffects.events.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.events.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [TransactionEffects.events.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.events.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [TransactionEffects.<b>executionError</b>](#)[<b>ExecutionError</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-error.md)  
Rich execution error information for failed transactions.

#### [TransactionEffects.<b>gasEffects</b>](#)[<b>GasEffects</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-effects.md)  
Effects related to the gas object used for the transaction (costs incurred and the identity of the smashed gas object returned).

#### [TransactionEffects.<b>lamportVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The latest version of all objects (apart from packages) that have been created or modified by this transaction, immediately following this transaction.

#### [TransactionEffects.<b>objectChanges</b>](#)[<b>ObjectChangeConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change-connection.md)  
The before and after state of objects that were modified by this transaction.
##### [TransactionEffects.objectChanges.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.objectChanges.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [TransactionEffects.objectChanges.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.objectChanges.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [TransactionEffects.<b>status</b>](#)[<b>ExecutionStatus</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/execution-status.md)  
Whether the transaction executed successfully or not.

#### [TransactionEffects.<b>timestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
Timestamp corresponding to the checkpoint this transaction was finalized in.

`null` for executed/simulated transactions that have not been included in a checkpoint.

#### [TransactionEffects.<b>transaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that ran to produce these effects.

#### [TransactionEffects.<b>unchangedConsensusObjects</b>](#)[<b>UnchangedConsensusObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/unchanged-consensus-object-connection.md)  
The unchanged consensus-managed objects that were referenced by this transaction.
##### [TransactionEffects.unchangedConsensusObjects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.unchangedConsensusObjects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [TransactionEffects.unchangedConsensusObjects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [TransactionEffects.unchangedConsensusObjects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Returned By

[`multiGetTransactionEffects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-transaction-effects.md)  [`transactionEffects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/transaction-effects.md)  

### Member Of

[`ExecutionResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-result.md)  [`SimulationResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/simulation-result.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)