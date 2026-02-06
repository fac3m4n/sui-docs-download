This module provides handy functionality for wallets and sui::Coin management.

-  [Constants](#@Constants_0)
-  [Function keep](#sui_pay_keep)
-  [Function split](#sui_pay_split)
-  [Function split_vec](#sui_pay_split_vec)
-  [Function split_and_transfer](#sui_pay_split_and_transfer)
-  [Function divide_and_keep](#sui_pay_divide_and_keep)
-  [Function join](#sui_pay_join)
-  [Function join_vec](#sui_pay_join_vec)
-  [Function join_vec_and_transfer](#sui_pay_join_vec_and_transfer)

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
<b>use</b> <a href="../sui_sui/accumulator_settlement#sui_accumulator_settlement">sui::accumulator_settlement</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/bag#sui_bag">sui::bag</a>;
<b>use</b> <a href="../sui_sui/balance#sui_balance">sui::balance</a>;
<b>use</b> <a href="../sui_sui/bcs#sui_bcs">sui::bcs</a>;
<b>use</b> <a href="../sui_sui/coin#sui_coin">sui::coin</a>;
<b>use</b> <a href="../sui_sui/config#sui_config">sui::config</a>;
<b>use</b> <a href="../sui_sui/deny_list#sui_deny_list">sui::deny_list</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/dynamic_object_field#sui_dynamic_object_field">sui::dynamic_object_field</a>;
<b>use</b> <a href="../sui_sui/event#sui_event">sui::event</a>;
<b>use</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator">sui::funds_accumulator</a>;
<b>use</b> <a href="../sui_sui/hash#sui_hash">sui::hash</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
</code>

Constants

For when empty vector is supplied into join function.

<code><b>const</b> <a href="../sui_sui/pay#sui_pay_ENoCoins">ENoCoins</a>: u64 = 0;
</code>

Function <code>keep</code>

Transfer c to the sender of the current transaction

<code><b>public</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_keep">keep</a>&lt;T&gt;(c: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_keep">keep</a>&lt;T&gt;(c: Coin&lt;T&gt;, ctx: &TxContext) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(c, ctx.sender())
}
</code></pre>

Function <code>split</code>

Split <a href="../sui_sui/coin#sui_coin">coin</a> to two coins, one with balance split_amount,
and the remaining balance is left in <a href="../sui_sui/coin#sui_coin">coin</a>.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split">split</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, split_amount: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split">split</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<b>mut</b> Coin&lt;T&gt;, split_amount: u64, ctx: &<b>mut</b> TxContext) {
    <a href="../sui_sui/pay#sui_pay_keep">keep</a>(<a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/pay#sui_pay_split">split</a>(split_amount, ctx), ctx)
}
</code></pre>

Function <code>split_vec</code>

Split coin self into multiple coins, each with balance specified
in split_amounts. Remaining balance is left in self.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split_vec">split_vec</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, split_amounts: vector&lt;u64&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split_vec">split_vec</a>&lt;T&gt;(self: &<b>mut</b> Coin&lt;T&gt;, split_amounts: vector&lt;u64&gt;, ctx: &<b>mut</b> TxContext) {
    split_amounts.do!(|amount| <a href="../sui_sui/pay#sui_pay_split">split</a>(self, amount, ctx));
}
</code></pre>

Function <code>split_and_transfer</code>

Send amount units of c to recipient
Aborts with <a href="../sui_sui/balance#sui_balance_ENotEnough">sui::balance::ENotEnough</a> if amount is greater than the balance in c

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split_and_transfer">split_and_transfer</a>&lt;T&gt;(c: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, amount: u64, recipient: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_split_and_transfer">split_and_transfer</a>&lt;T&gt;(
    c: &<b>mut</b> Coin&lt;T&gt;,
    amount: u64,
    recipient: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(c.<a href="../sui_sui/pay#sui_pay_split">split</a>(amount, ctx), recipient)
}
</code></pre>

Function <code>divide_and_keep</code>

Divide coin self into n - 1 coins with equal balances. If the balance is
not evenly divisible by n, the remainder is left in self.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_divide_and_keep">divide_and_keep</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, n: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_divide_and_keep">divide_and_keep</a>&lt;T&gt;(self: &<b>mut</b> Coin&lt;T&gt;, n: u64, ctx: &<b>mut</b> TxContext) {
    self.divide_into_n(n, ctx).destroy!(|<a href="../sui_sui/coin#sui_coin">coin</a>| <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(<a href="../sui_sui/coin#sui_coin">coin</a>, ctx.sender()));
}
</code></pre>

Function <code>join</code>

Join <a href="../sui_sui/coin#sui_coin">coin</a> into self. Re-exports <a href="../sui_sui/coin#sui_coin_join">coin::join</a> function.
Deprecated: you should call <a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/pay#sui_pay_join">join</a>(other) directly.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join">join</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join">join</a>&lt;T&gt;(self: &<b>mut</b> Coin&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: Coin&lt;T&gt;) {
    self.<a href="../sui_sui/pay#sui_pay_join">join</a>(<a href="../sui_sui/coin#sui_coin">coin</a>)
}
</code></pre>

Function <code>join_vec</code>

Join everything in coins with self

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join_vec">join_vec</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, coins: vector&lt;<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join_vec">join_vec</a>&lt;T&gt;(self: &<b>mut</b> Coin&lt;T&gt;, coins: vector&lt;Coin&lt;T&gt;&gt;) {
    coins.destroy!(|<a href="../sui_sui/coin#sui_coin">coin</a>| self.<a href="../sui_sui/pay#sui_pay_join">join</a>(<a href="../sui_sui/coin#sui_coin">coin</a>));
}
</code></pre>

Function <code>join_vec_and_transfer</code>

Join a vector of Coin into a single object and transfer it to receiver.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join_vec_and_transfer">join_vec_and_transfer</a>&lt;T&gt;(coins: vector&lt;<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;&gt;, receiver: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/pay#sui_pay_join_vec_and_transfer">join_vec_and_transfer</a>&lt;T&gt;(<b>mut</b> coins: vector&lt;Coin&lt;T&gt;&gt;, receiver: <b>address</b>) {
    <b>assert</b>!(coins.length() &gt; 0, <a href="../sui_sui/pay#sui_pay_ENoCoins">ENoCoins</a>);
    <b>let</b> <b>mut</b> self = coins.pop_back();
    <a href="../sui_sui/pay#sui_pay_join_vec">join_vec</a>(&<b>mut</b> self, coins);
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(self, receiver)
}
</code></pre>