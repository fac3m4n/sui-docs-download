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

No description

```graphql
type ObjectConnection {
  edges: [ObjectEdge!]!
  nodes: [Object!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [ObjectConnection.<b>edges</b>](#)[<b>[ObjectEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-edge.mdx)   
A list of edges.

#### [ObjectConnection.<b>nodes</b>](#)[<b>[Object!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.mdx)   
A list of nodes.

#### [ObjectConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`objects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/objects.md)  [`objectVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object-versions.md)  

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`GasInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-input.md)  [`GenesisTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/genesis-transaction.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)