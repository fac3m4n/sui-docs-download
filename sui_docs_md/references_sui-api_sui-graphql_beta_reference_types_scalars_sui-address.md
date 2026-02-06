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

String containing 32 byte hex-encoded address, with a leading '0x'. Leading zeroes can be omitted on input but will always appear in outputs (SuiAddress in output is guaranteed to be 66 characters long).

```graphql
scalar SuiAddress
```

### Member Of

[`address`](/references/sui-api/sui-graphql/beta/reference/operations/queries/address.md)  [`Address`](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  [`AddressKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/address-key.md)  [`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`ConsensusObjectCancelled`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-object-cancelled.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`EventFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/event-filter.md)  [`IAddressable`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iaddressable.md)  [`Linkage`](/references/sui-api/sui-graphql/beta/reference/types/objects/linkage.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`MutateConsensusStreamEnded`](/references/sui-api/sui-graphql/beta/reference/types/objects/mutate-consensus-stream-ended.md)  [`object`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`ObjectChange`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change.md)  [`ObjectFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)  [`ObjectKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-key.md)  [`objectVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/object-versions.md)  [`package`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package.md)  [`PackageKey`](/references/sui-api/sui-graphql/beta/reference/types/inputs/package-key.md)  [`packageVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package-versions.md)  [`PublishCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/publish-command.md)  [`ReadConsensusStreamEnded`](/references/sui-api/sui-graphql/beta/reference/types/objects/read-consensus-stream-ended.md)  [`SharedInput`](/references/sui-api/sui-graphql/beta/reference/types/objects/shared-input.md)  [`TransactionFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/transaction-filter.md)  [`TypeOrigin`](/references/sui-api/sui-graphql/beta/reference/types/objects/type-origin.md)  [`UpgradeCommand`](/references/sui-api/sui-graphql/beta/reference/types/objects/upgrade-command.md)  [`verifyZkLoginSignature`](/references/sui-api/sui-graphql/beta/reference/operations/queries/verify-zk-login-signature.md)