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

Dynamic fields are heterogenous fields that can be added or removed from an object at runtime. Their names are arbitrary Move values that have `copy`, `drop`, and `store`.

There are two sub-types of dynamic fields:

- Dynamic fields can store any value that has `store`. Objects stored in this kind of field will be considered wrapped (not accessible via its ID by external tools like explorers, wallets, etc. accessing storage).
- Dynamic object fields can only store objects (values that have the `key` ability, and an `id: UID` as its first field) that have `store`, but they will still be directly accessible off-chain via their ID after being attached as a field.

```graphql
type DynamicField implements Node, IAddressable, IMoveObject, IObject {
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
  contents: MoveValue
  defaultNameRecord: NameRecord
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
  id: ID!
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
  name: MoveValue
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
  storageRebate: BigInt
  value: DynamicFieldValue
  version: UInt53
}
```

### Fields

#### [DynamicField.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The DynamicField's ID.

#### [DynamicField.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [DynamicField.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [DynamicField.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [DynamicField.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

If the address does not own any coins of that type, a balance of zero is returned.
##### [DynamicField.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [DynamicField.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [DynamicField.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [DynamicField.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The structured representation of the object's contents.

#### [DynamicField.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [DynamicField.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
32-byte hash that identifies the object's contents, encoded in Base58.

#### [DynamicField.<b>dynamicField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic field with that name could not be found attached to this object.
##### [DynamicField.dynamicField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [DynamicField.<b>dynamicFields</b>](#)[<b>DynamicFieldConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  
Dynamic fields owned by this object.

Dynamic fields on wrapped objects can be accessed using `Address.dynamicFields`.
##### [DynamicField.dynamicFields.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.dynamicFields.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.dynamicFields.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.dynamicFields.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [DynamicField.<b>dynamicObjectField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic object field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic object field with that name could not be found attached to this object.
##### [DynamicField.dynamicObjectField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [DynamicField.<b>hasPublicTransfer</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether this object can be transfered using the `TransferObjects` Programmable Transaction Command or `sui::transfer::public_transfer`.

Both these operations require the object to have both the `key` and `store` abilities.

#### [DynamicField.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The dynamic field's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [DynamicField.<b>moveObjectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialize of this object, as a `MoveObject`.

#### [DynamicField.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [DynamicField.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [DynamicField.<b>multiGetDynamicFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic fields on an object using their types and BCS-encoded names.

Returns a list of dynamic fields that is guaranteed to be the same length as `keys`. If a dynamic field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [DynamicField.multiGetDynamicFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [DynamicField.<b>multiGetDynamicObjectFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic object fields on an object using their types and BCS-encoded names.

Returns a list of dynamic object fields that is guaranteed to be the same length as `keys`. If a dynamic object field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [DynamicField.multiGetDynamicObjectFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [DynamicField.<b>name</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The dynamic field's name, as a Move value.

#### [DynamicField.<b>objectAt</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Fetch the object with the same ID, at a different version, root version bound, or checkpoint.
##### [DynamicField.objectAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [DynamicField.objectAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [DynamicField.objectAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [DynamicField.<b>objectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this object, as an `Object`.

#### [DynamicField.<b>objectVersionsAfter</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object after this one.
##### [DynamicField.objectVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objectVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objectVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objectVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objectVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [DynamicField.<b>objectVersionsBefore</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object before this one.
##### [DynamicField.objectVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objectVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objectVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objectVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objectVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [DynamicField.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this object, optionally filtered by type.
##### [DynamicField.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

#### [DynamicField.<b>owner</b>](#)[<b>Owner</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)  
The object's owner kind.

#### [DynamicField.<b>previousTransaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that created this version of the object.

#### [DynamicField.<b>receivedTransactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions that sent objects to this object.
##### [DynamicField.receivedTransactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.receivedTransactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.receivedTransactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [DynamicField.receivedTransactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [DynamicField.receivedTransactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [DynamicField.<b>storageRebate</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The SUI returned to the sponsor or sender of the transaction that modifies or deletes this object.

#### [DynamicField.<b>value</b>](#)[<b>DynamicFieldValue</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/dynamic-field-value.md)  
The dynamic field's value, as a Move value for dynamic fields and as a MoveObject for dynamic object fields.

#### [DynamicField.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of this object that this content comes from.

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

#### [<b>IAddressable</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  
Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

#### [<b>IMoveObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  
Interface implemented by types that represent a Move object on-chain (A Move value whose type has `key`).

#### [<b>IObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  
Interface implemented by versioned on-chain values that are addressable by an ID (also referred to as its address). This includes Move objects and packages.

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`DynamicFieldConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  [`DynamicFieldEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-edge.md)  [`IMoveObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)