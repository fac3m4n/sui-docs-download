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

A function defined in a Move module.

```graphql
type MoveFunction {
  fullyQualifiedName: String!
  isEntry: Boolean
  module: MoveModule!
  name: String!
  parameters: [OpenMoveType!]
  return: [OpenMoveType!]
  typeParameters: [MoveFunctionTypeParameter!]
  visibility: MoveVisibility
}
```

### Fields

#### [MoveFunction.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The function's fully-qualified name, including package address, module name, and function name.

#### [MoveFunction.<b>isEntry</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether the function is marked `entry` or not.

#### [MoveFunction.<b>module</b>](#)[<b>MoveModule!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)   
The module that this function is defined in.

#### [MoveFunction.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The function's unqualified name.

#### [MoveFunction.<b>parameters</b>](#)[<b>[OpenMoveType!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/open-move-type.mdx)   
The function's parameter types. These types can reference type parameters introduced by this function (see `typeParameters`).

#### [MoveFunction.<b>return</b>](#)[<b>[OpenMoveType!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/open-move-type.mdx)   
The function's return types. There can be multiple because functions in Move can return multiple values. These types can reference type parameters introduced by this function (see `typeParameters`).

#### [MoveFunction.<b>typeParameters</b>](#)[<b>[MoveFunctionTypeParameter!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-type-parameter.mdx)   
Constraints on the function's formal type parameters.

Move bytecode does not name type parameters, so when they are referenced (e.g. in parameter and return types), they are identified by their index in this list.

#### [MoveFunction.<b>visibility</b>](#)[<b>MoveVisibility</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-visibility.md)  
The function's visibility: `public`, `public(friend)`, or `private`.

### Member Of

[`ExecutionError`](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-error.md)  [`MoveCallCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-call-command.md)  [`MoveFunctionConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-connection.md)  [`MoveFunctionEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-edge.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)