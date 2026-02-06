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
type MoveDatatypeConnection {
  edges: [MoveDatatypeEdge!]!
  nodes: [MoveDatatype!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveDatatypeConnection.<b>edges</b>](#)[<b>[MoveDatatypeEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-edge.mdx)   
A list of edges.

#### [MoveDatatypeConnection.<b>nodes</b>](#)[<b>[MoveDatatype!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.mdx)   
A list of nodes.

#### [MoveDatatypeConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)