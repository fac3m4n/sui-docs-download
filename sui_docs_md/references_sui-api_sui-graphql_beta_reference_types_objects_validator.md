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
type Validator {
  atRisk: UInt53
  contents: MoveValue
  reportRecords(
    first: Int
    before: String
    last: Int
    after: String
  ): ValidatorConnection
}
```

### Fields

#### [Validator.<b>atRisk</b>](#)[<b>UInt53</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/uint-53.md)  
The number of epochs for which this validator has been below the low stake threshold.

#### [Validator.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
On-chain representation of the underlying `0x3::validator::Validator` value.

#### [Validator.<b>reportRecords</b>](#)[<b>ValidatorConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-connection.md)  
Other validators this validator has reported.
##### [Validator.reportRecords.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Validator.reportRecords.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [Validator.reportRecords.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [Validator.reportRecords.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

### Member Of

[`ValidatorConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-connection.md)  [`ValidatorEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-edge.md)