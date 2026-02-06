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
type MoveStructConnection {
  edges: [MoveStructEdge!]!
  nodes: [MoveStruct!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveStructConnection.<b>edges</b>](#)[<b>[MoveStructEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct-edge.mdx)   
A list of edges.

#### [MoveStructConnection.<b>nodes</b>](#)[<b>[MoveStruct!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.mdx)   
A list of nodes.

#### [MoveStructConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)