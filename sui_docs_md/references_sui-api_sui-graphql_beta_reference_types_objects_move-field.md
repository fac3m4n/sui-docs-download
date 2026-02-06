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

No description

```graphql
type MoveField {
  name: String
  type: OpenMoveType
}
```

### Fields

#### [MoveField.<b>name</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The field's name.

#### [MoveField.<b>type</b>](#)[<b>OpenMoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/open-move-type.md)  
The field's type.

This type can reference type parameters introduced by the defining struct (see `typeParameters`).

### Member Of

[`MoveEnumVariant`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-variant.md)  [`MoveStruct`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)