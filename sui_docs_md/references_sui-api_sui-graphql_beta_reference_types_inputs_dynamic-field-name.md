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

A description of a dynamic field's name.

Names can either be given as serialized `bcs` accompanied by its `type`, or as a Display v2 `literal` expression. Other combinations of inputs are not supported.

```graphql
input DynamicFieldName {
  bcs: Base64
  literal: String
  type: String
}
```

### Fields

#### [DynamicFieldName.<b>bcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of the dynamic field's 'name'.

#### [DynamicFieldName.<b>literal</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The name represented as a Display v2 literal expression.

#### [DynamicFieldName.<b>type</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The type of the dynamic field's name, like 'u64' or '0x2::kiosk::Listing'.