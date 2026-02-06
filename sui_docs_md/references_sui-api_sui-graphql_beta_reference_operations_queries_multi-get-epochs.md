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

Fetch epochs by their IDs.

Returns a list of epochs that is guaranteed to be the same length as `keys`. If an epoch in `keys` could not be found in the store, its corresponding entry in the result will be `null`. This could be because the epoch does not exist yet, or because it was pruned.

```graphql
multiGetEpochs(
  keys: [UInt53!]!
): [Epoch]!
```

### Arguments

#### [multiGetEpochs.<b>keys</b>](#)[<b>[UInt53!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.mdx)   

### Type

#### [<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
Activity on Sui is partitioned in time, into epochs.

Epoch changes are opportunities for the network to reconfigure itself (perform protocol or system package upgrades, or change the committee) and distribute staking rewards. The network aims to keep epochs roughly the same duration as each other.

During a particular epoch the following data is fixed:

- protocol version,
- reference gas price,
- system package versions,
- validators in the committee.