Similar to <a href="../sui_sui/table#sui_table">sui::table</a>, an <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt; is a map-like collection. But unlike
<a href="../sui_sui/table#sui_table">sui::table</a>, the values bound to these dynamic fields _must_ be objects themselves. This allows
for the objects to still exist within in storage, which may be important for external tools.
The difference is otherwise not observable from within Move.

-  [Struct ObjectTable](#sui_object_table_ObjectTable)
-  [Constants](#@Constants_0)
-  [Function new](#sui_object_table_new)
-  [Function add](#sui_object_table_add)
-  [Function borrow](#sui_object_table_borrow)
-  [Function borrow_mut](#sui_object_table_borrow_mut)
-  [Function remove](#sui_object_table_remove)
-  [Function contains](#sui_object_table_contains)
-  [Function length](#sui_object_table_length)
-  [Function is_empty](#sui_object_table_is_empty)
-  [Function destroy_empty](#sui_object_table_destroy_empty)
-  [Function value_id](#sui_object_table_value_id)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/dynamic_object_field#sui_dynamic_object_field">sui::dynamic_object_field</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
</code>

Struct <code>ObjectTable</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;<b>phantom</b> K: <b>copy</b>, drop, store, <b>phantom</b> V: key, store&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
 the ID of this table
</dd>
<dt>
<code>size: u64</code>
</dt>
<dd>
 the number of key-value pairs in the table
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/object_table#sui_object_table_ETableNotEmpty">ETableNotEmpty</a>: u64 = 0;
</code>

Function <code>new</code>

Creates a new, empty table

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_new">new</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_new">new</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt; {
    <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        size: 0,
    }
}
</code></pre>

Function <code>add</code>

Adds a key-value pair to the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldAlreadyExists">sui::dynamic_field::EFieldAlreadyExists</a> if the table already has an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_add">add</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K, v: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_add">add</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;, k: K, v: V) {
    ofield::add(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k, v);
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size + 1;
}
</code></pre>

Function <code>borrow</code>

Immutable borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;, k: K): &V {
    ofield::borrow(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>borrow_mut</code>

Mutably borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(
    <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;,
    k: K,
): &<b>mut</b> V {
    ofield::borrow_mut(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>remove</code>

Removes the key-value pair in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt; and returns the value.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_remove">remove</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K): V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_remove">remove</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;, k: K): V {
    <b>let</b> v = ofield::remove(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k);
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size - 1;
    v
}
</code></pre>

Function <code>contains</code>

Returns true if there is a value associated with the key k: K in table
<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_contains">contains</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_contains">contains</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;, k: K): bool {
    ofield::exists_&lt;K&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>length</code>

Returns the size of the table, the number of key-value pairs

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_length">length</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_length">length</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;): u64 {
    <a href="../sui_sui/table#sui_table">table</a>.size
}
</code></pre>

Function <code>is_empty</code>

Returns true if the table is empty (if <a href="../sui_sui/object_table#sui_object_table_length">length</a> returns 0)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_is_empty">is_empty</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_is_empty">is_empty</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;): bool {
    <a href="../sui_sui/table#sui_table">table</a>.size == 0
}
</code></pre>

Function <code>destroy_empty</code>

Destroys an empty table
Aborts with <a href="../sui_sui/object_table#sui_object_table_ETableNotEmpty">ETableNotEmpty</a> if the table still contains values

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a> { id, size } = <a href="../sui_sui/table#sui_table">table</a>;
    <b>assert</b>!(size == 0, <a href="../sui_sui/object_table#sui_object_table_ETableNotEmpty">ETableNotEmpty</a>);
    id.delete()
}
</code></pre>

Function <code>value_id</code>

Returns the ID of the object associated with the key if the table has an entry with key k: K
Returns none otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_value_id">value_id</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">sui::object_table::ObjectTable</a>&lt;K, V&gt;, k: K): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_table#sui_object_table_value_id">value_id</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(
    <a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/object_table#sui_object_table_ObjectTable">ObjectTable</a>&lt;K, V&gt;,
    k: K,
): Option&lt;ID&gt; {
    ofield::id(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>