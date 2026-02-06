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

Checkpoints contain finalized transactions and are used for node synchronization and global transaction ordering.

```graphql
type Checkpoint implements Node {
  artifactsDigest: String
  contentBcs: Base64
  contentDigest: String
  digest: String
  epoch: Epoch
  id: ID!
  networkTotalTransactions: UInt53
  previousCheckpointDigest: String
  query: Query
  rollingGasSummary: GasCostSummary
  sequenceNumber: UInt53!
  summaryBcs: Base64
  timestamp: DateTime
  transactions(
    first: Int
    after: String
    last: Int
    before: String
    filter: TransactionFilter
  ): TransactionConnection
  validatorSignatures: ValidatorAggregatedSignature
}
```

### Fields

#### [Checkpoint.<b>artifactsDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A commitment by the committee at each checkpoint on the artifacts of the checkpoint.
e.g., object checkpoint states

#### [Checkpoint.<b>contentBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64 serialized BCS bytes of this checkpoint's contents.

#### [Checkpoint.<b>contentDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A 32-byte hash that uniquely identifies the checkpoint's content, encoded in Base58.

#### [Checkpoint.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A 32-byte hash that uniquely identifies the checkpoint, encoded in Base58. This is a hash of the checkpoint's summary.

#### [Checkpoint.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
The epoch that this checkpoint is part of.

#### [Checkpoint.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The checkpoint's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [Checkpoint.<b>networkTotalTransactions</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The total number of transactions in the network by the end of this checkpoint.

#### [Checkpoint.<b>previousCheckpointDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The digest of the previous checkpoint's summary.

#### [Checkpoint.<b>query</b>](#)<b>Query</b>  
Query the RPC as if this checkpoint were the latest checkpoint.

#### [Checkpoint.<b>rollingGasSummary</b>](#)[<b>GasCostSummary</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-cost-summary.md)  
The computation cost, storage cost, storage rebate, and non-refundable storage fee accumulated during this epoch, up to and including this checkpoint. These values increase monotonically across checkpoints in the same epoch, and reset on epoch boundaries.

#### [Checkpoint.<b>sequenceNumber</b>](#)[<b>UInt53!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)   
The checkpoint's position in the total order of finalized checkpoints, agreed upon by consensus.

#### [Checkpoint.<b>summaryBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64 serialized BCS bytes of this checkpoint's summary.

#### [Checkpoint.<b>timestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
The timestamp at which the checkpoint is agreed to have happened according to consensus. Transactions that access time in this checkpoint will observe this timestamp.

#### [Checkpoint.<b>transactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  

##### [Checkpoint.transactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Checkpoint.transactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Checkpoint.transactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Checkpoint.transactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Checkpoint.transactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [Checkpoint.<b>validatorSignatures</b>](#)[<b>ValidatorAggregatedSignature</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-aggregated-signature.md)  
The aggregation of signatures from a quorum of validators for the checkpoint proposal.

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

### Returned By

[`checkpoint`](/references/sui-api/sui-graphql/beta/reference/operations/queries/checkpoint.md)  [`multiGetCheckpoints`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-checkpoints.md)  

### Member Of

[`AvailableRange`](/references/sui-api/sui-graphql/beta/reference/types/objects/available-range.md)  [`CheckpointConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-connection.md)  [`CheckpointEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-edge.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)