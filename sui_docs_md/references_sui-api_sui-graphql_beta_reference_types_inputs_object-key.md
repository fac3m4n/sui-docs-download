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

Identifies a specific version of an object.

The `address` field must be specified, as well as at most one of `version`, `rootVersion`, or `atCheckpoint`. If none are provided, the object is fetched at the current checkpoint.

Specifying a `version` or a `rootVersion` disables nested queries for paginating owned objects or dynamic fields (these queries are only supported at checkpoint boundaries).

See `Query.object` for more details.

```graphql
input ObjectKey {
  address: SuiAddress!
  atCheckpoint: UInt53
  rootVersion: UInt53
  version: UInt53
}
```

### Fields

#### [ObjectKey.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The object's ID.

#### [ObjectKey.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, tries to fetch the latest version as of this checkpoint. Fails if the checkpoint is later than the RPC's latest checkpoint.

#### [ObjectKey.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, tries to fetch the latest version of the object at or before this version. Nested dynamic field accesses will also be subject to this bound.

This can be used to fetch a child or ancestor object bounded by its root object's version. For any wrapped or child (object-owned) object, its root object can be defined recursively as:

- The root object of the object it is wrapped in, if it is wrapped.
- The root object of its owner, if it is owned by another object.
- The object itself, if it is not object-owned or wrapped.

#### [ObjectKey.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, tries to fetch the object at this exact version.

### Member Of

[`multiGetObjects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-objects.md)