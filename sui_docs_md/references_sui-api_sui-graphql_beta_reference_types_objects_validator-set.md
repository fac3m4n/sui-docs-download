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

Representation of `0x3::validator_set::ValidatorSet`.

```graphql
type ValidatorSet {
  activeValidators(
    first: Int
    after: String
    last: Int
    before: String
  ): ValidatorConnection
  contents: MoveValue
}
```

### Fields

#### [ValidatorSet.<b>activeValidators</b>](#)[<b>ValidatorConnection</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/validator-connection.md)  
The validators currently in the committee for this validator set.
##### [ValidatorSet.activeValidators.<b>first</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ValidatorSet.activeValidators.<b>after</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

##### [ValidatorSet.activeValidators.<b>last</b>](#)[<b>Int</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/int.md)  

##### [ValidatorSet.activeValidators.<b>before</b>](#)[<b>String</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)  

#### [ValidatorSet.<b>contents</b>](#)[<b>MoveValue</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)  
On-chain representation of the underlying `0x3::validator_set::ValidatorSet` value.

### Member Of

[`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)