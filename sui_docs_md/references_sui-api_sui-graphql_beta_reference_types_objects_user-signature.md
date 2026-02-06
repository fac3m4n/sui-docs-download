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
type UserSignature {
  signatureBytes: Base64
}
```

### Fields

#### [UserSignature.<b>signatureBytes</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The signature bytes, Base64-encoded.
For simple signatures: flag || signature || pubkey
For complex signatures: flag || bcs&#x005F;serialized&#x005F;struct

### Member Of

[`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)