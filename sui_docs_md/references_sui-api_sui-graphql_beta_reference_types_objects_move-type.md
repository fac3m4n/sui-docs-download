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

Represents instances of concrete types (no type parameters, no references).

```graphql
type MoveType {
  abilities: [MoveAbility!]
  layout: MoveTypeLayout
  repr: String!
  signature: MoveTypeSignature!
}
```

### Fields

#### [MoveType.<b>abilities</b>](#)[<b>[MoveAbility!]</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/move-ability.mdx)   
The abilities this concrete type has. Returns no abilities if the type is invalid.

#### [MoveType.<b>layout</b>](#)[<b>MoveTypeLayout</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/move-type-layout.md)  
Structured representation of the "shape" of values that match this type. May return no
layout if the type is invalid.

#### [MoveType.<b>repr</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
Flat representation of the type signature, as a displayable string.

#### [MoveType.<b>signature</b>](#)[<b>MoveTypeSignature!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/move-type-signature.md)   
Structured representation of the type signature.

### Returned By

[`multiGetTypes`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-types.md)  [`type`](/references/sui-api/sui-graphql/beta/reference/operations/queries/type.md)  

### Member Of

[`Balance`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  [`BalanceChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change.md)  [`BalanceWithdraw`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-withdraw.md)  [`MakeMoveVecCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/make-move-vec-command.md)  [`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)