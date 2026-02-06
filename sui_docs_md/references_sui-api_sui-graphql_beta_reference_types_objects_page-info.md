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

Information about pagination in a connection

```graphql
type PageInfo {
  endCursor: String
  hasNextPage: Boolean!
  hasPreviousPage: Boolean!
  startCursor: String
}
```

### Fields

#### [PageInfo.<b>endCursor</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
When paginating forwards, the cursor to continue.

#### [PageInfo.<b>hasNextPage</b>](#)[<b>Boolean!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)   
When paginating forwards, are there more items?

#### [PageInfo.<b>hasPreviousPage</b>](#)[<b>Boolean!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)   
When paginating backwards, are there more items?

#### [PageInfo.<b>startCursor</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  
When paginating backwards, the cursor to continue.

### Member Of

[`ActiveJwkConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/active-jwk-connection.md)  [`BalanceChangeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-change-connection.md)  [`BalanceConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/balance-connection.md)  [`CheckpointConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint-connection.md)  [`CommandConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-connection.md)  [`DynamicFieldConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/dynamic-field-connection.md)  [`EndOfEpochTransactionKindConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction-kind-connection.md)  [`EpochConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch-connection.md)  [`EventConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/event-connection.md)  [`MoveDatatypeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-datatype-connection.md)  [`MoveEnumConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-enum-connection.md)  [`MoveFunctionConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function-connection.md)  [`MoveModuleConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-module-connection.md)  [`MoveObjectConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-object-connection.md)  [`MovePackageConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-connection.md)  [`MoveStructConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-struct-connection.md)  [`ObjectChangeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change-connection.md)  [`ObjectConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-connection.md)  [`TransactionConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-connection.md)  [`TransactionInputConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-input-connection.md)  [`UnchangedConsensusObjectConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/unchanged-consensus-object-connection.md)  [`ValidatorConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-connection.md)