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

Simulate a transaction to preview its effects without executing it on chain.

Accepts a JSON transaction matching the [Sui gRPC API schema](https://docs.sui.io/references/fullnode-protocol#sui-rpc-v2-Transaction).
The JSON format allows for partial transaction specification where certain fields can be automatically resolved by the server.

Alternatively, for already serialized transactions, you can pass BCS-encoded data:
`{"bcs": {"value": ""}}`

Unlike `executeTransaction`, this does not require signatures since the transaction is not committed to the blockchain. This allows for previewing transaction effects, estimating gas costs, and testing transaction logic without spending gas or requiring valid signatures.

- `checksEnabled`: If true, enables transaction validation checks during simulation. Defaults to true.
- `doGasSelection`: If true, enables automatic gas coin selection and budget estimation. Defaults to false.

```graphql
simulateTransaction(
  transaction: JSON!
  checksEnabled: Boolean
  doGasSelection: Boolean
): SimulationResult!
```

### Arguments

#### [<code style={{ fontWeight: 'normal' }}>simulateTransaction.<b>transaction</code>](#)[<b>JSON!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)   

#### [simulateTransaction.<b>checksEnabled</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  

#### [simulateTransaction.<b>doGasSelection</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  

### Type

#### [<b>SimulationResult</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/simulation-result.md)  
The result of simulating a transaction, including the predicted effects and any errors.