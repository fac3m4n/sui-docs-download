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
type EndOfEpochTransactionKindConnection {
  edges: [EndOfEpochTransactionKindEdge!]!
  nodes: [EndOfEpochTransactionKind!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [EndOfEpochTransactionKindConnection.<b>edges</b>](#)[<b>[EndOfEpochTransactionKindEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction-kind-edge.mdx)   
A list of edges.

#### [EndOfEpochTransactionKindConnection.<b>nodes</b>](#)[<b>[EndOfEpochTransactionKind!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.mdx)   
A list of nodes.

#### [EndOfEpochTransactionKindConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`EndOfEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction.md)