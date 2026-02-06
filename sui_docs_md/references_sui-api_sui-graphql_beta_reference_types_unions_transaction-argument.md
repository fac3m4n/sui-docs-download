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

An argument to a programmable transaction command.

```graphql
union TransactionArgument = GasCoin | Input | TxResult
```

### Possible types

#### [TransactionArgument.<b>GasCoin</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-coin.md)  
Access to the gas inputs, after they have been smashed into one coin. The gas coin can only be used by reference, except for with `TransferObjectsTransaction` that can accept it by value.

#### [TransactionArgument.<b>Input</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/input.md)  

#### [TransactionArgument.<b>TxResult</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/tx-result.md)  
The result of another command.

### Member Of

[`CommandOutput`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-output.md)  [`MakeMoveVecCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/make-move-vec-command.md)  [`MergeCoinsCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/merge-coins-command.md)  [`MoveCallCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-call-command.md)  [`SplitCoinsCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/split-coins-command.md)  [`TransferObjectsCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/transfer-objects-command.md)  [`UpgradeCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/upgrade-command.md)