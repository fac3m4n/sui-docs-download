Kiosk is a primitive for building safe, decentralized and trustless trading
experiences. It allows storing and trading any types of assets as long as
the creator of these assets implements a TransferPolicy for them.

#### Principles and philosophy:

- Kiosk provides guarantees of "true ownership"; - just like single owner
objects, assets stored in the Kiosk can only be managed by the Kiosk owner.
Only the owner can <a href="../sui_sui/kiosk#sui_kiosk_place">place</a>, <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>, <a href="../sui_sui/kiosk#sui_kiosk_list">list</a>, perform any other actions on
assets in the Kiosk.

- Kiosk aims to be generic - allowing for a small set of default behaviors
and not imposing any restrictions on how the assets can be traded. The only
default scenario is a <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> + <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a> flow; any other trading logic can
be implemented on top using the <a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a> (and a matching
<a href="../sui_sui/kiosk#sui_kiosk_purchase_with_cap">purchase_with_cap</a>) flow.

- For every transaction happening with a third party a TransferRequest is
created - this way creators are fully in control of the trading experience.

#### Asset states in the Kiosk:

- placed -  An asset is <a href="../sui_sui/kiosk#sui_kiosk_place">place</a>d into the Kiosk and can be <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>n out by
the Kiosk owner; it's freely tradable and modifiable via the <a href="../sui_sui/kiosk#sui_kiosk_borrow_mut">borrow_mut</a>
and <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a> functions.

- locked - Similar to placed except that <a href="../sui_sui/kiosk#sui_kiosk_take">take</a> is disabled and the only
way to move the asset out of the Kiosk is to <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> it or
<a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a> therefore performing a trade (issuing a
TransferRequest). The check on the <a href="../sui_sui/kiosk#sui_kiosk_lock">lock</a> function makes sure that the
TransferPolicy exists to not lock the item in a <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> forever.

- listed - A <a href="../sui_sui/kiosk#sui_kiosk_place">place</a>d or a <a href="../sui_sui/kiosk#sui_kiosk_lock">lock</a>ed item can be <a href="../sui_sui/kiosk#sui_kiosk_list">list</a>ed for a fixed price
allowing anyone to <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a> it from the Kiosk. While listed, an item can
not be taken or modified. However, an immutable borrow via <a href="../sui_sui/borrow#sui_borrow">borrow</a> call is
still available. The <a href="../sui_sui/kiosk#sui_kiosk_delist">delist</a> function returns the asset to the previous
state.

- listed_exclusively - An item is listed via the <a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>
function (and a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> is created). While listed this way, an item
can not be <a href="../sui_sui/kiosk#sui_kiosk_delist">delist</a>-ed unless a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> is returned. All actions
available at this item state require a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>:

1. <a href="../sui_sui/kiosk#sui_kiosk_purchase_with_cap">purchase_with_cap</a> - to purchase the item for a price equal or higher
than the min_price set in the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>.
2. <a href="../sui_sui/kiosk#sui_kiosk_return_purchase_cap">return_purchase_cap</a> - to return the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> and return the asset
into the previous state.

When an item is listed exclusively it cannot be modified nor taken and
losing a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> would lock the item in the Kiosk forever. Therefore,
it is recommended to only use <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> functionality in trusted
applications and not use it for direct trading (eg sending to another
account).

#### Using multiple Transfer Policies for different "tracks":

Every <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a> or purchase_with_purchase_cap creates a TransferRequest
hot potato which must be resolved in a matching TransferPolicy for the
transaction to pass. While the default scenario implies that there should be
a single TransferPolicy&lt;T&gt; for T; it is possible to have multiple, each
one having its own set of rules.

#### Examples:

- I create one TransferPolicy with "Royalty Rule" for everyone
- I create a special TransferPolicy for bearers of a "Club Membership"
object so they don't have to pay anything
- I create and wrap a TransferPolicy so that players of my game can
transfer items between <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>s in game without any charge (and maybe not
even paying the price with a 0 SUI PurchaseCap)

```
Kiosk -> (Item, TransferRequest)
... TransferRequest ------> Common Transfer Policy
... TransferRequest ------> In-game Wrapped Transfer Policy
... TransferRequest ------> Club Membership Transfer Policy
```

