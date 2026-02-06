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
type ValidatorConnection {
  edges: [ValidatorEdge!]!
  nodes: [Validator!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [ValidatorConnection.<b>edges</b>](#)[<b>[ValidatorEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-edge.mdx)   
A list of edges.

#### [ValidatorConnection.<b>nodes</b>](#)[<b>[Validator!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator.mdx)   
A list of nodes.

#### [ValidatorConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`Validator`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator.md)  [`ValidatorSet`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-set.md)