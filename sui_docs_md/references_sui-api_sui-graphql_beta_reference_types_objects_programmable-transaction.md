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
type ProgrammableTransaction {
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

#### [ProgrammableTransaction.<b>commands</b>](#)[<b>CommandConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-connection.md)  
The transaction commands, executed sequentially.
##### [ProgrammableTransaction.commands.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableTransaction.commands.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ProgrammableTransaction.commands.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableTransaction.commands.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [ProgrammableTransaction.<b>inputs</b>](#)[<b>TransactionInputConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-connection.md)  
Input objects or primitive values.
##### [ProgrammableTransaction.inputs.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableTransaction.inputs.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ProgrammableTransaction.inputs.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ProgrammableTransaction.inputs.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Implemented By

[`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)