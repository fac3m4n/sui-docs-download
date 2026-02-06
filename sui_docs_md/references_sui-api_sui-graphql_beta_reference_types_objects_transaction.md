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

Description of a transaction, the unit of activity on Sui.

```graphql
type Transaction implements Node {
  digest: String!
  effects: TransactionEffects
  expiration: Epoch
  gasInput: GasInput
  id: ID!
  kind: TransactionKind
  sender: Address
  signatures: [UserSignature!]!
  transactionBcs: Base64
  transactionJson: JSON
}
```

### Fields

#### [Transaction.<b>digest</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   
A 32-byte hash that uniquely identifies the transaction contents, encoded in Base58.

#### [Transaction.<b>effects</b>](#)[<b>TransactionEffects</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)  
The results to the chain of executing this transaction.

#### [Transaction.<b>expiration</b>](#)[<b>Epoch</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  
This field is set by senders of a transaction block. It is an epoch reference that sets a deadline after which validators will no longer consider the transaction valid. By default, there is no deadline for when a transaction must execute.

#### [Transaction.<b>gasInput</b>](#)[<b>GasInput</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/gas-input.md)  
The gas input field provides information on what objects were used as gas as well as the owner of the gas object(s) and information on the gas price and budget.

#### [Transaction.<b>id</b>](#)[<b>ID!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/id.md)   
The transaction's globally unique identifier, which can be passed to `Query.node` to refetch it.

#### [Transaction.<b>kind</b>](#)[<b>TransactionKind</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-kind.md)  
The type of this transaction as well as the commands and/or parameters comprising the transaction of this kind.

#### [Transaction.<b>sender</b>](#)[<b>Address</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/address.md)  
The address corresponding to the public key that signed this transaction. System transactions do not have senders.

#### [Transaction.<b>signatures</b>](#)[<b>[UserSignature!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/user-signature.mdx)   
User signatures for this transaction.

#### [Transaction.<b>transactionBcs</b>](#)[<b>Base64</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.md)  
The Base64-encoded BCS serialization of this transaction, as a `TransactionData`.

#### [Transaction.<b>transactionJson</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
The transaction as a JSON blob, matching the gRPC proto format (excluding BCS).

### Interfaces

#### [<b>Node</b>](/references/sui-api/sui-graphql/beta/reference/types/interfaces/node.md)  
An interface implemented by types that can be uniquely identified by a globally unique `ID`, following the GraphQL Global Object Identification specification.

### Returned By

[`multiGetTransactions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/multi-get-transactions.md)  [`transaction`](/references/sui-api/sui-graphql/beta/reference/operations/queries/transaction.md)  

### Member Of

[`CoinMetadata`](/references/sui-api/sui-graphql/beta/reference/types/objects/coin-metadata.md)  [`DynamicField`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`IObject`](/references/sui-api/sui-graphql/beta/reference/types/interfaces/iobject.md)  [`MoveObject`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  [`Object`](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  [`TransactionConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  [`TransactionEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-edge.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)