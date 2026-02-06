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
type ActiveJwkConnection {
  edges: [ActiveJwkEdge!]!
  nodes: [ActiveJwk!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [ActiveJwkConnection.<b>edges</b>](#)[<b>[ActiveJwkEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk-edge.mdx)   
A list of edges.

#### [ActiveJwkConnection.<b>nodes</b>](#)[<b>[ActiveJwk!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk.mdx)   
A list of nodes.

#### [ActiveJwkConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Member Of

[`AuthenticatorStateUpdateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-update-transaction.md)