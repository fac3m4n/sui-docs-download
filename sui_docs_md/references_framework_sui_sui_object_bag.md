Similar to <a href="../sui_sui/bag#sui_bag">sui::bag</a>, an <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> is a heterogeneous map-like collection. But unlike
<a href="../sui_sui/bag#sui_bag">sui::bag</a>, the values bound to these dynamic fields _must_ be objects themselves. This allows
for the objects to still exist in storage, which may be important for external tools.
The difference is otherwise not observable from within Move.

-  [Struct ObjectBag](#sui_object_bag_ObjectBag)
-  [Constants](#@Constants_0)
-  [Function new](#sui_object_bag_new)
-  [Function add](#sui_object_bag_add)
-  [Function borrow](#sui_object_bag_borrow)
-  [Function borrow_mut](#sui_object_bag_borrow_mut)
-  [Function remove](#sui_object_bag_remove)
-  [Function contains](#sui_object_bag_contains)
-  [Function contains_with_type](#sui_object_bag_contains_with_type)
-  [Function length](#sui_object_bag_length)
-  [Function is_empty](#sui_object_bag_is_empty)
-  [Function destroy_empty](#sui_object_bag_destroy_empty)
-  [Function value_id](#sui_object_bag_value_id)

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

Struct <code>ObjectBag</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
 the ID of this bag
</dd>
<dt>
<code>size: u64</code>
</dt>
<dd>
 the number of key-value pairs in the bag
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/object_bag#sui_object_bag_EBagNotEmpty">EBagNotEmpty</a>: u64 = 0;
</code>

Function <code>new</code>

Creates a new, empty bag

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_new">new</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_new">new</a>(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> {
    <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        size: 0,
    }
}
</code></pre>

Function <code>add</code>

Adds a key-value pair to the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldAlreadyExists">sui::dynamic_field::EFieldAlreadyExists</a> if the bag already has an entry with
that key k: K.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_add">add</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K, v: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_add">add</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K, v: V) {
    ofield::add(&<b>mut</b> <a href="../sui_sui/bag#sui_bag">bag</a>.id, k, v);
    <a href="../sui_sui/bag#sui_bag">bag</a>.size = <a href="../sui_sui/bag#sui_bag">bag</a>.size + 1;
}
</code></pre>

Function <code>borrow</code>

Immutably borrows the value associated with the key in the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the bag does not have an entry with
that key k: K.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldTypeMismatch">sui::dynamic_field::EFieldTypeMismatch</a> if the bag has an entry for the key, but
the value does not have the specified type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): &V {
    ofield::borrow(&<a href="../sui_sui/bag#sui_bag">bag</a>.id, k)
}
</code></pre>

Function <code>borrow_mut</code>

Mutably borrows the value associated with the key in the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the bag does not have an entry with
that key k: K.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldTypeMismatch">sui::dynamic_field::EFieldTypeMismatch</a> if the bag has an entry for the key, but
the value does not have the specified type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_borrow_mut">borrow_mut</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): &<b>mut</b> V {
    ofield::borrow_mut(&<b>mut</b> <a href="../sui_sui/bag#sui_bag">bag</a>.id, k)
}
</code></pre>

Function <code>remove</code>

Mutably borrows the key-value pair in the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> and returns the value.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldDoesNotExist">sui::dynamic_field::EFieldDoesNotExist</a> if the bag does not have an entry with
that key k: K.
Aborts with <a href="../sui_sui/dynamic_field#sui_dynamic_field_EFieldTypeMismatch">sui::dynamic_field::EFieldTypeMismatch</a> if the bag has an entry for the key, but
the value does not have the specified type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_remove">remove</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_remove">remove</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<b>mut</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): V {
    <b>let</b> v = ofield::remove(&<b>mut</b> <a href="../sui_sui/bag#sui_bag">bag</a>.id, k);
    <a href="../sui_sui/bag#sui_bag">bag</a>.size = <a href="../sui_sui/bag#sui_bag">bag</a>.size - 1;
    v
}
</code></pre>

Function <code>contains</code>

Returns true iff there is an value associated with the key k: K in the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_contains">contains</a>&lt;K: <b>copy</b>, drop, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_contains">contains</a>&lt;K: <b>copy</b> + drop + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): bool {
    ofield::exists_&lt;K&gt;(&<a href="../sui_sui/bag#sui_bag">bag</a>.id, k)
}
</code></pre>

Function <code>contains_with_type</code>

Returns true iff there is an value associated with the key k: K in the bag <a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>
with an assigned value of type V

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_contains_with_type">contains_with_type</a>&lt;K: <b>copy</b>, drop, store, V: key, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_contains_with_type">contains_with_type</a>&lt;K: <b>copy</b> + drop + store, V: key + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): bool {
    ofield::exists_with_type&lt;K, V&gt;(&<a href="../sui_sui/bag#sui_bag">bag</a>.id, k)
}
</code></pre>

Function <code>length</code>

Returns the size of the bag, the number of key-value pairs

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_length">length</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_length">length</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>): u64 {
    <a href="../sui_sui/bag#sui_bag">bag</a>.size
}
</code></pre>

Function <code>is_empty</code>

Returns true iff the bag is empty (if <a href="../sui_sui/object_bag#sui_object_bag_length">length</a> returns 0)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_is_empty">is_empty</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_is_empty">is_empty</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>): bool {
    <a href="../sui_sui/bag#sui_bag">bag</a>.size == 0
}
</code></pre>

Function <code>destroy_empty</code>

Destroys an empty bag
Aborts with <a href="../sui_sui/object_bag#sui_object_bag_EBagNotEmpty">EBagNotEmpty</a> if the bag still contains values

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_destroy_empty">destroy_empty</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_destroy_empty">destroy_empty</a>(<a href="../sui_sui/bag#sui_bag">bag</a>: <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>) {
    <b>let</b> <a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a> { id, size } = <a href="../sui_sui/bag#sui_bag">bag</a>;
    <b>assert</b>!(size == 0, <a href="../sui_sui/object_bag#sui_object_bag_EBagNotEmpty">EBagNotEmpty</a>);
    id.delete()
}
</code></pre>

Function <code>value_id</code>

Returns the ID of the object associated with the key if the bag has an entry with key k: K
Returns none otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_value_id">value_id</a>&lt;K: <b>copy</b>, drop, store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">sui::object_bag::ObjectBag</a>, k: K): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object_bag#sui_object_bag_value_id">value_id</a>&lt;K: <b>copy</b> + drop + store&gt;(<a href="../sui_sui/bag#sui_bag">bag</a>: &<a href="../sui_sui/object_bag#sui_object_bag_ObjectBag">ObjectBag</a>, k: K): Option&lt;ID&gt; {
    ofield::id(&<a href="../sui_sui/bag#sui_bag">bag</a>.id, k)
}
</code></pre>