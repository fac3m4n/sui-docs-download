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

Fetch transactions by their digests.

Returns a list of transactions that is guaranteed to be the same length as `keys`. If a digest in `keys` could not be found in the store, its corresponding entry in the result will be `null`. This could be because the transaction never existed, or because it was pruned.

```graphql
multiGetTransactions(
  keys: [String!]!
): [Transaction]!
```

### Arguments

#### [multiGetTransactions.<b>keys</b>](#)[<b>[String!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

### Type

#### [<b>Transaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  
Description of a transaction, the unit of activity on Sui.