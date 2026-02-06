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

Information about which previous versions of a package introduced its types.

```graphql
type TypeOrigin {
  definingId: SuiAddress
  module: String
  struct: String
}
```

### Fields

#### [TypeOrigin.<b>definingId</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The storage ID of the package that first defined this type.

#### [TypeOrigin.<b>module</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Module defining the type.

#### [TypeOrigin.<b>struct</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Name of the struct.

### Member Of

[`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)