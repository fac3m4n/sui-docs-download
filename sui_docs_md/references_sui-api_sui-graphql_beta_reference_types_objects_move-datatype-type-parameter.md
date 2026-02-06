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

Declaration of a type parameter on a Move struct.

```graphql
type MoveDatatypeTypeParameter {
  constraints: [MoveAbility!]!
  isPhantom: Boolean!
}
```

### Fields

#### [MoveDatatypeTypeParameter.<b>constraints</b>](#)[<b>[MoveAbility!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Ability constraints on this type parameter.

#### [MoveDatatypeTypeParameter.<b>isPhantom</b>](#)[<b>Boolean!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)   
Whether this type parameter is marked `phantom` or not.

Phantom type parameters are not referenced in the struct's fields.

### Member Of

[`IMoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  [`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveEnum`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  [`MoveStruct`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)