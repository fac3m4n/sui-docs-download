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

Interface implemented by versioned on-chain values that are addressable by an ID (also referred to as its address). This includes Move objects and packages.

```graphql
interface IObject {
  digest: String
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

#### [IObject.<b>digest</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
32-byte hash that identifies the object's contents, encoded in Base58.

#### [IObject.<b>objectAt</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
Fetch the object with the same ID, at a different version, root version bound, or checkpoint.
##### [IObject.objectAt.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [IObject.objectAt.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [IObject.objectAt.<b>checkpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [IObject.<b>objectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this object, as an `Object`.

#### [IObject.<b>objectVersionsAfter</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object after this one.
##### [IObject.objectVersionsAfter.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.objectVersionsAfter.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.objectVersionsAfter.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.objectVersionsAfter.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.objectVersionsAfter.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [IObject.<b>objectVersionsBefore</b>](#)[<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  
Paginate all versions of this object before this one.
##### [IObject.objectVersionsBefore.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.objectVersionsBefore.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.objectVersionsBefore.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.objectVersionsBefore.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.objectVersionsBefore.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

#### [IObject.<b>owner</b>](#)[<b>Owner</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)  
The object's owner kind.

#### [IObject.<b>previousTransaction</b>](#)[<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
The transaction that created this version of the object

#### [IObject.<b>receivedTransactions</b>](#)[<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  
The transactions that sent objects to this object.
##### [IObject.receivedTransactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.receivedTransactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.receivedTransactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IObject.receivedTransactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IObject.receivedTransactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

#### [IObject.<b>storageRebate</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The SUI returned to the sponsor or sender of the transaction that modifies or deletes this object.

#### [IObject.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of this object that this content comes from.

### Implemented By

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)