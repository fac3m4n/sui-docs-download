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
type EndOfEpochTransactionKindEdge {
  cursor: String!
  node: EndOfEpochTransactionKind!
}
```

### Fields

#### [EndOfEpochTransactionKindEdge.<b>cursor</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A cursor for use in pagination

#### [EndOfEpochTransactionKindEdge.<b>node</b>](#)[<b>EndOfEpochTransactionKind!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.md)   
The item at the end of the edge

### Member Of

[`EndOfEpochTransactionKindConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction-kind-connection.md)