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

Object is exclusively owned by a single object, and is mutable. Note that the owning object may be inaccessible because it is wrapped.

```graphql
type ObjectOwner {
  address: Address
}
```

### Fields

#### [ObjectOwner.<b>address</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The owner's address.

### Implemented By

[`Owner`](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)