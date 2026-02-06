-  [Struct UnverifiedValidatorOperationCap](#sui_system_validator_cap_UnverifiedValidatorOperationCap)
-  [Struct ValidatorOperationCap](#sui_system_validator_cap_ValidatorOperationCap)
-  [Function unverified_operation_cap_address](#sui_system_validator_cap_unverified_operation_cap_address)
-  [Function verified_operation_cap_address](#sui_system_validator_cap_verified_operation_cap_address)
-  [Function new_unverified_validator_operation_cap_and_transfer](#sui_system_validator_cap_new_unverified_validator_operation_cap_and_transfer)
-  [Function into_verified](#sui_system_validator_cap_into_verified)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>UnverifiedValidatorOperationCap</code>

The capability object is created when creating a new Validator or when the
validator explicitly creates a new capability object for rotation/revocation.
The holder address of this object can perform some validator operations on behalf of
the authorizer validator. Thus, if a validator wants to separate the keys for operation
(such as reference gas price setting or tallying rule reporting) from fund/staking, it
could transfer this capability object to another address.
To facilitate rotating/revocation, Validator stores the ID of currently valid
<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a>. Thus, before converting <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a>
to <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a>, verification needs to be done to make sure
the cap object is still valid.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>authorizer_validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ValidatorOperationCap</code>

Privileged operations require <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a> for permission check.
This is only constructed after successful verification.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>authorizer_validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
</dl>

Function <code>unverified_operation_cap_address</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_unverified_operation_cap_address">unverified_operation_cap_address</a>(cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>): &<b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_unverified_operation_cap_address">unverified_operation_cap_address</a>(
    cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a>,
): &<b>address</b> {
    &cap.authorizer_validator_address
}
</code></pre>

Function <code>verified_operation_cap_address</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_verified_operation_cap_address">verified_operation_cap_address</a>(cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>): &<b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_verified_operation_cap_address">verified_operation_cap_address</a>(cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a>): &<b>address</b> {
    &cap.authorizer_validator_address
}
</code></pre>

Function <code>new_unverified_validator_operation_cap_and_transfer</code>

Should be only called by the friend modules when adding a Validator
or rotating an existing validaotr's operation_cap_id.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_new_unverified_validator_operation_cap_and_transfer">new_unverified_validator_operation_cap_and_transfer</a>(validator_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_new_unverified_validator_operation_cap_and_transfer">new_unverified_validator_operation_cap_and_transfer</a>(
    validator_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
): ID {
    // This function needs to be called only by the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> itself, except
    // 1. in <a href="../sui_sui_system/genesis#sui_system_genesis">genesis</a> where all valdiators are created by @0x0
    // 2. in tests where @0x0 could be used to simplify the setup
    <b>let</b> sender_address = ctx.sender();
    <b>assert</b>!(sender_address == @0x0 || sender_address == validator_address, 0);
    <b>let</b> operation_cap = <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a> {
        id: object::new(ctx),
        authorizer_validator_address: validator_address,
    };
    <b>let</b> operation_cap_id = object::id(&operation_cap);
    transfer::public_transfer(operation_cap, validator_address);
    operation_cap_id
}
</code></pre>

Function <code>into_verified</code>

Convert an <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a> to <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a>.
Should only be called by <a href="../sui_sui_system/validator_set#sui_system_validator_set">validator_set</a> module AFTER verification.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_into_verified">into_verified</a>(cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>): <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_into_verified">into_verified</a>(cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">UnverifiedValidatorOperationCap</a>): <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a> {
    <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">ValidatorOperationCap</a> { authorizer_validator_address: cap.authorizer_validator_address }
}
</code></pre>