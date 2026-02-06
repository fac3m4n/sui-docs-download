A table is a map-like collection. But unlike a traditional collection, it's keys and values are
not stored within the <a href="../sui_sui/table#sui_table_Table">Table</a> value, but instead are stored using Sui's object system. The
<a href="../sui_sui/table#sui_table_Table">Table</a> struct acts only as a handle into the object system to retrieve those keys and values.
Note that this means that <a href="../sui_sui/table#sui_table_Table">Table</a> values with exactly the same key-value mapping will not be
equal, with ==, at runtime. For example
```
let table1 = table::new<u64, bool>();
let table2 = table::new<u64, bool>();
table::add(&mut table1, 0, false);
table::add(&mut table1, 1, true);
table::add(&mut table2, 0, false);
table::add(&mut table2, 1, true);
// table1 does not equal table2, despite having the same entries
assert!(&table1 != &table2);
```

-  [Struct Table](#sui_table_Table)
-  [Constants](#@Constants_0)
-  [Function new](#sui_table_new)
-  [Function add](#sui_table_add)
-  [Function borrow](#sui_table_borrow)
-  [Function borrow_mut](#sui_table_borrow_mut)
-  [Function remove](#sui_table_remove)
-  [Function contains](#sui_table_contains)
-  [Function length](#sui_table_length)
-  [Function is_empty](#sui_table_is_empty)
-  [Function destroy_empty](#sui_table_destroy_empty)
-  [Function drop](#sui_table_drop)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
</code>

Struct <code>Table</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;<b>phantom</b> K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, <b>phantom</b> V: store&gt; <b>has</b> key, store
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

<code><b>const</b> <a href="../sui_sui/table#sui_table_ETableNotEmpty">ETableNotEmpty</a>: u64 = 0;
</code>

Function <code>new</code>

Creates a new, empty table

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_new">new</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_new">new</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt; {
    <a href="../sui_sui/table#sui_table_Table">Table</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        size: 0,
    }
}
</code></pre>

Function <code>add</code>

Adds a key-value pair to the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldAlreadyExists">sui::dynamic_field::EFieldAlreadyExists</a> if the table already has an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_add">add</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;, k: K, v: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_add">add</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;, k: K, v: V) {
    field::add(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k, v);
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size + 1;
}
</code></pre>

Function <code>borrow</code>

Immutable borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;, k: K): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;, k: K): &V {
    field::borrow(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>borrow_mut</code>

Mutably borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;, k: K): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;, k: K): &<b>mut</b> V {
    field::borrow_mut(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>remove</code>

Removes the key-value pair in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt; and returns the value.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_remove">remove</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;, k: K): V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_remove">remove</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;, k: K): V {
    <b>let</b> v = field::remove(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k);
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size - 1;
    v
}
</code></pre>

Function <code>contains</code>

Returns true if there is a value associated with the key k: K in table <a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_contains">contains</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;, k: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_contains">contains</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;, k: K): bool {
    field::exists_with_type&lt;K, V&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>length</code>

Returns the size of the table, the number of key-value pairs

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_length">length</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_length">length</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;): u64 {
    <a href="../sui_sui/table#sui_table">table</a>.size
}
</code></pre>

Function <code>is_empty</code>

Returns true if the table is empty (if <a href="../sui_sui/table#sui_table_length">length</a> returns 0)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_is_empty">is_empty</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_is_empty">is_empty</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;): bool {
    <a href="../sui_sui/table#sui_table">table</a>.size == 0
}
</code></pre>

Function <code>destroy_empty</code>

Destroys an empty table
Aborts with <a href="../sui_sui/table#sui_table_ETableNotEmpty">ETableNotEmpty</a> if the table still contains values

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/table#sui_table_Table">Table</a> { id, size } = <a href="../sui_sui/table#sui_table">table</a>;
    <b>assert</b>!(size == 0, <a href="../sui_sui/table#sui_table_ETableNotEmpty">ETableNotEmpty</a>);
    id.delete()
}
</code></pre>

Function <code>drop</code>

Drop a possibly non-empty table.
Usable only if the value type V has the <a href="../sui_sui/table#sui_table_drop">drop</a> ability

<code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_drop">drop</a>&lt;K: <b>copy</b>, <a href="../sui_sui/table#sui_table_drop">drop</a>, store, V: <a href="../sui_sui/table#sui_table_drop">drop</a>, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/table#sui_table_drop">drop</a>&lt;K: <b>copy</b> + <a href="../sui_sui/table#sui_table_drop">drop</a> + store, V: <a href="../sui_sui/table#sui_table_drop">drop</a> + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/table#sui_table_Table">Table</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/table#sui_table_Table">Table</a> { id, size: _ } = <a href="../sui_sui/table#sui_table">table</a>;
    id.delete()
}
</code></pre>