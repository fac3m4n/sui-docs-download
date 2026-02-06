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

The execution status of this transaction: success or failure.

```graphql
enum ExecutionStatus {
  SUCCESS
  FAILURE
}
```

### Values

#### [ExecutionStatus.<b>SUCCESS</b>](#)  
The transaction was successfully executed.

#### [ExecutionStatus.<b>FAILURE</b>](#)  
The transaction could not be executed.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)