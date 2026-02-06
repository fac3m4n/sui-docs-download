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

String representation of an arbitrary width, possibly signed integer

```graphql
scalar BigInt
```

### Member Of

[`Balance`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance.md)  [`BalanceChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`ExecutionError`](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-error.md)  [`GasInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-input.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`WithdrawMaxAmountU64`](/references/sui-api/sui-graphql/beta/reference/types/objects/withdraw-max-amount-u64.md)