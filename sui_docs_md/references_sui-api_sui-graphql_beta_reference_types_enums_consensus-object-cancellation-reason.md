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

Reason why a transaction that attempted to access a consensus-managed object was cancelled.

```graphql
enum ConsensusObjectCancellationReason {
  CANCELLED_READ
  CONGESTED
  RANDOMNESS_UNAVAILABLE
  UNKNOWN
}
```

### Values

#### [ConsensusObjectCancellationReason.<b>CANCELLED&#x005F;READ</b>](#)  
Read operation was cancelled.

#### [ConsensusObjectCancellationReason.<b>CONGESTED</b>](#)  
Object congestion prevented execution.

#### [ConsensusObjectCancellationReason.<b>RANDOMNESS&#x005F;UNAVAILABLE</b>](#)  
Randomness service was unavailable.

#### [ConsensusObjectCancellationReason.<b>UNKNOWN</b>](#)  
Internal use only.

### Member Of

[`ConsensusObjectCancelled`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-object-cancelled.md)