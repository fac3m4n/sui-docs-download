-  [Struct TxContext](#sui_tx_context_TxContext)
-  [Function sender](#sui_tx_context_sender)
-  [Function native_sender](#sui_tx_context_native_sender)
-  [Function digest](#sui_tx_context_digest)
-  [Function epoch](#sui_tx_context_epoch)
-  [Function native_epoch](#sui_tx_context_native_epoch)
-  [Function epoch_timestamp_ms](#sui_tx_context_epoch_timestamp_ms)
-  [Function native_epoch_timestamp_ms](#sui_tx_context_native_epoch_timestamp_ms)
-  [Function sponsor](#sui_tx_context_sponsor)
-  [Function fresh_object_address](#sui_tx_context_fresh_object_address)
-  [Function fresh_id](#sui_tx_context_fresh_id)
-  [Function reference_gas_price](#sui_tx_context_reference_gas_price)
-  [Function native_rgp](#sui_tx_context_native_rgp)
-  [Function gas_price](#sui_tx_context_gas_price)
-  [Function native_gas_price](#sui_tx_context_native_gas_price)
-  [Function native_ids_created](#sui_tx_context_native_ids_created)
-  [Function native_gas_budget](#sui_tx_context_native_gas_budget)
-  [Function option_sponsor](#sui_tx_context_option_sponsor)
-  [Function native_sponsor](#sui_tx_context_native_sponsor)
-  [Function derive_id](#sui_tx_context_derive_id)

<code><b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>TxContext</code>

Information about the transaction currently being executed.
This cannot be constructed by a transaction--it is a privileged object created by
the VM and passed in to the entrypoint of the transaction as &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/tx_context#sui_tx_context_sender">sender</a>: <b>address</b></code>
</dt>
<dd>
 The address of the user that signed the current transaction
</dd>
<dt>
<code>tx_hash: vector&lt;u8&gt;</code>
</dt>
<dd>
 Hash of the current transaction
</dd>
<dt>
<code><a href="../sui_sui/tx_context#sui_tx_context_epoch">epoch</a>: u64</code>
</dt>
<dd>
 The current epoch number
</dd>
<dt>
<code><a href="../sui_sui/tx_context#sui_tx_context_epoch_timestamp_ms">epoch_timestamp_ms</a>: u64</code>
</dt>
<dd>
 Timestamp that the epoch started at
</dd>
<dt>
<code>ids_created: u64</code>
</dt>
<dd>
 Counter recording the number of fresh id's created while executing
 this transaction. Always 0 at the start of a transaction
</dd>
</dl>

Function <code>sender</code>

Return the address of the user that signed the current
transaction

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_sender">sender</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_sender">sender</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): <b>address</b> {
    <a href="../sui_sui/tx_context#sui_tx_context_native_sender">native_sender</a>()
}
</code></pre>

Function <code>native_sender</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_sender">native_sender</a>(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_sender">native_sender</a>(): <b>address</b>;
</code></pre>

Function <code>digest</code>

Return the transaction digest (hash of transaction inputs).
Please do not use as a source of randomness.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_digest">digest</a>(self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_digest">digest</a>(self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): &vector&lt;u8&gt; {
    &self.tx_hash
}
</code></pre>

Function <code>epoch</code>

Return the current epoch

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_epoch">epoch</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_epoch">epoch</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): u64 {
    <a href="../sui_sui/tx_context#sui_tx_context_native_epoch">native_epoch</a>()
}
</code></pre>

Function <code>native_epoch</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_epoch">native_epoch</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_epoch">native_epoch</a>(): u64;
</code></pre>

Function <code>epoch_timestamp_ms</code>

Return the epoch start time as a unix timestamp in milliseconds.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_epoch_timestamp_ms">epoch_timestamp_ms</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_epoch_timestamp_ms">epoch_timestamp_ms</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): u64 {
    <a href="../sui_sui/tx_context#sui_tx_context_native_epoch_timestamp_ms">native_epoch_timestamp_ms</a>()
}
</code></pre>

Function <code>native_epoch_timestamp_ms</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_epoch_timestamp_ms">native_epoch_timestamp_ms</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_epoch_timestamp_ms">native_epoch_timestamp_ms</a>(): u64;
</code></pre>

Function <code>sponsor</code>

Return the adress of the transaction sponsor or None if there was no sponsor.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_sponsor">sponsor</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_sponsor">sponsor</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): Option&lt;<b>address</b>&gt; {
    <a href="../sui_sui/tx_context#sui_tx_context_option_sponsor">option_sponsor</a>()
}
</code></pre>

Function <code>fresh_object_address</code>

Create an <b>address</b> that has not been used. As it is an object address, it will never
occur as the address for a user.
In other words, the generated address is a globally unique object ID.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_fresh_object_address">fresh_object_address</a>(_ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_fresh_object_address">fresh_object_address</a>(_ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): <b>address</b> {
    <a href="../sui_sui/tx_context#sui_tx_context_fresh_id">fresh_id</a>()
}
</code></pre>

Function <code>fresh_id</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_fresh_id">fresh_id</a>(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_fresh_id">fresh_id</a>(): <b>address</b>;
</code></pre>

Function <code>reference_gas_price</code>

Return the reference gas price in effect for the epoch the transaction
is being executed in.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_reference_gas_price">reference_gas_price</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_reference_gas_price">reference_gas_price</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): u64 {
    <a href="../sui_sui/tx_context#sui_tx_context_native_rgp">native_rgp</a>()
}
</code></pre>

Function <code>native_rgp</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_rgp">native_rgp</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_rgp">native_rgp</a>(): u64;
</code></pre>

Function <code>gas_price</code>

Return the gas price submitted for the current transaction.
That is the value the user submitted with the transaction data.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_gas_price">gas_price</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_gas_price">gas_price</a>(_self: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">TxContext</a>): u64 {
    <a href="../sui_sui/tx_context#sui_tx_context_native_gas_price">native_gas_price</a>()
}
</code></pre>

Function <code>native_gas_price</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_gas_price">native_gas_price</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_gas_price">native_gas_price</a>(): u64;
</code></pre>

Function <code>native_ids_created</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_ids_created">native_ids_created</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_ids_created">native_ids_created</a>(): u64;
</code></pre>

Function <code>native_gas_budget</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_gas_budget">native_gas_budget</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_gas_budget">native_gas_budget</a>(): u64;
</code></pre>

Function <code>option_sponsor</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_option_sponsor">option_sponsor</a>(): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_option_sponsor">option_sponsor</a>(): Option&lt;<b>address</b>&gt; {
    <b>let</b> <a href="../sui_sui/tx_context#sui_tx_context_sponsor">sponsor</a> = <a href="../sui_sui/tx_context#sui_tx_context_native_sponsor">native_sponsor</a>();
    <b>if</b> (<a href="../sui_sui/tx_context#sui_tx_context_sponsor">sponsor</a>.length() == 0) option::none() <b>else</b> option::some(<a href="../sui_sui/tx_context#sui_tx_context_sponsor">sponsor</a>[0])
}
</code></pre>

Function <code>native_sponsor</code>

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_sponsor">native_sponsor</a>(): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_native_sponsor">native_sponsor</a>(): vector&lt;<b>address</b>&gt;;
</code></pre>

Function <code>derive_id</code>

Native function for deriving an ID via hash(tx_hash || ids_created)

<code><b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_derive_id">derive_id</a>(tx_hash: vector&lt;u8&gt;, ids_created: u64): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/tx_context#sui_tx_context_derive_id">derive_id</a>(tx_hash: vector&lt;u8&gt;, ids_created: u64): <b>address</b>;
</code></pre>