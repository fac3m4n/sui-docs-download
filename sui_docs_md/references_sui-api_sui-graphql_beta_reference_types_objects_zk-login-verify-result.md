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

The result of the zkLogin signature verification.

```graphql
type ZkLoginVerifyResult {
  error: String
  success: Boolean
}
```

### Fields

#### [ZkLoginVerifyResult.<b>error</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The error field capture reasons why the signature could not be verified, assuming the inputs are valid and there are no internal errors.

#### [ZkLoginVerifyResult.<b>success</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
The boolean result of the verification. If true, errors should be empty.

### Returned By

[`verifyZkLoginSignature`](/references/sui-api/sui-graphql/beta/reference/operations/queries/verify-zk-login-signature.md)