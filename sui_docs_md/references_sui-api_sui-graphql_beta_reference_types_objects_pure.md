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

BCS encoded primitive value (not an object or Move struct).

```graphql
type Pure {
  bytes: Base64
}
```

### Fields

#### [Pure.<b>bytes</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
BCS serialized and Base64 encoded primitive value.

### Implemented By

[`TransactionInput`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)