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

Fetch transaction effects by its transaction's digest.

Returns `null` if the transaction effects do not exist in the store, either because that transaction was not executed, or it was pruned.

```graphql
transactionEffects(
  digest: String!
): TransactionEffects
```

### Arguments

#### [transactionEffects.<b>digest</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

### Type

#### [<b>TransactionEffects</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  
The results of executing a transaction.