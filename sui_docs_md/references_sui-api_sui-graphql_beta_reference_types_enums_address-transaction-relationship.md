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

The possible relationship types for a transaction: sent or affected.

```graphql
enum AddressTransactionRelationship {
  SENT
  AFFECTED
}
```

### Values

#### [AddressTransactionRelationship.<b>SENT</b>](#)  
Transactions this address has sent.

#### [AddressTransactionRelationship.<b>AFFECTED</b>](#)  
Transactions that this address was involved in, either as the sender, sponsor, or as the owner of some object that was created, modified or transferred.