See <a href="../sui_sui/transfer_policy#sui_transfer_policy">transfer_policy</a> module for more details on how they function.

        -  [Principles and philosophy:](#@Principles_and_philosophy:_0)
        -  [Asset states in the Kiosk:](#@Asset_states_in_the_Kiosk:_1)
        -  [Using multiple Transfer Policies for different "tracks":](#@Using_multiple_Transfer_Policies_for_different_"tracks":_2)
        -  [Examples:](#@Examples:_3)
-  [Struct Kiosk](#sui_kiosk_Kiosk)
-  [Struct KioskOwnerCap](#sui_kiosk_KioskOwnerCap)
-  [Struct PurchaseCap](#sui_kiosk_PurchaseCap)
-  [Struct Borrow](#sui_kiosk_Borrow)
-  [Struct Item](#sui_kiosk_Item)
-  [Struct Listing](#sui_kiosk_Listing)
-  [Struct Lock](#sui_kiosk_Lock)
-  [Struct ItemListed](#sui_kiosk_ItemListed)
-  [Struct ItemPurchased](#sui_kiosk_ItemPurchased)
-  [Struct ItemDelisted](#sui_kiosk_ItemDelisted)
-  [Constants](#@Constants_4)
-  [Function default](#sui_kiosk_default)
-  [Function new](#sui_kiosk_new)
-  [Function close_and_withdraw](#sui_kiosk_close_and_withdraw)
-  [Function set_owner](#sui_kiosk_set_owner)
-  [Function set_owner_custom](#sui_kiosk_set_owner_custom)
-  [Function place](#sui_kiosk_place)
-  [Function lock](#sui_kiosk_lock)
-  [Function take](#sui_kiosk_take)
-  [Function list](#sui_kiosk_list)
-  [Function place_and_list](#sui_kiosk_place_and_list)
-  [Function delist](#sui_kiosk_delist)
-  [Function purchase](#sui_kiosk_purchase)
-  [Function list_with_purchase_cap](#sui_kiosk_list_with_purchase_cap)
-  [Function purchase_with_cap](#sui_kiosk_purchase_with_cap)
-  [Function return_purchase_cap](#sui_kiosk_return_purchase_cap)
-  [Function withdraw](#sui_kiosk_withdraw)
-  [Function lock_internal](#sui_kiosk_lock_internal)
-  [Function place_internal](#sui_kiosk_place_internal)
-  [Function uid_mut_internal](#sui_kiosk_uid_mut_internal)
-  [Function has_item](#sui_kiosk_has_item)
-  [Function has_item_with_type](#sui_kiosk_has_item_with_type)
-  [Function is_locked](#sui_kiosk_is_locked)
-  [Function is_listed](#sui_kiosk_is_listed)
-  [Function is_listed_exclusively](#sui_kiosk_is_listed_exclusively)
-  [Function has_access](#sui_kiosk_has_access)
-  [Function uid_mut_as_owner](#sui_kiosk_uid_mut_as_owner)
-  [Function set_allow_extensions](#sui_kiosk_set_allow_extensions)
-  [Function uid](#sui_kiosk_uid)
-  [Function uid_mut](#sui_kiosk_uid_mut)
-  [Function owner](#sui_kiosk_owner)
-  [Function item_count](#sui_kiosk_item_count)
-  [Function profits_amount](#sui_kiosk_profits_amount)
-  [Function profits_mut](#sui_kiosk_profits_mut)
-  [Function borrow](#sui_kiosk_borrow)
-  [Function borrow_mut](#sui_kiosk_borrow_mut)
-  [Function borrow_val](#sui_kiosk_borrow_val)
-  [Function return_val](#sui_kiosk_return_val)
-  [Function kiosk_owner_cap_for](#sui_kiosk_kiosk_owner_cap_for)
-  [Function purchase_cap_kiosk](#sui_kiosk_purchase_cap_kiosk)
-  [Function purchase_cap_item](#sui_kiosk_purchase_cap_item)
-  [Function purchase_cap_min_price](#sui_kiosk_purchase_cap_min_price)

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

Struct <code>Kiosk</code>

An object which allows selling collectibles within "kiosk" ecosystem.
By default gives the functionality to list an item openly - for anyone
to purchase providing the guarantees for creators that every transfer
needs to be approved via the TransferPolicy.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>profits: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
 Balance of the Kiosk - all profits from sales go here.
</dd>
<dt>
<code><a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>: <b>address</b></code>
</dt>
<dd>
 Always point to <code>sender</code> of the transaction.
 Can be changed by calling <code><a href="../sui_sui/kiosk#sui_kiosk_set_owner">set_owner</a></code> with Cap.
</dd>
<dt>
<code><a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>: u32</code>
</dt>
<dd>
 Number of items stored in a Kiosk. Used to allow unpacking
 an empty Kiosk if it was wrapped or has a single owner.
</dd>
<dt>
<code>allow_extensions: bool</code>
</dt>
<dd>
 [DEPRECATED] Please, don't use the <code>allow_extensions</code> and the matching
 <code><a href="../sui_sui/kiosk#sui_kiosk_set_allow_extensions">set_allow_extensions</a></code> function - it is a legacy feature that is being
 replaced by the <code><a href="../sui_sui/kiosk_extension#sui_kiosk_extension">kiosk_extension</a></code> module and its Extensions API.
 Exposes <code><a href="../sui_sui/kiosk#sui_kiosk_uid_mut">uid_mut</a></code> publicly when set to <code><b>true</b></code>, set to <code><b>false</b></code> by default.
</dd>
</dl>

Struct <code>KioskOwnerCap</code>

A Capability granting the bearer a right to <a href="../sui_sui/kiosk#sui_kiosk_place">place</a> and <a href="../sui_sui/kiosk#sui_kiosk_take">take</a> items
from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> as well as to <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> them and <a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><b>for</b>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>PurchaseCap</code>

A capability which locks an item and gives a permission to
purchase it from a <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> for any price no less than min_price.

Allows exclusive listing: only bearer of the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> can
purchase the asset. However, the capability should be used
carefully as losing it would lock the asset in the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

The main application for the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> is building extensions
on top of the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;<b>phantom</b> T: key, store&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>kiosk_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 ID of the <code><a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a></code> the cap belongs to.
</dd>
<dt>
<code>item_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 ID of the listed item.
</dd>
<dt>
<code>min_price: u64</code>
</dt>
<dd>
 Minimum price for which the item can be purchased.
</dd>
</dl>

Struct <code>Borrow</code>

Hot potato to ensure an item was returned after being taken using
the <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a> call.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>kiosk_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>item_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Item</code>

Dynamic field key for an item placed into the kiosk.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Listing</code>

Dynamic field key for an active offer to purchase the T. If an
item is listed without a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>, exclusive is set to <b>false</b>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>is_exclusive: bool</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Lock</code>

Dynamic field key which marks that an item is locked in the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> and
can't be <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>n. The item then can only be listed / sold via the PurchaseCap.
Lock is released on <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ItemListed</code>

Emitted when an item was listed by the safe owner. Can be used
to track available offers anywhere on the network; the event is
type-indexed which allows for searching for offers of a specific T

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_ItemListed">ItemListed</a>&lt;<b>phantom</b> T: key, store&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>price: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ItemPurchased</code>

Emitted when an item was purchased from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>. Can be used
to track finalized sales across the network. The event is emitted
in both cases: when an item is purchased via the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> or
when it's purchased directly (via <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> + <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a>).

The price is also emitted and might differ from the price set
in the <a href="../sui_sui/kiosk#sui_kiosk_ItemListed">ItemListed</a> event. This is because the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> only
sets a minimum price for the item, and the actual price is defined
by the trading module / extension.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_ItemPurchased">ItemPurchased</a>&lt;<b>phantom</b> T: key, store&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>price: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ItemDelisted</code>

Emitted when an item was delisted by the safe owner. Can be used
to close tracked offers.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/kiosk#sui_kiosk_ItemDelisted">ItemDelisted</a>&lt;<b>phantom</b> T: key, store&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

Trying to withdraw profits and sender is not owner.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>: u64 = 0;
</code>

Coin paid does not match the offer price.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EIncorrectAmount">EIncorrectAmount</a>: u64 = 1;
</code>

Trying to withdraw higher amount than stored.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_ENotEnough">ENotEnough</a>: u64 = 2;
</code>

Trying to close a Kiosk and it has items in it.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_ENotEmpty">ENotEmpty</a>: u64 = 3;
</code>

Attempt to take an item that has a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> issued.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EListedExclusively">EListedExclusively</a>: u64 = 4;
</code>

<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> does not match the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EWrongKiosk">EWrongKiosk</a>: u64 = 5;
</code>

Trying to exclusively list an already listed item.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EAlreadyListed">EAlreadyListed</a>: u64 = 6;
</code>

Trying to call <a href="../sui_sui/kiosk#sui_kiosk_uid_mut">uid_mut</a> when allow_extensions set to false.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EUidAccessNotAllowed">EUidAccessNotAllowed</a>: u64 = 7;
</code>

Attempt to <a href="../sui_sui/kiosk#sui_kiosk_take">take</a> an item that is locked.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EItemLocked">EItemLocked</a>: u64 = 8;
</code>

Taking or mutably borrowing an item that is listed.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EItemIsListed">EItemIsListed</a>: u64 = 9;
</code>

Item does not match <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a> in <a href="../sui_sui/kiosk#sui_kiosk_return_val">return_val</a>.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EItemMismatch">EItemMismatch</a>: u64 = 10;
</code>

An is not found while trying to borrow.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>: u64 = 11;
</code>

Delisting an item that is not listed.

<code><b>const</b> <a href="../sui_sui/kiosk#sui_kiosk_ENotListed">ENotListed</a>: u64 = 12;
</code>

Function <code>default</code>

Creates a new Kiosk in a default configuration: sender receives the
<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> and becomes the Owner, the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> is shared.

<code><b>entry</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_default">default</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>entry</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_default">default</a>(ctx: &<b>mut</b> TxContext) {
    <b>let</b> (<a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>, cap) = <a href="../sui_sui/kiosk#sui_kiosk_new">new</a>(ctx);
    <a href="../sui_sui/transfer#sui_transfer_transfer">sui::transfer::transfer</a>(cap, ctx.sender());
    <a href="../sui_sui/transfer#sui_transfer_share_object">sui::transfer::share_object</a>(<a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>);
}
</code></pre>

Function <code>new</code>

Creates a new <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> with a matching <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_new">new</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_new">new</a>(ctx: &<b>mut</b> TxContext): (<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>) {
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk">kiosk</a> = <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        profits: <a href="../sui_sui/balance#sui_balance_zero">balance::zero</a>(),
        <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>: ctx.sender(),
        <a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>: 0,
        allow_extensions: <b>false</b>,
    };
    <b>let</b> cap = <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <span className="code-inline"><b>for</b></span>: <a href="../sui_sui/object#sui_object_id">object::id</a>(&<a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>),
    };
    (<a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>, cap)
}
</code></pre>

Function <code>close_and_withdraw</code>

Unpacks and destroys a Kiosk returning the profits (even if "0").
Can only be performed by the bearer of the <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> in the
case where there's no items inside and a <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> is not shared.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_close_and_withdraw">close_and_withdraw</a>(self: <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_close_and_withdraw">close_and_withdraw</a>(self: <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, ctx: &<b>mut</b> TxContext): Coin&lt;SUI&gt; {
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> { id, profits, <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>: _, <a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>, allow_extensions: _ } = self;
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> { id: cap_id, <span className="code-inline"><b>for</b></span> } = cap;
    <b>assert</b>!(id.to_inner() == <span className="code-inline"><b>for</b></span>, <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> == 0, <a href="../sui_sui/kiosk#sui_kiosk_ENotEmpty">ENotEmpty</a>);
    cap_id.delete();
    id.delete();
    profits.into_coin(ctx)
}
</code></pre>

Function <code>set_owner</code>

Change the <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a> field to the transaction sender.
The change is purely cosmetical and does not affect any of the
basic kiosk functions unless some logic for this is implemented
in a third party module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_owner">set_owner</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_owner">set_owner</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, ctx: &TxContext) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a> = ctx.sender();
}
</code></pre>

Function <code>set_owner_custom</code>

Update the <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a> field with a custom address. Can be used for
implementing a custom logic that relies on the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> owner.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_owner_custom">set_owner_custom</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_owner_custom">set_owner_custom</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>: <b>address</b>) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a> = <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>
}
</code></pre>

Function <code>place</code>

Place any object into a Kiosk.
Performs an authorization check to make sure only owner can do that.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place">place</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, item: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place">place</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, item: T) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_place_internal">place_internal</a>(item)
}
</code></pre>

Function <code>lock</code>

Place an item to the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> and issue a <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> for it. Once placed this
way, an item can only be listed either with a <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> function or with a
<a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>.

Requires policy for T to make sure that there's an issued TransferPolicy
and the item can be sold, otherwise the asset might be locked forever.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_lock">lock</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, _policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, item: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_lock">lock</a>&lt;T: key + store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>,
    _policy: &TransferPolicy&lt;T&gt;,
    item: T,
) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_lock_internal">lock_internal</a>(item)
}
</code></pre>

Function <code>take</code>

Take any object from the Kiosk.
Performs an authorization check to make sure only owner can do that.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID): T {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_locked">is_locked</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemLocked">EItemLocked</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EListedExclusively">EListedExclusively</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> = self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> - 1;
    df::remove_if_exists&lt;<a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a>, u64&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>false</b> });
    dof::remove(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id })
}
</code></pre>

Function <code>list</code>

List the item by setting a price and making it available for purchase.
Performs an authorization check to make sure only owner can sell.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_list">list</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_list">list</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID, price: u64) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item_with_type">has_item_with_type</a>&lt;T&gt;(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EListedExclusively">EListedExclusively</a>);
    df::add(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>false</b> }, price);
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/kiosk#sui_kiosk_ItemListed">ItemListed</a>&lt;T&gt; { <a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_id">object::id</a>(self), id, price })
}
</code></pre>

Function <code>place_and_list</code>

Calls <a href="../sui_sui/kiosk#sui_kiosk_place">place</a> and <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> together - simplifies the flow.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place_and_list">place_and_list</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, item: T, price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place_and_list">place_and_list</a>&lt;T: key + store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>,
    item: T,
    price: u64,
) {
    <b>let</b> id = <a href="../sui_sui/object#sui_object_id">object::id</a>(&item);
    self.<a href="../sui_sui/kiosk#sui_kiosk_place">place</a>(cap, item);
    self.<a href="../sui_sui/kiosk#sui_kiosk_list">list</a>&lt;T&gt;(cap, id, price)
}
</code></pre>

Function <code>delist</code>

Remove an existing listing from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> and keep the item in the
user Kiosk. Can only be performed by the owner of the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_delist">delist</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_delist">delist</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item_with_type">has_item_with_type</a>&lt;T&gt;(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EListedExclusively">EListedExclusively</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_ENotListed">ENotListed</a>);
    df::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a>, u64&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>false</b> });
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/kiosk#sui_kiosk_ItemDelisted">ItemDelisted</a>&lt;T&gt; { <a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_id">object::id</a>(self), id })
}
</code></pre>

Function <code>purchase</code>

Make a trade: pay the owner of the item and request a Transfer to the target
kiosk (to prevent item being taken by the approving party).

Received TransferRequest needs to be handled by the publisher of the T,
if they have a method implemented that allows a trade, it is possible to
request their approval (by calling some function) so that the trade can be
finalized.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, payment: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;): (T, <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a>&lt;T: key + store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    id: ID,
    payment: Coin&lt;SUI&gt;,
): (T, TransferRequest&lt;T&gt;) {
    <b>let</b> price = df::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a>, u64&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>false</b> });
    <b>let</b> inner = dof::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a>, T&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id });
    self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> = self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> - 1;
    <b>assert</b>!(price == payment.value(), <a href="../sui_sui/kiosk#sui_kiosk_EIncorrectAmount">EIncorrectAmount</a>);
    df::remove_if_exists&lt;<a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a>, bool&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> { id });
    <a href="../sui_sui/coin#sui_coin_put">coin::put</a>(&<b>mut</b> self.profits, payment);
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/kiosk#sui_kiosk_ItemPurchased">ItemPurchased</a>&lt;T&gt; { <a href="../sui_sui/kiosk#sui_kiosk">kiosk</a>: <a href="../sui_sui/object#sui_object_id">object::id</a>(self), id, price });
    (inner, <a href="../sui_sui/transfer_policy#sui_transfer_policy_new_request">transfer_policy::new_request</a>(id, price, <a href="../sui_sui/object#sui_object_id">object::id</a>(self)))
}
</code></pre>

Function <code>list_with_purchase_cap</code>

Creates a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> which gives the right to purchase an item
for any price equal or higher than the min_price.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, min_price: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>&lt;T: key + store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>,
    id: ID,
    min_price: u64,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt; {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item_with_type">has_item_with_type</a>&lt;T&gt;(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EAlreadyListed">EAlreadyListed</a>);
    df::add(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>true</b> }, min_price);
    <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt; {
        min_price,
        item_id: id,
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        kiosk_id: <a href="../sui_sui/object#sui_object_id">object::id</a>(self),
    }
}
</code></pre>

Function <code>purchase_with_cap</code>

Unpack the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> and call <a href="../sui_sui/kiosk#sui_kiosk_purchase">purchase</a>. Sets the payment amount
as the price for the listing making sure it's no less than min_amount.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_with_cap">purchase_with_cap</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, purchase_cap: <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;, payment: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;): (T, <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_with_cap">purchase_with_cap</a>&lt;T: key + store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    purchase_cap: <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt;,
    payment: Coin&lt;SUI&gt;,
): (T, TransferRequest&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> { id, item_id, kiosk_id, min_price } = purchase_cap;
    id.delete();
    <b>let</b> id = item_id;
    <b>let</b> paid = payment.value();
    <b>assert</b>!(paid &gt;= min_price, <a href="../sui_sui/kiosk#sui_kiosk_EIncorrectAmount">EIncorrectAmount</a>);
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == kiosk_id, <a href="../sui_sui/kiosk#sui_kiosk_EWrongKiosk">EWrongKiosk</a>);
    df::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a>, u64&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>true</b> });
    <a href="../sui_sui/coin#sui_coin_put">coin::put</a>(&<b>mut</b> self.profits, payment);
    self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> = self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> - 1;
    df::remove_if_exists&lt;<a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a>, bool&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> { id });
    <b>let</b> item = dof::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a>, T&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id });
    (item, <a href="../sui_sui/transfer_policy#sui_transfer_policy_new_request">transfer_policy::new_request</a>(id, paid, <a href="../sui_sui/object#sui_object_id">object::id</a>(self)))
}
</code></pre>

Function <code>return_purchase_cap</code>

Return the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> without making a purchase; remove an active offer and
allow the item for taking. Can only be returned to its <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, aborts otherwise.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_return_purchase_cap">return_purchase_cap</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, purchase_cap: <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_return_purchase_cap">return_purchase_cap</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, purchase_cap: <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> { id, item_id, kiosk_id, min_price: _ } = purchase_cap;
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == kiosk_id, <a href="../sui_sui/kiosk#sui_kiosk_EWrongKiosk">EWrongKiosk</a>);
    df::remove&lt;<a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a>, u64&gt;(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id: item_id, is_exclusive: <b>true</b> });
    id.delete()
}
</code></pre>

Function <code>withdraw</code>

Withdraw profits from the Kiosk.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_withdraw">withdraw</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, amount: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_withdraw">withdraw</a>(
    self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>,
    cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>,
    amount: Option&lt;u64&gt;,
    ctx: &<b>mut</b> TxContext,
): Coin&lt;SUI&gt; {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>let</b> amount = <b>if</b> (amount.is_some()) {
        <b>let</b> amt = amount.destroy_some();
        <b>assert</b>!(amt &lt;= self.profits.value(), <a href="../sui_sui/kiosk#sui_kiosk_ENotEnough">ENotEnough</a>);
        amt
    } <b>else</b> {
        self.profits.value()
    };
    <a href="../sui_sui/coin#sui_coin_take">coin::take</a>(&<b>mut</b> self.profits, amount, ctx)
}
</code></pre>

Function <code>lock_internal</code>

Internal: "lock" an item disabling the <a href="../sui_sui/kiosk#sui_kiosk_take">take</a> action.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_lock_internal">lock_internal</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, item: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_lock_internal">lock_internal</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, item: T) {
    df::add(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> { id: <a href="../sui_sui/object#sui_object_id">object::id</a>(&item) }, <b>true</b>);
    self.<a href="../sui_sui/kiosk#sui_kiosk_place_internal">place_internal</a>(item)
}
</code></pre>

Function <code>place_internal</code>

Internal: "place" an item to the Kiosk and increment the item count.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place_internal">place_internal</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, item: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_place_internal">place_internal</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, item: T) {
    self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> = self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a> + 1;
    dof::add(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id: <a href="../sui_sui/object#sui_object_id">object::id</a>(&item) }, item)
}
</code></pre>

Function <code>uid_mut_internal</code>

Internal: get a mutable access to the UID.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut_internal">uid_mut_internal</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut_internal">uid_mut_internal</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): &<b>mut</b> UID {
    &<b>mut</b> self.id
}
</code></pre>

Function <code>has_item</code>

Check whether the item is present in the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, id: ID): bool {
    dof::exists_(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id })
}
</code></pre>

Function <code>has_item_with_type</code>

Check whether the item is present in the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> and has type T.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_item_with_type">has_item_with_type</a>&lt;T: key, store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_item_with_type">has_item_with_type</a>&lt;T: key + store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, id: ID): bool {
    dof::exists_with_type&lt;<a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a>, T&gt;(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id })
}
</code></pre>

Function <code>is_locked</code>

Check whether an item with the id is locked in the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>. Meaning
that the only two actions that can be performed on it are <a href="../sui_sui/kiosk#sui_kiosk_list">list</a> and
<a href="../sui_sui/kiosk#sui_kiosk_list_with_purchase_cap">list_with_purchase_cap</a>, it cannot be <a href="../sui_sui/kiosk#sui_kiosk_take">take</a>n out of the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_locked">is_locked</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_locked">is_locked</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, id: ID): bool {
    df::exists_(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Lock">Lock</a> { id })
}
</code></pre>

Function <code>is_listed</code>

Check whether an item is listed (exclusively or non exclusively).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, id: ID): bool {
    df::exists_(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>false</b> })
        || self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(id)
}
</code></pre>

Function <code>is_listed_exclusively</code>

Check whether there's a <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a> issued for an item.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_is_listed_exclusively">is_listed_exclusively</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, id: ID): bool {
    df::exists_(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Listing">Listing</a> { id, is_exclusive: <b>true</b> })
}
</code></pre>

Function <code>has_access</code>

Check whether the <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a> matches the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>): bool {
    <a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>
}
</code></pre>

Function <code>uid_mut_as_owner</code>

Access the UID using the <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut_as_owner">uid_mut_as_owner</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>): &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut_as_owner">uid_mut_as_owner</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>): &<b>mut</b> UID {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    &<b>mut</b> self.id
}
</code></pre>

Function <code>set_allow_extensions</code>

[DEPRECATED]
Allow or disallow <a href="../sui_sui/kiosk#sui_kiosk_uid">uid</a> and <a href="../sui_sui/kiosk#sui_kiosk_uid_mut">uid_mut</a> access via the allow_extensions
setting.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_allow_extensions">set_allow_extensions</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, allow_extensions: bool)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_set_allow_extensions">set_allow_extensions</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, allow_extensions: bool) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    self.allow_extensions = allow_extensions;
}
</code></pre>

Function <code>uid</code>

Get the immutable UID for dynamic field access.
Always enabled.

Given the &UID can be used for reading keys and authorization,
its access

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid">uid</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid">uid</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): &UID {
    &self.id
}
</code></pre>

