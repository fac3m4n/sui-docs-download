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

A rendered JSON blob based on an on-chain template.

```graphql
type Display {
  errors: JSON
  output: JSON
}
```

### Fields

#### [Display.<b>errors</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
If any fields failed to render, this will contain a mapping from failed field names to error messages. If all fields succeed, this will be `null`.

#### [Display.<b>output</b>](#)[<b>JSON</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/json.md)  
Output for all successfully substituted display fields. Unsuccessful fields will be `null`, and will be accompanied by a field in `errors`, explaining the error.

### Member Of

[`MoveValue`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-value.md)