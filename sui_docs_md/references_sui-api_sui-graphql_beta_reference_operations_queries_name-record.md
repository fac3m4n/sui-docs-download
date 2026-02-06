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

Look-up a Name Service NameRecord by its domain name.

Returns `null` if the record does not exist or has expired.

```graphql
nameRecord(
  name: String!
): NameRecord
```

### Arguments

#### [nameRecord.<b>name</b>](#)[<b>String!</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/string.md)   

### Type

#### [<b>NameRecord</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/name-record.md)  
A Name Service NameRecord representing a domain name registration.