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

Paginate events that are emitted in the network, optionally filtered by event filters.

```graphql
events(
  first: Int
  after: String
  last: Int
  before: String
  filter: EventFilter
): EventConnection
```

### Arguments

#### [events.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [events.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [events.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [events.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [events.<b>filter</b>](#)[<b>EventFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/event-filter.md)  

### Type

#### [<b>EventConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/event-connection.md)