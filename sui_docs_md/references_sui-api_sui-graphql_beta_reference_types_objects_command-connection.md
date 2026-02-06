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
type CommandConnection {
  edges: [CommandEdge!]!
  nodes: [Command!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [CommandConnection.<b>edges</b>](#)[<b>[CommandEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-edge.mdx)   
A list of edges.

#### [CommandConnection.<b>nodes</b>](#)[<b>[Command!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/command.mdx)   
A list of nodes.

#### [CommandConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`ProgrammableSystemTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-system-transaction.md)  [`ProgrammableTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-transaction.md)