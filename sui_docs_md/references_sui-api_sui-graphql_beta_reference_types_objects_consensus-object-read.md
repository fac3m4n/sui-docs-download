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

No description

```graphql
type ConsensusObjectRead {
  object: Object
}
```

### Fields

#### [ConsensusObjectRead.<b>object</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
The version of the consensus-managed object that was read by this transaction.

### Implemented By

[`UnchangedConsensusObject`](/references/sui-api/sui-graphql/beta/reference/types/unions/unchanged-consensus-object.md)