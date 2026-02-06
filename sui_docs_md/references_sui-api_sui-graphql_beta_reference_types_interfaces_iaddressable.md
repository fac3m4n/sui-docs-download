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

Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

```graphql
interface IAddressable {
  address: SuiAddress!
  addressAt(
    rootVersion: UInt53
    checkpoint: UInt53
  ): Address
  balance(
    coinType: String!
  ): Balance
  balances(
    first: Int
    after: String
    last: Int
    before: String
  ): BalanceConnection
  defaultNameRecord: NameRecord
  multiGetBalances(
    keys: [String!]!
  ): [Balance!]
  objects(
    first: Int
    after: String
    last: Int
    before: String
    filter: ObjectFilter
  ): MoveObjectConnection
}
```

### Fields

#### [IAddressable.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   

#### [IAddressable.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [IAddressable.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [IAddressable.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [IAddressable.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

If the address does not own any coins of that type, a balance of zero is returned.
##### [IAddressable.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [IAddressable.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [IAddressable.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IAddressable.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IAddressable.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IAddressable.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [IAddressable.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [IAddressable.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

Returns `null` when no checkpoint is set in scope (e.g. execution scope). If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [IAddressable.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [IAddressable.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this address, optionally filtered by type.
##### [IAddressable.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IAddressable.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IAddressable.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IAddressable.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IAddressable.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

### Implemented By

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)