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

A Move object that's shared.

```graphql
type SharedInput {
  address: SuiAddress
  initialSharedVersion: UInt53
  mutable: Boolean
}
```

### Fields

#### [SharedInput.<b>address</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The address of the shared object.

#### [SharedInput.<b>initialSharedVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version that this object was shared at.

#### [SharedInput.<b>mutable</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Controls whether the transaction block can reference the shared object as a mutable reference or by value.

This has implications for scheduling: Transactions that just read shared objects at a certain version (mutable = false) can be executed concurrently, while transactions that write shared objects (mutable = true) must be executed serially with respect to each other.

### Implemented By

[`TransactionInput`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)