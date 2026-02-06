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

Look-up an account by its SuiAddress.

If `rootVersion` is specified, nested dynamic field accesses will be fetched at or before this version. This can be used to fetch a child or descendant object bounded by its root object's version, when its immediate parent is wrapped, or a value in a dynamic object field. For any wrapped or child (object-owned) object, its root object can be defined recursively as:

- The root object of the object it is wrapped in, if it is wrapped.
- The root object of its owner, if it is owned by another object.
- The object itself, if it is not object-owned or wrapped.

Specifying a `rootVersion` disables nested queries for paginating owned objects or dynamic fields (these queries are only supported at checkpoint boundaries).

If `atCheckpoint` is specified, the address will be fetched at the latest version as of this checkpoint. This will fail if the provided checkpoint is after the RPC's latest checkpoint.

If none of the above are specified, the address is fetched at the checkpoint being viewed.

If the address is fetched by name and the name does not resolve to an address (e.g. the name does not exist or has expired), `null` is returned.

```graphql
address(
  address: SuiAddress
  name: String
  rootVersion: UInt53
  atCheckpoint: UInt53
): Address
```

### Arguments

#### [address.<b>address</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  

#### [address.<b>name</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [address.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

#### [address.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

### Type

#### [<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)