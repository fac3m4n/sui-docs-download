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

A value produced or modified during command execution.

This can represent either a return value from a command or an argument that was mutated by reference.

```graphql
type CommandOutput {
  argument: TransactionArgument
  value: MoveValue
}
```

### Fields

#### [CommandOutput.<b>argument</b>](#)[<b>TransactionArgument</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)  
The transaction argument that this value corresponds to (if any).

#### [CommandOutput.<b>value</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
The structured Move value, if available.

### Member Of

[`CommandResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-result.md)