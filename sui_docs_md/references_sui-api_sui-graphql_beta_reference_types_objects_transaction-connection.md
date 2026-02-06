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
type TransactionConnection {
  edges: [TransactionEdge!]!
  nodes: [Transaction!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [TransactionConnection.<b>edges</b>](#)[<b>[TransactionEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-edge.mdx)   
A list of edges.

#### [TransactionConnection.<b>nodes</b>](#)[<b>[Transaction!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.mdx)   
A list of nodes.

#### [TransactionConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`transactions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/transactions.md)  

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)