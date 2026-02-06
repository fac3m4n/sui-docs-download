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

Fetch a transaction by its digest.

Returns `null` if the transaction does not exist in the store, either because it never existed or because it was pruned.

```graphql
transaction(
  digest: String!
): Transaction
```

### Arguments

#### [transaction.<b>digest</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

### Type

#### [<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
Description of a transaction, the unit of activity on Sui.