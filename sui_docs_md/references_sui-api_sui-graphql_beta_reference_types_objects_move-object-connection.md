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
type MoveObjectConnection {
  edges: [MoveObjectEdge!]!
  nodes: [MoveObject!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveObjectConnection.<b>edges</b>](#)[<b>[MoveObjectEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-edge.mdx)   
A list of edges.

#### [MoveObjectConnection.<b>nodes</b>](#)[<b>[MoveObject!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.mdx)   
A list of nodes.

#### [MoveObjectConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)