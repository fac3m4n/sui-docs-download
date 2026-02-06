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

Filter for paginating the history of an Object or MovePackage.

```graphql
input VersionFilter {
  afterVersion: UInt53
  beforeVersion: UInt53
}
```

### Fields

#### [VersionFilter.<b>afterVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to versions that are strictly newer than this one, defaults to fetching from the earliest version known to this RPC (this could be the initial version, or some later version if the initial version has been pruned).

#### [VersionFilter.<b>beforeVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to versions that are strictly older than this one, defaults to fetching up to the latest version (inclusive).

### Member Of

[`objectVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object-versions.md)  [`packageVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package-versions.md)