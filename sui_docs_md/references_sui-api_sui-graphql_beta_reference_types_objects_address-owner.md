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

Object is exclusively owned by a single address, and is mutable.

```graphql
type AddressOwner {
  address: Address
}
```

### Fields

#### [AddressOwner.<b>address</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The owner's address.

### Implemented By

[`Owner`](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)