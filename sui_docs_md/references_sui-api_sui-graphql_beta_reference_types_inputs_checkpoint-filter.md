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
input CheckpointFilter {
  afterCheckpoint: UInt53
  atCheckpoint: UInt53
  atEpoch: UInt53
  beforeCheckpoint: UInt53
}
```

### Fields

#### [CheckpointFilter.<b>afterCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit query results to checkpoints that occured strictly after the given checkpoint.

#### [CheckpointFilter.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit query results to checkpoints that occured at the given checkpoint.

#### [CheckpointFilter.<b>atEpoch</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit query results to checkpoints at this epoch.

#### [CheckpointFilter.<b>beforeCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Limit query results to checkpoints that occured strictly before the given checkpoint.

### Member Of

[`checkpoints`](/references/sui-api/sui-graphql/beta/reference/operations/queries/checkpoints.md)