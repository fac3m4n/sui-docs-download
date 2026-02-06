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

A Name Service NameRecord representing a domain name registration.

```graphql
type NameRecord {
  contents: MoveValue!
  domain: String!
  parent: NameRecord
  target(
    rootVersion: UInt53
    atCheckpoint: UInt53
  ): Address
}
```

### Fields

#### [NameRecord.<b>contents</b>](#)[<b>MoveValue!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)   
On-chain representation of the underlying Name Service `NameRecord` Move value.

#### [NameRecord.<b>domain</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The domain name this record is for.

#### [NameRecord.<b>parent</b>](#)[<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
The Name Service Name Record of the parent domain, if this is a subdomain.

Returns `null` if this is not a subdomain.

#### [NameRecord.<b>target</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The address this domain points to.

`rootVersion` and `atCheckpoint` control how the target `Address` is scoped. If neither is provided, the `Address` is scoped to the latest checkpoint known to the RPC.
##### [NameRecord.target.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

##### [NameRecord.target.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

### Returned By

[`nameRecord`](/references/sui-api/sui-graphql/beta/reference/operations/queries/name-record.md)  

### Member Of

[`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`NameRecord`](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)