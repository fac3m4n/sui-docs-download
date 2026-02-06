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

Constants that control how the chain operates.

These can only change during protocol upgrades which happen on epoch boundaries. Configuration is split into feature flags (which are just booleans), and configs which can take any value (including no value at all), and will be represented by a string.

```graphql
type ProtocolConfigs {
  config(
    key: String!
  ): ProtocolConfig
  configs: [ProtocolConfig!]!
  featureFlag(
    key: String!
  ): FeatureFlag
  featureFlags: [FeatureFlag!]!
  protocolVersion: UInt53!
}
```

### Fields

#### [ProtocolConfigs.<b>config</b>](#)[<b>ProtocolConfig</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-config.md)  
Query for the value of the configuration with name `key`.
##### [ProtocolConfigs.config.<b>key</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [ProtocolConfigs.<b>configs</b>](#)[<b>[ProtocolConfig!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-config.mdx)   
List all available configurations and their values.

#### [ProtocolConfigs.<b>featureFlag</b>](#)[<b>FeatureFlag</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/feature-flag.md)  
Query for the state of the feature flag with name `key`.
##### [ProtocolConfigs.featureFlag.<b>key</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [ProtocolConfigs.<b>featureFlags</b>](#)[<b>[FeatureFlag!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/feature-flag.mdx)   
List all available feature flags and their values.

#### [ProtocolConfigs.<b>protocolVersion</b>](#)[<b>UInt53!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)   

### Returned By

[`protocolConfigs`](/references/sui-api/sui-graphql/beta/reference/operations/queries/protocol-configs.md)  

### Member Of

[`ChangeEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)