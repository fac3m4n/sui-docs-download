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

Splits off coins with denominations in `amounts` from `coin`, returning multiple results (as many as there are amounts.)

```graphql
type SplitCoinsCommand {
  amounts: [TransactionArgument!]!
  coin: TransactionArgument
}
```

### Fields

#### [SplitCoinsCommand.<b>amounts</b>](#)[<b>[TransactionArgument!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.mdx)   
The denominations to split off from the coin.

#### [SplitCoinsCommand.<b>coin</b>](#)[<b>TransactionArgument</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)  
The coin to split.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)