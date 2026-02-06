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

Fetch checkpoints by their sequence numbers.

Returns a list of checkpoints that is guaranteed to be the same length as `keys`. If a checkpoint in `keys` could not be found in the store, its corresponding entry in the result will be `null`. This could be because the checkpoint does not exist yet, or because it was pruned.

```graphql
multiGetCheckpoints(
  keys: [UInt53!]!
): [Checkpoint]!
```

### Arguments

#### [multiGetCheckpoints.<b>keys</b>](#)[<b>[UInt53!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.mdx)   

### Type

#### [<b>Checkpoint</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  
Checkpoints contain finalized transactions and are used for node synchronization and global transaction ordering.