A storable handler for Balances in general. Is used in the Coin
module to allow balance operations and can be used to implement
custom coins with <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> and <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>s.

-  [Struct Supply](#sui_balance_Supply)
-  [Struct Balance](#sui_balance_Balance)
-  [Constants](#@Constants_0)
-  [Function value](#sui_balance_value)
-  [Function supply_value](#sui_balance_supply_value)
-  [Function create_supply](#sui_balance_create_supply)
-  [Function increase_supply](#sui_balance_increase_supply)
-  [Function decrease_supply](#sui_balance_decrease_supply)
-  [Function zero](#sui_balance_zero)
-  [Function join](#sui_balance_join)
-  [Function split](#sui_balance_split)
-  [Function withdraw_all](#sui_balance_withdraw_all)
-  [Function destroy_zero](#sui_balance_destroy_zero)
-  [Function send_funds](#sui_balance_send_funds)
-  [Function redeem_funds](#sui_balance_redeem_funds)
-  [Function withdraw_funds_from_object](#sui_balance_withdraw_funds_from_object)
-  [Function settled_funds_value](#sui_balance_settled_funds_value)
-  [Function create_supply_internal](#sui_balance_create_supply_internal)
-  [Function create_staking_rewards](#sui_balance_create_staking_rewards)
-  [Function destroy_storage_rebates](#sui_balance_destroy_storage_rebates)
-  [Function destroy_supply](#sui_balance_destroy_supply)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/internal#std_internal">std::internal</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/u128#std_u128">std::u128</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/accumulator#sui_accumulator">sui::accumulator</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator">sui::funds_accumulator</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Supply</code>

A Supply of T. Used for minting and burning.
Wrapped into a TreasuryCap in the Coin module.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;<b>phantom</b> T&gt; <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/balance#sui_balance_value">value</a>: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Balance</code>

Storable balance - an inner struct of a Coin type.
Can be used to store coins which don't need the key ability.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;<b>phantom</b> T&gt; <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/balance#sui_balance_value">value</a>: u64</code>
</dt>
<dd>
</dd>
</dl>

Constants

For when trying to destroy a non-zero balance.

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_ENonZero">ENonZero</a>: u64 = 0;
</code>

For when an overflow is happening on Supply operations.

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_EOverflow">EOverflow</a>: u64 = 1;
</code>

For when trying to withdraw more than there is.

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_ENotEnough">ENotEnough</a>: u64 = 2;
</code>

Sender is not @0x0 the system address.

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_ENotSystemAddress">ENotSystemAddress</a>: u64 = 3;
</code>

System operation performed for a coin other than SUI

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_ENotSUI">ENotSUI</a>: u64 = 4;
</code>

<code><b>const</b> <a href="../sui_sui/balance#sui_balance_SUI_TYPE_NAME">SUI_TYPE_NAME</a>: vector&lt;u8&gt; = vector[48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 50, 58, 58, 115, 117, 105, 58, 58, 83, 85, 73];
</code>

Function <code>value</code>

Get the amount stored in a <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_value">value</a>&lt;T&gt;(self: &<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_value">value</a>&lt;T&gt;(self: &<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;): u64 {
    self.<a href="../sui_sui/balance#sui_balance_value">value</a>
}
</code></pre>

Function <code>supply_value</code>

Get the <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> value.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_supply_value">supply_value</a>&lt;T&gt;(supply: &<a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_supply_value">supply_value</a>&lt;T&gt;(supply: &<a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt;): u64 {
    supply.<a href="../sui_sui/balance#sui_balance_value">value</a>
}
</code></pre>

Function <code>create_supply</code>

Create a new supply for type T.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_create_supply">create_supply</a>&lt;T: drop&gt;(_: T): <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_create_supply">create_supply</a>&lt;T: drop&gt;(_: T): <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt; {
    <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> { <a href="../sui_sui/balance#sui_balance_value">value</a>: 0 }
}
</code></pre>

Function <code>increase_supply</code>

Increase supply by <a href="../sui_sui/balance#sui_balance_value">value</a> and create a new <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; with this value.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_increase_supply">increase_supply</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_increase_supply">increase_supply</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    <b>assert</b>!(<a href="../sui_sui/balance#sui_balance_value">value</a> &lt;= (<a href="../sui_std/u64#std_u64_max_value">std::u64::max_value</a>!() - self.<a href="../sui_sui/balance#sui_balance_value">value</a>), <a href="../sui_sui/balance#sui_balance_EOverflow">EOverflow</a>);
    self.<a href="../sui_sui/balance#sui_balance_value">value</a> = self.<a href="../sui_sui/balance#sui_balance_value">value</a> + <a href="../sui_sui/balance#sui_balance_value">value</a>;
    <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> }
}
</code></pre>

Function <code>decrease_supply</code>

Burn a Balance<T> and decrease Supply<T>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_decrease_supply">decrease_supply</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_decrease_supply">decrease_supply</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;): u64 {
    <b>let</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> } = <a href="../sui_sui/balance#sui_balance">balance</a>;
    <b>assert</b>!(self.<a href="../sui_sui/balance#sui_balance_value">value</a> &gt;= <a href="../sui_sui/balance#sui_balance_value">value</a>, <a href="../sui_sui/balance#sui_balance_EOverflow">EOverflow</a>);
    self.<a href="../sui_sui/balance#sui_balance_value">value</a> = self.<a href="../sui_sui/balance#sui_balance_value">value</a> - <a href="../sui_sui/balance#sui_balance_value">value</a>;
    <a href="../sui_sui/balance#sui_balance_value">value</a>
}
</code></pre>

Function <code>zero</code>

Create a zero <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> for type T.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_zero">zero</a>&lt;T&gt;(): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_zero">zero</a>&lt;T&gt;(): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a>: 0 }
}
</code></pre>

Function <code>join</code>

Join two balances together.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_join">join</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_join">join</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;): u64 {
    <b>let</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> } = <a href="../sui_sui/balance#sui_balance">balance</a>;
    self.<a href="../sui_sui/balance#sui_balance_value">value</a> = self.<a href="../sui_sui/balance#sui_balance_value">value</a> + <a href="../sui_sui/balance#sui_balance_value">value</a>;
    self.<a href="../sui_sui/balance#sui_balance_value">value</a>
}
</code></pre>

Function <code>split</code>

Split a <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> and take a sub balance from it.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_split">split</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_split">split</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    <b>assert</b>!(self.<a href="../sui_sui/balance#sui_balance_value">value</a> &gt;= <a href="../sui_sui/balance#sui_balance_value">value</a>, <a href="../sui_sui/balance#sui_balance_ENotEnough">ENotEnough</a>);
    self.<a href="../sui_sui/balance#sui_balance_value">value</a> = self.<a href="../sui_sui/balance#sui_balance_value">value</a> - <a href="../sui_sui/balance#sui_balance_value">value</a>;
    <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> }
}
</code></pre>

Function <code>withdraw_all</code>

Withdraw all balance. After this the remaining balance must be 0.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_withdraw_all">withdraw_all</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_withdraw_all">withdraw_all</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/balance#sui_balance_value">value</a> = self.<a href="../sui_sui/balance#sui_balance_value">value</a>;
    <a href="../sui_sui/balance#sui_balance_split">split</a>(self, <a href="../sui_sui/balance#sui_balance_value">value</a>)
}
</code></pre>

Function <code>destroy_zero</code>

Destroy a zero <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_zero">destroy_zero</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_zero">destroy_zero</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;) {
    <b>assert</b>!(<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/balance#sui_balance_value">value</a> == 0, <a href="../sui_sui/balance#sui_balance_ENonZero">ENonZero</a>);
    <b>let</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a>: _ } = <a href="../sui_sui/balance#sui_balance">balance</a>;
}
</code></pre>

Function <code>send_funds</code>

Send a <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> to an address's funds accumulator.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_send_funds">send_funds</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_send_funds">send_funds</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;, recipient: <b>address</b>) {
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_add_impl">sui::funds_accumulator::add_impl</a>(<a href="../sui_sui/balance#sui_balance">balance</a>, recipient);
}
</code></pre>

Function <code>redeem_funds</code>

Redeem a Withdrawal&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt; to get the underlying <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; from an address's funds
accumulator.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_redeem_funds">redeem_funds</a>&lt;T&gt;(withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;&gt;): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_redeem_funds">redeem_funds</a>&lt;T&gt;(withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt;): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    withdrawal.redeem(internal::permit())
}
</code></pre>

Function <code>withdraw_funds_from_object</code>

Create a Withdrawal&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt; from an object to withdraw funds from it.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_withdraw_funds_from_object">withdraw_funds_from_object</a>&lt;T&gt;(obj: &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_withdraw_funds_from_object">withdraw_funds_from_object</a>&lt;T&gt;(obj: &<b>mut</b> UID, <a href="../sui_sui/balance#sui_balance_value">value</a>: u64): Withdrawal&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt; {
    <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_withdraw_from_object">sui::funds_accumulator::withdraw_from_object</a>(obj, <a href="../sui_sui/balance#sui_balance_value">value</a> <b>as</b> u256)
}
</code></pre>

Function <code>settled_funds_value</code>

Read the value of the funds of type T owned by <b>address</b> as of the beginning of
the current consensus commit. Can read either address-owned or object-owned balances.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_settled_funds_value">settled_funds_value</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, <b>address</b>: <b>address</b>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance_settled_funds_value">settled_funds_value</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, <b>address</b>: <b>address</b>): u64 {
    <b>if</b> (!root.u128_exists&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt;(<b>address</b>)) {
        <b>return</b> 0
    };
    <b>let</b> val: u128 = root.u128_read&lt;<a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;&gt;(<b>address</b>);
    <b>let</b> val = <a href="../sui_std/u128#std_u128_min">std::u128::min</a>(<a href="../sui_std/u64#std_u64_max_value">std::u64::max_value</a>!() <b>as</b> u128, val);
    val <b>as</b> u64
}
</code></pre>

Function <code>create_supply_internal</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/balance#sui_balance_create_supply_internal">create_supply_internal</a>&lt;T&gt;(): <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/balance#sui_balance_create_supply_internal">create_supply_internal</a>&lt;T&gt;(): <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt; {
    <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> { <a href="../sui_sui/balance#sui_balance_value">value</a>: 0 }
}
</code></pre>

Function <code>create_staking_rewards</code>

CAUTION: this function creates a <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> without increasing the supply.
It should only be called by the epoch change system txn to create staking rewards,
and nowhere else.

<code><b>fun</b> <a href="../sui_sui/balance#sui_balance_create_staking_rewards">create_staking_rewards</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance_value">value</a>: u64, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/balance#sui_balance_create_staking_rewards">create_staking_rewards</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance_value">value</a>: u64, ctx: &TxContext): <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt; {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/balance#sui_balance_ENotSystemAddress">ENotSystemAddress</a>);
    <b>assert</b>!(
        <a href="../sui_std/type_name#std_type_name_with_defining_ids">std::type_name::with_defining_ids</a>&lt;T&gt;().into_string().into_bytes() == <a href="../sui_sui/balance#sui_balance_SUI_TYPE_NAME">SUI_TYPE_NAME</a>,
        <a href="../sui_sui/balance#sui_balance_ENotSUI">ENotSUI</a>,
    );
    <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> }
}
</code></pre>

Function <code>destroy_storage_rebates</code>

CAUTION: this function destroys a <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> without decreasing the supply.
It should only be called by the epoch change system txn to destroy storage rebates,
and nowhere else.

<code><b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_storage_rebates">destroy_storage_rebates</a>&lt;T&gt;(self: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_storage_rebates">destroy_storage_rebates</a>&lt;T&gt;(self: <a href="../sui_sui/balance#sui_balance_Balance">Balance</a>&lt;T&gt;, ctx: &TxContext) {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/balance#sui_balance_ENotSystemAddress">ENotSystemAddress</a>);
    <b>assert</b>!(
        <a href="../sui_std/type_name#std_type_name_with_defining_ids">std::type_name::with_defining_ids</a>&lt;T&gt;().into_string().into_bytes() == <a href="../sui_sui/balance#sui_balance_SUI_TYPE_NAME">SUI_TYPE_NAME</a>,
        <a href="../sui_sui/balance#sui_balance_ENotSUI">ENotSUI</a>,
    );
    <b>let</b> <a href="../sui_sui/balance#sui_balance_Balance">Balance</a> { <a href="../sui_sui/balance#sui_balance_value">value</a>: _ } = self;
}
</code></pre>

Function <code>destroy_supply</code>

Destroy a <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> preventing any further minting and burning.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_supply">destroy_supply</a>&lt;T&gt;(self: <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/balance#sui_balance_destroy_supply">destroy_supply</a>&lt;T&gt;(self: <a href="../sui_sui/balance#sui_balance_Supply">Supply</a>&lt;T&gt;): u64 {
    <b>let</b> <a href="../sui_sui/balance#sui_balance_Supply">Supply</a> { <a href="../sui_sui/balance#sui_balance_value">value</a> } = self;
    <a href="../sui_sui/balance#sui_balance_value">value</a>
}
</code></pre>