Function <code>uid_mut</code>

Get the mutable UID for dynamic field access and extensions.
Aborts if allow_extensions set to <b>false</b>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut">uid_mut</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_uid_mut">uid_mut</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): &<b>mut</b> UID {
    <b>assert</b>!(self.allow_extensions, <a href="../sui_sui/kiosk#sui_kiosk_EUidAccessNotAllowed">EUidAccessNotAllowed</a>);
    &<b>mut</b> self.id
}
</code></pre>

Function <code>owner</code>

Get the owner of the Kiosk.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): <b>address</b> {
    self.<a href="../sui_sui/kiosk#sui_kiosk_owner">owner</a>
}
</code></pre>

Function <code>item_count</code>

Get the number of items stored in a Kiosk.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): u32
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): u32 {
    self.<a href="../sui_sui/kiosk#sui_kiosk_item_count">item_count</a>
}
</code></pre>

Function <code>profits_amount</code>

Get the amount of profits collected by selling items.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_profits_amount">profits_amount</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_profits_amount">profits_amount</a>(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>): u64 {
    self.profits.value()
}
</code></pre>

Function <code>profits_mut</code>

Get mutable access to profits - owner only action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_profits_mut">profits_mut</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>): &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_profits_mut">profits_mut</a>(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>): &<b>mut</b> Balance&lt;SUI&gt; {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    &<b>mut</b> self.profits
}
</code></pre>

