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

An object representing metadata about a coin type.

```graphql
type CoinMetadata implements IAddressable, IMoveObject, IObject {
  address: SuiAddress!
  addressAt(
    rootVersion: UInt53
    checkpoint: UInt53
  ): Address
  allowGlobalPause: Boolean
  balance(
    coinType: String!
  ): Balance
  balances(
    first: Int
    after: String
    last: Int
    before: String
  ): BalanceConnection
  contents: MoveValue
  decimals: Int
  defaultNameRecord: NameRecord
  denyCap: MoveObject
  description: String
  digest: String
  dynamicField(
    name: DynamicFieldName!
  ): DynamicField
  dynamicFields(
    first: Int
    after: String
    last: Int
    before: String
  ): DynamicFieldConnection
  dynamicObjectField(
    name: DynamicFieldName!
  ): DynamicField
  hasPublicTransfer: Boolean
  iconUrl: String
  moveObjectBcs: Base64
  multiGetBalances(
    keys: [String!]!
  ): [Balance!]
  multiGetDynamicFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
  multiGetDynamicObjectFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
  name: String
  objectAt(
    version: UInt53
    rootVersion: UInt53
    checkpoint: UInt53
  ): Object
  objectBcs: Base64
  objectVersionsAfter(
    first: Int
    after: String
    last: Int
    before: String
    filter: VersionFilter
  ): ObjectConnection
  objectVersionsBefore(
    first: Int
    after: String
    last: Int
    before: String
    filter: VersionFilter
  ): ObjectConnection
  objects(
    first: Int
    after: String
    last: Int
    before: String
    filter: ObjectFilter
  ): MoveObjectConnection
  owner: Owner
  previousTransaction: Transaction
  receivedTransactions(
    first: Int
    after: String
    last: Int
    before: String
    filter: TransactionFilter
  ): TransactionConnection
  regulatedState: RegulatedState
  storageRebate: BigInt
  supply: BigInt
  supplyState: SupplyState
  symbol: String
  version: UInt53
}
```

### Fields

#### [CoinMetadata.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The CoinMetadata's ID.

#### [CoinMetadata.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [CoinMetadata.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [CoinMetadata.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [CoinMetadata.<b>allowGlobalPause</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether the `DenyCap` can be used to enable a global pause that behaves as if all addresses were added to the deny list. `null` indicates that it is not known whether the currency can be paused or not. This field is only populated on currencies held in the Coin Registry. To determine whether a legacy currency can be paused, check the contents of its `DenyCap`, if it can be found.

#### [CoinMetadata.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

If the address does not own any coins of that type, a balance of zero is returned.
##### [CoinMetadata.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [CoinMetadata.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [CoinMetadata.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [CoinMetadata.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The structured representation of the object's contents.

#### [CoinMetadata.<b>decimals</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Number of decimal places the coin uses.

#### [CoinMetadata.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [CoinMetadata.<b>denyCap</b>](#)[<b>MoveObject</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  
If the currency is regulated, this object represents the capability to modify the deny list. If a capability is known but wrapped, its address can be fetched but other fields will not be accessible.

#### [CoinMetadata.<b>description</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Description of the coin.

#### [CoinMetadata.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
32-byte hash that identifies the object's contents, encoded in Base58.

#### [CoinMetadata.<b>dynamicField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic field with that name could not be found attached to this object.
##### [CoinMetadata.dynamicField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [CoinMetadata.<b>dynamicFields</b>](#)[<b>DynamicFieldConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  
Dynamic fields owned by this object.

Dynamic fields on wrapped objects can be accessed using `Address.dynamicFields`.
##### [CoinMetadata.dynamicFields.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.dynamicFields.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.dynamicFields.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.dynamicFields.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [CoinMetadata.<b>dynamicObjectField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic object field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic object field with that name could not be found attached to this object.
##### [CoinMetadata.dynamicObjectField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [CoinMetadata.<b>hasPublicTransfer</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether this object can be transfered using the `TransferObjects` Programmable Transaction Command or `sui::transfer::public_transfer`.

Both these operations require the object to have both the `key` and `store` abilities.

#### [CoinMetadata.<b>iconUrl</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
URL for the coin logo.

#### [CoinMetadata.<b>moveObjectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialize of this object, as a `MoveObject`.

#### [CoinMetadata.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [CoinMetadata.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [CoinMetadata.<b>multiGetDynamicFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic fields on an object using their types and BCS-encoded names.

Returns a list of dynamic fields that is guaranteed to be the same length as `keys`. If a dynamic field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [CoinMetadata.multiGetDynamicFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [CoinMetadata.<b>multiGetDynamicObjectFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic object fields on an object using their types and BCS-encoded names.

Returns a list of dynamic object fields that is guaranteed to be the same length as `keys`. If a dynamic object field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [CoinMetadata.multiGetDynamicObjectFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [CoinMetadata.<b>name</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Name for the coin.

#### [CoinMetadata.<b>objectAt</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Fetch the object with the same ID, at a different version, root version bound, or checkpoint.
##### [CoinMetadata.objectAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [CoinMetadata.objectAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [CoinMetadata.objectAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [CoinMetadata.<b>objectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this object, as an `Object`.

#### [CoinMetadata.<b>objectVersionsAfter</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object after this one.
##### [CoinMetadata.objectVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objectVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objectVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objectVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objectVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [CoinMetadata.<b>objectVersionsBefore</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object before this one.
##### [CoinMetadata.objectVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objectVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objectVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objectVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objectVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [CoinMetadata.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this object, optionally filtered by type.
##### [CoinMetadata.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

#### [CoinMetadata.<b>owner</b>](#)[<b>Owner</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)  
The object's owner kind.

#### [CoinMetadata.<b>previousTransaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that created this version of the object.

#### [CoinMetadata.<b>receivedTransactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions that sent objects to this object.
##### [CoinMetadata.receivedTransactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.receivedTransactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.receivedTransactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [CoinMetadata.receivedTransactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [CoinMetadata.receivedTransactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [CoinMetadata.<b>regulatedState</b>](#)[<b>RegulatedState</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/regulated-state.md)  
Whether the currency is regulated or not. `null` indicates that the regulatory status is unknown.

#### [CoinMetadata.<b>storageRebate</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The SUI returned to the sponsor or sender of the transaction that modifies or deletes this object.

#### [CoinMetadata.<b>supply</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The overall balance of coins issued.

#### [CoinMetadata.<b>supplyState</b>](#)[<b>SupplyState</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/supply-state.md)  
Future behavior of the supply. `null` indicates that the future behavior of the supply is not known because the currency's treasury still exists.

#### [CoinMetadata.<b>symbol</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Symbol for the coin.

#### [CoinMetadata.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of this object that this content comes from.

### Interfaces

#### [<b>IAddressable</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  
Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

#### [<b>IMoveObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  
Interface implemented by types that represent a Move object on-chain (A Move value whose type has `key`).

#### [<b>IObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  
Interface implemented by versioned on-chain values that are addressable by an ID (also referred to as its address). This includes Move objects and packages.

### Returned By

[`coinMetadata`](/references/sui-api/sui-graphql/beta/reference/operations/queries/coin-metadata.md)  

### Member Of

[`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)