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

Effects to the balance (sum of coin values per coin type) of addresses and objects.

```graphql
type BalanceChange {
  amount: BigInt
  coinType: MoveType
  owner: Address
}
```

### Fields

#### [BalanceChange.<b>amount</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The signed balance change.

#### [BalanceChange.<b>coinType</b>](#)[<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
The inner type of the coin whose balance has changed (e.g. `0x2::sui::SUI`).

#### [BalanceChange.<b>owner</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The address or object whose balance has changed.

### Member Of

[`BalanceChangeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change-connection.md)  [`BalanceChangeEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change-edge.md)