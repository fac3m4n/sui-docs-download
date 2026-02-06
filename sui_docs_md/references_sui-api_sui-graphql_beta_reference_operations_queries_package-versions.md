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

Paginate all versions of a package at `address`, optionally bounding the versions exclusively from below with `filter.afterVersion` or from above with `filter.beforeVersion`.

Different versions of a package will have different object IDs, unless they are system packages, but will share the same original ID.

```graphql
packageVersions(
  first: Int
  after: String
  last: Int
  before: String
  address: SuiAddress!
  filter: VersionFilter
): MovePackageConnection
```

### Arguments

#### [packageVersions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [packageVersions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [packageVersions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [packageVersions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [packageVersions.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   

#### [packageVersions.<b>filter</b>](#)[<b>VersionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)  

### Type

#### [<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)