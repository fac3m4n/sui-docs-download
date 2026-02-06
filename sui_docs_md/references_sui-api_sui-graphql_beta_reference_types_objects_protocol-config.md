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

A protocol configuration that can hold an arbitrary value (or no value at all).

```graphql
type ProtocolConfig {
  key: String!
  value: String
}
```

### Fields

#### [ProtocolConfig.<b>key</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
Configuration name.

#### [ProtocolConfig.<b>value</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
Configuration value.

### Member Of

[`ProtocolConfigs`](/references/sui-api/sui-graphql/beta/reference/types/objects/protocol-configs.md)