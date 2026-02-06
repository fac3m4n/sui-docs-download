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
type MoveEnumConnection {
  edges: [MoveEnumEdge!]!
  nodes: [MoveEnum!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveEnumConnection.<b>edges</b>](#)[<b>[MoveEnumEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-edge.mdx)   
A list of edges.

#### [MoveEnumConnection.<b>nodes</b>](#)[<b>[MoveEnum!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.mdx)   
A list of nodes.

#### [MoveEnumConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)