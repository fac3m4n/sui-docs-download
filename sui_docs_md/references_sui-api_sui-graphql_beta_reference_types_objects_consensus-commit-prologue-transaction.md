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

System transaction that runs at the beginning of a checkpoint, and is responsible for setting the current value of the clock, based on the timestamp from consensus.

```graphql
type ConsensusCommitPrologueTransaction {
  additionalStateDigest: String
  commitTimestamp: DateTime
  consensusCommitDigest: String
  epoch: Epoch
  round: UInt53
  subDagIndex: UInt53
}
```

### Fields

#### [ConsensusCommitPrologueTransaction.<b>additionalStateDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Digest of any additional state computed by the consensus handler.
Used to detect forking bugs as early as possible.

Present in V4.

#### [ConsensusCommitPrologueTransaction.<b>commitTimestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
Unix timestamp from consensus.

Present in V1, V2, V3, V4.

#### [ConsensusCommitPrologueTransaction.<b>consensusCommitDigest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Digest of consensus output, encoded as a Base58 string.

Present in V2, V3, V4.

#### [ConsensusCommitPrologueTransaction.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
Epoch of the commit prologue transaction.

Present in V1, V2, V3, V4.

#### [ConsensusCommitPrologueTransaction.<b>round</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Consensus round of the commit.

Present in V1, V2, V3, V4.

#### [ConsensusCommitPrologueTransaction.<b>subDagIndex</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The sub DAG index of the consensus commit. This field is populated if there
are multiple consensus commits per round.

Present in V3, V4.

### Implemented By

[`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)