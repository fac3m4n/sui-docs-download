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

An unsigned integer that can hold values up to 2^53 - 1. This can be treated similarly to `Int`, but it is guaranteed to be non-negative, and it may be larger than 2^32 - 1.

```graphql
scalar UInt53
```

### Member Of

[`address`](/references/sui-api/sui-graphql/beta/reference/operations/queries/address.md)  [`AddressKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/address-key.md)  [`AuthenticatorStateExpireTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-expire-transaction.md)  [`AuthenticatorStateUpdateTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-update-transaction.md)  [`BridgeCommitteeInitTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/bridge-committee-init-transaction.md)  [`ChangeEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  [`checkpoint`](/references/sui-api/sui-graphql/beta/reference/operations/queries/checkpoint.md)  [`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`CheckpointFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/checkpoint-filter.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`ConsensusAddressOwner`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-address-owner.md)  [`ConsensusCommitPrologueTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-commit-prologue-transaction.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`epoch`](/references/sui-api/sui-graphql/beta/reference/operations/queries/epoch.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`EventFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/event-filter.md)  [`GasCostSummary`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-cost-summary.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`Linkage`](/references/sui-api/sui-graphql/beta/reference/types/objects/linkage.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`multiGetCheckpoints`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-checkpoints.md)  [`multiGetEpochs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-epochs.md)  [`MutateConsensusStreamEnded`](/references/sui-api/sui-graphql/beta/reference/types/objects/mutate-consensus-stream-ended.md)  [`object`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`ObjectKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-key.md)  [`package`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package.md)  [`PackageCheckpointFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/package-checkpoint-filter.md)  [`PackageKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/package-key.md)  [`protocolConfigs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/protocol-configs.md)  [`ProtocolConfigs`](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)  [`ReadConsensusStreamEnded`](/references/sui-api/sui-graphql/beta/reference/types/objects/read-consensus-stream-ended.md)  [`Shared`](/references/sui-api/sui-graphql/beta/reference/types/objects/shared.md)  [`SharedInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/shared-input.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  [`TransactionFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  [`Validator`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator.md)  [`VersionFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/version-filter.md)