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

The account to withdraw funds from.

```graphql
enum WithdrawFrom {
  SENDER
  SPONSOR
}
```

### Values

#### [WithdrawFrom.<b>SENDER</b>](#)  
The funds are withdrawn from the transaction sender's account.

#### [WithdrawFrom.<b>SPONSOR</b>](#)  
The funds are withdrawn from the sponsor's account.

### Member Of

[`BalanceWithdraw`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-withdraw.md)