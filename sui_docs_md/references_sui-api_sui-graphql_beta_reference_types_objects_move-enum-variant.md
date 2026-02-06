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
type MoveEnumVariant {
  fields: [MoveField!]
  name: String
}
```

### Fields

#### [MoveEnumVariant.<b>fields</b>](#)[<b>[MoveField!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-field.mdx)   
The names and types of the variant's fields.

Field types reference type parameters by their index in the defining struct's `typeParameters` list.

#### [MoveEnumVariant.<b>name</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The variant's name.

### Member Of

[`MoveEnum`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)