A module for accumulating funds, i.e. Balance-like types.

-  [Struct Withdrawal](#sui_funds_accumulator_Withdrawal)
-  [Constants](#@Constants_0)
-  [Function withdrawal_owner](#sui_funds_accumulator_withdrawal_owner)
-  [Function withdrawal_limit](#sui_funds_accumulator_withdrawal_limit)
-  [Function withdrawal_split](#sui_funds_accumulator_withdrawal_split)
-  [Function withdrawal_join](#sui_funds_accumulator_withdrawal_join)
-  [Function redeem](#sui_funds_accumulator_redeem)
-  [Function withdraw_from_object](#sui_funds_accumulator_withdraw_from_object)
-  [Function add_impl](#sui_funds_accumulator_add_impl)
-  [Function withdraw_impl](#sui_funds_accumulator_withdraw_impl)
-  [Function add_to_accumulator_address](#sui_funds_accumulator_add_to_accumulator_address)
-  [Function withdraw_from_accumulator_address](#sui_funds_accumulator_withdraw_from_accumulator_address)
-  [Function create_withdrawal](#sui_funds_accumulator_create_withdrawal)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/internal#std_internal">std::internal</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/accumulator#sui_accumulator">sui::accumulator</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Withdrawal</code>

Allows for withdrawing funds from a given address. The <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> can be created in PTBs for
the transaction sender, or dynamically from an object via <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_object">withdraw_from_object</a>.
The redemption of the funds must be initiated from the module that defines T.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;<b>phantom</b> T: store&gt; <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>owner: <b>address</b></code>
</dt>
<dd>
 The owner of the funds, either an object or a transaction sender
</dd>
<dt>
<code>limit: u256</code>
</dt>
<dd>
 At signing we check the limit <= balance when taking this as a call arg.
 If this was generated from an object, we cannot check this until redemption.
</dd>
</dl>

Constants

Attempted to withdraw more than the maximum value of the underlying integer type.

<code><b>const</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOverflow">EOverflow</a>: u64 = 0;
</code>

Attempt to split more than the current limit of a <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>.

<code>#[error]
<b>const</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EInvalidSubLimit">EInvalidSubLimit</a>: vector&lt;u8&gt; = b"Sub-limit exceeds current withdrawal limit";
</code>

Attempted to join two withdrawals with different owners.

<code>#[error]
<b>const</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOwnerMismatch">EOwnerMismatch</a>: vector&lt;u8&gt; = b"<a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> owners do not match";
</code>

Attempted to withdraw funds from an object when the feature flag is not enabled.

<code>#[error]
<b>const</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EObjectFundsWithdrawNotEnabled">EObjectFundsWithdrawNotEnabled</a>: vector&lt;u8&gt; = b"Object funds withdraw is not enabled";
</code>

Function <code>withdrawal_owner</code>

Returns the owner, either a sender's address or an object, of the withdrawal.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_owner">withdrawal_owner</a>&lt;T: store&gt;(withdrawal: &<a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_owner">withdrawal_owner</a>&lt;T: store&gt;(withdrawal: &<a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;): <b>address</b> {
    withdrawal.owner
}
</code></pre>

Function <code>withdrawal_limit</code>

Returns the remaining limit of the withdrawal.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_limit">withdrawal_limit</a>&lt;T: store&gt;(withdrawal: &<a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;): u256
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_limit">withdrawal_limit</a>&lt;T: store&gt;(withdrawal: &<a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;): u256 {
    withdrawal.limit
}
</code></pre>

Function <code>withdrawal_split</code>

Split a <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> and take a sub-withdrawal from it with the specified sub-limit.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_split">withdrawal_split</a>&lt;T: store&gt;(withdrawal: &<b>mut</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;, sub_limit: u256): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_split">withdrawal_split</a>&lt;T: store&gt;(
    withdrawal: &<b>mut</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;,
    sub_limit: u256,
): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt; {
    <b>assert</b>!(withdrawal.limit &gt;= sub_limit, <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EInvalidSubLimit">EInvalidSubLimit</a>);
    withdrawal.limit = withdrawal.limit - sub_limit;
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> { owner: withdrawal.owner, limit: sub_limit }
}
</code></pre>

Function <code>withdrawal_join</code>

Join two withdrawals together, increasing the limit of self by the limit of other.
Aborts with <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOwnerMismatch">EOwnerMismatch</a> if the owners are not equal.
Aborts with <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOverflow">EOverflow</a> if the resulting limit would overflow u256.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_join">withdrawal_join</a>&lt;T: store&gt;(withdrawal: &<b>mut</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;, other: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdrawal_join">withdrawal_join</a>&lt;T: store&gt;(withdrawal: &<b>mut</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;, other: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;) {
    <b>assert</b>!(withdrawal.owner == other.owner, <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOwnerMismatch">EOwnerMismatch</a>);
    <b>assert</b>!(<a href="../sui_std/u256#std_u256_max_value">std::u256::max_value</a>!() - withdrawal.limit &gt;= other.limit, <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EOverflow">EOverflow</a>);
    withdrawal.limit = withdrawal.limit + other.limit;
}
</code></pre>

Function <code>redeem</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_redeem">redeem</a>&lt;T: store&gt;(withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;, _: <a href="../sui_std/internal#std_internal_Permit">std::internal::Permit</a>&lt;T&gt;): T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_redeem">redeem</a>&lt;T: store&gt;(withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt;, _: internal::Permit&lt;T&gt;): T {
    <b>let</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> { owner, limit: value } = withdrawal;
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_impl">withdraw_impl</a>(owner, value)
}
</code></pre>

Function <code>withdraw_from_object</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_object">withdraw_from_object</a>&lt;T: store&gt;(obj: &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, limit: u256): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_object">withdraw_from_object</a>&lt;T: store&gt;(obj: &<b>mut</b> UID, limit: u256): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt; {
    <b>assert</b>!(
        <a href="../sui_sui/protocol_config#sui_protocol_config_is_feature_enabled">sui::protocol_config::is_feature_enabled</a>(b"enable_object_funds_withdraw"),
        <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_EObjectFundsWithdrawNotEnabled">EObjectFundsWithdrawNotEnabled</a>,
    );
    <b>let</b> owner = obj.to_address();
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> { owner, limit }
}
</code></pre>

Function <code>add_impl</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_impl">add_impl</a>&lt;T: store&gt;(value: T, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_impl">add_impl</a>&lt;T: store&gt;(value: T, recipient: <b>address</b>) {
    <b>let</b> <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a> = <a href="../sui_sui/accumulator#sui_accumulator_accumulator_address">sui::accumulator::accumulator_address</a>&lt;T&gt;(recipient);
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_to_accumulator_address">add_to_accumulator_address</a>&lt;T&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>, recipient, value)
}
</code></pre>

Function <code>withdraw_impl</code>

<code><b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_impl">withdraw_impl</a>&lt;T: store&gt;(owner: <b>address</b>, value: u256): T
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_impl">withdraw_impl</a>&lt;T: store&gt;(owner: <b>address</b>, value: u256): T {
    <b>let</b> <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a> = <a href="../sui_sui/accumulator#sui_accumulator_accumulator_address">sui::accumulator::accumulator_address</a>&lt;T&gt;(owner);
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_accumulator_address">withdraw_from_accumulator_address</a>&lt;T&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>, owner, value)
}
</code></pre>

Function <code>add_to_accumulator_address</code>

<code><b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_to_accumulator_address">add_to_accumulator_address</a>&lt;T: store&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>, recipient: <b>address</b>, value: T)
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_to_accumulator_address">add_to_accumulator_address</a>&lt;T: store&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>, recipient: <b>address</b>, value: T);
</code></pre>

Function <code>withdraw_from_accumulator_address</code>

<code><b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_accumulator_address">withdraw_from_accumulator_address</a>&lt;T: store&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>, owner: <b>address</b>, value: u256): T
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_accumulator_address">withdraw_from_accumulator_address</a>&lt;T: store&gt;(
    <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>,
    owner: <b>address</b>,
    value: u256,
): T;
</code></pre>

Function <code>create_withdrawal</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_create_withdrawal">create_withdrawal</a>&lt;T: store&gt;(owner: <b>address</b>, limit: u256): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_create_withdrawal">create_withdrawal</a>&lt;T: store&gt;(owner: <b>address</b>, limit: u256): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a>&lt;T&gt; {
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">Withdrawal</a> { owner, limit }
}
</code></pre>