-  [Struct AccumulatorRoot](#sui_accumulator_AccumulatorRoot)
-  [Struct U128](#sui_accumulator_U128)
-  [Struct Key](#sui_accumulator_Key)
-  [Constants](#@Constants_0)
-  [Function create](#sui_accumulator_create)
-  [Function root_id](#sui_accumulator_root_id)
-  [Function root_id_mut](#sui_accumulator_root_id_mut)
-  [Function accumulator_u128_exists](#sui_accumulator_accumulator_u128_exists)
-  [Function accumulator_u128_read](#sui_accumulator_accumulator_u128_read)
-  [Function create_u128](#sui_accumulator_create_u128)
-  [Function destroy_u128](#sui_accumulator_destroy_u128)
-  [Function update_u128](#sui_accumulator_update_u128)
-  [Function is_zero_u128](#sui_accumulator_is_zero_u128)
-  [Function accumulator_key](#sui_accumulator_accumulator_key)
-  [Function accumulator_address](#sui_accumulator_accumulator_address)
-  [Function root_has_accumulator](#sui_accumulator_root_has_accumulator)
-  [Function root_add_accumulator](#sui_accumulator_root_add_accumulator)
-  [Function root_borrow_accumulator_mut](#sui_accumulator_root_borrow_accumulator_mut)
-  [Function root_borrow_accumulator](#sui_accumulator_root_borrow_accumulator)
-  [Function root_remove_accumulator](#sui_accumulator_root_remove_accumulator)
-  [Function emit_deposit_event](#sui_accumulator_emit_deposit_event)
-  [Function emit_withdraw_event](#sui_accumulator_emit_withdraw_event)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>AccumulatorRoot</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>U128</code>

Storage for 128-bit accumulator values.

Currently only used to represent the sum of 64 bit values (such as Balance&lt;T&gt;).
The additional bits are necessary to prevent overflow, as it would take 2^64 deposits of U64_MAX
to cause an overflow.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>value: u128</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Key</code>

<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a> is used only for computing the field id of accumulator objects.
T is the type of the accumulated value, e.g. Balance&lt;SUI&gt;

<code><b>public</b> <b>struct</b> <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><b>address</b>: <b>address</b></code>
</dt>
<dd>
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/accumulator#sui_accumulator_ENotSystemAddress">ENotSystemAddress</a>: u64 = 0;
</code>

Function <code>create</code>

<code><b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_create">create</a>(ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_create">create</a>(ctx: &TxContext) {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/accumulator#sui_accumulator_ENotSystemAddress">ENotSystemAddress</a>);
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a> {
        id: <a href="../sui_sui/object#sui_object_sui_accumulator_root_object_id">object::sui_accumulator_root_object_id</a>(),
    })
}
</code></pre>

Function <code>root_id</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_id">root_id</a>(accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>): &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_id">root_id</a>(accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>): &UID {
    &accumulator_root.id
}
</code></pre>

Function <code>root_id_mut</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_id_mut">root_id_mut</a>(accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>): &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_id_mut">root_id_mut</a>(accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>): &<b>mut</b> UID {
    &<b>mut</b> accumulator_root.id
}
</code></pre>

Function <code>accumulator_u128_exists</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_u128_exists">accumulator_u128_exists</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, <b>address</b>: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_u128_exists">accumulator_u128_exists</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>, <b>address</b>: <b>address</b>): bool {
    root.has_accumulator&lt;T, <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a>&gt;(<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;T&gt; { <b>address</b> })
}
</code></pre>

Function <code>accumulator_u128_read</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_u128_read">accumulator_u128_read</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, <b>address</b>: <b>address</b>): u128
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_u128_read">accumulator_u128_read</a>&lt;T&gt;(root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>, <b>address</b>: <b>address</b>): u128 {
    <b>let</b> <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a> = root.borrow_accumulator&lt;T, <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a>&gt;(<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;T&gt; { <b>address</b> });
    <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>.value
}
</code></pre>

Function <code>create_u128</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_create_u128">create_u128</a>(value: u128): <a href="../sui_sui/accumulator#sui_accumulator_U128">sui::accumulator::U128</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_create_u128">create_u128</a>(value: u128): <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a> {
    <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a> { value }
}
</code></pre>

Function <code>destroy_u128</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_destroy_u128">destroy_u128</a>(u128: <a href="../sui_sui/accumulator#sui_accumulator_U128">sui::accumulator::U128</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_destroy_u128">destroy_u128</a>(u128: <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a>) {
    <b>let</b> <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a> { value: _ } = u128;
}
</code></pre>

Function <code>update_u128</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_update_u128">update_u128</a>(u128: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_U128">sui::accumulator::U128</a>, merge: u128, split: u128)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_update_u128">update_u128</a>(u128: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a>, merge: u128, split: u128) {
    u128.value = u128.value + merge - split;
}
</code></pre>

Function <code>is_zero_u128</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_is_zero_u128">is_zero_u128</a>(u128: &<a href="../sui_sui/accumulator#sui_accumulator_U128">sui::accumulator::U128</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_is_zero_u128">is_zero_u128</a>(u128: &<a href="../sui_sui/accumulator#sui_accumulator_U128">U128</a>): bool {
    u128.value == 0
}
</code></pre>

Function <code>accumulator_key</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_key">accumulator_key</a>&lt;T&gt;(<b>address</b>: <b>address</b>): <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_key">accumulator_key</a>&lt;T&gt;(<b>address</b>: <b>address</b>): <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;T&gt; {
    <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a> { <b>address</b> }
}
</code></pre>

Function <code>accumulator_address</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_address">accumulator_address</a>&lt;T&gt;(<b>address</b>: <b>address</b>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_accumulator_address">accumulator_address</a>&lt;T&gt;(<b>address</b>: <b>address</b>): <b>address</b> {
    <b>let</b> key = <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;T&gt; { <b>address</b> };
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_hash_type_and_key">dynamic_field::hash_type_and_key</a>(sui_accumulator_root_address(), key)
}
</code></pre>

Function <code>root_has_accumulator</code>

Balance object methods

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_has_accumulator">root_has_accumulator</a>&lt;K, V: store&gt;(accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, name: <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;K&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_has_accumulator">root_has_accumulator</a>&lt;K, V: store&gt;(
    accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>,
    name: <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;,
): bool {
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_exists_with_type">dynamic_field::exists_with_type</a>&lt;<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;, V&gt;(&accumulator_root.id, name)
}
</code></pre>

Function <code>root_add_accumulator</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_add_accumulator">root_add_accumulator</a>&lt;K, V: store&gt;(accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, name: <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;K&gt;, value: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_add_accumulator">root_add_accumulator</a>&lt;K, V: store&gt;(
    accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>,
    name: <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;,
    value: V,
) {
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_add">dynamic_field::add</a>(&<b>mut</b> accumulator_root.id, name, value);
}
</code></pre>

Function <code>root_borrow_accumulator_mut</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_borrow_accumulator_mut">root_borrow_accumulator_mut</a>&lt;K, V: store&gt;(accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, name: <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;K&gt;): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_borrow_accumulator_mut">root_borrow_accumulator_mut</a>&lt;K, V: store&gt;(
    accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>,
    name: <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;,
): &<b>mut</b> V {
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_borrow_mut">dynamic_field::borrow_mut</a>&lt;<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;, V&gt;(&<b>mut</b> accumulator_root.id, name)
}
</code></pre>

Function <code>root_borrow_accumulator</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_borrow_accumulator">root_borrow_accumulator</a>&lt;K, V: store&gt;(accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, name: <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;K&gt;): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_borrow_accumulator">root_borrow_accumulator</a>&lt;K, V: store&gt;(
    accumulator_root: &<a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>,
    name: <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;,
): &V {
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_borrow">dynamic_field::borrow</a>&lt;<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;, V&gt;(&accumulator_root.id, name)
}
</code></pre>

Function <code>root_remove_accumulator</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_remove_accumulator">root_remove_accumulator</a>&lt;K, V: store&gt;(accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">sui::accumulator::AccumulatorRoot</a>, name: <a href="../sui_sui/accumulator#sui_accumulator_Key">sui::accumulator::Key</a>&lt;K&gt;): V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_root_remove_accumulator">root_remove_accumulator</a>&lt;K, V: store&gt;(
    accumulator_root: &<b>mut</b> <a href="../sui_sui/accumulator#sui_accumulator_AccumulatorRoot">AccumulatorRoot</a>,
    name: <a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;,
): V {
    <a href="../sui_sui/dynamic_field#sui_dynamic_field_remove">dynamic_field::remove</a>&lt;<a href="../sui_sui/accumulator#sui_accumulator_Key">Key</a>&lt;K&gt;, V&gt;(&<b>mut</b> accumulator_root.id, name)
}
</code></pre>

Function <code>emit_deposit_event</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_emit_deposit_event">emit_deposit_event</a>&lt;T&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>, recipient: <b>address</b>, amount: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_emit_deposit_event">emit_deposit_event</a>&lt;T&gt;(
    <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>,
    recipient: <b>address</b>,
    amount: u64,
);
</code></pre>

Function <code>emit_withdraw_event</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_emit_withdraw_event">emit_withdraw_event</a>&lt;T&gt;(<a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>, owner: <b>address</b>, amount: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/accumulator#sui_accumulator_emit_withdraw_event">emit_withdraw_event</a>&lt;T&gt;(
    <a href="../sui_sui/accumulator#sui_accumulator">accumulator</a>: <b>address</b>,
    owner: <b>address</b>,
    amount: u64,
);
</code></pre>