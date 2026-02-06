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
type BalanceConnection {
  edges: [BalanceEdge!]!
  nodes: [Balance!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [BalanceConnection.<b>edges</b>](#)[<b>[BalanceEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-edge.mdx)   
A list of edges.

#### [BalanceConnection.<b>nodes</b>](#)[<b>[Balance!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
A list of nodes.

#### [BalanceConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)