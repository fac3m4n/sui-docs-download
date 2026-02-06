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

An input filter selecting for either system or programmable transactions.

```graphql
enum TransactionKindInput {
  SYSTEM_TX
  PROGRAMMABLE_TX
}
```

### Values

#### [TransactionKindInput.<b>SYSTEM&#x005F;TX</b>](#)  
A system transaction can be one of several types of transactions.
See [unions/transaction-block-kind] for more details.

#### [TransactionKindInput.<b>PROGRAMMABLE&#x005F;TX</b>](#)  
A user submitted transaction block.

### Member Of

[`TransactionFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)