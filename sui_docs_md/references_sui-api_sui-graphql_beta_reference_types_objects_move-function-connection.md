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
type MoveFunctionConnection {
  edges: [MoveFunctionEdge!]!
  nodes: [MoveFunction!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveFunctionConnection.<b>edges</b>](#)[<b>[MoveFunctionEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-edge.mdx)   
A list of edges.

#### [MoveFunctionConnection.<b>nodes</b>](#)[<b>[MoveFunction!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.mdx)   
A list of nodes.

#### [MoveFunctionConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)