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

A transaction that was cancelled before it could access the consensus-managed object, so the object was an input but remained unchanged.

```graphql
type ConsensusObjectCancelled {
  address: SuiAddress
  cancellationReason: ConsensusObjectCancellationReason
}
```

### Fields

#### [ConsensusObjectCancelled.<b>address</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The ID of the consensus-managed object that the transaction intended to access.

#### [ConsensusObjectCancelled.<b>cancellationReason</b>](#)[<b>ConsensusObjectCancellationReason</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/consensus-object-cancellation-reason.md)  
Reason why the transaction was cancelled.

### Implemented By

[`UnchangedConsensusObject`](/references/sui-api/sui-graphql/beta/reference/types/unions/unchanged-consensus-object.md)