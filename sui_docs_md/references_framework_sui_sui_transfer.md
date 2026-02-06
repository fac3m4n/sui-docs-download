-  [Struct Receiving](#sui_transfer_Receiving)
-  [Constants](#@Constants_0)
-  [Function transfer](#sui_transfer_transfer)
-  [Function public_transfer](#sui_transfer_public_transfer)
-  [Function party_transfer](#sui_transfer_party_transfer)
-  [Function public_party_transfer](#sui_transfer_public_party_transfer)
-  [Function freeze_object](#sui_transfer_freeze_object)
-  [Function public_freeze_object](#sui_transfer_public_freeze_object)
-  [Function share_object](#sui_transfer_share_object)
-  [Function public_share_object](#sui_transfer_public_share_object)
-  [Function receive](#sui_transfer_receive)
-  [Function public_receive](#sui_transfer_public_receive)
-  [Function receiving_object_id](#sui_transfer_receiving_object_id)
-  [Function freeze_object_impl](#sui_transfer_freeze_object_impl)
-  [Function share_object_impl](#sui_transfer_share_object_impl)
-  [Function party_transfer_impl](#sui_transfer_party_transfer_impl)
-  [Function transfer_impl](#sui_transfer_transfer_impl)
-  [Function receive_impl](#sui_transfer_receive_impl)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Receiving</code>

This represents the ability to <a href="../sui_sui/transfer#sui_transfer_receive">receive</a> an object of type T.
This type is ephemeral per-transaction and cannot be stored on-chain.
This does not represent the obligation to receive the object that it
references, but simply the ability to receive the object with object ID
id at version version if you can prove mutable access to the parent
object during the transaction.
Internals of this struct are opaque outside this module.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a>&lt;<b>phantom</b> T: key&gt; <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>version: u64</code>
</dt>
<dd>
</dd>
</dl>

Constants

Shared an object that was previously created. Shared objects must currently
be constructed in the transaction they are created.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_ESharedNonNewObject">ESharedNonNewObject</a>: u64 = 0;
</code>

Serialization of the object failed.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_EBCSSerializationFailure">EBCSSerializationFailure</a>: u64 = 1;
</code>

The object being received is not of the expected type.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_EReceivingObjectTypeMismatch">EReceivingObjectTypeMismatch</a>: u64 = 2;
</code>

Represents both the case where the object does not exist and the case where the object is not
able to be accessed through the parent that is passed-in.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_EUnableToReceiveObject">EUnableToReceiveObject</a>: u64 = 3;
</code>

Shared object operations such as wrapping, freezing, and converting to owned are not allowed.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_ESharedObjectOperationNotSupported">ESharedObjectOperationNotSupported</a>: u64 = 4;
</code>

Operation is not yet supported by the network. The functionality might still be in development.

<code><b>const</b> <a href="../sui_sui/transfer#sui_transfer_ENotSupported">ENotSupported</a>: u64 = 5;
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/transfer#sui_transfer_EInvalidPartyPermissions">EInvalidPartyPermissions</a>: vector&lt;u8&gt; = b"Party <a href="../sui_sui/transfer#sui_transfer">transfer</a> is currently limited to one <a href="../sui_sui/party#sui_party">party</a>.";
</code>

Function <code>transfer</code>

Transfer ownership of obj to recipient. obj must have the key attribute,
which (in turn) ensures that obj has a globally unique ID. Note that if the recipient
address represents an object ID, the obj sent will be inaccessible after the transfer
(though they will be retrievable at a future date once new features are added).
This function has custom rules performed by the Sui Move bytecode verifier that ensures
that T is an object defined in the module where <a href="../sui_sui/transfer#sui_transfer">transfer</a> is invoked. Use
<a href="../sui_sui/transfer#sui_transfer_public_transfer">public_transfer</a> to transfer an object with store outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>&lt;T: key&gt;(obj: T, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>&lt;T: key&gt;(obj: T, recipient: <b>address</b>) {
    <a href="../sui_sui/transfer#sui_transfer_transfer_impl">transfer_impl</a>(obj, recipient)
}
</code></pre>

Function <code>public_transfer</code>

Transfer ownership of obj to recipient. obj must have the key attribute,
which (in turn) ensures that obj has a globally unique ID. Note that if the recipient
address represents an object ID, the obj sent will be inaccessible after the transfer
(though they will be retrievable at a future date once new features are added).
The object must have store to be transferred outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_transfer">public_transfer</a>&lt;T: key, store&gt;(obj: T, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_transfer">public_transfer</a>&lt;T: key + store&gt;(obj: T, recipient: <b>address</b>) {
    <a href="../sui_sui/transfer#sui_transfer_transfer_impl">transfer_impl</a>(obj, recipient)
}
</code></pre>

Function <code>party_transfer</code>

Transfer ownership of obj to the <a href="../sui_sui/party#sui_party">party</a>. This transfer behaves similar to both
<a href="../sui_sui/transfer#sui_transfer">transfer</a> and <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a>. It is similar to <a href="../sui_sui/transfer#sui_transfer">transfer</a> in that the object is authorized for
use only by the recipient(s), in this case the <a href="../sui_sui/party#sui_party">party</a>. This means that only the members
can use the object as an input to a transaction. It is similar to <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a> two ways. One
in that the object can potentially be used by anyone, as defined by the default permissions of
the Party value. The other in that the object must be used in consensus and cannot be
used in the fast path.
This function has custom rules performed by the Sui Move bytecode verifier that ensures that T
is an object defined in the module where <a href="../sui_sui/transfer#sui_transfer">transfer</a> is invoked. Use <a href="../sui_sui/transfer#sui_transfer_public_party_transfer">public_party_transfer</a>
to transfer an object with store outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_party_transfer">party_transfer</a>&lt;T: key&gt;(obj: T, <a href="../sui_sui/party#sui_party">party</a>: <a href="../sui_sui/party#sui_party_Party">sui::party::Party</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_party_transfer">party_transfer</a>&lt;T: key&gt;(obj: T, <a href="../sui_sui/party#sui_party">party</a>: <a href="../sui_sui/party#sui_party_Party">sui::party::Party</a>) {
    <b>assert</b>!(<a href="../sui_sui/party#sui_party">party</a>.is_single_owner(), <a href="../sui_sui/transfer#sui_transfer_EInvalidPartyPermissions">EInvalidPartyPermissions</a>);
    <b>let</b> (default, addresses, permissions) = <a href="../sui_sui/party#sui_party">party</a>.into_native();
    <a href="../sui_sui/transfer#sui_transfer_party_transfer_impl">party_transfer_impl</a>(obj, default, addresses, permissions)
}
</code></pre>

Function <code>public_party_transfer</code>

Transfer ownership of obj to the <a href="../sui_sui/party#sui_party">party</a>. This transfer behaves similar to both
<a href="../sui_sui/transfer#sui_transfer">transfer</a> and <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a>. It is similar to <a href="../sui_sui/transfer#sui_transfer">transfer</a> in that the object is authorized for
use only by the recipient(s), in this case the <a href="../sui_sui/party#sui_party">party</a>. This means that only the members
can use the object as an input to a transaction. It is similar to <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a> two ways. One
in that the object can potentially be used by anyone, as defined by the default permissions of
the Party value. The other in that the object must be used in consensus and cannot be
used in the fast path.
The object must have store to be transferred outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_party_transfer">public_party_transfer</a>&lt;T: key, store&gt;(obj: T, <a href="../sui_sui/party#sui_party">party</a>: <a href="../sui_sui/party#sui_party_Party">sui::party::Party</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_party_transfer">public_party_transfer</a>&lt;T: key + store&gt;(obj: T, <a href="../sui_sui/party#sui_party">party</a>: <a href="../sui_sui/party#sui_party_Party">sui::party::Party</a>) {
    <b>assert</b>!(<a href="../sui_sui/party#sui_party">party</a>.is_single_owner(), <a href="../sui_sui/transfer#sui_transfer_EInvalidPartyPermissions">EInvalidPartyPermissions</a>);
    <b>let</b> (default, addresses, permissions) = <a href="../sui_sui/party#sui_party">party</a>.into_native();
    <a href="../sui_sui/transfer#sui_transfer_party_transfer_impl">party_transfer_impl</a>(obj, default, addresses, permissions)
}
</code></pre>

Function <code>freeze_object</code>

Freeze obj. After freezing obj becomes immutable and can no longer be transferred or
mutated.
This function has custom rules performed by the Sui Move bytecode verifier that ensures
that T is an object defined in the module where <a href="../sui_sui/transfer#sui_transfer_freeze_object">freeze_object</a> is invoked. Use
<a href="../sui_sui/transfer#sui_transfer_public_freeze_object">public_freeze_object</a> to freeze an object with store outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_freeze_object">freeze_object</a>&lt;T: key&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_freeze_object">freeze_object</a>&lt;T: key&gt;(obj: T) {
    <a href="../sui_sui/transfer#sui_transfer_freeze_object_impl">freeze_object_impl</a>(obj)
}
</code></pre>

Function <code>public_freeze_object</code>

Freeze obj. After freezing obj becomes immutable and can no longer be transferred or
mutated.
The object must have store to be frozen outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_freeze_object">public_freeze_object</a>&lt;T: key, store&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_freeze_object">public_freeze_object</a>&lt;T: key + store&gt;(obj: T) {
    <a href="../sui_sui/transfer#sui_transfer_freeze_object_impl">freeze_object_impl</a>(obj)
}
</code></pre>

Function <code>share_object</code>

Turn the given object into a mutable shared object that everyone can access and mutate.
This is irreversible, i.e. once an object is shared, it will stay shared forever.
Aborts with <a href="../sui_sui/transfer#sui_transfer_ESharedNonNewObject">ESharedNonNewObject</a> of the object being shared was not created in this
transaction. This restriction may be relaxed in the future.
This function has custom rules performed by the Sui Move bytecode verifier that ensures
that T is an object defined in the module where <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a> is invoked. Use
<a href="../sui_sui/transfer#sui_transfer_public_share_object">public_share_object</a> to share an object with store outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a>&lt;T: key&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_share_object">share_object</a>&lt;T: key&gt;(obj: T) {
    <a href="../sui_sui/transfer#sui_transfer_share_object_impl">share_object_impl</a>(obj)
}
</code></pre>

Function <code>public_share_object</code>

Turn the given object into a mutable shared object that everyone can access and mutate.
This is irreversible, i.e. once an object is shared, it will stay shared forever.
Aborts with <a href="../sui_sui/transfer#sui_transfer_ESharedNonNewObject">ESharedNonNewObject</a> of the object being shared was not created in this
transaction. This restriction may be relaxed in the future.
The object must have store to be shared outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_share_object">public_share_object</a>&lt;T: key, store&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_share_object">public_share_object</a>&lt;T: key + store&gt;(obj: T) {
    <a href="../sui_sui/transfer#sui_transfer_share_object_impl">share_object_impl</a>(obj)
}
</code></pre>

Function <code>receive</code>

Given mutable (i.e., locked) access to the parent and a <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a> argument
referencing an object of type T owned by parent use the to_receive
argument to receive and return the referenced owned object of type T.
This function has custom rules performed by the Sui Move bytecode verifier that ensures
that T is an object defined in the module where <a href="../sui_sui/transfer#sui_transfer_receive">receive</a> is invoked. Use
<a href="../sui_sui/transfer#sui_transfer_public_receive">public_receive</a> to receivne an object with store outside of its module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receive">receive</a>&lt;T: key&gt;(parent: &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, to_receive: <a href="../sui_sui/transfer#sui_transfer_Receiving">sui::transfer::Receiving</a>&lt;T&gt;): T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receive">receive</a>&lt;T: key&gt;(parent: &<b>mut</b> UID, to_receive: <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a>&lt;T&gt;): T {
    <b>let</b> <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a> { id, version } = to_receive;
    <a href="../sui_sui/transfer#sui_transfer_receive_impl">receive_impl</a>(parent.to_address(), id, version)
}
</code></pre>

Function <code>public_receive</code>

Given mutable (i.e., locked) access to the parent and a <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a> argument
referencing an object of type T owned by parent use the to_receive
argument to receive and return the referenced owned object of type T.
The object must have store to be received outside of its defining module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_receive">public_receive</a>&lt;T: key, store&gt;(parent: &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, to_receive: <a href="../sui_sui/transfer#sui_transfer_Receiving">sui::transfer::Receiving</a>&lt;T&gt;): T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_public_receive">public_receive</a>&lt;T: key + store&gt;(parent: &<b>mut</b> UID, to_receive: <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a>&lt;T&gt;): T {
    <b>let</b> <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a> { id, version } = to_receive;
    <a href="../sui_sui/transfer#sui_transfer_receive_impl">receive_impl</a>(parent.to_address(), id, version)
}
</code></pre>

Function <code>receiving_object_id</code>

Return the object ID that the given <a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a> argument references.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receiving_object_id">receiving_object_id</a>&lt;T: key&gt;(receiving: &<a href="../sui_sui/transfer#sui_transfer_Receiving">sui::transfer::Receiving</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receiving_object_id">receiving_object_id</a>&lt;T: key&gt;(receiving: &<a href="../sui_sui/transfer#sui_transfer_Receiving">Receiving</a>&lt;T&gt;): ID {
    receiving.id
}
</code></pre>

Function <code>freeze_object_impl</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_freeze_object_impl">freeze_object_impl</a>&lt;T: key&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_freeze_object_impl">freeze_object_impl</a>&lt;T: key&gt;(obj: T);
</code></pre>

Function <code>share_object_impl</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_share_object_impl">share_object_impl</a>&lt;T: key&gt;(obj: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_share_object_impl">share_object_impl</a>&lt;T: key&gt;(obj: T);
</code></pre>

Function <code>party_transfer_impl</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_party_transfer_impl">party_transfer_impl</a>&lt;T: key&gt;(obj: T, default_permissions: u64, addresses: vector&lt;<b>address</b>&gt;, permissions: vector&lt;u64&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_party_transfer_impl">party_transfer_impl</a>&lt;T: key&gt;(
    obj: T,
    default_permissions: u64,
    addresses: vector&lt;<b>address</b>&gt;,
    permissions: vector&lt;u64&gt;,
);
</code></pre>

Function <code>transfer_impl</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_transfer_impl">transfer_impl</a>&lt;T: key&gt;(obj: T, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>native</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_transfer_impl">transfer_impl</a>&lt;T: key&gt;(obj: T, recipient: <b>address</b>);
</code></pre>

Function <code>receive_impl</code>

<code><b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receive_impl">receive_impl</a>&lt;T: key&gt;(parent: <b>address</b>, to_receive: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, version: u64): T
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer_receive_impl">receive_impl</a>&lt;T: key&gt;(parent: <b>address</b>, to_receive: ID, version: u64): T;
</code></pre>