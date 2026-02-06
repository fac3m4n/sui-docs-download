Enables the creation of objects with deterministic addresses derived from a parent object's UID.
This module provides a way to generate objects with predictable addresses based on a parent UID
and a key, creating a namespace that ensures uniqueness for each parent-key combination,
which is usually how registries are built.

Key features:
- Deterministic address generation based on parent object UID and key
- Derived objects can exist and operate independently of their parent

The derived UIDs, once created, are independent and do not require sequencing on the parent
object. They can be used without affecting the parent. The parent only maintains a record of
which derived addresses have been claimed to prevent duplicates.

-  [Struct Claimed](#sui_derived_object_Claimed)
-  [Struct DerivedObjectKey](#sui_derived_object_DerivedObjectKey)
-  [Enum ClaimedStatus](#sui_derived_object_ClaimedStatus)
-  [Constants](#@Constants_0)
-  [Function claim](#sui_derived_object_claim)
-  [Function exists](#sui_derived_object_exists)
-  [Function derive_address](#sui_derived_object_derive_address)

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

Struct <code>Claimed</code>

Added as a DF to the parent's UID, to mark an ID as claimed.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/derived_object#sui_derived_object_Claimed">Claimed</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>0: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>DerivedObjectKey</code>

An internal key to protect from generating the same UID twice (e.g. collide with DFs)

<code><b>public</b> <b>struct</b> <a href="../sui_sui/derived_object#sui_derived_object_DerivedObjectKey">DerivedObjectKey</a>&lt;K: <b>copy</b>, drop, store&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>0: K</code>
</dt>
<dd>
</dd>
</dl>

Enum <code>ClaimedStatus</code>

The possible values of a claimed UID.
We make it an enum to make upgradeability easier in the future.

<code><b>public</b> <b>enum</b> <a href="../sui_sui/derived_object#sui_derived_object_ClaimedStatus">ClaimedStatus</a> <b>has</b> store
</code>

<summary>Variants</summary>

<dl>
<dt>
Variant <code>Reserved</code>
</dt>
<dd>
 The UID has been claimed and cannot be re-claimed or used.
</dd>
</dl>

Constants

Tries to create an object twice with the same parent-key combination.

<code>#[error]
<b>const</b> <a href="../sui_sui/derived_object#sui_derived_object_EObjectAlreadyExists">EObjectAlreadyExists</a>: vector&lt;u8&gt; = b"Derived <a href="../sui_sui/object#sui_object">object</a> is already claimed.";
</code>

Function <code>claim</code>

Claim a deterministic UID, using the parent's UID & any key.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_claim">claim</a>&lt;K: <b>copy</b>, drop, store&gt;(parent: &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, key: K): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_claim">claim</a>&lt;K: <b>copy</b> + drop + store&gt;(parent: &<b>mut</b> UID, key: K): UID {
    <b>let</b> addr = <a href="../sui_sui/derived_object#sui_derived_object_derive_address">derive_address</a>(parent.to_inner(), key);
    <b>let</b> id = addr.to_id();
    <b>assert</b>!(!df::exists_(parent, <a href="../sui_sui/derived_object#sui_derived_object_Claimed">Claimed</a>(id)), <a href="../sui_sui/derived_object#sui_derived_object_EObjectAlreadyExists">EObjectAlreadyExists</a>);
    df::add(parent, <a href="../sui_sui/derived_object#sui_derived_object_Claimed">Claimed</a>(id), ClaimedStatus::Reserved);
    <a href="../sui_sui/object#sui_object_new_uid_from_hash">object::new_uid_from_hash</a>(addr)
}
</code></pre>

Function <code>exists</code>

Checks if a provided key has been claimed for the given parent.
Note: If the UID has been deleted through <a href="../sui_sui/object#sui_object_delete">object::delete</a>, this will always return true.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_exists">exists</a>&lt;K: <b>copy</b>, drop, store&gt;(parent: &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, key: K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_exists">exists</a>&lt;K: <b>copy</b> + drop + store&gt;(parent: &UID, key: K): bool {
    <b>let</b> addr = <a href="../sui_sui/derived_object#sui_derived_object_derive_address">derive_address</a>(parent.to_inner(), key);
    df::exists_(parent, <a href="../sui_sui/derived_object#sui_derived_object_Claimed">Claimed</a>(addr.to_id()))
}
</code></pre>

Function <code>derive_address</code>

Given an ID and a Key, it calculates the derived address.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_derive_address">derive_address</a>&lt;K: <b>copy</b>, drop, store&gt;(parent: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, key: K): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/derived_object#sui_derived_object_derive_address">derive_address</a>&lt;K: <b>copy</b> + drop + store&gt;(parent: ID, key: K): <b>address</b> {
    df::hash_type_and_key(parent.to_address(), <a href="../sui_sui/derived_object#sui_derived_object_DerivedObjectKey">DerivedObjectKey</a>(key))
}
</code></pre>