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

Transfers `inputs` to `address`. All inputs must have the `store` ability (allows public transfer) and must not be previously immutable or shared.

```graphql
type TransferObjectsCommand {
  address: TransactionArgument
  inputs: [TransactionArgument!]!
}
```

### Fields

#### [TransferObjectsCommand.<b>address</b>](#)[<b>TransactionArgument</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)  
The address to transfer to.

#### [TransferObjectsCommand.<b>inputs</b>](#)[<b>[TransactionArgument!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.mdx)   
The objects to transfer.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)