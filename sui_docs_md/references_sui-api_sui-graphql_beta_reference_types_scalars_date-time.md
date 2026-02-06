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

ISO-8601 Date and Time: RFC3339 in UTC with format: YYYY-MM-DDTHH:MM:SS.mmmZ. Note that the milliseconds part is optional, and it may be omitted if its value is 0.

```graphql
scalar DateTime
```

### Member Of

[`ChangeEpochTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  [`Checkpoint`](/references/sui-api/sui-graphql/beta/reference/types/objects/checkpoint.md)  [`ConsensusCommitPrologueTransaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-commit-prologue-transaction.md)  [`Epoch`](/references/sui-api/sui-graphql/beta/reference/types/objects/epoch.md)  [`Event`](/references/sui-api/sui-graphql/beta/reference/types/objects/event.md)  [`TransactionEffects`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction-effects.md)