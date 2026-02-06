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
type DynamicFieldConnection {
  edges: [DynamicFieldEdge!]!
  nodes: [DynamicField!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [DynamicFieldConnection.<b>edges</b>](#)[<b>[DynamicFieldEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-edge.mdx)   
A list of edges.

#### [DynamicFieldConnection.<b>nodes</b>](#)[<b>[DynamicField!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
A list of nodes.

#### [DynamicFieldConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IMoveObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)