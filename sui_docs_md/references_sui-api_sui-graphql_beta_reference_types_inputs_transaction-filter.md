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
input TransactionFilter {
  affectedAddress: SuiAddress
  affectedObject: SuiAddress
  afterCheckpoint: UInt53
  atCheckpoint: UInt53
  beforeCheckpoint: UInt53
  function: String
  kind: TransactionKindInput
  sentAddress: SuiAddress
}
```

### Fields

#### [TransactionFilter.<b>affectedAddress</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
Limit to transactions that interacted with the given address.
The address could be a sender, sponsor, or recipient of the transaction.

#### [TransactionFilter.<b>affectedObject</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
Limit to transactions that interacted with the given object.
The object could have been created, read, modified, deleted, wrapped, or unwrapped by the transaction.
Objects that were passed as a `Receiving` input are not considered to have been affected by a transaction unless they were actually received.

#### [TransactionFilter.<b>afterCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to transactions that occurred strictly after the given checkpoint.

#### [TransactionFilter.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to transactions in the given checkpoint.

#### [TransactionFilter.<b>beforeCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to transaction that occurred strictly before the given checkpoint.

#### [TransactionFilter.<b>function</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Filter transactions by move function called. Calls can be filtered by the `package`, `package::module`, or the `package::module::name` of their function.

#### [TransactionFilter.<b>kind</b>](#)[<b>TransactionKindInput</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/transaction-kind-input.md)  
An input filter selecting for either system or programmable transactions.

#### [TransactionFilter.<b>sentAddress</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
Limit to transactions that were sent by the given address.

### Member Of

[`transactions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/transactions.md)