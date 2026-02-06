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

No description

```graphql
type MovePackageConnection {
  edges: [MovePackageEdge!]!
  nodes: [MovePackage!]!
  pageInfo: PageInfo!
}
```

### Fields

#### [MovePackageConnection.<b>edges</b>](#)[<b>[MovePackageEdge!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package-edge.mdx)   
A list of edges.

#### [MovePackageConnection.<b>nodes</b>](#)[<b>[MovePackage!]!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.mdx)   
A list of nodes.

#### [MovePackageConnection.<b>pageInfo</b>](#)[<b>PageInfo!</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/page-info.md)   
Information to aid in pagination.

### Returned By

[`packages`](/references/sui-api/sui-graphql/beta/reference/operations/queries/packages.md)  [`packageVersions`](/references/sui-api/sui-graphql/beta/reference/operations/queries/package-versions.md)  

### Member Of

[`ChangeEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`MovePackage`](/references/sui-api/sui-graphql/beta/reference/types/objects/move-package.md)