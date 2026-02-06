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
input EventFilter {
  afterCheckpoint: UInt53
  atCheckpoint: UInt53
  beforeCheckpoint: UInt53
  module: String
  sender: SuiAddress
  type: String
}
```

### Fields

#### [EventFilter.<b>afterCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit to events that occured strictly after the given checkpoint.

#### [EventFilter.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit to events in the given checkpoint.

#### [EventFilter.<b>beforeCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit to event that occured strictly before the given checkpoint.

#### [EventFilter.<b>module</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Events emitted by a particular module. An event is emitted by a particular module if some function in the module is called by a PTB and emits an event.

Modules can be filtered by their package, or package::module. We currently do not support filtering by emitting module and event type at the same time so if both are provided in one filter, the query will error.

#### [EventFilter.<b>sender</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
Filter on events by transaction sender address.

#### [EventFilter.<b>type</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
This field is used to specify the type of event emitted.

Events can be filtered by their type's package, package::module, or their fully qualified type name.

Generic types can be queried by either the generic type name, e.g. `0x2::coin::Coin`, or by the full type name, such as `0x2::coin::Coin<0x2::sui::SUI>`.

### Member Of

[`events`](/references/sui-api/sui-graphql/beta/reference/operations/queries/events.md)