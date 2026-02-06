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

Filter for paginating packages published within a range of checkpoints.

```graphql
input PackageCheckpointFilter {
  afterCheckpoint: UInt53
  beforeCheckpoint: UInt53
}
```

### Fields

#### [PackageCheckpointFilter.<b>afterCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to packages that were published strictly after this checkpoint, defaults to fetching from the earliest checkpoint known to this RPC (this could be the genesis checkpoint, or some later checkpoint if data has been pruned).

#### [PackageCheckpointFilter.<b>beforeCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Filter to packages published strictly before this checkpoint, defaults to fetching up to the latest checkpoint (inclusive).

### Member Of

[`packages`](/references/sui-api/sui-graphql/beta/reference/operations/queries/packages.md)