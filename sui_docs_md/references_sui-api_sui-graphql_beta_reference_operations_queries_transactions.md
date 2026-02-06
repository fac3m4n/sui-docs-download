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

The transactions that exist in the network, optionally filtered by transaction filters.

```graphql
transactions(
  first: Int
  after: String
  last: Int
  before: String
  filter: TransactionFilter
): TransactionConnection
```

### Arguments

#### [transactions.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [transactions.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [transactions.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [transactions.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [transactions.<b>filter</b>](#)[<b>TransactionFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  

### Type

#### [<b>TransactionConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)