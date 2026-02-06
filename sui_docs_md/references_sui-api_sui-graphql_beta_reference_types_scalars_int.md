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

The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.

```graphql
scalar Int
```

### Member Of

[`checkpoints`](/references/sui-api/sui-graphql/beta/reference/operations/queries/checkpoints.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`epochs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/epochs.md)  [`events`](/references/sui-api/sui-graphql/beta/reference/operations/queries/events.md)  [`ExecutionError`](/references/sui-api/sui-graphql/beta/reference/types/objects/execution-error.md)  [`Input`](/references/sui-api/sui-graphql/beta/reference/types/objects/input.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  [`objects`](/references/sui-api/sui-graphql/beta/reference/operations/queries/objects.md)  [`objectVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object-versions.md)  [`packages`](/references/sui-api/sui-graphql/beta/reference/operations/queries/packages.md)  [`packageVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package-versions.md)  [`RandomnessStateUpdateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/randomness-state-update-transaction.md)  [`ServiceConfig`](/references/sui-api/sui-graphql/beta/reference/types/objects/service-config.md)  [`transactions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/transactions.md)  [`TxResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/tx-result.md)  [`ValidatorAggregatedSignature`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-aggregated-signature.md)