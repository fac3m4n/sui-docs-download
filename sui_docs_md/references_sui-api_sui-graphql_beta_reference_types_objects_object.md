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

An Object on Sui is either a typed value (a Move Object) or a Package (modules containing functions and types).

Every object on Sui is identified by a unique address, and has a version number that increases with every modification. Objects also hold metadata detailing their current owner (who can sign for access to the object and whether that access can modify and/or delete the object), and the digest of the last transaction that modified the object.

```graphql
type Object implements Node, IAddressable, IObject {
  address: SuiAddress!
  addressAt(
    rootVersion: UInt53
    checkpoint: UInt53
  ): Address
  asMoveObject: MoveObject
  asMovePackage: MovePackage
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
  id: ID!
  multiGetBalances(
    keys: [String!]!
  ): [Balance!]
  multiGetDynamicFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
  multiGetDynamicObjectFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
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
  version: UInt53
}
```

### Fields

#### [Object.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The Object's ID.

#### [Object.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [Object.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [Object.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [Object.<b>asMoveObject</b>](#)[<b>MoveObject</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  
Attempts to convert the object into a MoveObject.

#### [Object.<b>asMovePackage</b>](#)[<b>MovePackage</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  
Attempts to convert the object into a MovePackage.

#### [Object.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

If the address does not own any coins of that type, a balance of zero is returned.
##### [Object.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [Object.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [Object.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [Object.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [Object.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
32-byte hash that identifies the object's contents, encoded in Base58.

#### [Object.<b>dynamicField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic field with that name could not be found attached to this object.
##### [Object.dynamicField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [Object.<b>dynamicFields</b>](#)[<b>DynamicFieldConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  
Dynamic fields owned by this object.
##### [Object.dynamicFields.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.dynamicFields.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.dynamicFields.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.dynamicFields.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [Object.<b>dynamicObjectField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic object field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic object field with that name could not be found attached to this object.
##### [Object.dynamicObjectField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [Object.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The object's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [Object.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

Returns `None` when no checkpoint is set in scope (e.g. execution scope).
If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [Object.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [Object.<b>multiGetDynamicFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic fields on an object using their types and BCS-encoded names.

Returns a list of dynamic fields that is guaranteed to be the same length as `keys`. If a dynamic field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [Object.multiGetDynamicFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [Object.<b>multiGetDynamicObjectFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic object fields on an object using their types and BCS-encoded names.

Returns a list of dynamic object fields that is guaranteed to be the same length as `keys`. If a dynamic object field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [Object.multiGetDynamicObjectFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [Object.<b>objectAt</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Fetch the object with the same ID, at a different version, root version bound, or checkpoint.

If no additional bound is provided, the object is fetched at the latest checkpoint known to the RPC.
##### [Object.objectAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [Object.objectAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [Object.objectAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [Object.<b>objectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this object, as an `Object`.

#### [Object.<b>objectVersionsAfter</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object after this one.
##### [Object.objectVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objectVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objectVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objectVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objectVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [Object.<b>objectVersionsBefore</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object before this one.
##### [Object.objectVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objectVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objectVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objectVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objectVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [Object.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this object, optionally filtered by type.
##### [Object.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

#### [Object.<b>owner</b>](#)[<b>Owner</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)  
The object's owner kind.

#### [Object.<b>previousTransaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that created this version of the object.

#### [Object.<b>receivedTransactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions that sent objects to this object
##### [Object.receivedTransactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.receivedTransactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.receivedTransactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Object.receivedTransactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Object.receivedTransactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [Object.<b>storageRebate</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The SUI returned to the sponsor or sender of the transaction that modifies or deletes this object.

#### [Object.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of this object that this content comes from.

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

#### [<b>IAddressable</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  
Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

#### [<b>IObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  
Interface implemented by versioned on-chain values that are addressable by an ID (also referred to as its address). This includes Move objects and packages.

### Returned By

[`multiGetObjects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-objects.md)  [`object`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object.md)  

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`ConsensusObjectRead`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-object-read.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`GasEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-effects.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`ObjectChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change.md)  [`ObjectConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  [`ObjectEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-edge.md)  [`OwnedOrImmutable`](/references/sui-api/sui-graphql/beta/reference/types/objects/owned-or-immutable.md)  [`PerEpochConfig`](/references/sui-api/sui-graphql/beta/reference/types/objects/per-epoch-config.md)  [`Receiving`](/references/sui-api/sui-graphql/beta/reference/types/objects/receiving.md)