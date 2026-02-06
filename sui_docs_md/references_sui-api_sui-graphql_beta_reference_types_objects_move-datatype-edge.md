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
type MoveDatatypeEdge {
  cursor: String!
  node: MoveDatatype!
}
```

### Fields

#### [MoveDatatypeEdge.<b>cursor</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A cursor for use in pagination

#### [MoveDatatypeEdge.<b>node</b>](#)[<b>MoveDatatype!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)   
The item at the end of the edge

### Member Of

[`MoveDatatypeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-connection.md)