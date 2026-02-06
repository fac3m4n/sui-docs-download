A simple library that enables hot-potato-locked borrow mechanics.

With Programmable transactions, it is possible to borrow a value within
a transaction, use it and put back in the end. Hot-potato <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a> makes
sure the object is returned and was not swapped for another one.

-  [Struct Referent](#sui_borrow_Referent)
-  [Struct Borrow](#sui_borrow_Borrow)
-  [Constants](#@Constants_0)
-  [Function new](#sui_borrow_new)
-  [Function borrow](#sui_borrow_borrow)
-  [Function put_back](#sui_borrow_put_back)
-  [Function destroy](#sui_borrow_destroy)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
</code>

Struct <code>Referent</code>

An object wrapping a T and providing the borrow API.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>&lt;T: key, store&gt; <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>value: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Borrow</code>

A hot potato making sure the object is put back once borrowed.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>ref: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>obj: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

The <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a> does not match the <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>.

<code><b>const</b> <a href="../sui_sui/borrow#sui_borrow_EWrongBorrow">EWrongBorrow</a>: u64 = 0;
</code>

An attempt to swap the <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>.value with another object of the same type.

<code><b>const</b> <a href="../sui_sui/borrow#sui_borrow_EWrongValue">EWrongValue</a>: u64 = 1;
</code>

Function <code>new</code>

Create a new <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a> struct

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_new">new</a>&lt;T: key, store&gt;(value: T, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/borrow#sui_borrow_Referent">sui::borrow::Referent</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_new">new</a>&lt;T: key + store&gt;(value: T, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>&lt;T&gt; {
    <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a> {
        id: ctx.fresh_object_address(),
        value: option::some(value),
    }
}
</code></pre>

Function <code>borrow</code>

Borrow the T from the <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>, receiving the T and a <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a>
hot potato.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/borrow#sui_borrow_Referent">sui::borrow::Referent</a>&lt;T&gt;): (T, <a href="../sui_sui/borrow#sui_borrow_Borrow">sui::borrow::Borrow</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>&lt;T&gt;): (T, <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a>) {
    <b>let</b> value = self.value.extract();
    <b>let</b> id = <a href="../sui_sui/object#sui_object_id">object::id</a>(&value);
    (
        value,
        <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a> {
            ref: self.id,
            obj: id,
        },
    )
}
</code></pre>

Function <code>put_back</code>

Put an object and the <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a> hot potato back.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_put_back">put_back</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/borrow#sui_borrow_Referent">sui::borrow::Referent</a>&lt;T&gt;, value: T, <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/borrow#sui_borrow_Borrow">sui::borrow::Borrow</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_put_back">put_back</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>&lt;T&gt;, value: T, <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a>) {
    <b>let</b> <a href="../sui_sui/borrow#sui_borrow_Borrow">Borrow</a> { ref, obj } = <a href="../sui_sui/borrow#sui_borrow">borrow</a>;
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(&value) == obj, <a href="../sui_sui/borrow#sui_borrow_EWrongValue">EWrongValue</a>);
    <b>assert</b>!(self.id == ref, <a href="../sui_sui/borrow#sui_borrow_EWrongBorrow">EWrongBorrow</a>);
    self.value.fill(value);
}
</code></pre>

Function <code>destroy</code>

Unpack the <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a> struct and return the value.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_destroy">destroy</a>&lt;T: key, store&gt;(self: <a href="../sui_sui/borrow#sui_borrow_Referent">sui::borrow::Referent</a>&lt;T&gt;): T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow_destroy">destroy</a>&lt;T: key + store&gt;(self: <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a>&lt;T&gt;): T {
    <b>let</b> <a href="../sui_sui/borrow#sui_borrow_Referent">Referent</a> { id: _, value } = self;
    value.destroy_some()
}
</code></pre>