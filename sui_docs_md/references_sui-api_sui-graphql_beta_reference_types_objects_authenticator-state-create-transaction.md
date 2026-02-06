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

System transaction for creating the on-chain state used by zkLogin.

```graphql
type AuthenticatorStateCreateTransaction {
  _: Boolean
}
```

### Fields

#### [AuthenticatorStateCreateTransaction.<b>&#x005F;</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
A workaround to define an empty variant of a GraphQL union.

### Implemented By

[`EndOfEpochTransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.md)