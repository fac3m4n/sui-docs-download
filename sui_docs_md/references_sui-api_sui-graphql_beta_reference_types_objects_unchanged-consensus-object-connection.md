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
type UnchangedConsensusObjectConnection {
  edges: [UnchangedConsensusObjectEdge!]!
  nodes: [UnchangedConsensusObject!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [UnchangedConsensusObjectConnection.<b>edges</b>](#)[<b>[UnchangedConsensusObjectEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/unchanged-consensus-object-edge.mdx)   
A list of edges.

#### [UnchangedConsensusObjectConnection.<b>nodes</b>](#)[<b>[UnchangedConsensusObject!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/unchanged-consensus-object.mdx)   
A list of nodes.

#### [UnchangedConsensusObjectConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)