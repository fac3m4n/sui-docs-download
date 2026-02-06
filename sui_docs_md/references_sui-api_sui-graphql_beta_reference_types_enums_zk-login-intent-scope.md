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

An enum that specifies the intent scope to be used to parse the bytes for signature verification.

```graphql
enum ZkLoginIntentScope {
  TRANSACTION_DATA
  PERSONAL_MESSAGE
}
```

### Values

#### [ZkLoginIntentScope.<b>TRANSACTION&#x005F;DATA</b>](#)  
Indicates that the bytes are to be parsed as transaction data bytes.

#### [ZkLoginIntentScope.<b>PERSONAL&#x005F;MESSAGE</b>](#)  
Indicates that the bytes are to be parsed as a personal message.

### Member Of

[`verifyZkLoginSignature`](/references/sui-api/sui-graphql/beta/reference/operations/queries/verify-zk-login-signature.md)