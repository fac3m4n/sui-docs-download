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
type PerEpochConfig {
  object: Object
}
```

### Fields

#### [PerEpochConfig.<b>object</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
The per-epoch configuration object as of when the transaction was executed.

### Implemented By

[`UnchangedConsensusObject`](/references/sui-api/sui-graphql/beta/reference/types/unions/unchanged-consensus-object.md)