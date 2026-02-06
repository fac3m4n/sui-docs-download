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

Identifies a specific version of a package.

The `address` field must be specified, as well as at most one of `version`, or `atCheckpoint`. If neither is provided, the package is fetched at the checkpoint being viewed.

See `Query.package` for more details.

```graphql
input PackageKey {
  address: SuiAddress!
  atCheckpoint: UInt53
  version: UInt53
}
```

### Fields

#### [PackageKey.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The object's ID.

#### [PackageKey.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, tries to fetch the latest version as of this checkpoint.

#### [PackageKey.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, tries to fetch the package at this exact version.

### Member Of

[`multiGetPackages`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-packages.md)