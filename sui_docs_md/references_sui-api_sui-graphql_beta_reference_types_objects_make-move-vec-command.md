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

Create a vector (can be empty).

```graphql
type MakeMoveVecCommand {
  elements: [TransactionArgument!]
  type: MoveType
}
```

### Fields

#### [MakeMoveVecCommand.<b>elements</b>](#)[<b>[TransactionArgument!]</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.mdx)   
The values to pack into the vector, all of the same type.

#### [MakeMoveVecCommand.<b>type</b>](#)[<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
If the elements are not objects, or the vector is empty, a type must be supplied.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)