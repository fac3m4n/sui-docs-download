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
type EventConnection {
  edges: [EventEdge!]!
  nodes: [Event!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [EventConnection.<b>edges</b>](#)[<b>[EventEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/event-edge.mdx)   
A list of edges.

#### [EventConnection.<b>nodes</b>](#)[<b>[Event!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/event.mdx)   
A list of nodes.

#### [EventConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`events`](/references/sui-api/sui-graphql/beta/reference/operations/queries/events.md)  

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)