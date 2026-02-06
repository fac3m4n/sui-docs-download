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

Paginate objects in the live object set, optionally filtered by owner and/or type. `filter` can be one of:

- A filter on type (all live objects whose type matches that filter).
- Fetching all objects owned by an address or object, optionally filtered by type.
- Fetching all shared or immutable objects, filtered by type.

```graphql
objects(
  first: Int
  after: String
  last: Int
  before: String
  filter: ObjectFilter!
): ObjectConnection
```

### Arguments

#### [objects.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [objects.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [objects.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [objects.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [objects.<b>filter</b>](#)[<b>ObjectFilter!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)   

### Type

#### [<b>ObjectConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)