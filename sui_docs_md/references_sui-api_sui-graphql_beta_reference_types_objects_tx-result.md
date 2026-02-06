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

The result of another command.

```graphql
type TxResult {
  cmd: Int
  ix: Int
}
```

### Fields

#### [TxResult.<b>cmd</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
The index of the command that produced this result.

#### [TxResult.<b>ix</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
For nested results, the index within the result.

### Implemented By

[`TransactionArgument`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)