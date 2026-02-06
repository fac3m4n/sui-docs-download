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

No description

```graphql
type WithdrawMaxAmountU64 {
  amount: BigInt
}
```

### Fields

#### [WithdrawMaxAmountU64.<b>amount</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  

### Implemented By

[`WithdrawalReservation`](/references/sui-api/sui-graphql/beta/reference/types/unions/withdrawal-reservation.md)