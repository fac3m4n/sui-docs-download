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

Future behavior of a currency's supply.

```graphql
enum SupplyState {
  BURN_ONLY
  FIXED
}
```

### Values

#### [SupplyState.<b>BURN&#x005F;ONLY</b>](#)  
The supply can only decrease.

#### [SupplyState.<b>FIXED</b>](#)  
The supply can neither increase nor decrease.

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)