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

ProgrammableSystemTransaction is identical to ProgrammableTransaction, but GraphQL does not allow multiple variants with the same type.

```graphql
type ProgrammableSystemTransaction {
  commands(
    first: Int
    after: String
    last: Int
    before: String
  ): CommandConnection
  inputs(
    first: Int
    after: String
    last: Int
    before: String
  ): TransactionInputConnection
}
```

### Fields

#### [ProgrammableSystemTransaction.<b>commands</b>](#)[<b>CommandConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-connection.md)  
The transaction commands, executed sequentially.
##### [ProgrammableSystemTransaction.commands.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableSystemTransaction.commands.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ProgrammableSystemTransaction.commands.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableSystemTransaction.commands.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [ProgrammableSystemTransaction.<b>inputs</b>](#)[<b>TransactionInputConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-connection.md)  
Input objects or primitive values.
##### [ProgrammableSystemTransaction.inputs.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableSystemTransaction.inputs.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ProgrammableSystemTransaction.inputs.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableSystemTransaction.inputs.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Implemented By

[`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)