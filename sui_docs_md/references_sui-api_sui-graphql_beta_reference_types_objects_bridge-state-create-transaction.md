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

System transaction for creating bridge state for cross-chain operations.

```graphql
type BridgeStateCreateTransaction {
  chainIdentifier: String
}
```

### Fields

#### [BridgeStateCreateTransaction.<b>chainIdentifier</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The chain identifier for which this bridge state is being created.

### Implemented By

[`EndOfEpochTransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.md)