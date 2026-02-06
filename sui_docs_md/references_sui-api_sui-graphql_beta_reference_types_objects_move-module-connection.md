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
type MoveModuleConnection {
  edges: [MoveModuleEdge!]!
  nodes: [MoveModule!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MoveModuleConnection.<b>edges</b>](#)[<b>[MoveModuleEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-edge.mdx)   
A list of edges.

#### [MoveModuleConnection.<b>nodes</b>](#)[<b>[MoveModule!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.mdx)   
A list of nodes.

#### [MoveModuleConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)