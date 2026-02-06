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

String containing Base64-encoded binary data.

```graphql
scalar Base64
```

### Member Of

[`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`DynamicFieldName`](/references/sui-api/sui-graphql/beta/reference/types/inputs/dynamic-field-name.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`executeTransaction`](/references/sui-api/sui-graphql/beta/reference/operations/mutations/execute-transaction.md)  [`IMoveObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/imove-object.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveModule`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`PublishCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/publish-command.md)  [`Pure`](/references/sui-api/sui-graphql/beta/reference/types/objects/pure.md)  [`RandomnessStateUpdateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/randomness-state-update-transaction.md)  [`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  [`UpgradeCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/upgrade-command.md)  [`UserSignature`](/references/sui-api/sui-graphql/beta/reference/types/objects/user-signature.md)  [`ValidatorAggregatedSignature`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-aggregated-signature.md)  [`verifyZkLoginSignature`](/references/sui-api/sui-graphql/beta/reference/operations/queries/verify-zk-login-signature.md)