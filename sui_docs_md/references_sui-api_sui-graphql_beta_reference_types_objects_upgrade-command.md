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

Upgrades a Move Package.

```graphql
type UpgradeCommand {
  currentPackage: SuiAddress
  dependencies: [SuiAddress!]
  modules: [Base64!]
  upgradeTicket: TransactionArgument
}
```

### Fields

#### [UpgradeCommand.<b>currentPackage</b>](#)[<b>SuiAddress</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.md)  
ID of the package being upgraded.

#### [UpgradeCommand.<b>dependencies</b>](#)[<b>[SuiAddress!]</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/sui-address.mdx)   
IDs of the transitive dependencies of the package to be published.

#### [UpgradeCommand.<b>modules</b>](#)[<b>[Base64!]</b>](/references/sui-api/sui-graphql/beta/reference/types/scalars/base-64.mdx)   
Bytecode for the modules to be published, BCS serialized and Base64 encoded.

#### [UpgradeCommand.<b>upgradeTicket</b>](#)[<b>TransactionArgument</b>](/references/sui-api/sui-graphql/beta/reference/types/unions/transaction-argument.md)  
The `UpgradeTicket` authorizing the upgrade.

### Implemented By

[`Command`](/references/sui-api/sui-graphql/beta/reference/types/unions/command.md)