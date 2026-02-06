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

Description of a struct type, defined in a Move module.

```graphql
type MoveStruct implements IMoveDatatype {
  abilities: [MoveAbility!]
  fields: [MoveField!]
  fullyQualifiedName: String!
  module: MoveModule!
  name: String!
  typeParameters: [MoveDatatypeTypeParameter!]
}
```

### Fields

#### [MoveStruct.<b>abilities</b>](#)[<b>[MoveAbility!]</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Abilities on this struct definition.

#### [MoveStruct.<b>fields</b>](#)[<b>[MoveField!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-field.mdx)   
The names and types of the struct's fields.

Field types reference type parameters by their index in the defining struct's `typeParameters` list.

#### [MoveStruct.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The struct's fully-qualified name, including package address, module name, and datatype name.

#### [MoveStruct.<b>module</b>](#)[<b>MoveModule!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)   
The module that this struct is defined in.

#### [MoveStruct.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The struct's unqualified name.

#### [MoveStruct.<b>typeParameters</b>](#)[<b>[MoveDatatypeTypeParameter!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.mdx)   
Constraints on the struct's formal type parameters.

Move bytecode does not name type parameters, so when they are referenced (e.g. in field types), they are identified by their index in this list.

### Interfaces

#### [<b>IMoveDatatype</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  
Interface implemented by all GraphQL types that represent a Move datatype definition (either a struct or an enum definition).

This interface is used to provide a way to access fields that are shared by both structs and enums, e.g., the module that the datatype belongs to, the name of the datatype, type parameters etc.

### Member Of

[`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  [`MoveStructConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct-connection.md)  [`MoveStructEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct-edge.md)