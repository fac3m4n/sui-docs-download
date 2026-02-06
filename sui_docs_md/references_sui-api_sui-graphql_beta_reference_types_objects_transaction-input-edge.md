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

An edge in a connection.

```graphql
type TransactionInputEdge {
  cursor: String!
  node: TransactionInput!
}
```

### Fields

#### [TransactionInputEdge.<b>cursor</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A cursor for use in pagination

#### [TransactionInputEdge.<b>node</b>](#)[<b>TransactionInput!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)   
The item at the end of the edge

### Member Of

[`TransactionInputConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-connection.md)