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

A system transaction that updates epoch information on-chain (increments the current epoch). Executed by the system once per epoch, without using gas. Epoch change transactions cannot be submitted by users, because validators will refuse to sign them.

This transaction kind is deprecated in favour of `EndOfEpochTransaction`.

```graphql
type ChangeEpochTransaction {
  computationCharge: UInt53
  epoch: Epoch
  epochStartTimestamp: DateTime
  nonRefundableStorageFee: UInt53
  protocolConfigs: ProtocolConfigs
  storageCharge: UInt53
  storageRebate: UInt53
  systemPackages(
    first: Int
    after: String
    last: Int
    before: String
  ): MovePackageConnection
}
```

### Fields

#### [ChangeEpochTransaction.<b>computationCharge</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The total amount of gas charged for computation during the epoch.

#### [ChangeEpochTransaction.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
The next (to become) epoch.

#### [ChangeEpochTransaction.<b>epochStartTimestamp</b>](#)[<b>DateTime</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/date-time.md)  
Unix timestamp when epoch started.

#### [ChangeEpochTransaction.<b>nonRefundableStorageFee</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The non-refundable storage fee.

#### [ChangeEpochTransaction.<b>protocolConfigs</b>](#)[<b>ProtocolConfigs</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)  
The epoch's corresponding protocol configuration.

#### [ChangeEpochTransaction.<b>storageCharge</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The total amount of gas charged for storage during the epoch.

#### [ChangeEpochTransaction.<b>storageRebate</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The amount of storage rebate refunded to the transaction senders.

#### [ChangeEpochTransaction.<b>systemPackages</b>](#)[<b>MovePackageConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  
System packages that will be written by validators before the new epoch starts, to upgrade them on-chain. These objects do not have a "previous transaction" because they are not written on-chain yet. Consult `effects.objectChanges` for this transaction to see the actual objects written.
##### [ChangeEpochTransaction.systemPackages.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ChangeEpochTransaction.systemPackages.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ChangeEpochTransaction.systemPackages.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ChangeEpochTransaction.systemPackages.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Implemented By

[`EndOfEpochTransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.md)  [`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)