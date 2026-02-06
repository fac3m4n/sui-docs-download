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

Verify a zkLogin signature os from the given `author`.

Returns a `ZkLoginVerifyResult` where `success` is `true` and `error` is empty if the signature is valid. If the signature is invalid, `success` is `false` and `error` contains the relevant error message.

- `bytes` are either the bytes of a serialized personal message, or `TransactionData`, Base64-encoded.
- `signature` is a serialized zkLogin signature, also Base64-encoded.
- `intentScope` indicates whether `bytes` are to be parsed as a personal message or `TransactionData`.
- `author` is the signer's address.

```graphql
verifyZkLoginSignature(
  bytes: Base64!
  signature: Base64!
  intentScope: ZkLoginIntentScope!
  author: SuiAddress!
): ZkLoginVerifyResult!
```

### Arguments

#### [verifyZkLoginSignature.<b>bytes</b>](#)[<b>Base64!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)   

#### [verifyZkLoginSignature.<b>signature</b>](#)[<b>Base64!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)   

#### [verifyZkLoginSignature.<b>intentScope</b>](#)[<b>ZkLoginIntentScope!</b>](/references/sui-api/sui-graphql/beta/reference/types/enums/zk-login-intent-scope.md)   

#### [verifyZkLoginSignature.<b>author</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   

### Type

#### [<b>ZkLoginVerifyResult</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/zk-login-verify-result.md)  
The result of the zkLogin signature verification.