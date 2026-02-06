-  [Struct StorageFund](#sui_system_storage_fund_StorageFund)
-  [Function new](#sui_system_storage_fund_new)
-  [Function advance_epoch](#sui_system_storage_fund_advance_epoch)
-  [Function total_object_storage_rebates](#sui_system_storage_fund_total_object_storage_rebates)
-  [Function total_balance](#sui_system_storage_fund_total_balance)

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
<b>use</b> <a href="../sui_sui/sui#sui_sui">sui::sui</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
</code>

Struct <code>StorageFund</code>

Struct representing the storage fund, containing two Balances:
- <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a> has the invariant that it's the sum of storage_rebate of
all objects currently stored on-chain. To maintain this invariant, the only inflow of this
balance is storage charges collected from transactions, and the only outflow is storage rebates
of transactions, including both the portion refunded to the transaction senders as well as
the non-refundable portion taken out and put into non_refundable_balance.
- non_refundable_balance contains any remaining inflow of the storage fund that should not
be taken out of the fund.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>non_refundable_balance: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Function <code>new</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> at genesis time.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_new">new</a>(initial_fund: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;): <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">sui_system::storage_fund::StorageFund</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_new">new</a>(initial_fund: Balance&lt;SUI&gt;): <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a> {
    <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a> {
        // At the beginning there's no object in the storage yet
        <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>: balance::zero(),
        non_refundable_balance: initial_fund,
    }
}
</code></pre>

Function <code>advance_epoch</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> at epoch change times to process the inflows and outflows of storage fund.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_advance_epoch">advance_epoch</a>(self: &<b>mut</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">sui_system::storage_fund::StorageFund</a>, storage_charges: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, storage_fund_reinvestment: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, leftover_staking_rewards: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, storage_rebate_amount: u64, non_refundable_storage_fee_amount: u64): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_advance_epoch">advance_epoch</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a>,
    storage_charges: Balance&lt;SUI&gt;,
    storage_fund_reinvestment: Balance&lt;SUI&gt;,
    leftover_staking_rewards: Balance&lt;SUI&gt;,
    storage_rebate_amount: u64,
    non_refundable_storage_fee_amount: u64,
): Balance&lt;SUI&gt; {
    // Both the reinvestment and leftover rewards are not to be refunded so they go to the non-refundable balance.
    self.non_refundable_balance.join(storage_fund_reinvestment);
    self.non_refundable_balance.join(leftover_staking_rewards);
    // The storage charges <b>for</b> the epoch come from the storage rebate of the <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_new">new</a> objects created
    // and the <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_new">new</a> storage rebates of the objects modified during the epoch so we put the charges
    // into <span className="code-inline"><a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a></span>.
    self.<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>.join(storage_charges);
    // Split out the non-refundable portion of the storage rebate and put it into the non-refundable balance.
    <b>let</b> non_refundable_storage_fee = self
        .<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>
        .split(non_refundable_storage_fee_amount);
    self.non_refundable_balance.join(non_refundable_storage_fee);
    // <span className="code-inline">storage_rebates</span> include the already refunded rebates of deleted objects and old rebates of modified objects and
    // should be taken out of the <span className="code-inline"><a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a></span>.
    <b>let</b> storage_rebate = self.<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>.split(storage_rebate_amount);
    // The storage rebate <b>has</b> already been returned to individual transaction senders' gas coins
    // so we <b>return</b> the balance to be burnt at the very end of epoch change.
    storage_rebate
}
</code></pre>

Function <code>total_object_storage_rebates</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>(self: &<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">sui_system::storage_fund::StorageFund</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>(self: &<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a>): u64 {
    self.<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>.value()
}
</code></pre>

Function <code>total_balance</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_balance">total_balance</a>(self: &<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">sui_system::storage_fund::StorageFund</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_balance">total_balance</a>(self: &<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_StorageFund">StorageFund</a>): u64 {
    self.<a href="../sui_sui_system/storage_fund#sui_system_storage_fund_total_object_storage_rebates">total_object_storage_rebates</a>.value() + self.non_refundable_balance.value()
}
</code></pre>