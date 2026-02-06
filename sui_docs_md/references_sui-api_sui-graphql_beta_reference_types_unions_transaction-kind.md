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

Different types of transactions that can be executed on the Sui network.

```graphql
union TransactionKind = GenesisTransaction | ConsensusCommitPrologueTransaction | ChangeEpochTransaction | RandomnessStateUpdateTransaction | AuthenticatorStateUpdateTransaction | EndOfEpochTransaction | ProgrammableTransaction | ProgrammableSystemTransaction
```

### Possible types

#### [TransactionKind.<b>GenesisTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/genesis-transaction.md)  
System transaction that initializes the network and writes the initial set of objects on-chain.

#### [TransactionKind.<b>ConsensusCommitPrologueTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/consensus-commit-prologue-transaction.md)  
System transaction that runs at the beginning of a checkpoint, and is responsible for setting the current value of the clock, based on the timestamp from consensus.

#### [TransactionKind.<b>ChangeEpochTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/change-epoch-transaction.md)  
A system transaction that updates epoch information on-chain (increments the current epoch). Executed by the system once per epoch, without using gas. Epoch change transactions cannot be submitted by users, because validators will refuse to sign them.

This transaction kind is deprecated in favour of `EndOfEpochTransaction`.

#### [TransactionKind.<b>RandomnessStateUpdateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/randomness-state-update-transaction.md)  
System transaction to update the source of on-chain randomness.

#### [TransactionKind.<b>AuthenticatorStateUpdateTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/authenticator-state-update-transaction.md)  

#### [TransactionKind.<b>EndOfEpochTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/end-of-epoch-transaction.md)  
System transaction that supersedes `ChangeEpochTransaction` as the new way to run transactions at the end of an epoch. Behaves similarly to `ChangeEpochTransaction` but can accommodate other optional transactions to run at the end of the epoch.

#### [TransactionKind.<b>ProgrammableTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-transaction.md)  

#### [TransactionKind.<b>ProgrammableSystemTransaction</b>](/references/sui-api/sui-graphql/beta/reference/types/objects/programmable-system-transaction.md)  
ProgrammableSystemTransaction is identical to ProgrammableTransaction, but GraphQL does not allow multiple variants with the same type.

### Member Of

[`Transaction`](/references/sui-api/sui-graphql/beta/reference/types/objects/transaction.md)