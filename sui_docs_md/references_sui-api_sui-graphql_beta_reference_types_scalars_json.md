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

Arbitrary JSON data.

```graphql
scalar JSON
```

### Member Of

[`Display`](/references/sui-api/sui-graphql/beta/reference/types/objects/display.md)  [`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  [`simulateTransaction`](/references/sui-api/sui-graphql/beta/reference/operations/queries/simulate-transaction.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)