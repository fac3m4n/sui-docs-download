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

Represents types that could contain references or free type parameters.  Such types can appear
as function parameters, in fields of structs, or as actual type parameter.

```graphql
type OpenMoveType {
  repr: String!
  signature: OpenMoveTypeSignature!
}
```

### Fields

#### [OpenMoveType.<b>repr</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
Flat representation of the type signature, as a displayable string.

#### [OpenMoveType.<b>signature</b>](#)[<b>OpenMoveTypeSignature!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/open-move-type-signature.md)   
Structured representation of the type signature.

### Member Of

[`MoveField`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-field.md)  [`MoveFunction`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)