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

The object's owner kind.

```graphql
union Owner = AddressOwner | ObjectOwner | Shared | Immutable | ConsensusAddressOwner
```

### Possible types

#### [Owner.<b>AddressOwner</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address-owner.md)  
Object is exclusively owned by a single address, and is mutable.

#### [Owner.<b>ObjectOwner</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object-owner.md)  
Object is exclusively owned by a single object, and is mutable. Note that the owning object may be inaccessible because it is wrapped.

#### [Owner.<b>Shared</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/shared.md)  
Object is shared, can be used by any address, and is mutable.

#### [Owner.<b>Immutable</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/immutable.md)  
Object is accessible to all addresses, and is immutable.

#### [Owner.<b>ConsensusAddressOwner</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-address-owner.md)  
Object is exclusively owned by a single adderss and sequenced via consensus.

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)