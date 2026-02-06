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

The value of a dynamic field (`MoveValue`) or dynamic object field (`MoveObject`).

```graphql
union DynamicFieldValue = MoveObject | MoveValue
```

### Possible types

#### [DynamicFieldValue.<b>MoveObject</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  
A MoveObject is a kind of Object that reprsents data stored on-chain.

#### [DynamicFieldValue.<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  

### Member Of

[`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)