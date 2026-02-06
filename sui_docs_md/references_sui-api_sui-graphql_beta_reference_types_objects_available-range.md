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

Checkpoint range for which data is available.

```graphql
type AvailableRange {
  first: Checkpoint
  last: Checkpoint
}
```

### Fields

#### [AvailableRange.<b>first</b>](#)[<b>Checkpoint</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  
Inclusive lower checkpoint for which data is available.

#### [AvailableRange.<b>last</b>](#)[<b>Checkpoint</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  
Inclusive upper checkpoint for which data is available.

### Member Of

[`ServiceConfig`](/references/sui-api/sui-graphql/beta/reference/types/objects/service-config.md)