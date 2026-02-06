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
type CheckpointConnection {
  edges: [CheckpointEdge!]!
  nodes: [Checkpoint!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [CheckpointConnection.<b>edges</b>](#)[<b>[CheckpointEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-edge.mdx)   
A list of edges.

#### [CheckpointConnection.<b>nodes</b>](#)[<b>[Checkpoint!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.mdx)   
A list of nodes.

#### [CheckpointConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`checkpoints`](/references/sui-api/sui-graphql/beta/reference/operations/queries/checkpoints.md)  

### Member Of

[`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)