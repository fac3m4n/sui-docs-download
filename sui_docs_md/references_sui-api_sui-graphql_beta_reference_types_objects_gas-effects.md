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

Effects related to gas (costs incurred and the identity of the smashed gas object returned).

```graphql
type GasEffects {
  gasObject: Object
  gasSummary: GasCostSummary
}
```

### Fields

#### [GasEffects.<b>gasObject</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
The gas object used to pay for this transaction. If multiple gas coins were provided, this represents the combined coin after smashing.

#### [GasEffects.<b>gasSummary</b>](#)[<b>GasCostSummary</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-cost-summary.md)  
Breakdown of the gas costs for this transaction.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)