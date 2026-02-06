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

Placeholder for unimplemented command types

```graphql
type OtherCommand {
  _: Boolean
}
```

### Fields

#### [OtherCommand.<b>&#x005F;</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Placeholder field for unimplemented commands

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)