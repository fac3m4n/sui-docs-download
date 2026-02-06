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

Reservation details for a withdrawal.

```graphql
union WithdrawalReservation = WithdrawMaxAmountU64
```

### Possible types

#### [WithdrawalReservation.<b>WithdrawMaxAmountU64</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/withdraw-max-amount-u64.md)  

### Member Of

[`BalanceWithdraw`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-withdraw.md)