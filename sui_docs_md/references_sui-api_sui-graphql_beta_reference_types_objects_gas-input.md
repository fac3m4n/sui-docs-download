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
type GasInput {
  gasBudget: BigInt
  gasPayment(
    first: Int
    after: String
    last: Int
    before: String
  ): ObjectConnection
  gasPrice: BigInt
  gasSponsor: Address
}
```

### Fields

#### [GasInput.<b>gasBudget</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The maximum SUI that can be expended by executing this transaction

#### [GasInput.<b>gasPayment</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Objects used to pay for a transaction's execution and storage
##### [GasInput.gasPayment.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [GasInput.gasPayment.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [GasInput.gasPayment.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [GasInput.gasPayment.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [GasInput.<b>gasPrice</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
An unsigned integer specifying the number of native tokens per gas unit this transaction will pay (in MIST).

#### [GasInput.<b>gasSponsor</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Address of the owner of the gas object(s) used.

### Member Of

[`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)