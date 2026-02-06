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

The total balance for a particular coin type.

```graphql
type Balance {
  addressBalance: BigInt
  coinBalance: BigInt
  coinType: MoveType
  totalBalance: BigInt
}
```

### Fields

#### [Balance.<b>addressBalance</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The balance as tracked by the accumulator object for the address.

#### [Balance.<b>coinBalance</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
Total balance across all owned coin objects of the coin type.

#### [Balance.<b>coinType</b>](#)[<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
Coin type for the balance, such as `0x2::sui::SUI`.

#### [Balance.<b>totalBalance</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The sum total of the accumulator balance and individual coin balances owned by the address.

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`BalanceConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  [`BalanceEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-edge.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)