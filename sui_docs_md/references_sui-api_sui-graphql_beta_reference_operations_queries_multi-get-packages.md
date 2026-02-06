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

Fetch packages by their keys.

Returns a list of packages that is guaranteed to be the same length as `keys`. If a package in `keys` could not be found in the store, its corresponding entry in the result will be `null`. This could be because that address never pointed to a package, or because the package was pruned.

```graphql
multiGetPackages(
  keys: [PackageKey!]!
): [MovePackage]!
```

### Arguments

#### [multiGetPackages.<b>keys</b>](#)[<b>[PackageKey!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/inputs/package-key.mdx)   

### Type

#### [<b>MovePackage</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)  
A MovePackage is a kind of Object that represents code that has been published on-chain. It exposes information about its modules, type definitions, functions, and dependencies.