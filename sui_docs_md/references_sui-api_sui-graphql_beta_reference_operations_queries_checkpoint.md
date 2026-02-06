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

Fetch a checkpoint by its sequence number, or the latest checkpoint if no sequence number is provided.

Returns `null` if the checkpoint does not exist in the store, either because it never existed or because it was pruned.

```graphql
checkpoint(
  sequenceNumber: UInt53
): Checkpoint
```

### Arguments

#### [checkpoint.<b>sequenceNumber</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

### Type

#### [<b>Checkpoint</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  
Checkpoints contain finalized transactions and are used for node synchronization and global transaction ordering.