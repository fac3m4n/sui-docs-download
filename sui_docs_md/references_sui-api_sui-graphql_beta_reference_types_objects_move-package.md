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

A MovePackage is a kind of Object that represents code that has been published on-chain. It exposes information about its modules, type definitions, functions, and dependencies.

```graphql
type MovePackage implements Node, IAddressable, IObject {
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
  digest: String
  id: ID!
  linkage: [Linkage!]
  module(
    name: String!
  ): MoveModule
  moduleBcs: Base64
  modules(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveModuleConnection
  multiGetBalances(
    keys: [String!]!
  ): [Balance!]
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
  packageAt(
    version: UInt53
    checkpoint: UInt53
  ): MovePackage
  packageBcs: Base64
  packageVersionsAfter(
    first: Int
    after: String
    last: Int
    before: String
    filter: VersionFilter
  ): MovePackageConnection
  packageVersionsBefore(
    first: Int
    after: String
    last: Int
    before: String
    filter: VersionFilter
  ): MovePackageConnection
  previousTransaction: Transaction
  receivedTransactions(
    first: Int
    after: String
    last: Int
    before: String
    filter: TransactionFilter
  ): TransactionConnection
  storageRebate: BigInt
  typeOrigins: [TypeOrigin!]
  version: UInt53
}
```

### Fields

#### [MovePackage.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The MovePackage's ID.

#### [MovePackage.<b>addressAt</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Fetch the address as it was at a different root version, or checkpoint.

If no additional bound is provided, the address is fetched at the latest checkpoint known to the RPC.
##### [MovePackage.addressAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [MovePackage.addressAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [MovePackage.<b>balance</b>](#)[<b>Balance</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  
Fetch the total balance for coins with marker type `coinType` (e.g. `0x2::sui::SUI`), owned by this address.

If the address does not own any coins of that type, a balance of zero is returned.
##### [MovePackage.balance.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MovePackage.<b>balances</b>](#)[<b>BalanceConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  
Total balance across coins owned by this address, grouped by coin type.
##### [MovePackage.balances.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.balances.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.balances.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.balances.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MovePackage.<b>defaultNameRecord</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The domain explicitly configured as the default Name Service name for this address.

#### [MovePackage.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
32-byte hash that identifies the package's contents, encoded in Base58.

#### [MovePackage.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The package's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [MovePackage.<b>linkage</b>](#)[<b>[Linkage!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/linkage.mdx)   
The transitive dependencies of this package.

#### [MovePackage.<b>module</b>](#)[<b>MoveModule</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  
The module named `name` in this package.
##### [MovePackage.module.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MovePackage.<b>moduleBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
BCS representation of the package's modules.  Modules appear as a sequence of pairs (module name, followed by module bytes), in alphabetic order by module name.

#### [MovePackage.<b>modules</b>](#)[<b>MoveModuleConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-connection.md)  
Paginate through this package's modules.
##### [MovePackage.modules.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.modules.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.modules.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.modules.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MovePackage.<b>multiGetBalances</b>](#)[<b>[Balance!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.mdx)   
Fetch the total balances keyed by coin types (e.g. `0x2::sui::SUI`) owned by this address.

If the address does not own any coins of a given type, a balance of zero is returned for that type.
##### [MovePackage.multiGetBalances.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [MovePackage.<b>objectAt</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Fetch the package as an object with the same ID, at a different version, root version bound, or checkpoint.

If no additional bound is provided, the latest version of this object is fetched at the latest checkpoint.
##### [MovePackage.objectAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [MovePackage.objectAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [MovePackage.objectAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [MovePackage.<b>objectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this package, as an `Object`.

#### [MovePackage.<b>objectVersionsAfter</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this package treated as an object, after this one.
##### [MovePackage.objectVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objectVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objectVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objectVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objectVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [MovePackage.<b>objectVersionsBefore</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this package treated as an object, before this one.
##### [MovePackage.objectVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objectVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objectVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objectVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objectVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [MovePackage.<b>objects</b>](#)[<b>MoveObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  
Objects owned by this package, optionally filtered by type.
##### [MovePackage.objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.objects.<b>filter</b>](#)[<b>ObjectFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  

#### [MovePackage.<b>owner</b>](#)[<b>Owner</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)  
The object's owner kind.

#### [MovePackage.<b>packageAt</b>](#)[<b>MovePackage</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  
Fetch the package with the same original ID, at a different version, or checkpoint.

If no additional bound is provided, the package is fetched at the latest checkpoint known to the RPC.
##### [MovePackage.packageAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [MovePackage.packageAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [MovePackage.<b>packageBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this package, as a `MovePackage`.

#### [MovePackage.<b>packageVersionsAfter</b>](#)[<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  
Paginate all versions of this package after this one.
##### [MovePackage.packageVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.packageVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.packageVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.packageVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.packageVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [MovePackage.<b>packageVersionsBefore</b>](#)[<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  
Paginate all versions of this package before this one.
##### [MovePackage.packageVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.packageVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.packageVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.packageVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.packageVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [MovePackage.<b>previousTransaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that created this version of the object.

#### [MovePackage.<b>receivedTransactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions that sent objects to this object.
##### [MovePackage.receivedTransactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.receivedTransactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.receivedTransactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MovePackage.receivedTransactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MovePackage.receivedTransactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [MovePackage.<b>storageRebate</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The SUI returned to the sponsor or sender of the transaction that modifies or deletes this object.

#### [MovePackage.<b>typeOrigins</b>](#)[<b>[TypeOrigin!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/type-origin.mdx)   
A table identifying which versions of a package introduced each of its types.

#### [MovePackage.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of this package that this content comes from.

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

#### [<b>IAddressable</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  
Interface implemented by GraphQL types representing entities that are identified by an address.

An address uniquely represents either the public key of an account, or an object's ID, but never both. It is not possible to determine which type an address represents up-front. If an object is wrapped, its contents will not be accessible via its address, but it will still be possible to access other objects it owns.

#### [<b>IObject</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  
Interface implemented by versioned on-chain values that are addressable by an ID (also referred to as its address). This includes Move objects and packages.

### Returned By

[`multiGetPackages`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-packages.md)  [`package`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package.md)  

### Member Of

[`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`MovePackageConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  [`MovePackageEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-edge.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)