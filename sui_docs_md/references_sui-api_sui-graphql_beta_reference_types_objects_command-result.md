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

The intermediate results for each command of a transaction simulation.

```graphql
type CommandResult {
  mutatedReferences: [CommandOutput!]
  returnValues: [CommandOutput!]
}
```

### Fields

#### [CommandResult.<b>mutatedReferences</b>](#)[<b>[CommandOutput!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-output.mdx)   
Changes made to arguments that were mutably borrowed by each command in this transaction.

#### [CommandResult.<b>returnValues</b>](#)[<b>[CommandOutput!]</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/command-output.mdx)   
Return results of each command in this transaction.

### Member Of

[`SimulationResult`](/references/sui-api/sui-graphql/beta/reference/types/objects/simulation-result.md)