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
type AuthenticatorStateUpdateTransaction {
  authenticatorObjInitialSharedVersion: UInt53
  epoch: Epoch
  newActiveJwks(
    first: Int
    after: String
    last: Int
    before: String
  ): ActiveJwkConnection
  round: UInt53
}
```

### Fields

#### [AuthenticatorStateUpdateTransaction.<b>authenticatorObjInitialSharedVersion</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The initial version of the authenticator object that it was shared at.

#### [AuthenticatorStateUpdateTransaction.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
Epoch of the authenticator state update transaction.

#### [AuthenticatorStateUpdateTransaction.<b>newActiveJwks</b>](#)[<b>ActiveJwkConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk-connection.md)  
Newly active JWKs (JSON Web Keys).
##### [AuthenticatorStateUpdateTransaction.newActiveJwks.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [AuthenticatorStateUpdateTransaction.newActiveJwks.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [AuthenticatorStateUpdateTransaction.newActiveJwks.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [AuthenticatorStateUpdateTransaction.newActiveJwks.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [AuthenticatorStateUpdateTransaction.<b>round</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
Consensus round of the authenticator state update.

### Implemented By

[`TransactionKind`](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)