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

Represents execution error information for failed transactions.

```graphql
type ExecutionError {
  abortCode: BigInt
  constant: String
  function: MoveFunction
  identifier: String
  instructionOffset: Int
  message: String!
  module: MoveModule
  sourceLineNumber: Int
}
```

### Fields

#### [ExecutionError.<b>abortCode</b>](#)[<b>BigInt</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/big-int.md)  
The error code of the Move abort, populated if this transaction failed with a Move abort.

Returns the explicit code if the abort used `code` annotation (e.g., `abort(ERR, code = 5)` returns 5), otherwise returns the raw abort code containing encoded error information.

#### [ExecutionError.<b>constant</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
An associated constant for the error. Only populated for clever errors.

Constants are returned as human-readable strings when possible. Complex types are returned as Base64-encoded bytes.

#### [ExecutionError.<b>function</b>](#)[<b>MoveFunction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)  
The function that the abort originated from. Only populated for Move aborts and primitive runtime errors that have function name information.

#### [ExecutionError.<b>identifier</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
The error's name. Only populated for clever errors.

#### [ExecutionError.<b>instructionOffset</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
The instruction offset in the Move bytecode where the error occurred. Populated for Move aborts and primitive runtime errors.

#### [ExecutionError.<b>message</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
Human readable explanation of why the transaction failed.

For Move aborts, the error message will be resolved to a human-readable form if possible, otherwise it will fall back to displaying the abort code and location.

#### [ExecutionError.<b>module</b>](#)[<b>MoveModule</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module.md)  
The module that the abort originated from. Only populated for Move aborts and primitive runtime errors.

#### [ExecutionError.<b>sourceLineNumber</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
The source line number for the abort. Only populated for clever errors.

### Member Of

[`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)