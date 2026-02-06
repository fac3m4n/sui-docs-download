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
type BalanceChangeConnection {
  edges: [BalanceChangeEdge!]!
  nodes: [BalanceChange!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [BalanceChangeConnection.<b>edges</b>](#)[<b>[BalanceChangeEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change-edge.mdx)   
A list of edges.

#### [BalanceChangeConnection.<b>nodes</b>](#)[<b>[BalanceChange!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change.mdx)   
A list of nodes.

#### [BalanceChangeConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)