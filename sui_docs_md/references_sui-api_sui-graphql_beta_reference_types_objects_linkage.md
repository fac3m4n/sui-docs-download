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

Information used by a package to link to a specific version of its dependency.

```graphql
type Linkage {
  originalId: SuiAddress
  upgradedId: SuiAddress
  version: UInt53
}
```

### Fields

#### [Linkage.<b>originalId</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The ID on-chain of the first version of the dependency.

#### [Linkage.<b>upgradedId</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The ID on-chain of the version of the dependency that this package depends on.

#### [Linkage.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version of the dependency that this package depends on.

### Member Of

[`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)