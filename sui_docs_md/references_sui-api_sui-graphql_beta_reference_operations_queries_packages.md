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

Paginate all packages published on-chain, optionally bounded to packages published strictly after `filter.afterCheckpoint` and/or strictly before `filter.beforeCheckpoint`.

```graphql
packages(
  first: Int
  after: String
  last: Int
  before: String
  filter: PackageCheckpointFilter
): MovePackageConnection
```

### Arguments

#### [packages.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [packages.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [packages.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [packages.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [packages.<b>filter</b>](#)[<b>PackageCheckpointFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/package-checkpoint-filter.md)  

### Type

#### [<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)