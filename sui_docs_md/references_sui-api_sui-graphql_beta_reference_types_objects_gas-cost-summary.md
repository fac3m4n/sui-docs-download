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

Summary of charges from transactions.

Storage is charged in three parts -- `storage_cost`, `-storage_rebate`, and `non_refundable_storage_fee` -- independently of `computation_cost`.

The overall cost of a transaction, deducted from its gas coins, is its `computation_cost + storage_cost - storage_rebate`. `non_refundable_storage_fee` is collected from objects being mutated or deleted and accumulated by the system in storage funds, the remaining storage costs of previous object versions are what become the `storage_rebate`. The ratio between `non_refundable_storage_fee` and `storage_rebate` is set by the protocol.

```graphql
type GasCostSummary {
  computationCost: UInt53
  nonRefundableStorageFee: UInt53
  storageCost: UInt53
  storageRebate: UInt53
}
```

### Fields

#### [GasCostSummary.<b>computationCost</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The sum cost of computation/execution

#### [GasCostSummary.<b>nonRefundableStorageFee</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Amount that is retained by the system in the storage fund from the cost of the previous versions of objects being mutated or deleted.

#### [GasCostSummary.<b>storageCost</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Cost for storage at the time the transaction is executed, calculated as the size of the objects being mutated in bytes multiplied by a storage cost per byte (part of the protocol).

#### [GasCostSummary.<b>storageRebate</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Amount the user gets back from the storage cost of the previous versions of objects being mutated or deleted.

### Member Of

[`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`GasEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-effects.md)