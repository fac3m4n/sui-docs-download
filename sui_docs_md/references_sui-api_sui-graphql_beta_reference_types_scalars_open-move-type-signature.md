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

The shape of an abstract Move Type (a type that can contain free type parameters, and can optionally be taken by reference), corresponding to the following recursive type:

type OpenMoveTypeSignature = &#x007B;
  ref: ("&" | "&mut")?,
  body: OpenMoveTypeSignatureBody,
&#x007D;

type OpenMoveTypeSignatureBody =
    "address"
  | "bool"
  | "u8" | "u16" | ... | "u256"
  | &#x007B; vector: OpenMoveTypeSignatureBody &#x007D;
  | &#x007B;
      datatype &#x007B;
        package: string,
        module: string,
        type: string,
        typeParameters: [OpenMoveTypeSignatureBody]
      &#x007D;
    &#x007D;
  | &#x007B; typeParameter: number &#x007D;

```graphql
scalar OpenMoveTypeSignature
```

### Member Of

[`OpenMoveType`](/references/sui-api/sui-graphql/beta/reference/types/objects/open-move-type.md)