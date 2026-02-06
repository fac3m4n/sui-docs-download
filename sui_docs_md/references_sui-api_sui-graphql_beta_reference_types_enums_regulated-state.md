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

Whether the currency is regulated or not.

```graphql
enum RegulatedState {
  REGULATED
  UNREGULATED
}
```

### Values

#### [RegulatedState.<b>REGULATED</b>](#)  
A `DenyCap` or a `RegulatedCoinMetadata` exists for this currency.

#### [RegulatedState.<b>UNREGULATED</b>](#)  
The currency was created without a deny list.

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)