Function <code>borrow</code>

Immutably borrow an item from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>. Any item can be <a href="../sui_sui/borrow#sui_borrow">borrow</a>ed
at any time.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;T: key, store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): &T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/borrow#sui_borrow">borrow</a>&lt;T: key + store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID): &T {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    dof::borrow(&self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id })
}
</code></pre>

Function <code>borrow_mut</code>

Mutably borrow an item from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>.
Item can be <a href="../sui_sui/kiosk#sui_kiosk_borrow_mut">borrow_mut</a>ed only if it's not <a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_borrow_mut">borrow_mut</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): &<b>mut</b> T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_borrow_mut">borrow_mut</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID): &<b>mut</b> T {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemIsListed">EItemIsListed</a>);
    dof::borrow_mut(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id })
}
</code></pre>

Function <code>borrow_val</code>

Take the item from the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a> with a guarantee that it will be returned.
Item can be <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a>-ed only if it's not <a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>, id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): (T, <a href="../sui_sui/kiosk#sui_kiosk_Borrow">sui::kiosk::Borrow</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>, id: ID): (T, <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a>) {
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_access">has_access</a>(cap), <a href="../sui_sui/kiosk#sui_kiosk_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(self.<a href="../sui_sui/kiosk#sui_kiosk_has_item">has_item</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemNotFound">EItemNotFound</a>);
    <b>assert</b>!(!self.<a href="../sui_sui/kiosk#sui_kiosk_is_listed">is_listed</a>(id), <a href="../sui_sui/kiosk#sui_kiosk_EItemIsListed">EItemIsListed</a>);
    (dof::remove(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id }), <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a> { kiosk_id: <a href="../sui_sui/object#sui_object_id">object::id</a>(self), item_id: id })
}
</code></pre>

