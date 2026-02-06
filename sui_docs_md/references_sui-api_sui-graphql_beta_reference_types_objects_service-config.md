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
type ServiceConfig {
  availableRange(
    type: String!
    field: String
    filters: [String!]
  ): AvailableRange!
  defaultPageSize(
    type: String!
    field: String!
  ): Int
  maxDisassembledModuleSize: Int
  maxDisplayFieldDepth: Int
  maxDisplayFormatNodes: Int
  maxDisplayObjectLoads: Int
  maxDisplayOutputSize: Int
  maxMoveValueBound: Int
  maxMoveValueDepth: Int
  maxMultiGetSize: Int
  maxOutputNodes: Int
  maxPageSize(
    type: String!
    field: String!
  ): Int
  maxQueryDepth: Int
  maxQueryNodes: Int
  maxQueryPayloadSize: Int
  maxRichQueries: Int
  maxTransactionPayloadSize: Int
  maxTypeArgumentDepth: Int
  maxTypeArgumentWidth: Int
  maxTypeNodes: Int
  mutationTimeoutMs: Int
  queryTimeoutMs: Int
}
```

### Fields

#### [ServiceConfig.<b>availableRange</b>](#)[<b>AvailableRange!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/available-range.md)   
Range of checkpoints for which data is available for a query type, field and optional filter. If filter is not provided, the strictest retention range for the query and type is returned.
##### [ServiceConfig.availableRange.<b>type</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

##### [ServiceConfig.availableRange.<b>field</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ServiceConfig.availableRange.<b>filters</b>](#)[<b>[String!]</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.mdx)   

#### [ServiceConfig.<b>defaultPageSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Number of elements a paginated connection will return if a page size is not supplied.

Accepts `type` and `field` arguments which identify the connection that is being queried. If the field in question is paginated, its default page size is returned. If it does not exist or is not paginated, `null` is returned.
##### [ServiceConfig.defaultPageSize.<b>type</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

##### [ServiceConfig.defaultPageSize.<b>field</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [ServiceConfig.<b>maxDisassembledModuleSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum output size of a disassembled MoveModule, in bytes.

#### [ServiceConfig.<b>maxDisplayFieldDepth</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum depth of nested field access supported in display outputs.

#### [ServiceConfig.<b>maxDisplayFormatNodes</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of components in a Display v2 format string.

#### [ServiceConfig.<b>maxDisplayObjectLoads</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of objects that can be loaded while evaluating a display.

#### [ServiceConfig.<b>maxDisplayOutputSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum output size of a display output.

#### [ServiceConfig.<b>maxMoveValueBound</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum budget in bytes to spend when outputting a structured `MoveValue`.

#### [ServiceConfig.<b>maxMoveValueDepth</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum nesting allowed in datatype fields when calculating the layout of a single type.

#### [ServiceConfig.<b>maxMultiGetSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of elements that can be requested from a multi-get query. A request to fetch more keys will result in an error.

#### [ServiceConfig.<b>maxOutputNodes</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of estimated output nodes in a GraphQL response.

The estimate is an upperbound of how many nodes there would be in the output assuming every requested field is present, paginated requests return full page sizes, and multi-get queries find all requested keys. Below is a worked example query:

```graphql
|  0: query {                            # 514 = total
|  1:   checkpoint {                     # 1
|  2:     sequenceNumber                 # 1
|  3:   }
|  4:
|  5:   multiGetObjects([$a, $b, $c]) {  # 1 (* 3)
|  6:     address                        # 3
|  7:     digest                         # 3
|  8:   }
|  9:
| 10:   # default page size is 20
| 11:   transactions {                   # 1 (* 20)
| 12:     pageInfo {                     # 1
| 13:       hasNextPage                  # 1
| 14:       endCursor                    # 1
| 15:     }
| 16:
| 17:     nodes                          # 1
| 18:     {                              # 20
| 19:       digest                       # 20
| 20:       effects {                    # 20
| 21:         objectChanges(first: 10) { # 20 (* 10)
| 22:           nodes                    # 20
| 23:           {                        # 200
| 24:             address                # 200
| 25:           }
| 26:         }
| 27:       }
| 28:     }
| 29:   }
| 30: }
```

#### [ServiceConfig.<b>maxPageSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of elements that can be requested from a paginated connection. A request to fetch more elements will result in an error.

Accepts `type` and `field` arguments which identify the connection that is being queried. If the field in question is paginated, its max page size is returned. If it does not exist or is not paginated, `null` is returned.
##### [ServiceConfig.maxPageSize.<b>type</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

##### [ServiceConfig.maxPageSize.<b>field</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

#### [ServiceConfig.<b>maxQueryDepth</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum depth of a GraphQL query that can be accepted by this service.

#### [ServiceConfig.<b>maxQueryNodes</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
The maximum number of nodes (field names) the service will accept in a single query.

#### [ServiceConfig.<b>maxQueryPayloadSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum size in bytes of a single GraphQL request, excluding the elements covered by `maxTransactionPayloadSize`.

#### [ServiceConfig.<b>maxRichQueries</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of paginated fields that can return results in a single request. Queries on paginated fields that exceed this limit will return an error.

#### [ServiceConfig.<b>maxTransactionPayloadSize</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum size in bytes allowed for the `txBytes` and `signatures` parameters of an `executeTransaction` or `simulateTransaction` field, or the `bytes` and `signature` parameters of a `verifyZkLoginSignature` field.

This is cumulative across all matching fields in a single GraphQL request.

#### [ServiceConfig.<b>maxTypeArgumentDepth</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum amount of nesting among type arguments (type arguments nest when a type argument is itself generic and has arguments).

#### [ServiceConfig.<b>maxTypeArgumentWidth</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of type parameters a type can have.

#### [ServiceConfig.<b>maxTypeNodes</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum number of datatypes that need to be processed when calculating the layout of a single type.

#### [ServiceConfig.<b>mutationTimeoutMs</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum time in milliseconds spent waiting for a response from fullnode after issuing a transaction to execute. Note that the transaction may still succeed even in the case of a timeout. Transactions are idempotent, so a transaction that times out should be re-submitted until the network returns a definite response (success or failure, not timeout).

#### [ServiceConfig.<b>queryTimeoutMs</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  
Maximum time in milliseconds that will be spent to serve one query request.

### Returned By

[`serviceConfig`](/references/sui-api/sui-graphql/beta/reference/operations/queries/service-config.md)