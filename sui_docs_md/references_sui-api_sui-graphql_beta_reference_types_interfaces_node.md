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

An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

```graphql
interface Node {
  id: ID!
}
```

### Fields

#### [Node.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The node's globally unique identifier, which can be passed to `Query.node` to refetch it.

### Returned By

[`node`](/references/sui-api/sui-graphql/beta/reference/operations/queries/node.md)  

### Implemented By

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)