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

Object is exclusively owned by a single adderss and sequenced via consensus.

```graphql
type ConsensusAddressOwner {
  address: Address
  startVersion: UInt53
}
```

### Fields

#### [ConsensusAddressOwner.<b>address</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The owner's address.

#### [ConsensusAddressOwner.<b>startVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The version at which the object most recently bcame a consensus object. This serves the same function as `Shared.initialSharedVersion`, except it may change if the object's `owner` type changes.

### Implemented By

[`Owner`](/references/sui-api/sui-graphql/beta/reference/types/unions/owner.md)