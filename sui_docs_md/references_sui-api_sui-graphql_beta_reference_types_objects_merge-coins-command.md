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

Merges `coins` into the first `coin` (produces no results).

```graphql
type MergeCoinsCommand {
  coin: TransactionArgument
  coins: [TransactionArgument!]!
}
```

### Fields

#### [MergeCoinsCommand.<b>coin</b>](#)[<b>TransactionArgument</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)  
The coin to merge into.

#### [MergeCoinsCommand.<b>coins</b>](#)[<b>[TransactionArgument!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.mdx)   
The coins to be merged.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)