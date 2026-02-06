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
type TransactionInputConnection {
  edges: [TransactionInputEdge!]!
  nodes: [TransactionInput!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [TransactionInputConnection.<b>edges</b>](#)[<b>[TransactionInputEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-edge.mdx)   
A list of edges.

#### [TransactionInputConnection.<b>nodes</b>](#)[<b>[TransactionInput!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.mdx)   
A list of nodes.

#### [TransactionInputConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`ProgrammableSystemTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-system-transaction.md)  [`ProgrammableTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-transaction.md)