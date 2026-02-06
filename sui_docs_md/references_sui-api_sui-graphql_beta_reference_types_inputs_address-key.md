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

Identifies a specific version of an address.

Exactly one of `address` or `name` must be specified. Additionally, at most one of `rootVersion` or `atCheckpoint` can be specified. If neither bound is provided, the address is fetched at the checkpoint being viewed.

See `Query.address` for more details.

```graphql
input AddressKey {
  address: SuiAddress
  atCheckpoint: UInt53
  name: String
  rootVersion: UInt53
}
```

### Fields

#### [AddressKey.<b>address</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
The address.

#### [AddressKey.<b>atCheckpoint</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, sets a checkpoint bound for this address.

#### [AddressKey.<b>name</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
A SuiNS name to resolve to an address.

#### [AddressKey.<b>rootVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
If specified, sets a root version bound for this address.

### Member Of

[`multiGetAddresses`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-addresses.md)