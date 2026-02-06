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

No description

```graphql
type ValidatorAggregatedSignature {
  epoch: Epoch
  signature: Base64
  signersMap: [Int!]!
}
```

### Fields

#### [ValidatorAggregatedSignature.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
The epoch when this aggregate signature was produced.

#### [ValidatorAggregatedSignature.<b>signature</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64 encoded BLS12381 aggregated signature.

#### [ValidatorAggregatedSignature.<b>signersMap</b>](#)[<b>[Int!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.mdx)   
The indexes of validators that contributed to this signature.

### Member Of

[`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)