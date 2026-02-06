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
type MoveValue {
  asAddress: Address
  bcs: Base64
  display: Display
  extract(
    path: String!
  ): MoveValue
  format(
    format: String!
  ): JSON
  json: JSON
  type: MoveType
}
```

### Fields

#### [MoveValue.<b>asAddress</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
Attempts to treat this value as an `Address`.

If the value is of type `address` or `0x2::object::ID`, it is interpreted as an address pointer, and it is scoped to the current checkpoint.

If the value is of type `0x2::object::UID`, it is interpreted as a wrapped object whose version is bounded by the root version of the current value. Such values do not support nested owned object queries, but `Address.addressAt` can be used to re-scope it to a checkpoint (defaults to the current checkpoint), instead of a root version, allowing owned object queries.

Values of other types cannot be interpreted as addresses, and `null` is returned.

#### [MoveValue.<b>bcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The BCS representation of this value, Base64-encoded.

#### [MoveValue.<b>display</b>](#)[<b>Display</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/display.md)  
A rendered JSON blob based on an on-chain template, substituted with data from this value.

Returns `null` if the value's type does not have an associated `Display` template.

#### [MoveValue.<b>extract</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
Extract a nested value at the given path.

`path` is a Display v2 'chain' expression, allowing access to nested, named and positional fields, vector indices, VecMap keys, and dynamic (object) field accesses.
##### [MoveValue.extract.<b>path</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveValue.<b>format</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
Render a single Display v2 format string against this value.

Returns `null` if the value does not have a valid type, or if any of the expressions in the format string fail to evaluate (e.g. field does not exist).
##### [MoveValue.format.<b>format</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [MoveValue.<b>json</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
Representation of a Move value in JSON, where:

- Addresses, IDs, and UIDs are represented in canonical form, as JSON strings.
- Bools are represented by JSON boolean literals.
- u8, u16, and u32 are represented as JSON numbers.
- u64, u128, and u256 are represented as JSON strings.
- Balances, Strings, and Urls are represented as JSON strings.
- Vectors of bytes are represented as Base64 blobs, and other vectors are represented by JSON arrays.
- Structs are represented by JSON objects.
- Enums are represented by JSON objects, with a field named `@variant` containing the variant name.
- Empty optional values are represented by `null`.

#### [MoveValue.<b>type</b>](#)[<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
The value's type.

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`CommandOutput`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-output.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`IMoveObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  [`NameRecord`](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  [`Validator`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator.md)  [`ValidatorSet`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-set.md)  

### Implemented By

[`DynamicFieldValue`](/references/sui-api/sui-graphql/beta/reference/types/unions/dynamic-field-value.md)  [`TransactionInput`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)