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

Abilities are keywords in Sui Move that define how types behave at the compiler level.

```graphql
enum MoveAbility {
  COPY
  DROP
  KEY
  STORE
}
```

### Values

#### [MoveAbility.<b>COPY</b>](#)  
Enables values to be copied.

#### [MoveAbility.<b>DROP</b>](#)  
Enables values to be popped/dropped.

#### [MoveAbility.<b>KEY</b>](#)  
Enables values to be held directly in global storage.

#### [MoveAbility.<b>STORE</b>](#)  
Enables values to be held inside a struct in global storage.

### Member Of

[`IMoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-datatype.md)  [`MoveDatatype`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype.md)  [`MoveDatatypeTypeParameter`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.md)  [`MoveEnum`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum.md)  [`MoveFunctionTypeParameter`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-type-parameter.md)  [`MoveStruct`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct.md)  [`MoveType`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)