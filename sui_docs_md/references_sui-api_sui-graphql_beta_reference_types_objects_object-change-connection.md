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
type ObjectChangeConnection {
  edges: [ObjectChangeEdge!]!
  nodes: [ObjectChange!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [ObjectChangeConnection.<b>edges</b>](#)[<b>[ObjectChangeEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change-edge.mdx)   
A list of edges.

#### [ObjectChangeConnection.<b>nodes</b>](#)[<b>[ObjectChange!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change.mdx)   
A list of nodes.

#### [ObjectChangeConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)