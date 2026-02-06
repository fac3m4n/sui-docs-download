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

Paginate checkpoints in the network, optionally bounded to checkpoints in the given epoch.

```graphql
checkpoints(
  first: Int
  after: String
  last: Int
  before: String
  filter: CheckpointFilter
): CheckpointConnection
```

### Arguments

#### [checkpoints.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [checkpoints.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [checkpoints.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

#### [checkpoints.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [checkpoints.<b>filter</b>](#)[<b>CheckpointFilter</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/checkpoint-filter.md)  

### Type

#### [<b>CheckpointConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-connection.md)