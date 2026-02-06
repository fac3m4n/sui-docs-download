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

Declaration of a type parameter on a Move function.

```graphql
type MoveFunctionTypeParameter {
  constraints: [MoveAbility!]!
}
```

### Fields

#### [MoveFunctionTypeParameter.<b>constraints</b>](#)[<b>[MoveAbility!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
Ability constraints on this type parameter.

### Member Of

[`MoveFunction`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)