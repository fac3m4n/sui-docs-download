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

Input for withdrawing funds from an accumulator.

```graphql
type BalanceWithdraw {
  reservation: WithdrawalReservation
  type: MoveType
  withdrawFrom: WithdrawFrom
}
```

### Fields

#### [BalanceWithdraw.<b>reservation</b>](#)[<b>WithdrawalReservation</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/withdrawal-reservation.md)  
How much to withdraw from the accumulator.

#### [BalanceWithdraw.<b>type</b>](#)[<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
The type of the funds accumulator to withdraw from (e.g. `0x2::balance::Balance<0x2::sui::SUI>`).

#### [BalanceWithdraw.<b>withdrawFrom</b>](#)[<b>WithdrawFrom</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/withdraw-from.md)  
The account to withdraw funds from.

### Implemented By

[`TransactionInput`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-input.md)