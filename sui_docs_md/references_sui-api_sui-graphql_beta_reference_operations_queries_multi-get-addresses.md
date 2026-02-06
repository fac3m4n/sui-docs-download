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

Fetch addresses by their keys.

Returns a list of addresses that is guaranteed to be the same length as `keys`. If an address in `keys` is fetched by name and the name does not resolve to an address, its corresponding entry in the result will be `null`.

```graphql
multiGetAddresses(
  keys: [AddressKey!]!
): [Address]!
```

### Arguments

#### [multiGetAddresses.<b>keys</b>](#)[<b>[AddressKey!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/address-key.mdx)   

### Type

#### [<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)