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

The `Boolean` scalar type represents `true` or `false`.

```graphql
scalar Boolean
```

### Member Of

[`AccumulatorRootCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/accumulator-root-create-transaction.md)  [`AddressAliasStateCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/address-alias-state-create-transaction.md)  [`AuthenticatorStateCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-create-transaction.md)  [`CoinDenyListStateCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-deny-list-state-create-transaction.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`CoinRegistryCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-registry-create-transaction.md)  [`DisplayRegistryCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/display-registry-create-transaction.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`FeatureFlag`](/references/sui-api/sui-graphql/beta/reference/types/objects/feature-flag.md)  [`GasCoin`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-coin.md)  [`Immutable`](/references/sui-api/sui-graphql/beta/reference/types/objects/immutable.md)  [`IMoveObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  [`include`](/references/sui-api/sui-graphql/beta/reference/operations/directives/include.md)  [`MoveDatatypeTypeParameter`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-type-parameter.md)  [`MoveFunction`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`ObjectChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change.md)  [`OtherCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/other-command.md)  [`PageInfo`](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)  [`RandomnessStateCreateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/randomness-state-create-transaction.md)  [`SharedInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/shared-input.md)  [`simulateTransaction`](/references/sui-api/sui-graphql/beta/reference/operations/queries/simulate-transaction.md)  [`skip`](/references/sui-api/sui-graphql/beta/reference/operations/directives/skip.md)  [`StoreExecutionTimeObservationsTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/store-execution-time-observations-transaction.md)  [`WriteAccumulatorStorageCostTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/write-accumulator-storage-cost-transaction.md)  [`ZkLoginVerifyResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/zk-login-verify-result.md)