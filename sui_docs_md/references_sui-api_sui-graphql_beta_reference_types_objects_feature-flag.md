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

A boolean protocol configuration.

```graphql
type FeatureFlag {
  key: String!
  value: Boolean!
}
```

### Fields

#### [FeatureFlag.<b>key</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
Feature flag name.

#### [FeatureFlag.<b>value</b>](#)[<b>Boolean!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)   
Feature flag value.

### Member Of

[`ProtocolConfigs`](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)