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

A Move object, either immutable, or owned mutable.

```graphql
type OwnedOrImmutable {
  object: Object
}
```

### Fields

#### [OwnedOrImmutable.<b>object</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  

### Implemented By

[`TransactionInput`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)