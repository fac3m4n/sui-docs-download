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
type ObjectChange {
  address: SuiAddress!
  idCreated: Boolean
  idDeleted: Boolean
  inputState: Object
  outputState: Object
}
```

### Fields

#### [ObjectChange.<b>address</b>](#)[<b>SuiAddress!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)   
The address of the object that has changed.

#### [ObjectChange.<b>idCreated</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether the ID was created in this transaction.

#### [ObjectChange.<b>idDeleted</b>](#)[<b>Boolean</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/boolean.md)  
Whether the ID was deleted in this transaction.

#### [ObjectChange.<b>inputState</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
The contents of the object immediately before the transaction.

#### [ObjectChange.<b>outputState</b>](#)[<b>Object</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/object.md)  
The contents of the object immediately after the transaction.

### Member Of

[`ObjectChangeConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change-connection.md)  [`ObjectChangeEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/object-change-edge.md)