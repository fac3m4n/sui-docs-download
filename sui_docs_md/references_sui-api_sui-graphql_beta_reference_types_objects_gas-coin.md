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

Access to the gas inputs, after they have been smashed into one coin. The gas coin can only be used by reference, except for with `TransferObjectsTransaction` that can accept it by value.

```graphql
type GasCoin {
  _: Boolean
}
```

### Fields

#### [GasCoin.<b>&#x005F;</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Placeholder field (gas coin has no additional data)

### Implemented By

[`TransactionArgument`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)