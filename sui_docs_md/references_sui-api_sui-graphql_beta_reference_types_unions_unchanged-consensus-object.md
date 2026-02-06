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

Details pertaining to consensus-managed objects that are referenced by but not changed by a transaction.

```graphql
union UnchangedConsensusObject = ConsensusObjectRead | MutateConsensusStreamEnded | ReadConsensusStreamEnded | ConsensusObjectCancelled | PerEpochConfig
```

### Possible types

#### [UnchangedConsensusObject.<b>ConsensusObjectRead</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-object-read.md)  

#### [UnchangedConsensusObject.<b>MutateConsensusStreamEnded</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/mutate-consensus-stream-ended.md)  
A transaction that wanted to mutate a consensus-managed object but couldn't because it became not-consensus-managed before the transaction executed (for example, it was deleted, turned into an owned object, or wrapped).

#### [UnchangedConsensusObject.<b>ReadConsensusStreamEnded</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/read-consensus-stream-ended.md)  
A transaction that wanted to read a consensus-managed object but couldn't because it became not-consensus-managed before the transaction executed (for example, it was deleted, turned into an owned object, or wrapped).

#### [UnchangedConsensusObject.<b>ConsensusObjectCancelled</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-object-cancelled.md)  
A transaction that was cancelled before it could access the consensus-managed object, so the object was an input but remained unchanged.

#### [UnchangedConsensusObject.<b>PerEpochConfig</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/per-epoch-config.md)  

### Member Of

[`UnchangedConsensusObjectConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/unchanged-consensus-object-connection.md)  [`UnchangedConsensusObjectEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/unchanged-consensus-object-edge.md)