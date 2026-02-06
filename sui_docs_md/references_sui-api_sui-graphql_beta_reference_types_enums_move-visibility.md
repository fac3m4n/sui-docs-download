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

The visibility modifier describes which modules can access this module member.

By default, a module member can be called only within the same module.

```graphql
enum MoveVisibility {
  PUBLIC
  PRIVATE
  FRIEND
}
```

### Values

#### [MoveVisibility.<b>PUBLIC</b>](#)  
A public member can be accessed by any module.

#### [MoveVisibility.<b>PRIVATE</b>](#)  
A private member can be accessed in the module it is defined in.

#### [MoveVisibility.<b>FRIEND</b>](#)  
A friend member can be accessed in the module it is defined in and any other module in its package that is explicitly specified in its friend list.

### Member Of

[`MoveFunction`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-function.md)