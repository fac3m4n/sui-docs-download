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

The result of simulating a transaction, including the predicted effects and any errors.

```graphql
type SimulationResult {
  effects: TransactionEffects
  error: String
  outputs: [CommandResult!]
}
```

### Fields

#### [SimulationResult.<b>effects</b>](#)[<b>TransactionEffects</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  
The predicted effects of the transaction if it were executed.

`None` if the simulation failed due to an error.

#### [SimulationResult.<b>error</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Error message if the simulation failed.

`None` if the simulation was successful.

#### [SimulationResult.<b>outputs</b>](#)[<b>[CommandResult!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-result.mdx)   
The intermediate outputs for each command of the transaction simulation, including contents of mutated references and return values.

### Returned By

[`simulateTransaction`](/references/sui-api/sui-graphql/beta/reference/operations/queries/simulate-transaction.md)