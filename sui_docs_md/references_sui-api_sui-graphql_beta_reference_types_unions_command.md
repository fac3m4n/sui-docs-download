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

A single command in the programmable transaction.

```graphql
union Command = MakeMoveVecCommand | MergeCoinsCommand | MoveCallCommand | PublishCommand | SplitCoinsCommand | TransferObjectsCommand | UpgradeCommand | OtherCommand
```

### Possible types

#### [Command.<b>MakeMoveVecCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/make-move-vec-command.md)  
Create a vector (can be empty).

#### [Command.<b>MergeCoinsCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/merge-coins-command.md)  
Merges `coins` into the first `coin` (produces no results).

#### [Command.<b>MoveCallCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/move-call-command.md)  

#### [Command.<b>PublishCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/publish-command.md)  
Publishes a Move Package.

#### [Command.<b>SplitCoinsCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/split-coins-command.md)  
Splits off coins with denominations in `amounts` from `coin`, returning multiple results (as many as there are amounts.)

#### [Command.<b>TransferObjectsCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/transfer-objects-command.md)  
Transfers `inputs` to `address`. All inputs must have the `store` ability (allows public transfer) and must not be previously immutable or shared.

#### [Command.<b>UpgradeCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/upgrade-command.md)  
Upgrades a Move Package.

#### [Command.<b>OtherCommand</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/other-command.md)  
Placeholder for unimplemented command types

### Member Of

[`CommandConnection`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-connection.md)  [`CommandEdge`](/references/sui-api/sui-graphql/beta/reference/types/objects/command-edge.md)