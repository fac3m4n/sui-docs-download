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

Modules are a unit of code organization in Move.

Modules belong to packages, and contain type and function definitions.

```graphql
type MoveModule {
  bytes: Base64
  datatype(
    name: String!
  ): MoveDatatype
  datatypes(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveDatatypeConnection
  disassembly: String
  enum(
    name: String!
  ): MoveEnum
  enums(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveEnumConnection
  fileFormatVersion: Int
  friends(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveModuleConnection
  fullyQualifiedName: String!
  function(
    name: String!
  ): MoveFunction
  functions(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveFunctionConnection
  name: String!
  package: MovePackage
  struct(
    name: String!
  ): MoveStruct
  structs(
    first: Int
    after: String
    last: Int
    before: String
  ): MoveStructConnection
}
```

### Fields

#### [MoveModule.<b>bytes</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
Base64 encoded bytes of the serialized CompiledModule.

#### [MoveModule.<b>datatype</b>](#)[<b>MoveDatatype</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  
The datatype (struct or enum) named `name` in this module.
##### [MoveModule.datatype.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveModule.<b>datatypes</b>](#)[<b>MoveDatatypeConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-connection.md)  
Paginate through this module's datatype definitions.
##### [MoveModule.datatypes.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.datatypes.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MoveModule.datatypes.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.datatypes.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MoveModule.<b>disassembly</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Textual representation of the module's bytecode.

#### [MoveModule.<b>enum</b>](#)[<b>MoveEnum</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  
The enum named `name` in this module.
##### [MoveModule.enum.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveModule.<b>enums</b>](#)[<b>MoveEnumConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-connection.md)  
Paginate through this module's enum definitions.
##### [MoveModule.enums.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.enums.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MoveModule.enums.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.enums.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MoveModule.<b>fileFormatVersion</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Bytecode format version.

#### [MoveModule.<b>friends</b>](#)[<b>MoveModuleConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-connection.md)  
Modules that this module considers friends. These modules can call `public(package)` functions in this module.
##### [MoveModule.friends.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.friends.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MoveModule.friends.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.friends.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MoveModule.<b>fullyQualifiedName</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The module's fully-qualified name, including its package address.

#### [MoveModule.<b>function</b>](#)[<b>MoveFunction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)  
The function named `name` in this module.
##### [MoveModule.function.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveModule.<b>functions</b>](#)[<b>MoveFunctionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-connection.md)  
Paginate through this module's function definitions.
##### [MoveModule.functions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.functions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MoveModule.functions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.functions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [MoveModule.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
The module's unqualified name.

#### [MoveModule.<b>package</b>](#)[<b>MovePackage</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  
The package that this module was defined in.

#### [MoveModule.<b>struct</b>](#)[<b>MoveStruct</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)  
The struct named `name` in this module.
##### [MoveModule.struct.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveModule.<b>structs</b>](#)[<b>MoveStructConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct-connection.md)  
Paginate through this module's struct definitions.
##### [MoveModule.structs.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.structs.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [MoveModule.structs.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [MoveModule.structs.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Member Of

[`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`ExecutionError`](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-error.md)  [`IMoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  [`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveEnum`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  [`MoveFunction`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)  [`MoveModuleConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-connection.md)  [`MoveModuleEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-edge.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`MoveStruct`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)