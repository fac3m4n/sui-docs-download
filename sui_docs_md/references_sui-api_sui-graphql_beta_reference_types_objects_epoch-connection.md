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
type EpochConnection {
  edges: [EpochEdge!]!
  nodes: [Epoch!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [EpochConnection.<b>edges</b>](#)[<b>[EpochEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch-edge.mdx)   
A list of edges.

#### [EpochConnection.<b>nodes</b>](#)[<b>[Epoch!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.mdx)   
A list of nodes.

#### [EpochConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`epochs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/epochs.md)