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

No description

```graphql
union EndOfEpochTransactionKind = ChangeEpochTransaction | AuthenticatorStateCreateTransaction | AuthenticatorStateExpireTransaction | RandomnessStateCreateTransaction | CoinDenyListStateCreateTransaction | StoreExecutionTimeObservationsTransaction | BridgeStateCreateTransaction | BridgeCommitteeInitTransaction | AccumulatorRootCreateTransaction | CoinRegistryCreateTransaction | DisplayRegistryCreateTransaction | AddressAliasStateCreateTransaction | WriteAccumulatorStorageCostTransaction
```

### Possible types

#### [EndOfEpochTransactionKind.<b>ChangeEpochTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  
A system transaction that updates epoch information on-chain (increments the current epoch). Executed by the system once per epoch, without using gas. Epoch change transactions cannot be submitted by users, because validators will refuse to sign them.

This transaction kind is deprecated in favour of `EndOfEpochTransaction`.

#### [EndOfEpochTransactionKind.<b>AuthenticatorStateCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-create-transaction.md)  
System transaction for creating the on-chain state used by zkLogin.

#### [EndOfEpochTransactionKind.<b>AuthenticatorStateExpireTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-expire-transaction.md)  
System transaction that is executed at the end of an epoch to expire JSON Web Keys (JWKs) that are no longer valid, based on their associated epoch. This is part of the on-chain state management for zkLogin and authentication.

#### [EndOfEpochTransactionKind.<b>RandomnessStateCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/randomness-state-create-transaction.md)  
System transaction for creating the on-chain randomness state.

#### [EndOfEpochTransactionKind.<b>CoinDenyListStateCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-deny-list-state-create-transaction.md)  
System transaction for creating the coin deny list state.

#### [EndOfEpochTransactionKind.<b>StoreExecutionTimeObservationsTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/store-execution-time-observations-transaction.md)  
System transaction for storing execution time observations.

#### [EndOfEpochTransactionKind.<b>BridgeStateCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/bridge-state-create-transaction.md)  
System transaction for creating bridge state for cross-chain operations.

#### [EndOfEpochTransactionKind.<b>BridgeCommitteeInitTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/bridge-committee-init-transaction.md)  
System transaction for initializing bridge committee.

#### [EndOfEpochTransactionKind.<b>AccumulatorRootCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/accumulator-root-create-transaction.md)  
System transaction for creating the accumulator root.

#### [EndOfEpochTransactionKind.<b>CoinRegistryCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-registry-create-transaction.md)  
System transaction for creating the coin registry.

#### [EndOfEpochTransactionKind.<b>DisplayRegistryCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/display-registry-create-transaction.md)  
System transaction for creating the display registry.

#### [EndOfEpochTransactionKind.<b>AddressAliasStateCreateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address-alias-state-create-transaction.md)  
System transaction for creating the alias state.

#### [EndOfEpochTransactionKind.<b>WriteAccumulatorStorageCostTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/write-accumulator-storage-cost-transaction.md)  
System transaction for writing the pre-computed storage cost for accumulator objects.

### Member Of

[`EndOfEpochTransactionKindConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction-kind-connection.md)  [`EndOfEpochTransactionKindEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction-kind-edge.md)