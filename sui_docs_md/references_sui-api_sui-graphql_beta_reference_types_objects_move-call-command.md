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
type MoveCallCommand {
  arguments: [TransactionArgument!]!
  function: MoveFunction!
}
```

### Fields

#### [MoveCallCommand.<b>arguments</b>](#)[<b>[TransactionArgument!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.mdx)   
The actual function parameters passed in for this move call.

#### [MoveCallCommand.<b>function</b>](#)[<b>MoveFunction!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)   
The function being called.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)