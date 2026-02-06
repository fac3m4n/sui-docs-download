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

Input argument to a Programmable Transaction Block (PTB) command.

```graphql
union TransactionInput = Pure | MoveValue | OwnedOrImmutable | SharedInput | Receiving | BalanceWithdraw
```

### Possible types

#### [TransactionInput.<b>Pure</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/pure.md)  
BCS encoded primitive value (not an object or Move struct).

#### [TransactionInput.<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  

#### [TransactionInput.<b>OwnedOrImmutable</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/owned-or-immutable.md)  
A Move object, either immutable, or owned mutable.

#### [TransactionInput.<b>SharedInput</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/shared-input.md)  
A Move object that's shared.

#### [TransactionInput.<b>Receiving</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/receiving.md)  
A Move object that can be received in this transaction.

#### [TransactionInput.<b>BalanceWithdraw</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-withdraw.md)  
Input for withdrawing funds from an accumulator.

### Member Of

[`TransactionInputConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-connection.md)  [`TransactionInputEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-edge.md)