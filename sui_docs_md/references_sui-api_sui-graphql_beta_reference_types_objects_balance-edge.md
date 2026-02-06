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
type BalanceEdge {
  cursor: String!
  node: Balance!
}
```

### Fields

#### [BalanceEdge.<b>cursor</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A cursor for use in pagination

#### [BalanceEdge.<b>node</b>](#)[<b>Balance!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)   
The item at the end of the edge

### Member Of

[`BalanceConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)