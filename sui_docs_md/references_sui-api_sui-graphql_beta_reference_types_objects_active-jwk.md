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
type ActiveJwk {
  alg: String
  e: String
  epoch: Epoch
  iss: String
  kid: String
  kty: String
  n: String
}
```

### Fields

#### [ActiveJwk.<b>alg</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The JWK algorithm parameter, (RFC 7517, Section 4.4).

#### [ActiveJwk.<b>e</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The JWK RSA public exponent, (RFC 7517, Section 9.3).

#### [ActiveJwk.<b>epoch</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
The most recent epoch in which the JWK was validated.

#### [ActiveJwk.<b>iss</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The string (Issuing Authority) that identifies the OIDC provider.

#### [ActiveJwk.<b>kid</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The string (Key ID) that identifies the JWK among a set of JWKs, (RFC 7517, Section 4.5).

#### [ActiveJwk.<b>kty</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The JWK key type parameter, (RFC 7517, Section 4.1).

#### [ActiveJwk.<b>n</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The JWK RSA modulus, (RFC 7517, Section 9.3).

### Member Of

[`ActiveJwkConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk-connection.md)  [`ActiveJwkEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk-edge.md)