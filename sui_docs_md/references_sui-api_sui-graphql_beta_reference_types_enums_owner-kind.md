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

Filter on who owns an object.

```graphql
enum OwnerKind {
  ADDRESS
  OBJECT
  SHARED
  IMMUTABLE
}
```

### Values

#### [OwnerKind.<b>ADDRESS</b>](#)  
Object is owned by an address.

#### [OwnerKind.<b>OBJECT</b>](#)  
Object is a child of another object (e.g. a dynamic field or dynamic object field).

#### [OwnerKind.<b>SHARED</b>](#)  
Object is shared among multiple owners.

#### [OwnerKind.<b>IMMUTABLE</b>](#)  
Object is frozen.

### Member Of

[`ObjectFilter`](/references/sui-api/sui-graphql/beta/reference/types/inputs/object-filter.md)