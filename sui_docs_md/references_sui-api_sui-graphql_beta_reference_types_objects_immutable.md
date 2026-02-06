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

Object is accessible to all addresses, and is immutable.

```graphql
type Immutable {
  _: Boolean
}
```

### Fields

#### [Immutable.<b>&#x005F;</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  

### Implemented By

[`Owner`](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)