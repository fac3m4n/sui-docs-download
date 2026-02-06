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

The signature of a concrete Move Type (a type with all its type parameters instantiated with concrete types, that contains no references), corresponding to the following recursive type:

type MoveTypeSignature =
    "address"
  | "bool"
  | "u8" | "u16" | ... | "u256"
  | &#x007B; vector: MoveTypeSignature &#x007D;
  | &#x007B;
      datatype: &#x007B;
        package: string,
        module: string,
        type: string,
        typeParameters: [MoveTypeSignature],
      &#x007D;
    &#x007D;

```graphql
scalar MoveTypeSignature
```

### Member Of

[`MoveType`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)