Defines the <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> type - platform wide representation of fungible
tokens and coins. <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> can be described as a secure wrapper around
Balance type.

-  [Struct Coin](#sui_coin_Coin)
-  [Struct CoinMetadata](#sui_coin_CoinMetadata)
-  [Struct RegulatedCoinMetadata](#sui_coin_RegulatedCoinMetadata)
-  [Struct TreasuryCap](#sui_coin_TreasuryCap)
-  [Struct DenyCapV2](#sui_coin_DenyCapV2)
-  [Struct CurrencyCreated](#sui_coin_CurrencyCreated)
-  [Struct DenyCap](#sui_coin_DenyCap)
-  [Constants](#@Constants_0)
-  [Function total_supply](#sui_coin_total_supply)
-  [Function treasury_into_supply](#sui_coin_treasury_into_supply)
-  [Function supply_immut](#sui_coin_supply_immut)
-  [Function supply_mut](#sui_coin_supply_mut)
-  [Function value](#sui_coin_value)
-  [Function balance](#sui_coin_balance)
-  [Function balance_mut](#sui_coin_balance_mut)
-  [Function from_balance](#sui_coin_from_balance)
-  [Function into_balance](#sui_coin_into_balance)
-  [Function take](#sui_coin_take)
-  [Function put](#sui_coin_put)
-  [Function redeem_funds](#sui_coin_redeem_funds)
-  [Function send_funds](#sui_coin_send_funds)
-  [Function join](#sui_coin_join)
-  [Function split](#sui_coin_split)
-  [Function divide_into_n](#sui_coin_divide_into_n)
-  [Function zero](#sui_coin_zero)
-  [Function destroy_zero](#sui_coin_destroy_zero)
-  [Function create_currency](#sui_coin_create_currency)
-  [Function create_regulated_currency_v2](#sui_coin_create_regulated_currency_v2)
-  [Function migrate_regulated_currency_to_v2](#sui_coin_migrate_regulated_currency_to_v2)
-  [Function mint](#sui_coin_mint)
-  [Function mint_balance](#sui_coin_mint_balance)
-  [Function burn](#sui_coin_burn)
-  [Function deny_list_v2_add](#sui_coin_deny_list_v2_add)
-  [Function deny_list_v2_remove](#sui_coin_deny_list_v2_remove)
-  [Function deny_list_v2_contains_current_epoch](#sui_coin_deny_list_v2_contains_current_epoch)
-  [Function deny_list_v2_contains_next_epoch](#sui_coin_deny_list_v2_contains_next_epoch)
-  [Function deny_list_v2_enable_global_pause](#sui_coin_deny_list_v2_enable_global_pause)
-  [Function deny_list_v2_disable_global_pause](#sui_coin_deny_list_v2_disable_global_pause)
-  [Function deny_list_v2_is_global_pause_enabled_current_epoch](#sui_coin_deny_list_v2_is_global_pause_enabled_current_epoch)
-  [Function deny_list_v2_is_global_pause_enabled_next_epoch](#sui_coin_deny_list_v2_is_global_pause_enabled_next_epoch)
-  [Function mint_and_transfer](#sui_coin_mint_and_transfer)
-  [Function update_name](#sui_coin_update_name)
-  [Function update_symbol](#sui_coin_update_symbol)
-  [Function update_description](#sui_coin_update_description)
-  [Function update_icon_url](#sui_coin_update_icon_url)
-  [Function get_decimals](#sui_coin_get_decimals)
-  [Function get_name](#sui_coin_get_name)
-  [Function get_symbol](#sui_coin_get_symbol)
-  [Function get_description](#sui_coin_get_description)
-  [Function get_icon_url](#sui_coin_get_icon_url)
-  [Function destroy_metadata](#sui_coin_destroy_metadata)
-  [Function deny_cap_id](#sui_coin_deny_cap_id)
-  [Function new_deny_cap_v2](#sui_coin_new_deny_cap_v2)
-  [Function new_treasury_cap](#sui_coin_new_treasury_cap)
-  [Function allow_global_pause](#sui_coin_allow_global_pause)
-  [Function new_coin_metadata](#sui_coin_new_coin_metadata)
-  [Function update_coin_metadata](#sui_coin_update_coin_metadata)
-  [Function supply](#sui_coin_supply)
-  [Function create_regulated_currency](#sui_coin_create_regulated_currency)
-  [Function deny_list_add](#sui_coin_deny_list_add)
-  [Function deny_list_remove](#sui_coin_deny_list_remove)
-  [Function deny_list_contains](#sui_coin_deny_list_contains)

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
<b>use</b> <a href="../sui_sui/config#sui_config">sui::config</a>;
<b>use</b> <a href="../sui_sui/deny_list#sui_deny_list">sui::deny_list</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/dynamic_object_field#sui_dynamic_object_field">sui::dynamic_object_field</a>;
<b>use</b> <a href="../sui_sui/event#sui_event">sui::event</a>;
<b>use</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator">sui::funds_accumulator</a>;
<b>use</b> <a href="../sui_sui/hash#sui_hash">sui::hash</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
</code>

Struct <code>Coin</code>

A coin of type T worth <a href="../sui_sui/coin#sui_coin_value">value</a>. Transferable and storable

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>CoinMetadata</code>

Each Coin type T created through <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a> function will have a
unique instance of CoinMetadata<T> that stores the metadata for this coin type.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>decimals: u8</code>
</dt>
<dd>
 Number of decimal places the coin uses.
 A coin with <code><a href="../sui_sui/coin#sui_coin_value">value</a> </code> N and <code>decimals</code> D should be shown as N / 10^D
 E.g., a coin with <code><a href="../sui_sui/coin#sui_coin_value">value</a></code> 7002 and decimals 3 should be displayed as 7.002
 This is metadata for display usage only.
</dd>
<dt>
<code>name: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Name for the token
</dd>
<dt>
<code>symbol: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a></code>
</dt>
<dd>
 Symbol for the token
</dd>
<dt>
<code>description: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Description of the token
</dd>
<dt>
<code>icon_url: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>&gt;</code>
</dt>
<dd>
 URL for the token logo
</dd>
</dl>

Struct <code>RegulatedCoinMetadata</code>

Similar to CoinMetadata, but created only for regulated coins that use the DenyList.
This object is always immutable.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">RegulatedCoinMetadata</a>&lt;<b>phantom</b> T&gt; <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>coin_metadata_object: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 The ID of the coin's CoinMetadata object.
</dd>
<dt>
<code>deny_cap_object: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 The ID of the coin's DenyCap object.
</dd>
</dl>

Struct <code>TreasuryCap</code>

Capability allowing the bearer to mint and burn
coins of type T. Transferable

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>: <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>DenyCapV2</code>

Capability allowing the bearer to deny addresses from using the currency's coins--
immediately preventing those addresses from interacting with the coin as an input to a
transaction and at the start of the next preventing them from receiving the coin.
If <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a> is true, the bearer can enable a global pause that behaves as if
all addresses were added to the deny list.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>CurrencyCreated</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_CurrencyCreated">CurrencyCreated</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>decimals: u8</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>DenyCap</code>

Capability allowing the bearer to freeze addresses, preventing those addresses from
interacting with the coin as an input to a transaction.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

A type passed to create_supply is not a one-time witness.

<code><b>const</b> <a href="../sui_sui/coin#sui_coin_EBadWitness">EBadWitness</a>: u64 = 0;
</code>

Invalid arguments are passed to a function.

<code><b>const</b> <a href="../sui_sui/coin#sui_coin_EInvalidArg">EInvalidArg</a>: u64 = 1;
</code>

Trying to split a coin more times than its balance allows.

<code><b>const</b> <a href="../sui_sui/coin#sui_coin_ENotEnough">ENotEnough</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_sui/coin#sui_coin_EGlobalPauseNotAllowed">EGlobalPauseNotAllowed</a>: u64 = 3;
</code>

The index into the deny list vector for the <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a> type.

<code><b>const</b> <a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>: u64 = 0;
</code>

Function <code>total_supply</code>

Return the total number of T's in circulation.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>&lt;T&gt;(cap: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>&lt;T&gt;(cap: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;): u64 {
    <a href="../sui_sui/balance#sui_balance_supply_value">balance::supply_value</a>(&cap.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>)
}
</code></pre>

Function <code>treasury_into_supply</code>

Unwrap <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> getting the Supply.

Operation is irreversible. Supply cannot be converted into a <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> due
to different security guarantees (TreasuryCap can be created only once for a type)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_treasury_into_supply">treasury_into_supply</a>&lt;T&gt;(treasury: <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;): <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_treasury_into_supply">treasury_into_supply</a>&lt;T&gt;(treasury: <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;): Supply&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> { id, <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a> } = treasury;
    id.delete();
    <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>
}
</code></pre>

Function <code>supply_immut</code>

Get immutable reference to the treasury's Supply.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply_immut">supply_immut</a>&lt;T&gt;(treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;): &<a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply_immut">supply_immut</a>&lt;T&gt;(treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;): &Supply&lt;T&gt; {
    &treasury.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>
}
</code></pre>

Function <code>supply_mut</code>

Get mutable reference to the treasury's Supply.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply_mut">supply_mut</a>&lt;T&gt;(treasury: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;): &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply_mut">supply_mut</a>&lt;T&gt;(treasury: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;): &<b>mut</b> Supply&lt;T&gt; {
    &<b>mut</b> treasury.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>
}
</code></pre>

Function <code>value</code>

Public getter for the coin's value

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_value">value</a>&lt;T&gt;(self: &<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_value">value</a>&lt;T&gt;(self: &<a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;): u64 {
    self.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_value">value</a>()
}
</code></pre>

Function <code>balance</code>

Get immutable reference to the balance of a coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance">balance</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;): &<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/balance#sui_balance">balance</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;): &Balance&lt;T&gt; {
    &<a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/balance#sui_balance">balance</a>
}
</code></pre>

Function <code>balance_mut</code>

Get a mutable reference to the balance of a coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_balance_mut">balance_mut</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;): &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_balance_mut">balance_mut</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;): &<b>mut</b> Balance&lt;T&gt; {
    &<b>mut</b> <a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/balance#sui_balance">balance</a>
}
</code></pre>

Function <code>from_balance</code>

Wrap a balance into a Coin to make it transferable.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_from_balance">from_balance</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_from_balance">from_balance</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: Balance&lt;T&gt;, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx), <a href="../sui_sui/balance#sui_balance">balance</a> }
}
</code></pre>

Function <code>into_balance</code>

Destruct a Coin wrapper and keep the balance.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_into_balance">into_balance</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_into_balance">into_balance</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;): Balance&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = <a href="../sui_sui/coin#sui_coin">coin</a>;
    id.delete();
    <a href="../sui_sui/balance#sui_balance">balance</a>
}
</code></pre>

Function <code>take</code>

Take a <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> worth of <a href="../sui_sui/coin#sui_coin_value">value</a> from Balance.
Aborts if <a href="../sui_sui/coin#sui_coin_value">value</a> &gt; <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_value">value</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_take">take</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_take">take</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: &<b>mut</b> Balance&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_split">split</a>(<a href="../sui_sui/coin#sui_coin_value">value</a>),
    }
}
</code></pre>

Function <code>put</code>

Put a <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; to the Balance&lt;T&gt;.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_put">put</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_put">put</a>&lt;T&gt;(<a href="../sui_sui/balance#sui_balance">balance</a>: &<b>mut</b> Balance&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;) {
    <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_join">join</a>(<a href="../sui_sui/coin#sui_coin_into_balance">into_balance</a>(<a href="../sui_sui/coin#sui_coin">coin</a>));
}
</code></pre>

Function <code>redeem_funds</code>

Redeem a Withdrawal&lt;Balance&lt;T&gt;&gt; and create a <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; from the withdrawn Balance<T>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_redeem_funds">redeem_funds</a>&lt;T&gt;(withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_redeem_funds">redeem_funds</a>&lt;T&gt;(
    withdrawal: <a href="../sui_sui/funds_accumulator#sui_funds_accumulator_Withdrawal">sui::funds_accumulator::Withdrawal</a>&lt;Balance&lt;T&gt;&gt;,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/balance#sui_balance_redeem_funds">balance::redeem_funds</a>(withdrawal).into_coin(ctx)
}
</code></pre>

Function <code>send_funds</code>

Send a coin to an address balance

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_send_funds">send_funds</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_send_funds">send_funds</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;, recipient: <b>address</b>) {
    <a href="../sui_sui/balance#sui_balance_send_funds">balance::send_funds</a>(<a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/coin#sui_coin_into_balance">into_balance</a>(), recipient);
}
</code></pre>

Function <code>join</code>

Consume the coin c and add its value to self.
Aborts if c.<a href="../sui_sui/coin#sui_coin_value">value</a> + self.<a href="../sui_sui/coin#sui_coin_value">value</a> &gt; U64_MAX

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_join">join</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, c: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_join">join</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;, c: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = c;
    id.delete();
    self.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_join">join</a>(<a href="../sui_sui/balance#sui_balance">balance</a>);
}
</code></pre>

Function <code>split</code>

Split coin self to two coins, one with balance split_amount,
and the remaining balance is left is self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_split">split</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, split_amount: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_split">split</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;, split_amount: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_take">take</a>(&<b>mut</b> self.<a href="../sui_sui/balance#sui_balance">balance</a>, split_amount, ctx)
}
</code></pre>

Function <code>divide_into_n</code>

Split coin self into n - 1 coins with equal balances. The remainder is left in
self. Return newly created coins.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_divide_into_n">divide_into_n</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, n: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): vector&lt;<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_divide_into_n">divide_into_n</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;, n: u64, ctx: &<b>mut</b> TxContext): vector&lt;<a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;&gt; {
    <b>assert</b>!(n &gt; 0, <a href="../sui_sui/coin#sui_coin_EInvalidArg">EInvalidArg</a>);
    <b>assert</b>!(n &lt;= self.<a href="../sui_sui/coin#sui_coin_value">value</a>(), <a href="../sui_sui/coin#sui_coin_ENotEnough">ENotEnough</a>);
    <b>let</b> split_amount = self.<a href="../sui_sui/coin#sui_coin_value">value</a>() / n;
    vector::tabulate!(n - 1, |_| self.<a href="../sui_sui/coin#sui_coin_split">split</a>(split_amount, ctx))
}
</code></pre>

Function <code>zero</code>

Make any Coin with a zero value. Useful for placeholding
bids/payments or preemptively making empty balances.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_zero">zero</a>&lt;T&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_zero">zero</a>&lt;T&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx), <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_zero">balance::zero</a>() }
}
</code></pre>

Function <code>destroy_zero</code>

Destroy a coin with value zero

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_destroy_zero">destroy_zero</a>&lt;T&gt;(c: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_destroy_zero">destroy_zero</a>&lt;T&gt;(c: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = c;
    id.delete();
    <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/coin#sui_coin_destroy_zero">destroy_zero</a>()
}
</code></pre>

Function <code>create_currency</code>

Create a new currency type T as and return the <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> for
T to the caller. Can only be called with a one-time-witness
type, ensuring that there's only one <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> per T.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>&lt;T: drop&gt;(witness: T, decimals: u8, symbol: vector&lt;u8&gt;, name: vector&lt;u8&gt;, description: vector&lt;u8&gt;, icon_url: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>&lt;T: drop&gt;(
    witness: T,
    decimals: u8,
    symbol: vector&lt;u8&gt;,
    name: vector&lt;u8&gt;,
    description: vector&lt;u8&gt;,
    icon_url: Option&lt;Url&gt;,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;) {
    // Make sure there's only one instance of the type T
    <b>assert</b>!(<a href="../sui_sui/types#sui_types_is_one_time_witness">sui::types::is_one_time_witness</a>(&witness), <a href="../sui_sui/coin#sui_coin_EBadWitness">EBadWitness</a>);
    (
        <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> {
            id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
            <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>: <a href="../sui_sui/balance#sui_balance_create_supply">balance::create_supply</a>(witness),
        },
        <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a> {
            id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
            decimals,
            name: name.to_string(),
            symbol: symbol.to_ascii_string(),
            description: description.to_string(),
            icon_url,
        },
    )
}
</code></pre>

Function <code>create_regulated_currency_v2</code>

This creates a new currency, via <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>, but with an extra capability that
allows for specific addresses to have their coins frozen. When an address is added to the
deny list, it is immediately unable to interact with the currency's coin as input objects.
Additionally at the start of the next epoch, they will be unable to receive the currency's
coin.
The <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a> flag enables an additional API that will cause all addresses to
be denied. Note however, that this doesn't affect per-address entries of the deny list and
will not change the result of the "contains" APIs.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_regulated_currency_v2">create_regulated_currency_v2</a>&lt;T: drop&gt;(witness: T, decimals: u8, symbol: vector&lt;u8&gt;, name: vector&lt;u8&gt;, description: vector&lt;u8&gt;, icon_url: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>&gt;, <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_regulated_currency_v2">create_regulated_currency_v2</a>&lt;T: drop&gt;(
    witness: T,
    decimals: u8,
    symbol: vector&lt;u8&gt;,
    name: vector&lt;u8&gt;,
    description: vector&lt;u8&gt;,
    icon_url: Option&lt;Url&gt;,
    <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;) {
    <b>let</b> (treasury_cap, metadata) = <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>(
        witness,
        decimals,
        symbol,
        name,
        description,
        icon_url,
        ctx,
    );
    <b>let</b> deny_cap = <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>,
    };
    <a href="../sui_sui/transfer#sui_transfer_freeze_object">transfer::freeze_object</a>(<a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">RegulatedCoinMetadata</a>&lt;T&gt; {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        coin_metadata_object: <a href="../sui_sui/object#sui_object_id">object::id</a>(&metadata),
        deny_cap_object: <a href="../sui_sui/object#sui_object_id">object::id</a>(&deny_cap),
    });
    (treasury_cap, deny_cap, metadata)
}
</code></pre>

Function <code>migrate_regulated_currency_to_v2</code>

Given the <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a> for a regulated currency, migrate it to the new <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a> type.
All entries in the deny list will be migrated to the new format.
See <a href="../sui_sui/coin#sui_coin_create_regulated_currency_v2">create_regulated_currency_v2</a> for details on the new v2 of the deny list.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_migrate_regulated_currency_to_v2">migrate_regulated_currency_to_v2</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, cap: <a href="../sui_sui/coin#sui_coin_DenyCap">sui::coin::DenyCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_migrate_regulated_currency_to_v2">migrate_regulated_currency_to_v2</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    cap: <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a>&lt;T&gt;,
    <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a> { id } = cap;
    id.delete();
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.migrate_v1_to_v2(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, ctx);
    <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>,
    }
}
</code></pre>

Function <code>mint</code>

Create a coin worth <a href="../sui_sui/coin#sui_coin_value">value</a> and increase the total supply
in cap accordingly.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint">mint</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint">mint</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/balance#sui_balance">balance</a>: cap.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>.increase_supply(<a href="../sui_sui/coin#sui_coin_value">value</a>),
    }
}
</code></pre>

Function <code>mint_balance</code>

Mint some amount of T as a Balance and increase the total
supply in cap accordingly.
Aborts if <a href="../sui_sui/coin#sui_coin_value">value</a> + cap.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a> >= U64_MAX

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint_balance">mint_balance</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint_balance">mint_balance</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_value">value</a>: u64): Balance&lt;T&gt; {
    cap.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>.increase_supply(<a href="../sui_sui/coin#sui_coin_value">value</a>)
}
</code></pre>

Function <code>burn</code>

Destroy the coin c and decrease the total supply in cap
accordingly.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_burn">burn</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, c: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_burn">burn</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, c: <a href="../sui_sui/coin#sui_coin_Coin">Coin</a>&lt;T&gt;): u64 {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = c;
    id.delete();
    cap.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>.decrease_supply(<a href="../sui_sui/balance#sui_balance">balance</a>)
}
</code></pre>

Function <code>deny_list_v2_add</code>

Adds the given address to the deny list, preventing it from interacting with the specified
coin type as an input to a transaction. Additionally at the start of the next epoch, the
address will be unable to receive objects of this coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_add">deny_list_v2_add</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;, addr: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_add">deny_list_v2_add</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;,
    addr: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_add(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, addr, ctx)
}
</code></pre>

Function <code>deny_list_v2_remove</code>

Removes an address from the deny list. Similar to <a href="../sui_sui/coin#sui_coin_deny_list_v2_add">deny_list_v2_add</a>, the effect for input
objects will be immediate, but the effect for receiving objects will be delayed until the
next epoch.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_remove">deny_list_v2_remove</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;, addr: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_remove">deny_list_v2_remove</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;,
    addr: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_remove(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, addr, ctx)
}
</code></pre>

Function <code>deny_list_v2_contains_current_epoch</code>

Check if the deny list contains the given address for the current epoch. Denied addresses
in the current epoch will be unable to receive objects of this coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_contains_current_epoch">deny_list_v2_contains_current_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, addr: <b>address</b>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_contains_current_epoch">deny_list_v2_contains_current_epoch</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &DenyList,
    addr: <b>address</b>,
    ctx: &TxContext,
): bool {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_contains_current_epoch(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, addr, ctx)
}
</code></pre>

Function <code>deny_list_v2_contains_next_epoch</code>

Check if the deny list contains the given address for the next epoch. Denied addresses in
the next epoch will immediately be unable to use objects of this coin type as inputs. At the
start of the next epoch, the address will be unable to receive objects of this coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_contains_next_epoch">deny_list_v2_contains_next_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, addr: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_contains_next_epoch">deny_list_v2_contains_next_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &DenyList, addr: <b>address</b>): bool {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_contains_next_epoch(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, addr)
}
</code></pre>

Function <code>deny_list_v2_enable_global_pause</code>

Enable the global pause for the given coin type. This will immediately prevent all addresses
from using objects of this coin type as inputs. At the start of the next epoch, all
addresses will be unable to receive objects of this coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_enable_global_pause">deny_list_v2_enable_global_pause</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_enable_global_pause">deny_list_v2_enable_global_pause</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(deny_cap.<a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>, <a href="../sui_sui/coin#sui_coin_EGlobalPauseNotAllowed">EGlobalPauseNotAllowed</a>);
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_enable_global_pause(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, ctx)
}
</code></pre>

Function <code>deny_list_v2_disable_global_pause</code>

Disable the global pause for the given coin type. This will immediately allow all addresses
to resume using objects of this coin type as inputs. However, receiving objects of this coin
type will still be paused until the start of the next epoch.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_disable_global_pause">deny_list_v2_disable_global_pause</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_disable_global_pause">deny_list_v2_disable_global_pause</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(deny_cap.<a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>, <a href="../sui_sui/coin#sui_coin_EGlobalPauseNotAllowed">EGlobalPauseNotAllowed</a>);
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_disable_global_pause(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, ctx)
}
</code></pre>

Function <code>deny_list_v2_is_global_pause_enabled_current_epoch</code>

Check if the global pause is enabled for the given coin type in the current epoch.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_is_global_pause_enabled_current_epoch">deny_list_v2_is_global_pause_enabled_current_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_is_global_pause_enabled_current_epoch">deny_list_v2_is_global_pause_enabled_current_epoch</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &DenyList,
    ctx: &TxContext,
): bool {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_is_global_pause_enabled_current_epoch(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty, ctx)
}
</code></pre>

Function <code>deny_list_v2_is_global_pause_enabled_next_epoch</code>

Check if the global pause is enabled for the given coin type in the next epoch.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_is_global_pause_enabled_next_epoch">deny_list_v2_is_global_pause_enabled_next_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_v2_is_global_pause_enabled_next_epoch">deny_list_v2_is_global_pause_enabled_next_epoch</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &DenyList): bool {
    <b>let</b> ty = type_name::with_original_ids&lt;T&gt;().into_string().into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v2_is_global_pause_enabled_next_epoch(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, ty)
}
</code></pre>

Function <code>mint_and_transfer</code>

Mint amount of <a href="../sui_sui/coin#sui_coin_Coin">Coin</a> and send it to recipient. Invokes <a href="../sui_sui/coin#sui_coin_mint">mint</a>().

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint_and_transfer">mint_and_transfer</a>&lt;T&gt;(c: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, amount: u64, recipient: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_mint_and_transfer">mint_and_transfer</a>&lt;T&gt;(
    c: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;,
    amount: u64,
    recipient: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(c.<a href="../sui_sui/coin#sui_coin_mint">mint</a>(amount, ctx), recipient)
}
</code></pre>

Function <code>update_name</code>

Update name of the coin in <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_name">update_name</a>&lt;T&gt;(_treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_name">update_name</a>&lt;T&gt;(
    _treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;,
    metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;,
    name: string::String,
) {
    metadata.name = name;
}
</code></pre>

Function <code>update_symbol</code>

Update the symbol of the coin in <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_symbol">update_symbol</a>&lt;T&gt;(_treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, symbol: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_symbol">update_symbol</a>&lt;T&gt;(
    _treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;,
    metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;,
    symbol: ascii::String,
) {
    metadata.symbol = symbol;
}
</code></pre>

Function <code>update_description</code>

Update the description of the coin in <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_description">update_description</a>&lt;T&gt;(_treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, description: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_description">update_description</a>&lt;T&gt;(
    _treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;,
    metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;,
    description: string::String,
) {
    metadata.description = description;
}
</code></pre>

Function <code>update_icon_url</code>

Update the url of the coin in <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_icon_url">update_icon_url</a>&lt;T&gt;(_treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, <a href="../sui_sui/url#sui_url">url</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_icon_url">update_icon_url</a>&lt;T&gt;(
    _treasury: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;,
    metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;,
    <a href="../sui_sui/url#sui_url">url</a>: ascii::String,
) {
    metadata.icon_url = option::some(<a href="../sui_sui/url#sui_url_new_unsafe">url::new_unsafe</a>(<a href="../sui_sui/url#sui_url">url</a>));
}
</code></pre>

Function <code>get_decimals</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_decimals">get_decimals</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_decimals">get_decimals</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;): u8 {
    metadata.decimals
}
</code></pre>

Function <code>get_name</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_name">get_name</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_name">get_name</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;): string::String {
    metadata.name
}
</code></pre>

Function <code>get_symbol</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_symbol">get_symbol</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_symbol">get_symbol</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;): ascii::String {
    metadata.symbol
}
</code></pre>

Function <code>get_description</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_description">get_description</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_description">get_description</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;): string::String {
    metadata.description
}
</code></pre>

Function <code>get_icon_url</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_icon_url">get_icon_url</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_get_icon_url">get_icon_url</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;): Option&lt;Url&gt; {
    metadata.icon_url
}
</code></pre>

Function <code>destroy_metadata</code>

Destroy legacy <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a> object

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_destroy_metadata">destroy_metadata</a>&lt;T&gt;(metadata: <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_destroy_metadata">destroy_metadata</a>&lt;T&gt;(metadata: <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a> { id, .. } = metadata;
    id.delete()
}
</code></pre>

Function <code>deny_cap_id</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_cap_id">deny_cap_id</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">sui::coin::RegulatedCoinMetadata</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_cap_id">deny_cap_id</a>&lt;T&gt;(metadata: &<a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">RegulatedCoinMetadata</a>&lt;T&gt;): ID {
    metadata.deny_cap_object
}
</code></pre>

Function <code>new_deny_cap_v2</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_deny_cap_v2">new_deny_cap_v2</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_deny_cap_v2">new_deny_cap_v2</a>&lt;T&gt;(
    <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>: bool,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>,
    }
}
</code></pre>

Function <code>new_treasury_cap</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_treasury_cap">new_treasury_cap</a>&lt;T&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_treasury_cap">new_treasury_cap</a>&lt;T&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>: <a href="../sui_sui/balance#sui_balance_create_supply_internal">balance::create_supply_internal</a>(),
    }
}
</code></pre>

Function <code>allow_global_pause</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>&lt;T&gt;(cap: &<a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>&lt;T&gt;(cap: &<a href="../sui_sui/coin#sui_coin_DenyCapV2">DenyCapV2</a>&lt;T&gt;): bool {
    cap.<a href="../sui_sui/coin#sui_coin_allow_global_pause">allow_global_pause</a>
}
</code></pre>

Function <code>new_coin_metadata</code>

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_coin_metadata">new_coin_metadata</a>&lt;T&gt;(decimals: u8, name: <a href="../sui_std/string#std_string_String">std::string::String</a>, symbol: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, description: <a href="../sui_std/string#std_string_String">std::string::String</a>, icon_url: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_new_coin_metadata">new_coin_metadata</a>&lt;T&gt;(
    decimals: u8,
    name: string::String,
    symbol: ascii::String,
    description: string::String,
    icon_url: ascii::String,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        decimals,
        name,
        symbol,
        description,
        icon_url: option::some(<a href="../sui_sui/url#sui_url_new_unsafe">url::new_unsafe</a>(icon_url)),
    }
}
</code></pre>

Function <code>update_coin_metadata</code>

Internal function to refresh the <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a> with new values in
CoinRegistry borrowing.

<code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_coin_metadata">update_coin_metadata</a>&lt;T&gt;(metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>, symbol: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, description: <a href="../sui_std/string#std_string_String">std::string::String</a>, icon_url: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(<a href="../sui_sui/package#sui_package">package</a>) <b>fun</b> <a href="../sui_sui/coin#sui_coin_update_coin_metadata">update_coin_metadata</a>&lt;T&gt;(
    metadata: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;,
    name: string::String,
    symbol: ascii::String,
    description: string::String,
    icon_url: ascii::String,
) {
    metadata.name = name;
    metadata.symbol = symbol;
    metadata.description = description;
    metadata.icon_url = option::some(<a href="../sui_sui/url#sui_url_new_unsafe">url::new_unsafe</a>(icon_url));
}
</code></pre>

Function <code>supply</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply">supply</a>&lt;T&gt;(treasury: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;): &<a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_supply">supply</a>&lt;T&gt;(treasury: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;): &Supply&lt;T&gt; {
    &treasury.<a href="../sui_sui/coin#sui_coin_total_supply">total_supply</a>
}
</code></pre>

Function <code>create_regulated_currency</code>

This creates a new currency, via <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>, but with an extra capability that
allows for specific addresses to have their coins frozen. Those addresses cannot interact
with the coin as input objects.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_regulated_currency">create_regulated_currency</a>&lt;T: drop&gt;(witness: T, decimals: u8, symbol: vector&lt;u8&gt;, name: vector&lt;u8&gt;, description: vector&lt;u8&gt;, icon_url: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_DenyCap">sui::coin::DenyCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_create_regulated_currency">create_regulated_currency</a>&lt;T: drop&gt;(
    witness: T,
    decimals: u8,
    symbol: vector&lt;u8&gt;,
    name: vector&lt;u8&gt;,
    description: vector&lt;u8&gt;,
    icon_url: Option&lt;Url&gt;,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin#sui_coin_TreasuryCap">TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_CoinMetadata">CoinMetadata</a>&lt;T&gt;) {
    <b>let</b> (treasury_cap, metadata) = <a href="../sui_sui/coin#sui_coin_create_currency">create_currency</a>(
        witness,
        decimals,
        symbol,
        name,
        description,
        icon_url,
        ctx,
    );
    <b>let</b> deny_cap = <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
    };
    <a href="../sui_sui/transfer#sui_transfer_freeze_object">transfer::freeze_object</a>(<a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">RegulatedCoinMetadata</a>&lt;T&gt; {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        coin_metadata_object: <a href="../sui_sui/object#sui_object_id">object::id</a>(&metadata),
        deny_cap_object: <a href="../sui_sui/object#sui_object_id">object::id</a>(&deny_cap),
    });
    (treasury_cap, deny_cap, metadata)
}
</code></pre>

Function <code>deny_list_add</code>

Adds the given address to the deny list, preventing it
from interacting with the specified coin type as an input to a transaction.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_add">deny_list_add</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCap">sui::coin::DenyCap</a>&lt;T&gt;, addr: <b>address</b>, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_add">deny_list_add</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a>&lt;T&gt;,
    addr: <b>address</b>,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> <span className="code-inline">type</span> = type_name::into_string(type_name::get_with_original_ids&lt;T&gt;()).into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v1_add(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, <span className="code-inline">type</span>, addr)
}
</code></pre>

Function <code>deny_list_remove</code>

Removes an address from the deny list.
Aborts with ENotFrozen if the address is not already in the list.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_remove">deny_list_remove</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> <a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCap">sui::coin::DenyCap</a>&lt;T&gt;, addr: <b>address</b>, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_remove">deny_list_remove</a>&lt;T&gt;(
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<b>mut</b> DenyList,
    _deny_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_DenyCap">DenyCap</a>&lt;T&gt;,
    addr: <b>address</b>,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> <span className="code-inline">type</span> = type_name::into_string(type_name::get_with_original_ids&lt;T&gt;()).into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v1_remove(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, <span className="code-inline">type</span>, addr)
}
</code></pre>

Function <code>deny_list_contains</code>

Returns true iff the given address is denied for the given coin type. It will
return false if given a non-coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_contains">deny_list_contains</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &<a href="../sui_sui/deny_list#sui_deny_list_DenyList">sui::deny_list::DenyList</a>, addr: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin#sui_coin_deny_list_contains">deny_list_contains</a>&lt;T&gt;(<a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>: &DenyList, addr: <b>address</b>): bool {
    <b>let</b> name = type_name::get_with_original_ids&lt;T&gt;();
    <b>if</b> (type_name::is_primitive(&name)) <b>return</b> <b>false</b>;
    <b>let</b> <span className="code-inline">type</span> = type_name::into_string(name).into_bytes();
    <a href="../sui_sui/deny_list#sui_deny_list">deny_list</a>.v1_contains(<a href="../sui_sui/coin#sui_coin_DENY_LIST_COIN_INDEX">DENY_LIST_COIN_INDEX</a>, <span className="code-inline">type</span>, addr)
}
</code></pre>