Function <code>return_val</code>

Return the borrowed item to the <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>. This method cannot be avoided
if <a href="../sui_sui/kiosk#sui_kiosk_borrow_val">borrow_val</a> is used.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_return_val">return_val</a>&lt;T: key, store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">sui::kiosk::Kiosk</a>, item: T, <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/kiosk#sui_kiosk_Borrow">sui::kiosk::Borrow</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_return_val">return_val</a>&lt;T: key + store&gt;(self: &<b>mut</b> <a href="../sui_sui/kiosk#sui_kiosk_Kiosk">Kiosk</a>, item: T, <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a>) {
    <b>let</b> <a href="../sui_sui/kiosk#sui_kiosk_Borrow">Borrow</a> { kiosk_id, item_id } = <a href="../sui_sui/borrow#sui_borrow">borrow</a>;
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == kiosk_id, <a href="../sui_sui/kiosk#sui_kiosk_EWrongKiosk">EWrongKiosk</a>);
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(&item) == item_id, <a href="../sui_sui/kiosk#sui_kiosk_EItemMismatch">EItemMismatch</a>);
    dof::add(&<b>mut</b> self.id, <a href="../sui_sui/kiosk#sui_kiosk_Item">Item</a> { id: item_id }, item);
}
</code></pre>

Function <code>kiosk_owner_cap_for</code>

