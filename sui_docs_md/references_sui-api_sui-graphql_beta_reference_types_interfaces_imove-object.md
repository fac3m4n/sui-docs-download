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

Interface implemented by types that represent a Move object on-chain (A Move value whose type has `key`).

```graphql
interface IMoveObject {
  contents: MoveValue
  dynamicField(
    name: DynamicFieldName!
  ): DynamicField
  dynamicFields(
    first: Int
    after: String
    last: Int
    before: String
  ): DynamicFieldConnection
  dynamicObjectField(
    name: DynamicFieldName!
  ): DynamicField
  hasPublicTransfer: Boolean
  moveObjectBcs: Base64
  multiGetDynamicFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
  multiGetDynamicObjectFields(
    keys: [DynamicFieldName!]!
  ): [DynamicField]!
}
```

### Fields

#### [IMoveObject.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The structured representation of the object's contents.

#### [IMoveObject.<b>dynamicField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic field with that name could not be found attached to this object.
##### [IMoveObject.dynamicField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [IMoveObject.<b>dynamicFields</b>](#)[<b>DynamicFieldConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  
Dynamic fields and dynamic object fields owned by this object.

Dynamic fields on wrapped objects can be accessed using `Address.dynamicFields`.
##### [IMoveObject.dynamicFields.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IMoveObject.dynamicFields.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [IMoveObject.dynamicFields.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [IMoveObject.dynamicFields.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [IMoveObject.<b>dynamicObjectField</b>](#)[<b>DynamicField</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  
Access a dynamic object field on an object using its type and BCS-encoded name.

Returns `null` if a dynamic object field with that name could not be found attached to this object.
##### [IMoveObject.dynamicObjectField.<b>name</b>](#)[<b>DynamicFieldName!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)   

#### [IMoveObject.<b>hasPublicTransfer</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether this object can be transfered using the `TransferObjects` Programmable Transaction Command or `sui::transfer::public_transfer`.

Both these operations require the object to have both the `key` and `store` abilities.

#### [IMoveObject.<b>moveObjectBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialize of this object, as a `MoveObject`.

#### [IMoveObject.<b>multiGetDynamicFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic fields on an object using their types and BCS-encoded names.

Returns a list of dynamic fields that is guaranteed to be the same length as `keys`. If a dynamic field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [IMoveObject.multiGetDynamicFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

#### [IMoveObject.<b>multiGetDynamicObjectFields</b>](#)[<b>[DynamicField]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.mdx)   
Access dynamic object fields on an object using their types and BCS-encoded names.

Returns a list of dynamic object fields that is guaranteed to be the same length as `keys`. If a dynamic object field in `keys` could not be found in the store, its corresponding entry in the result will be `null`.
##### [IMoveObject.multiGetDynamicObjectFields.<b>keys</b>](#)[<b>[DynamicFieldName!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.mdx)   

### Implemented By

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)