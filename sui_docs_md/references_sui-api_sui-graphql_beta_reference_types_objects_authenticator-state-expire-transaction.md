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

System transaction that is executed at the end of an epoch to expire JSON Web Keys (JWKs) that are no longer valid, based on their associated epoch. This is part of the on-chain state management for zkLogin and authentication.

```graphql
type AuthenticatorStateExpireTransaction {
  authenticatorObjInitialSharedVersion: UInt53
  minEpoch: Epoch
}
```

### Fields

#### [AuthenticatorStateExpireTransaction.<b>authenticatorObjInitialSharedVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The initial version that the AuthenticatorStateUpdate was shared at.

#### [AuthenticatorStateExpireTransaction.<b>minEpoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
Expire JWKs that have a lower epoch than this.

### Implemented By

[`EndOfEpochTransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/end-of-epoch-transaction-kind.md)