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

Interface implemented by all GraphQL types that represent a Move datatype definition (either a struct or an enum definition).

This interface is used to provide a way to access fields that are shared by both structs and enums, e.g., the module that the datatype belongs to, the name of the datatype, type parameters etc.

```graphql
interface IMoveDatatype {
  abilities: [MoveAbility!]
  fullyQualifiedName: String!
  module: MoveModule!
  name: String!
  typeParameters: [MoveDatatypeTypeParameter!]
}
```

### Fields

#### [IMoveDatatype.<b>abilities</b>](#)[<b>[MoveAbility!]</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Abilities on this datatype definition.

#### [IMoveDatatype.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The datatype's fully-qualified name, including package address, module name, and datatype name.

#### [IMoveDatatype.<b>module</b>](#)[<b>MoveModule!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)   
The module that this datatype is defined in

#### [IMoveDatatype.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The datatype's unqualified name

#### [IMoveDatatype.<b>typeParameters</b>](#)[<b>[MoveDatatypeTypeParameter!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.mdx)   
Constraints on the datatype's formal type parameters

Move bytecode does not name type parameters, so when they are referenced (e.g. in field types), they are identified by their index in this list.

### Implemented By

[`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveEnum`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  [`MoveStruct`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)