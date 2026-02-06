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

Fetch the protocol config by protocol version, or the latest protocol config used on chain if no version is provided.

```graphql
protocolConfigs(
  version: UInt53
): ProtocolConfigs
```

### Arguments

#### [protocolConfigs.<b>version</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  

### Type

#### [<b>ProtocolConfigs</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)  
Constants that control how the chain operates.

These can only change during protocol upgrades which happen on epoch boundaries. Configuration is split into feature flags (which are just booleans), and configs which can take any value (including no value at all), and will be represented by a string.