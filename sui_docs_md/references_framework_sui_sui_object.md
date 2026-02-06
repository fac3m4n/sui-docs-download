Sui object identifiers

-  [Struct ID](#sui_object_ID)
-  [Struct UID](#sui_object_UID)
-  [Constants](#@Constants_0)
-  [Function id_to_bytes](#sui_object_id_to_bytes)
-  [Function id_to_address](#sui_object_id_to_address)
-  [Function id_from_bytes](#sui_object_id_from_bytes)
-  [Function id_from_address](#sui_object_id_from_address)
-  [Function sui_system_state](#sui_object_sui_system_state)
-  [Function clock](#sui_object_clock)
-  [Function authenticator_state](#sui_object_authenticator_state)
-  [Function randomness_state](#sui_object_randomness_state)
-  [Function sui_deny_list_object_id](#sui_object_sui_deny_list_object_id)
-  [Function sui_accumulator_root_object_id](#sui_object_sui_accumulator_root_object_id)
-  [Function sui_accumulator_root_address](#sui_object_sui_accumulator_root_address)
-  [Function sui_coin_registry_object_id](#sui_object_sui_coin_registry_object_id)
-  [Function sui_coin_registry_address](#sui_object_sui_coin_registry_address)
-  [Function bridge](#sui_object_bridge)
-  [Function address_alias_state](#sui_object_address_alias_state)
-  [Function uid_as_inner](#sui_object_uid_as_inner)
-  [Function uid_to_inner](#sui_object_uid_to_inner)
-  [Function uid_to_bytes](#sui_object_uid_to_bytes)
-  [Function uid_to_address](#sui_object_uid_to_address)
-  [Function new](#sui_object_new)
-  [Function delete](#sui_object_delete)
-  [Function id](#sui_object_id)
-  [Function borrow_id](#sui_object_borrow_id)
-  [Function id_bytes](#sui_object_id_bytes)
-  [Function id_address](#sui_object_id_address)
-  [Function borrow_uid](#sui_object_borrow_uid)
-  [Function new_uid_from_hash](#sui_object_new_uid_from_hash)
-  [Function delete_impl](#sui_object_delete_impl)
-  [Function record_new_uid](#sui_object_record_new_uid)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
</code>

Struct <code>ID</code>

An object ID. This is used to reference Sui Objects.
This is *not* guaranteed to be globally unique--anyone can create an <a href="../sui_sui/object#sui_object_ID">ID</a> from a <a href="../sui_sui/object#sui_object_UID">UID</a> or
from an object, and ID's can be freely copied and dropped.
Here, the values are not globally unique because there can be multiple values of type <a href="../sui_sui/object#sui_object_ID">ID</a>
with the same underlying bytes. For example, <a href="../sui_sui/object#sui_object_id">object::id</a>(&obj) can be called as many times
as you want for a given obj, and each <a href="../sui_sui/object#sui_object_ID">ID</a> value will be identical.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/object#sui_object_ID">ID</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>bytes: <b>address</b></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>UID</code>

Globally unique IDs that define an object's ID in storage. Any Sui Object, that is a struct
with the key ability, must have <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_UID">UID</a> as its first field.
These are globally unique in the sense that no two values of type <a href="../sui_sui/object#sui_object_UID">UID</a> are ever equal, in
other words for any two values id1: <a href="../sui_sui/object#sui_object_UID">UID</a> and id2: <a href="../sui_sui/object#sui_object_UID">UID</a>, id1 != id2.
This is a privileged type that can only be derived from a TxContext.
<a href="../sui_sui/object#sui_object_UID">UID</a> doesn't have the drop ability, so deleting a <a href="../sui_sui/object#sui_object_UID">UID</a> requires a call to <a href="../sui_sui/object#sui_object_delete">delete</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/object#sui_object_UID">UID</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

The hardcoded ID for the singleton Sui System State Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_SYSTEM_STATE_OBJECT_ID">SUI_SYSTEM_STATE_OBJECT_ID</a>: <b>address</b> = 0x5;
</code>

The hardcoded ID for the singleton Clock Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_CLOCK_OBJECT_ID">SUI_CLOCK_OBJECT_ID</a>: <b>address</b> = 0x6;
</code>

The hardcoded ID for the singleton AuthenticatorState Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_AUTHENTICATOR_STATE_ID">SUI_AUTHENTICATOR_STATE_ID</a>: <b>address</b> = 0x7;
</code>

The hardcoded ID for the singleton Random Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_RANDOM_ID">SUI_RANDOM_ID</a>: <b>address</b> = 0x8;
</code>

The hardcoded ID for the singleton DenyList.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_DENY_LIST_OBJECT_ID">SUI_DENY_LIST_OBJECT_ID</a>: <b>address</b> = 0x403;
</code>

The hardcoded ID for the singleton AccumulatorRoot Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_ACCUMULATOR_ROOT_OBJECT_ID">SUI_ACCUMULATOR_ROOT_OBJECT_ID</a>: <b>address</b> = 0xacc;
</code>

The hardcoded ID for the Bridge Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_BRIDGE_ID">SUI_BRIDGE_ID</a>: <b>address</b> = 0x9;
</code>

The hardcoded ID for the Coin Registry Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_COIN_REGISTRY_OBJECT_ID">SUI_COIN_REGISTRY_OBJECT_ID</a>: <b>address</b> = 0xc;
</code>

The hardcoded ID for the AddressAliasState Object.

<code><b>const</b> <a href="../sui_sui/object#sui_object_SUI_ADDRESS_ALIAS_STATE_ID">SUI_ADDRESS_ALIAS_STATE_ID</a>: <b>address</b> = 0xa;
</code>

Sender is not @0x0 the system address.

<code><b>const</b> <a href="../sui_sui/object#sui_object_ENotSystemAddress">ENotSystemAddress</a>: u64 = 0;
</code>

Function <code>id_to_bytes</code>

Get the raw bytes of a <a href="../sui_sui/object#sui_object_ID">ID</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_to_bytes">id_to_bytes</a>(<a href="../sui_sui/object#sui_object_id">id</a>: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_to_bytes">id_to_bytes</a>(<a href="../sui_sui/object#sui_object_id">id</a>: &<a href="../sui_sui/object#sui_object_ID">ID</a>): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>(&<a href="../sui_sui/object#sui_object_id">id</a>.bytes)
}
</code></pre>

Function <code>id_to_address</code>

Get the inner bytes of <a href="../sui_sui/object#sui_object_id">id</a> as an address.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_to_address">id_to_address</a>(<a href="../sui_sui/object#sui_object_id">id</a>: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_to_address">id_to_address</a>(<a href="../sui_sui/object#sui_object_id">id</a>: &<a href="../sui_sui/object#sui_object_ID">ID</a>): <b>address</b> {
    <a href="../sui_sui/object#sui_object_id">id</a>.bytes
}
</code></pre>

Function <code>id_from_bytes</code>

Make an <a href="../sui_sui/object#sui_object_ID">ID</a> from raw bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_from_bytes">id_from_bytes</a>(bytes: vector&lt;u8&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_from_bytes">id_from_bytes</a>(bytes: vector&lt;u8&gt;): <a href="../sui_sui/object#sui_object_ID">ID</a> {
    <a href="../sui_sui/address#sui_address_from_bytes">address::from_bytes</a>(bytes).to_id()
}
</code></pre>

Function <code>id_from_address</code>

Make an <a href="../sui_sui/object#sui_object_ID">ID</a> from an address.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_from_address">id_from_address</a>(bytes: <b>address</b>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_from_address">id_from_address</a>(bytes: <b>address</b>): <a href="../sui_sui/object#sui_object_ID">ID</a> {
    <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes }
}
</code></pre>

Function <code>sui_system_state</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton SuiSystemState object.
This should only be called once from sui_system.

<code><b>fun</b> <a href="../sui_sui/object#sui_object_sui_system_state">sui_system_state</a>(ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/object#sui_object_sui_system_state">sui_system_state</a>(ctx: &TxContext): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/object#sui_object_ENotSystemAddress">ENotSystemAddress</a>);
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_SYSTEM_STATE_OBJECT_ID">SUI_SYSTEM_STATE_OBJECT_ID</a> },
    }
}
</code></pre>

Function <code>clock</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton Clock object.
This should only be called once from <a href="../sui_sui/clock#sui_clock">clock</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/clock#sui_clock">clock</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/clock#sui_clock">clock</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_CLOCK_OBJECT_ID">SUI_CLOCK_OBJECT_ID</a> },
    }
}
</code></pre>

Function <code>authenticator_state</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton AuthenticatorState object.
This should only be called once from <a href="../sui_sui/authenticator_state#sui_authenticator_state">authenticator_state</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/authenticator_state#sui_authenticator_state">authenticator_state</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/authenticator_state#sui_authenticator_state">authenticator_state</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_AUTHENTICATOR_STATE_ID">SUI_AUTHENTICATOR_STATE_ID</a> },
    }
}
</code></pre>

Function <code>randomness_state</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton Random object.
This should only be called once from <a href="../sui_sui/random#sui_random">random</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_randomness_state">randomness_state</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_randomness_state">randomness_state</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_RANDOM_ID">SUI_RANDOM_ID</a> },
    }
}
</code></pre>

Function <code>sui_deny_list_object_id</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton DenyList object.
This should only be called once from <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_deny_list_object_id">sui_deny_list_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_deny_list_object_id">sui_deny_list_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_DENY_LIST_OBJECT_ID">SUI_DENY_LIST_OBJECT_ID</a> },
    }
}
</code></pre>

Function <code>sui_accumulator_root_object_id</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_accumulator_root_object_id">sui_accumulator_root_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_accumulator_root_object_id">sui_accumulator_root_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_ACCUMULATOR_ROOT_OBJECT_ID">SUI_ACCUMULATOR_ROOT_OBJECT_ID</a> },
    }
}
</code></pre>

Function <code>sui_accumulator_root_address</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_accumulator_root_address">sui_accumulator_root_address</a>(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_accumulator_root_address">sui_accumulator_root_address</a>(): <b>address</b> {
    <a href="../sui_sui/object#sui_object_SUI_ACCUMULATOR_ROOT_OBJECT_ID">SUI_ACCUMULATOR_ROOT_OBJECT_ID</a>
}
</code></pre>

Function <code>sui_coin_registry_object_id</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton CoinRegistry object.
This should only be called once from <a href="../sui_sui/coin_registry#sui_coin_registry">coin_registry</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_coin_registry_object_id">sui_coin_registry_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_coin_registry_object_id">sui_coin_registry_object_id</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_COIN_REGISTRY_OBJECT_ID">SUI_COIN_REGISTRY_OBJECT_ID</a> },
    }
}
</code></pre>

Function <code>sui_coin_registry_address</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_coin_registry_address">sui_coin_registry_address</a>(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_sui_coin_registry_address">sui_coin_registry_address</a>(): <b>address</b> {
    <a href="../sui_sui/object#sui_object_SUI_COIN_REGISTRY_OBJECT_ID">SUI_COIN_REGISTRY_OBJECT_ID</a>
}
</code></pre>

Function <code>bridge</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton Bridge object.
This should only be called once from <a href="../sui_sui/object#sui_object_bridge">bridge</a>.

<code><b>fun</b> <a href="../sui_sui/object#sui_object_bridge">bridge</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/object#sui_object_bridge">bridge</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_BRIDGE_ID">SUI_BRIDGE_ID</a> },
    }
}
</code></pre>

Function <code>address_alias_state</code>

Create the <a href="../sui_sui/object#sui_object_UID">UID</a> for the singleton AddressAliasState object.
This should only be called once from <a href="../sui_sui/address_alias#sui_address_alias">address_alias</a>.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_address_alias_state">address_alias_state</a>(): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_address_alias_state">address_alias_state</a>(): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: <a href="../sui_sui/object#sui_object_SUI_ADDRESS_ALIAS_STATE_ID">SUI_ADDRESS_ALIAS_STATE_ID</a> },
    }
}
</code></pre>

Function <code>uid_as_inner</code>

Get the inner <a href="../sui_sui/object#sui_object_ID">ID</a> of uid

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_as_inner">uid_as_inner</a>(uid: &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>): &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_as_inner">uid_as_inner</a>(uid: &<a href="../sui_sui/object#sui_object_UID">UID</a>): &<a href="../sui_sui/object#sui_object_ID">ID</a> {
    &uid.<a href="../sui_sui/object#sui_object_id">id</a>
}
</code></pre>

Function <code>uid_to_inner</code>

Get the raw bytes of a uid's inner <a href="../sui_sui/object#sui_object_ID">ID</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_inner">uid_to_inner</a>(uid: &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_inner">uid_to_inner</a>(uid: &<a href="../sui_sui/object#sui_object_UID">UID</a>): <a href="../sui_sui/object#sui_object_ID">ID</a> {
    uid.<a href="../sui_sui/object#sui_object_id">id</a>
}
</code></pre>

Function <code>uid_to_bytes</code>

Get the raw bytes of a <a href="../sui_sui/object#sui_object_UID">UID</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_bytes">uid_to_bytes</a>(uid: &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_bytes">uid_to_bytes</a>(uid: &<a href="../sui_sui/object#sui_object_UID">UID</a>): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>(&uid.<a href="../sui_sui/object#sui_object_id">id</a>.bytes)
}
</code></pre>

Function <code>uid_to_address</code>

Get the inner bytes of <a href="../sui_sui/object#sui_object_id">id</a> as an address.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_address">uid_to_address</a>(uid: &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_uid_to_address">uid_to_address</a>(uid: &<a href="../sui_sui/object#sui_object_UID">UID</a>): <b>address</b> {
    uid.<a href="../sui_sui/object#sui_object_id">id</a>.bytes
}
</code></pre>

Function <code>new</code>

Create a new object. Returns the <a href="../sui_sui/object#sui_object_UID">UID</a> that must be stored in a Sui object.
This is the only way to create <a href="../sui_sui/object#sui_object_UID">UID</a>s.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_new">new</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_new">new</a>(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_UID">UID</a> {
        <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes: ctx.fresh_object_address() },
    }
}
</code></pre>

Function <code>delete</code>

Delete the object and its <a href="../sui_sui/object#sui_object_UID">UID</a>. This is the only way to eliminate a <a href="../sui_sui/object#sui_object_UID">UID</a>.
This exists to inform Sui of object deletions. When an object
gets unpacked, the programmer will have to do something with its
<a href="../sui_sui/object#sui_object_UID">UID</a>. The implementation of this function emits a deleted
system event so Sui knows to process the object deletion

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_delete">delete</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_delete">delete</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_UID">UID</a>) {
    <b>let</b> <a href="../sui_sui/object#sui_object_UID">UID</a> { <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes } } = <a href="../sui_sui/object#sui_object_id">id</a>;
    <a href="../sui_sui/object#sui_object_delete_impl">delete_impl</a>(bytes)
}
</code></pre>

Function <code>id</code>

Get the underlying <a href="../sui_sui/object#sui_object_ID">ID</a> of obj

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id">id</a>&lt;T: key&gt;(obj: &T): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id">id</a>&lt;T: key&gt;(obj: &T): <a href="../sui_sui/object#sui_object_ID">ID</a> {
    <a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>(obj).<a href="../sui_sui/object#sui_object_id">id</a>
}
</code></pre>

Function <code>borrow_id</code>

Borrow the underlying <a href="../sui_sui/object#sui_object_ID">ID</a> of obj

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_borrow_id">borrow_id</a>&lt;T: key&gt;(obj: &T): &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_borrow_id">borrow_id</a>&lt;T: key&gt;(obj: &T): &<a href="../sui_sui/object#sui_object_ID">ID</a> {
    &<a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>(obj).<a href="../sui_sui/object#sui_object_id">id</a>
}
</code></pre>

Function <code>id_bytes</code>

Get the raw bytes for the underlying <a href="../sui_sui/object#sui_object_ID">ID</a> of obj

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_bytes">id_bytes</a>&lt;T: key&gt;(obj: &T): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_bytes">id_bytes</a>&lt;T: key&gt;(obj: &T): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>(&<a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>(obj).<a href="../sui_sui/object#sui_object_id">id</a>)
}
</code></pre>

Function <code>id_address</code>

Get the inner bytes for the underlying <a href="../sui_sui/object#sui_object_ID">ID</a> of obj

<code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_address">id_address</a>&lt;T: key&gt;(obj: &T): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/object#sui_object_id_address">id_address</a>&lt;T: key&gt;(obj: &T): <b>address</b> {
    <a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>(obj).<a href="../sui_sui/object#sui_object_id">id</a>.bytes
}
</code></pre>

Function <code>borrow_uid</code>

Get the <a href="../sui_sui/object#sui_object_UID">UID</a> for obj.
Safe because Sui has an extra bytecode verifier pass that forces every struct with
the key ability to have a distinguished <a href="../sui_sui/object#sui_object_UID">UID</a> field.
Cannot be made public as the access to <a href="../sui_sui/object#sui_object_UID">UID</a> for a given object must be privileged, and
restrictable in the object's module.

<code><b>fun</b> <a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>&lt;T: key&gt;(obj: &T): &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/object#sui_object_borrow_uid">borrow_uid</a>&lt;T: key&gt;(obj: &T): &<a href="../sui_sui/object#sui_object_UID">UID</a>;
</code></pre>

Function <code>new_uid_from_hash</code>

Generate a new UID specifically used for creating a UID from a hash

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_new_uid_from_hash">new_uid_from_hash</a>(bytes: <b>address</b>): <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/object#sui_object_new_uid_from_hash">new_uid_from_hash</a>(bytes: <b>address</b>): <a href="../sui_sui/object#sui_object_UID">UID</a> {
    <a href="../sui_sui/object#sui_object_record_new_uid">record_new_uid</a>(bytes);
    <a href="../sui_sui/object#sui_object_UID">UID</a> { <a href="../sui_sui/object#sui_object_id">id</a>: <a href="../sui_sui/object#sui_object_ID">ID</a> { bytes } }
}
</code></pre>

Function <code>delete_impl</code>

<code><b>fun</b> <a href="../sui_sui/object#sui_object_delete_impl">delete_impl</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/object#sui_object_delete_impl">delete_impl</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <b>address</b>);
</code></pre>

Function <code>record_new_uid</code>

<code><b>fun</b> <a href="../sui_sui/object#sui_object_record_new_uid">record_new_uid</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/object#sui_object_record_new_uid">record_new_uid</a>(<a href="../sui_sui/object#sui_object_id">id</a>: <b>address</b>);
</code></pre>