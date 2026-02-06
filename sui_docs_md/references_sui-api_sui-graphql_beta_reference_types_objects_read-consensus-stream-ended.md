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

A transaction that wanted to read a consensus-managed object but couldn't because it became not-consensus-managed before the transaction executed (for example, it was deleted, turned into an owned object, or wrapped).

```graphql
type ReadConsensusStreamEnded {
  address: SuiAddress
  sequenceNumber: UInt53
}
```

### Fields

#### [ReadConsensusStreamEnded.<b>address</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The ID of the consensus-managed object.

#### [ReadConsensusStreamEnded.<b>sequenceNumber</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The sequence number associated with the consensus stream ending.

### Implemented By

[`UnchangedConsensusObject`](/references/sui-api/sui-graphql/beta/reference/types/unions/unchanged-consensus-object.md)