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

Execute a transaction, committing its effects on chain.

- `transactionDataBcs` contains the BCS-encoded transaction data (Base64-encoded).
- `signatures` are a list of `flag || signature || pubkey` bytes, Base64-encoded.

Waits until the transaction has reached finality on chain to return its transaction digest, or returns the error that prevented finality if that was not possible. A transaction is final when its effects are guaranteed on chain (it cannot be revoked).

There may be a delay between transaction finality and when GraphQL requests (including the request that issued the transaction) reflect its effects. As a result, queries that depend on indexing the state of the chain (e.g. contents of output objects, address-level balance information at the time of the transaction), must wait for indexing to catch up by polling for the transaction digest using `Query.transaction`.

```graphql
executeTransaction(
  transactionDataBcs: Base64!
  signatures: [Base64!]!
): ExecutionResult!
```

### Arguments

#### [executeTransaction.<b>transactionDataBcs</b>](#)[<b>Base64!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)   

#### [executeTransaction.<b>signatures</b>](#)[<b>[Base64!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.mdx)   

### Type

#### [<b>ExecutionResult</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-result.md)  
The execution result of a transaction, including the transaction effects and any potential errors due to signing or quorum-driving.