This module implements the Kiosk Extensions functionality. It allows
exposing previously protected (only-owner) methods to third-party apps.

A Kiosk Extension is a module that implements any functionality on top of
the Kiosk without discarding nor blocking the base. Given that Kiosk
itself is a trading primitive, most of the extensions are expected to be
related to trading. However, there's no limit to what can be built using the
<a href="../sui_sui/kiosk_extension#sui_kiosk_extension">kiosk_extension</a> module, as it gives certain benefits such as using Kiosk
as the storage for any type of data / assets.

#### Flow:

- An extension can only be installed by the Kiosk Owner and requires an
authorization via the KioskOwnerCap.
- When installed, the extension is given a permission bitmap that allows it
to perform certain protected actions (eg <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a>, <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a>). However, it is
possible to install an extension that does not have any permissions.
- Kiosk Owner can <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_disable">disable</a> the extension at any time, which prevents it
from performing any protected actions. The storage is still available to the
extension until it is completely removed.
- A disabled extension can be <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_enable">enable</a>d at any time giving the permissions
back to the extension.
- An extension permissions follow the all-or-nothing policy. Either all of
the requested permissions are granted or none of them (can't install).

#### Examples:

- An Auction extension can utilize the storage to store Auction-related data
while utilizing the same Kiosk object that the items are stored in.
- A Marketplace extension that implements custom events and fees for the
default trading functionality.

#### Notes:

- Trading functionality can utilize the PurchaseCap to build a custom
logic around the purchase flow. However, it should be carefully managed to
prevent asset locking.
- <a href="../sui_sui/kiosk_extension#sui_kiosk_extension">kiosk_extension</a> is a friend module to <a href="../sui_sui/kiosk#sui_kiosk">kiosk</a> and has access to its
internal functions (such as place_internal and lock_internal to
implement custom authorization scheme for <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a> and <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a> respectively).

        -  [Flow:](#@Flow:_0)
        -  [Examples:](#@Examples:_1)
        -  [Notes:](#@Notes:_2)
-  [Struct Extension](#sui_kiosk_extension_Extension)
-  [Struct ExtensionKey](#sui_kiosk_extension_ExtensionKey)
-  [Constants](#@Constants_3)
-  [Function add](#sui_kiosk_extension_add)
-  [Function disable](#sui_kiosk_extension_disable)
-  [Function enable](#sui_kiosk_extension_enable)
-  [Function remove](#sui_kiosk_extension_remove)
-  [Function storage](#sui_kiosk_extension_storage)
-  [Function storage_mut](#sui_kiosk_extension_storage_mut)
-  [Function place](#sui_kiosk_extension_place)
-  [Function lock](#sui_kiosk_extension_lock)
-  [Function is_installed](#sui_kiosk_extension_is_installed)
-  [Function is_enabled](#sui_kiosk_extension_is_enabled)
-  [Function can_place](#sui_kiosk_extension_can_place)
-  [Function can_lock](#sui_kiosk_extension_can_lock)
-  [Function extension](#sui_kiosk_extension_extension)
-  [Function extension_mut](#sui_kiosk_extension_extension_mut)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/internal#std_internal">std::internal</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/u128#std_u128">std::u128</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/accumulator#sui_accumulator">sui::accumulator</a>;
<b>use</b> <a href="../sui_sui/accumulator_settlement#sui_accumulator_settlement">sui::accumulator_settlement</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/bag#sui_bag">sui::bag</a>;
<b>use</b> <a href="../sui_sui/balance#sui_balance">sui::balance</a>;
<b>use</b> <a href="../sui_sui/bcs#sui_bcs">sui::bcs</a>;
<b>use</b> <a href="../sui_sui/coin#sui_coin">sui::coin</a>;
<b>use</b> <a href="../sui_sui/config#sui_config">sui::config</a>;
<b>use</b> <a href="../sui_sui/deny_list#sui_deny_list">sui::deny_list</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/dynamic_object_field#sui_dynamic_object_field">sui::dynamic_object_field</a>;
<b>use</b> <a href="../sui_sui/event#sui_event">sui::event</a>;
<b>use</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator">sui::funds_accumulator</a>;
<b>use</b> <a href="../sui_sui/hash#sui_hash">sui::hash</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/kiosk#sui_kiosk">sui::kiosk</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/package#sui_package">sui::package</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/sui#sui_sui">sui::sui</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy">sui::transfer_policy</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
</code>

Struct <code>Extension</code>

The Extension struct contains the data used by the extension and the
configuration for this extension. Stored under the <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>
dynamic field.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">Extension</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
 Storage for the extension, an isolated Bag. By putting the extension
 into a single dynamic field, we reduce the amount of fields on the
 top level (eg items / listings) while giving extension developers
 the ability to store any data they want.
</dd>
<dt>
<code>permissions: u128</code>
</dt>
<dd>
 Bitmap of permissions that the extension has (can be revoked any
 moment). It's all or nothing policy - either the extension has the
 required permissions or no permissions at all.
 1st bit - <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a></code> - allows to place items for sale
 2nd bit - <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a></code> and <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a></code> - allows to lock items (and place)
 For example:
 - <code>10</code> - allows to place items and lock them.
 - <code>11</code> - allows to place items and lock them (<code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a></code> includes <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a></code>).
 - <code>01</code> - allows to place items, but not lock them.
 - <code>00</code> - no permissions.
</dd>
<dt>
<code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>: bool</code>
</dt>
<dd>
 Whether the extension can call protected actions. By default, all
 extensions are enabled (on <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension_add">add</a></code> call), however the Kiosk
 owner can disable them at any time.
 Disabling the extension does not limit its access to the storage.
</dd>
</dl>

Struct <code>ExtensionKey</code>

The <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a> is a typed dynamic field key used to store the
extension configuration and data. Ext is a phantom type that is used
to identify the extension witness.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;<b>phantom</b> Ext&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

Trying to add an extension while not being the owner of the Kiosk.

<code><b>const</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ENotOwner">ENotOwner</a>: u64 = 0;
</code>

Extension is trying to access a permissioned action while not having
the required permission.

<code><b>const</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotAllowed">EExtensionNotAllowed</a>: u64 = 2;
</code>

Extension is not installed in the Kiosk.

<code><b>const</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>: u64 = 3;
</code>

Value that represents the <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a> permission in the permissions bitmap.

<code><b>const</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_PLACE">PLACE</a>: u128 = 1;
</code>

Value that represents the <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a> and <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a> permission in the
permissions bitmap.

<code><b>const</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_LOCK">LOCK</a>: u128 = 2;
</code>

Function <code>add</code>

Add an extension to the Kiosk. Can only be performed by the owner. The
extension witness is required to allow extensions define their set of
permissions in the custom <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_add">add</a> call.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_add">add</a>&lt;Ext: drop&gt;(_ext: Ext, self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, permissions: u128, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_add">add</a>&lt;Ext: drop&gt;(
    _ext: Ext,
    self: &<b>mut</b> Kiosk,
    cap: &KioskOwnerCap,
    permissions: u128,
    ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(self.has_access(cap), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ENotOwner">ENotOwner</a>);
    df::add(
        self.uid_mut_as_owner(cap),
        <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;Ext&gt; {},
        <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">Extension</a> {
            <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>: <a href="../sui_sui/bag#sui_bag_new">bag::new</a>(ctx),
            permissions,
            <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>: <b>true</b>,
        },
    )
}
</code></pre>

Function <code>disable</code>

Revoke permissions from the extension. While it does not remove the
extension completely, it keeps it from performing any protected actions.
The storage is still available to the extension (until it's removed).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_disable">disable</a>&lt;Ext: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_disable">disable</a>&lt;Ext: drop&gt;(self: &<b>mut</b> Kiosk, cap: &KioskOwnerCap) {
    <b>assert</b>!(self.has_access(cap), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension_mut">extension_mut</a>&lt;Ext&gt;(self).<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a> = <b>false</b>;
}
</code></pre>

Function <code>enable</code>

Re-enable the extension allowing it to call protected actions (eg
<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a>, <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a>). By default, all added extensions are enabled. Kiosk
owner can disable them via <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_disable">disable</a> call.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_enable">enable</a>&lt;Ext: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_enable">enable</a>&lt;Ext: drop&gt;(self: &<b>mut</b> Kiosk, cap: &KioskOwnerCap) {
    <b>assert</b>!(self.has_access(cap), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension_mut">extension_mut</a>&lt;Ext&gt;(self).<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a> = <b>true</b>;
}
</code></pre>

Function <code>remove</code>

Remove an extension from the Kiosk. Can only be performed by the owner,
the extension storage must be empty for the transaction to succeed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_remove">remove</a>&lt;Ext: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_remove">remove</a>&lt;Ext: drop&gt;(self: &<b>mut</b> Kiosk, cap: &KioskOwnerCap) {
    <b>assert</b>!(self.has_access(cap), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    <b>let</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">Extension</a> {
        <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>,
        permissions: _,
        <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>: _,
    } = df::remove(self.uid_mut_as_owner(cap), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;Ext&gt; {});
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>.destroy_empty();
}
</code></pre>

Function <code>storage</code>

Get immutable access to the extension storage. Can only be performed by
the extension as long as the extension is installed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>&lt;Ext: drop&gt;(_ext: Ext, self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>&lt;Ext: drop&gt;(_ext: Ext, self: &Kiosk): &Bag {
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    &<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext&gt;(self).<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>
}
</code></pre>

Function <code>storage_mut</code>

Get mutable access to the extension storage. Can only be performed by
the extension as long as the extension is installed. Disabling the
extension does not prevent it from accessing the storage.

Potentially dangerous: extension developer can keep data in a Bag
therefore never really allowing the KioskOwner to remove the extension.
However, it is the case with any other solution (1) and this way we
prevent intentional extension freeze when the owner wants to ruin a
trade (2) - eg locking extension while an auction is in progress.

Extensions should be crafted carefully, and the KioskOwner should be
aware of the risks.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage_mut">storage_mut</a>&lt;Ext: drop&gt;(_ext: Ext, self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<b>mut</b> <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage_mut">storage_mut</a>&lt;Ext: drop&gt;(_ext: Ext, self: &<b>mut</b> Kiosk): &<b>mut</b> Bag {
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    &<b>mut</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension_mut">extension_mut</a>&lt;Ext&gt;(self).<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_storage">storage</a>
}
</code></pre>

Function <code>place</code>

Protected action: place an item into the Kiosk. Can be performed by an
authorized extension. The extension must have the <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a> permission or
a <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a> permission.

To prevent non-tradable items from being placed into Kiosk the method
requires a TransferPolicy for the placed type to exist.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a>&lt;Ext: drop, T: key, store&gt;(_ext: Ext, self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, item: T, _policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a>&lt;Ext: drop, T: key + store&gt;(
    _ext: Ext,
    self: &<b>mut</b> Kiosk,
    item: T,
    _policy: &TransferPolicy&lt;T&gt;,
) {
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_place">can_place</a>&lt;Ext&gt;(self) || <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_lock">can_lock</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotAllowed">EExtensionNotAllowed</a>);
    self.place_internal(item)
}
</code></pre>

Function <code>lock</code>

Protected action: lock an item in the Kiosk. Can be performed by an
authorized extension. The extension must have the <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a> permission.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a>&lt;Ext: drop, T: key, store&gt;(_ext: Ext, self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, item: T, _policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a>&lt;Ext: drop, T: key + store&gt;(
    _ext: Ext,
    self: &<b>mut</b> Kiosk,
    item: T,
    _policy: &TransferPolicy&lt;T&gt;,
) {
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotInstalled">EExtensionNotInstalled</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_lock">can_lock</a>&lt;Ext&gt;(self), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_EExtensionNotAllowed">EExtensionNotAllowed</a>);
    self.lock_internal(item)
}
</code></pre>

Function <code>is_installed</code>

Check whether an extension of type Ext is installed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext: drop&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_installed">is_installed</a>&lt;Ext: drop&gt;(self: &Kiosk): bool {
    df::exists_(self.uid(), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;Ext&gt; {})
}
</code></pre>

Function <code>is_enabled</code>

Check whether an extension of type Ext is enabled.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>&lt;Ext: drop&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>&lt;Ext: drop&gt;(self: &Kiosk): bool {
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext&gt;(self).<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>
}
</code></pre>

Function <code>can_place</code>

Check whether an extension of type Ext can <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a> into Kiosk.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_place">can_place</a>&lt;Ext: drop&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_place">can_place</a>&lt;Ext: drop&gt;(self: &Kiosk): bool {
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>&lt;Ext&gt;(self) && <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext&gt;(self).permissions & <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_PLACE">PLACE</a> != 0
}
</code></pre>

Function <code>can_lock</code>

Check whether an extension of type Ext can <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_lock">lock</a> items in Kiosk.
Locking also enables <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_place">place</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_lock">can_lock</a>&lt;Ext: drop&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_can_lock">can_lock</a>&lt;Ext: drop&gt;(self: &Kiosk): bool {
    <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_is_enabled">is_enabled</a>&lt;Ext&gt;(self) && <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext&gt;(self).permissions & <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_LOCK">LOCK</a> != 0
}
</code></pre>

Function <code>extension</code>

Internal: get a read-only access to the Extension.

<code><b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext: drop&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">sui::kiosk_extension::Extension</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension">extension</a>&lt;Ext: drop&gt;(self: &Kiosk): &<a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">Extension</a> {
    df::borrow(self.uid(), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;Ext&gt; {})
}
</code></pre>

Function <code>extension_mut</code>

Internal: get a mutable access to the Extension.

<code><b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension_mut">extension_mut</a>&lt;Ext: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<b>mut</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">sui::kiosk_extension::Extension</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_extension_mut">extension_mut</a>&lt;Ext: drop&gt;(self: &<b>mut</b> Kiosk): &<b>mut</b> <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_Extension">Extension</a> {
    df::borrow_mut(self.uid_mut_internal(), <a href="../sui_sui/kiosk_extension#sui_kiosk_extension_ExtensionKey">ExtensionKey</a>&lt;Ext&gt; {})
}
</code></pre>