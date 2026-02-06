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
type Event {
  contents: MoveValue
  eventBcs: Base64
  sender: Address
  sequenceNumber: UInt53!
  timestamp: DateTime
  transaction: Transaction
  transactionModule: MoveModule
}
```

### Fields

#### [Event.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The Move value emitted for this event.

#### [Event.<b>eventBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64 encoded BCS serialized bytes of the entire Event structure from sui-types.
This includes: package&#x005F;id, transaction&#x005F;module, sender, type, and contents (which itself contains the BCS-serialized Move struct data).

#### [Event.<b>sender</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Address of the sender of the transaction that emitted this event.

#### [Event.<b>sequenceNumber</b>](#)[<b>UInt53!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)   
The position of the event among the events from the same transaction.

#### [Event.<b>timestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
Timestamp corresponding to the checkpoint this event's transaction was finalized in.
All events from the same transaction share the same timestamp.

`null` for simulated/executed transactions as they are not included in a checkpoint.

#### [Event.<b>transaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that emitted this event. This information is only available for events from indexed transactions, and not from transactions that have just been executed or dry-run.

#### [Event.<b>transactionModule</b>](#)[<b>MoveModule</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  
The module containing the function that was called in the programmable transaction, that resulted in this event being emitted.

### Member Of

[`EventConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/event-connection.md)  [`EventEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/event-edge.md)