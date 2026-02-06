Similar to <a href="../sui_sui/table#sui_table">sui::table</a> but the values are linked together, allowing for ordered insertion and
removal

-  [Struct LinkedTable](#sui_linked_table_LinkedTable)
-  [Struct Node](#sui_linked_table_Node)
-  [Constants](#@Constants_0)
-  [Function new](#sui_linked_table_new)
-  [Function front](#sui_linked_table_front)
-  [Function back](#sui_linked_table_back)
-  [Function push_front](#sui_linked_table_push_front)
-  [Function push_back](#sui_linked_table_push_back)
-  [Function borrow](#sui_linked_table_borrow)
-  [Function borrow_mut](#sui_linked_table_borrow_mut)
-  [Function prev](#sui_linked_table_prev)
-  [Function next](#sui_linked_table_next)
-  [Function remove](#sui_linked_table_remove)
-  [Function pop_front](#sui_linked_table_pop_front)
-  [Function pop_back](#sui_linked_table_pop_back)
-  [Function contains](#sui_linked_table_contains)
-  [Function length](#sui_linked_table_length)
-  [Function is_empty](#sui_linked_table_is_empty)
-  [Function destroy_empty](#sui_linked_table_destroy_empty)
-  [Function drop](#sui_linked_table_drop)

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

Struct <code>LinkedTable</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, <b>phantom</b> V: store&gt; <b>has</b> key, store
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
<dt>
<code>head: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;</code>
</dt>
<dd>
 the front of the table, i.e. the key of the first entry
</dd>
<dt>
<code>tail: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;</code>
</dt>
<dd>
 the back of the table, i.e. the key of the last entry
</dd>
</dl>

Struct <code>Node</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt; <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;</code>
</dt>
<dd>
 the previous key
</dd>
<dt>
<code><a href="../sui_sui/linked_table#sui_linked_table_next">next</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;</code>
</dt>
<dd>
 the next key
</dd>
<dt>
<code>value: V</code>
</dt>
<dd>
 the value being stored
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/linked_table#sui_linked_table_ETableNotEmpty">ETableNotEmpty</a>: u64 = 0;
</code>

<code><b>const</b> <a href="../sui_sui/linked_table#sui_linked_table_ETableIsEmpty">ETableIsEmpty</a>: u64 = 1;
</code>

Function <code>new</code>

Creates a new, empty table

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_new">new</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_new">new</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt; {
    <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        size: 0,
        head: option::none(),
        tail: option::none(),
    }
}
</code></pre>

Function <code>front</code>

Returns the key for the first element in the table, or None if the table is empty

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_front">front</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_front">front</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): &Option&lt;K&gt; {
    &<a href="../sui_sui/table#sui_table">table</a>.head
}
</code></pre>

Function <code>back</code>

Returns the key for the last element in the table, or None if the table is empty

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_back">back</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_back">back</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): &Option&lt;K&gt; {
    &<a href="../sui_sui/table#sui_table">table</a>.tail
}
</code></pre>

Function <code>push_front</code>

Inserts a key-value pair at the front of the table, i.e. the newly inserted pair will be
the first element in the table
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldAlreadyExists">sui::dynamic_field::EFieldAlreadyExists</a> if the table already has an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_push_front">push_front</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K, value: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_push_front">push_front</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(
    <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;,
    k: K,
    value: V,
) {
    <b>let</b> old_head = <a href="../sui_sui/table#sui_table">table</a>.head.swap_or_fill(k);
    <b>if</b> (<a href="../sui_sui/table#sui_table">table</a>.tail.is_none()) <a href="../sui_sui/table#sui_table">table</a>.tail.fill(k);
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a> = option::none();
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_next">next</a> = <b>if</b> (old_head.is_some()) {
        <b>let</b> old_head_k = old_head.destroy_some();
        field::borrow_mut&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, old_head_k).<a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a> = option::some(k);
        option::some(old_head_k)
    } <b>else</b> {
        option::none()
    };
    field::add(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a> { <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>, <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>, value });
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size + 1;
}
</code></pre>

Function <code>push_back</code>

Inserts a key-value pair at the back of the table, i.e. the newly inserted pair will be
the last element in the table
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldAlreadyExists">sui::dynamic_field::EFieldAlreadyExists</a> if the table already has an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_push_back">push_back</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K, value: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_push_back">push_back</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(
    <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;,
    k: K,
    value: V,
) {
    <b>if</b> (<a href="../sui_sui/table#sui_table">table</a>.head.is_none()) <a href="../sui_sui/table#sui_table">table</a>.head.fill(k);
    <b>let</b> old_tail = <a href="../sui_sui/table#sui_table">table</a>.tail.swap_or_fill(k);
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a> = <b>if</b> (old_tail.is_some()) {
        <b>let</b> old_tail_k = old_tail.destroy_some();
        field::borrow_mut&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, old_tail_k).<a href="../sui_sui/linked_table#sui_linked_table_next">next</a> = option::some(k);
        option::some(old_tail_k)
    } <b>else</b> {
        option::none()
    };
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_next">next</a> = option::none();
    field::add(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a> { <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>, <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>, value });
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size + 1;
}
</code></pre>

Function <code>borrow</code>

Immutable borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, k: K): &V {
    &field::borrow&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k).value
}
</code></pre>

Function <code>borrow_mut</code>

Mutably borrows the value associated with the key in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(
    <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;,
    k: K,
): &<b>mut</b> V {
    &<b>mut</b> field::borrow_mut&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k).value
}
</code></pre>

Function <code>prev</code>

Borrows the key for the previous entry of the specified key k: K in the table
<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;. Returns None if the entry does not have a predecessor.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, k: K): &Option&lt;K&gt; {
    &field::borrow&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k).<a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>
}
</code></pre>

Function <code>next</code>

Borrows the key for the next entry of the specified key k: K in the table
<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;. Returns None if the entry does not have a successor.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, k: K): &Option&lt;K&gt; {
    &field::borrow&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k).<a href="../sui_sui/linked_table#sui_linked_table_next">next</a>
}
</code></pre>

Function <code>remove</code>

Removes the key-value pair in the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt; and returns the value.
This splices the element out of the ordering.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the table does not have an entry with
that key k: K. Note: this is also what happens when the table is empty.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_remove">remove</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_remove">remove</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, k: K): V {
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt; { <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>, <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>, value } = field::remove(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, k);
    <a href="../sui_sui/table#sui_table">table</a>.size = <a href="../sui_sui/table#sui_table">table</a>.size - 1;
    <b>if</b> (<a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>.is_some()) {
        field::borrow_mut&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, *<a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>.<a href="../sui_sui/borrow#sui_borrow">borrow</a>()).<a href="../sui_sui/linked_table#sui_linked_table_next">next</a> = <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>
    };
    <b>if</b> (<a href="../sui_sui/linked_table#sui_linked_table_next">next</a>.is_some()) {
        field::borrow_mut&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<b>mut</b> <a href="../sui_sui/table#sui_table">table</a>.id, *<a href="../sui_sui/linked_table#sui_linked_table_next">next</a>.<a href="../sui_sui/borrow#sui_borrow">borrow</a>()).<a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a> = <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>
    };
    <b>if</b> (<a href="../sui_sui/table#sui_table">table</a>.head.<a href="../sui_sui/borrow#sui_borrow">borrow</a>() == &k) <a href="../sui_sui/table#sui_table">table</a>.head = <a href="../sui_sui/linked_table#sui_linked_table_next">next</a>;
    <b>if</b> (<a href="../sui_sui/table#sui_table">table</a>.tail.<a href="../sui_sui/borrow#sui_borrow">borrow</a>() == &k) <a href="../sui_sui/table#sui_table">table</a>.tail = <a href="../sui_sui/linked_table#sui_linked_table_prev">prev</a>;
    value
}
</code></pre>

Function <code>pop_front</code>

Removes the front of the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, returns the key and value.
Aborts with <a href="../sui_sui/linked_table#sui_linked_table_ETableIsEmpty">ETableIsEmpty</a> if the table is empty

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_pop_front">pop_front</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): (K, V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_pop_front">pop_front</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): (K, V) {
    <b>assert</b>!(<a href="../sui_sui/table#sui_table">table</a>.head.is_some(), <a href="../sui_sui/linked_table#sui_linked_table_ETableIsEmpty">ETableIsEmpty</a>);
    <b>let</b> head = *<a href="../sui_sui/table#sui_table">table</a>.head.<a href="../sui_sui/borrow#sui_borrow">borrow</a>();
    (head, <a href="../sui_sui/table#sui_table">table</a>.<a href="../sui_sui/linked_table#sui_linked_table_remove">remove</a>(head))
}
</code></pre>

Function <code>pop_back</code>

Removes the back of the table <a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, returns the key and value.
Aborts with <a href="../sui_sui/linked_table#sui_linked_table_ETableIsEmpty">ETableIsEmpty</a> if the table is empty

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_pop_back">pop_back</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): (K, V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_pop_back">pop_back</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<b>mut</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): (K, V) {
    <b>assert</b>!(<a href="../sui_sui/table#sui_table">table</a>.tail.is_some(), <a href="../sui_sui/linked_table#sui_linked_table_ETableIsEmpty">ETableIsEmpty</a>);
    <b>let</b> tail = *<a href="../sui_sui/table#sui_table">table</a>.tail.<a href="../sui_sui/borrow#sui_borrow">borrow</a>();
    (tail, <a href="../sui_sui/table#sui_table">table</a>.<a href="../sui_sui/linked_table#sui_linked_table_remove">remove</a>(tail))
}
</code></pre>