Get the <b>for</b> field of the <a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_kiosk_owner_cap_for">kiosk_owner_cap_for</a>(cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">sui::kiosk::KioskOwnerCap</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_kiosk_owner_cap_for">kiosk_owner_cap_for</a>(cap: &<a href="../sui_sui/kiosk#sui_kiosk_KioskOwnerCap">KioskOwnerCap</a>): ID {
    cap.<span className="code-inline"><b>for</b></span>
}
</code></pre>

Function <code>purchase_cap_kiosk</code>

Get the kiosk_id from the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_kiosk">purchase_cap_kiosk</a>&lt;T: key, store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_kiosk">purchase_cap_kiosk</a>&lt;T: key + store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt;): ID {
    self.kiosk_id
}
</code></pre>

Function <code>purchase_cap_item</code>

Get the Item_id from the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_item">purchase_cap_item</a>&lt;T: key, store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_item">purchase_cap_item</a>&lt;T: key + store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt;): ID {
    self.item_id
}
</code></pre>

Function <code>purchase_cap_min_price</code>

Get the min_price from the <a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_min_price">purchase_cap_min_price</a>&lt;T: key, store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">sui::kiosk::PurchaseCap</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/kiosk#sui_kiosk_purchase_cap_min_price">purchase_cap_min_price</a>&lt;T: key + store&gt;(self: &<a href="../sui_sui/kiosk#sui_kiosk_PurchaseCap">PurchaseCap</a>&lt;T&gt;): u64 {
    self.min_price
}
</code></pre>