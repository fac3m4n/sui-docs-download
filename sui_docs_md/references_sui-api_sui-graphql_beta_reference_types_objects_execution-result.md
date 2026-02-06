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

The execution result of a transaction, including the transaction effects and any potential errors due to signing or quorum-driving.

```graphql
type ExecutionResult {
  effects: TransactionEffects
  errors: [String!]
}
```

### Fields

#### [ExecutionResult.<b>effects</b>](#)[<b>TransactionEffects</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  
The effects of the transaction execution, if successful.

#### [ExecutionResult.<b>errors</b>](#)[<b>[String!]</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   
Errors that occurred during execution (e.g., network errors, validation failures).
These are distinct from execution failures within the transaction itself.

### Returned By

[`executeTransaction`](/references/sui-api/sui-graphql/beta/reference/operations/mutations/execute-transaction.md)