Function <code>contains</code>

Returns true iff there is a value associated with the key k: K in table
<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_contains">contains</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;, k: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_contains">contains</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;, k: K): bool {
    field::exists_with_type&lt;K, <a href="../sui_sui/linked_table#sui_linked_table_Node">Node</a>&lt;K, V&gt;&gt;(&<a href="../sui_sui/table#sui_table">table</a>.id, k)
}
</code></pre>

Function <code>length</code>

Returns the size of the table, the number of key-value pairs

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_length">length</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_length">length</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): u64 {
    <a href="../sui_sui/table#sui_table">table</a>.size
}
</code></pre>

Function <code>is_empty</code>

Returns true iff the table is empty (if <a href="../sui_sui/linked_table#sui_linked_table_length">length</a> returns 0)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_is_empty">is_empty</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_is_empty">is_empty</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: &<a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;): bool {
    <a href="../sui_sui/table#sui_table">table</a>.size == 0
}
</code></pre>

Function <code>destroy_empty</code>

Destroys an empty table
Aborts with <a href="../sui_sui/linked_table#sui_linked_table_ETableNotEmpty">ETableNotEmpty</a> if the table still contains values

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a> { id, size, head: _, tail: _ } = <a href="../sui_sui/table#sui_table">table</a>;
    <b>assert</b>!(size == 0, <a href="../sui_sui/linked_table#sui_linked_table_ETableNotEmpty">ETableNotEmpty</a>);
    id.delete()
}
</code></pre>

Function <code>drop</code>

Drop a possibly non-empty table.
Usable only if the value type V has the <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> ability

<code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>&lt;K: <b>copy</b>, <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store, V: <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>, store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">sui::linked_table::LinkedTable</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a>&lt;K: <b>copy</b> + <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store, V: <a href="../sui_sui/linked_table#sui_linked_table_drop">drop</a> + store&gt;(<a href="../sui_sui/table#sui_table">table</a>: <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/linked_table#sui_linked_table_LinkedTable">LinkedTable</a> { id, size: _, head: _, tail: _ } = <a href="../sui_sui/table#sui_table">table</a>;
    id.delete()
}
</code></pre>