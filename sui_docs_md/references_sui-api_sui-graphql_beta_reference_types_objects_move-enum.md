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

Description of an enum type, defined in a Move module.

```graphql
type MoveEnum implements IMoveDatatype {
  abilities: [MoveAbility!]
  fullyQualifiedName: String!
  module: MoveModule!
  name: String!
  typeParameters: [MoveDatatypeTypeParameter!]
  variants: [MoveEnumVariant!]
}
```

### Fields

#### [MoveEnum.<b>abilities</b>](#)[<b>[MoveAbility!]</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Abilities on this enum definition.

#### [MoveEnum.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The enum's fully-qualified name, including package address, module name, and datatype name.

#### [MoveEnum.<b>module</b>](#)[<b>MoveModule!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)   
The module that this enum is defined in.

#### [MoveEnum.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The enum's unqualified name.

#### [MoveEnum.<b>typeParameters</b>](#)[<b>[MoveDatatypeTypeParameter!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.mdx)   
Constraints on the enum's formal type parameters.

Move bytecode does not name type parameters, so when they are referenced (e.g. in field types), they are identified by their index in this list.

#### [MoveEnum.<b>variants</b>](#)[<b>[MoveEnumVariant!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-variant.mdx)   
The names and fields of the enum's variants

Field types reference type parameters by their index in the defining enum's `typeParameters` list.

### Interfaces

#### [<b>IMoveDatatype</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  
Interface implemented by all GraphQL types that represent a Move datatype definition (either a struct or an enum definition).

This interface is used to provide a way to access fields that are shared by both structs and enums, e.g., the module that the datatype belongs to, the name of the datatype, type parameters etc.

### Member Of

[`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveEnumConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-connection.md)  [`MoveEnumEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-edge.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)