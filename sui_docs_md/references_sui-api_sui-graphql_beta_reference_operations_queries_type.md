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

Fetch a structured representation of a concrete type, including its layout information.

Types are canonicalized: In the input they can be at any package address at or after the package that first defines them, and in the output they will be relocated to the package that first defines them.

Fails if the type is malformed, returns `null` if a type mentioned does not exist.

```graphql
type(
  type: String!
): MoveType
```

### Arguments

#### [type.<b>type</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

### Type

#### [<b>MoveType</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)  
Represents instances of concrete types (no type parameters, no references).