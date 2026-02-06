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

Fetch the CoinMetadata for a given coin type.

Returns `null` if no CoinMetadata object exists for the given coin type.

```graphql
coinMetadata(
  coinType: String!
): CoinMetadata
```

### Arguments

#### [coinMetadata.<b>coinType</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

### Type

#### [<b>CoinMetadata</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  
An object representing metadata about a coin type.