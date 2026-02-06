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

The shape of a concrete Move Type (a type with all its type parameters instantiated with concrete types), corresponding to the following recursive type:

type MoveTypeLayout =
    "address"
  | "bool"
  | "u8" | "u16" | ... | "u256"
  | &#x007B; vector: MoveTypeLayout &#x007D;
  | &#x007B;
      struct: &#x007B;
        type: string,
        fields: [&#x007B; name: string, layout: MoveTypeLayout &#x007D;],
      &#x007D;
    &#x007D;
  | &#x007B; enum: [&#x007B;
          type: string,
          variants: [&#x007B;
              name: string,
              fields: [&#x007B; name: string, layout: MoveTypeLayout &#x007D;],
          &#x007D;]
      &#x007D;]
  &#x007D;

```graphql
scalar MoveTypeLayout
```

### Member Of

[`MoveType`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-type.md)