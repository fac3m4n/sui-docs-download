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

Description of a datatype, defined in a Move module.

```graphql
type MoveDatatype implements IMoveDatatype {
  abilities: [MoveAbility!]
  asMoveEnum: MoveEnum
  asMoveStruct: MoveStruct
  fullyQualifiedName: String!
  module: MoveModule!
  name: String!
  typeParameters: [MoveDatatypeTypeParameter!]
}
```

### Fields

#### [MoveDatatype.<b>abilities</b>](#)[<b>[MoveAbility!]</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Abilities on this datatype definition.

#### [MoveDatatype.<b>asMoveEnum</b>](#)[<b>MoveEnum</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  
Attempts to convert the `MoveDatatype` to a `MoveEnum`.

#### [MoveDatatype.<b>asMoveStruct</b>](#)[<b>MoveStruct</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)  
Attempts to convert the `MoveDatatype` to a `MoveStruct`.

#### [MoveDatatype.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The datatype's fully-qualified name, including package address, module name, and datatype name.

#### [MoveDatatype.<b>module</b>](#)[<b>MoveModule!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)   
The module that this datatype is defined in.

#### [MoveDatatype.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The datatype's unqualified name.

#### [MoveDatatype.<b>typeParameters</b>](#)[<b>[MoveDatatypeTypeParameter!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.mdx)   
Constraints on the datatype's formal type parameters.

Move bytecode does not name type parameters, so when they are referenced (e.g. in field types), they are identified by their index in this list.

### Interfaces

#### [<b>IMoveDatatype</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  
Interface implemented by all GraphQL types that represent a Move datatype definition (either a struct or an enum definition).

This interface is used to provide a way to access fields that are shared by both structs and enums, e.g., the module that the datatype belongs to, the name of the datatype, type parameters etc.

### Member Of

[`MoveDatatypeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-connection.md)  [`MoveDatatypeEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-edge.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)