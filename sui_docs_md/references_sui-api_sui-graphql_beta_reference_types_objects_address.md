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
type Address implements Node, IAddressable {
  address: SuiAddress!
  addressAt(
    rootVersion: UInt53
    checkpoint: UInt53
  ): Address
  asObject: Object
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
  objects(
    first: Int
    after: String
    last: Int
    before: String
    filter: ObjectFilter
  ): MoveObjectConnection
  transactions(
    first: Int
    after: String
    last: Int
    before: String
    relation: AddressTransactionRelationship
    filter: TransactionFilter
  ): TransactionConnection
}
```

### Fields

#### [Address.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The Address' identifier, a 32-byte number represented as a 64-character hex string, with a lead "0x".

#### [Address.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [Address.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [Address.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [Address.<b>asObject</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Attempts to fetch the object at this address.

#### [Address.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

Returns `None` when no checkpoint is set in scope (e.g. execution scope).
If the address does not own any coins of that type, a balance of zero is returned.
##### [Address.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [Address.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [Address.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [Address.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [Address.<b>dynamicField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic field with that name could not be found attached to the object with this address.
##### [Address.dynamicField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [Address.<b>dynamicFields</b>](#)[<b>DynamicFieldConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  
Dynamic fields owned by this address.

The address must correspond to an object (account addresses cannot own dynamic fields), but that object may be wrapped.
##### [Address.dynamicFields.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.dynamicFields.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.dynamicFields.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.dynamicFields.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [Address.<b>dynamicObjectField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic object field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic object field with that name could not be found attached to the object with this address.
##### [Address.dynamicObjectField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [Address.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The address's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [Address.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

Returns `None` when no checkpoint is set in scope (e.g. execution scope).
If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [Address.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [Address.<b>multiGetDynamicFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic fields on an object using their types and BCS-encoded names.

Returns a list of dynamic fields that is guaranteed to be the same length as `keys`. If a dynamic field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [Address.multiGetDynamicFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [Address.<b>multiGetDynamicObjectFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic object fields on an object using their types and BCS-encoded names.

Returns a list of dynamic object fields that is guaranteed to be the same length as `keys`. If a dynamic object field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [Address.multiGetDynamicObjectFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [Address.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this address, optionally filtered by type.
##### [Address.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

#### [Address.<b>transactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
Transactions associated with this address.

Similar behavior to the `transactions` in Query but supporting the additional `AddressTransactionRelationship` filter, which defaults to `SENT`.
##### [Address.transactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.transactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.transactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Address.transactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Address.transactions.<b>relation</b>](#)[<b>AddressTransactionRelationship</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/address-transaction-relationship.md)  

##### [Address.transactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

#### [<b>IAddressable</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  
Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

### Returned By

[`address`](/references/sui-api/sui-graphql/beta/reference/operations/queries/address.md)  [`multiGetAddresses`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-addresses.md)  

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`AddressOwner`](/references/sui-api/sui-graphql/beta/reference/types/objects/address-owner.md)  [`BalanceChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`ConsensusAddressOwner`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-address-owner.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`GasInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-input.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  [`NameRecord`](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`ObjectOwner`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-owner.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)