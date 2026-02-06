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

A filter over the live object set, the filter can be one of:

- A filter on type (all live objects whose type matches that filter).
- Fetching all objects owned by an address or object, optionally filtered by type.
- Fetching all shared or immutable objects, filtered by type.

```graphql
input ObjectFilter {
  owner: SuiAddress
  ownerKind: OwnerKind
  type: String
}
```

### Fields

#### [ObjectFilter.<b>owner</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
Specifies the address of the owning address or object.

This field is required if `ownerKind` is "ADDRESS" or "OBJECT". If provided without `ownerKind`, `ownerKind` defaults to "ADDRESS".

#### [ObjectFilter.<b>ownerKind</b>](#)[<b>OwnerKind</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/owner-kind.md)  
Filter on whether the object is address-owned, object-owned, shared, or immutable.

- If this field is set to "ADDRESS" or "OBJECT", then an owner filter must also be provided.
- If this field is set to "SHARED" or "IMMUTABLE", then a type filter must also be provided.

#### [ObjectFilter.<b>type</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Filter on the object's type.

The filter can be one of:

- A package address: `0x2`,
- A module: `0x2::coin`,
- A fully-qualified name: `0x2::coin::Coin`,
- A type instantiation: `0x2::coin::Coin<0x2::sui::SUI>`.

### Member Of

[`objects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/objects.md)