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

System transaction to update the source of on-chain randomness.

```graphql
type RandomnessStateUpdateTransaction {
  epoch: Int
  randomBytes: Base64
  randomnessObjInitialSharedVersion: Int
  randomnessRound: Int
}
```

### Fields

#### [RandomnessStateUpdateTransaction.<b>epoch</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Epoch of the randomness state update transaction.

#### [RandomnessStateUpdateTransaction.<b>randomBytes</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
Updated random bytes, Base64 encoded.

#### [RandomnessStateUpdateTransaction.<b>randomnessObjInitialSharedVersion</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
The initial version of the randomness object that it was shared at.

#### [RandomnessStateUpdateTransaction.<b>randomnessRound</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Randomness round of the update.

### Implemented By

[`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)