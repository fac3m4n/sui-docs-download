Defines the system object for managing coin data in a central
registry. This module provides a centralized way to store and manage
metadata for all currencies in the Sui ecosystem, including their
supply information, regulatory status, and metadata capabilities.

-  [Struct CoinRegistry](#sui_coin_registry_CoinRegistry)
-  [Struct ExtraField](#sui_coin_registry_ExtraField)
-  [Struct CurrencyKey](#sui_coin_registry_CurrencyKey)
-  [Struct LegacyMetadataKey](#sui_coin_registry_LegacyMetadataKey)
-  [Struct MetadataCap](#sui_coin_registry_MetadataCap)
-  [Struct Borrow](#sui_coin_registry_Borrow)
-  [Struct Currency](#sui_coin_registry_Currency)
-  [Struct CurrencyInitializer](#sui_coin_registry_CurrencyInitializer)
-  [Enum SupplyState](#sui_coin_registry_SupplyState)
-  [Enum RegulatedState](#sui_coin_registry_RegulatedState)
-  [Enum MetadataCapState](#sui_coin_registry_MetadataCapState)
-  [Constants](#@Constants_0)
-  [Function new_currency](#sui_coin_registry_new_currency)
-  [Function new_currency_with_otw](#sui_coin_registry_new_currency_with_otw)
-  [Function claim_metadata_cap](#sui_coin_registry_claim_metadata_cap)
-  [Function make_regulated](#sui_coin_registry_make_regulated)
-  [Function make_supply_fixed_init](#sui_coin_registry_make_supply_fixed_init)
-  [Function make_supply_burn_only_init](#sui_coin_registry_make_supply_burn_only_init)
-  [Function make_supply_fixed](#sui_coin_registry_make_supply_fixed)
-  [Function make_supply_burn_only](#sui_coin_registry_make_supply_burn_only)
-  [Function finalize](#sui_coin_registry_finalize)
-  [Function finalize_and_delete_metadata_cap](#sui_coin_registry_finalize_and_delete_metadata_cap)
-  [Function finalize_registration](#sui_coin_registry_finalize_registration)
-  [Function delete_metadata_cap](#sui_coin_registry_delete_metadata_cap)
-  [Function burn](#sui_coin_registry_burn)
-  [Function burn_balance](#sui_coin_registry_burn_balance)
-  [Function set_name](#sui_coin_registry_set_name)
-  [Function set_description](#sui_coin_registry_set_description)
-  [Function set_icon_url](#sui_coin_registry_set_icon_url)
-  [Function set_treasury_cap_id](#sui_coin_registry_set_treasury_cap_id)
-  [Function migrate_legacy_metadata](#sui_coin_registry_migrate_legacy_metadata)
-  [Function update_from_legacy_metadata](#sui_coin_registry_update_from_legacy_metadata)
-  [Function delete_migrated_legacy_metadata](#sui_coin_registry_delete_migrated_legacy_metadata)
-  [Function migrate_regulated_state_by_metadata](#sui_coin_registry_migrate_regulated_state_by_metadata)
-  [Function migrate_regulated_state_by_cap](#sui_coin_registry_migrate_regulated_state_by_cap)
-  [Function borrow_legacy_metadata](#sui_coin_registry_borrow_legacy_metadata)
-  [Function return_borrowed_legacy_metadata](#sui_coin_registry_return_borrowed_legacy_metadata)
-  [Function decimals](#sui_coin_registry_decimals)
-  [Function name](#sui_coin_registry_name)
-  [Function symbol](#sui_coin_registry_symbol)
-  [Function description](#sui_coin_registry_description)
-  [Function icon_url](#sui_coin_registry_icon_url)
-  [Function is_metadata_cap_claimed](#sui_coin_registry_is_metadata_cap_claimed)
-  [Function is_metadata_cap_deleted](#sui_coin_registry_is_metadata_cap_deleted)
-  [Function metadata_cap_id](#sui_coin_registry_metadata_cap_id)
-  [Function treasury_cap_id](#sui_coin_registry_treasury_cap_id)
-  [Function deny_cap_id](#sui_coin_registry_deny_cap_id)
-  [Function is_supply_fixed](#sui_coin_registry_is_supply_fixed)
-  [Function is_supply_burn_only](#sui_coin_registry_is_supply_burn_only)
-  [Function is_regulated](#sui_coin_registry_is_regulated)
-  [Function total_supply](#sui_coin_registry_total_supply)
-  [Function exists](#sui_coin_registry_exists)
-  [Function is_migrated_from_legacy](#sui_coin_registry_is_migrated_from_legacy)
-  [Function to_legacy_metadata](#sui_coin_registry_to_legacy_metadata)
-  [Function create](#sui_coin_registry_create)
-  [Macro function finalize_impl](#sui_coin_registry_finalize_impl)
-  [Macro function migrate_legacy_metadata_impl](#sui_coin_registry_migrate_legacy_metadata_impl)
-  [Macro function is_ascii_printable](#sui_coin_registry_is_ascii_printable)

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
<b>use</b> <a href="../sui_sui/derived_object#sui_derived_object">sui::derived_object</a>;
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

Struct <code>CoinRegistry</code>

System object found at address 0xc that stores coin data for all
registered coin types. This is a shared object that acts as a central
registry for coin metadata, supply information, and regulatory status.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ExtraField</code>

Store only object that enables more flexible coin data
registration, allowing for additional fields to be added
without changing the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> structure.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ExtraField">ExtraField</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>0: <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a></code>
</dt>
<dd>
</dd>
<dt>
<code>1: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>CurrencyKey</code>

Key used to derive addresses when creating <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt; objects.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyKey">CurrencyKey</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Struct <code>LegacyMetadataKey</code>

Key used to store the legacy CoinMetadata for a <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Struct <code>MetadataCap</code>

Capability object that gates metadata (name, description, icon_url, symbol)
changes in the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>. It can only be created (or claimed) once, and can
be deleted to prevent changes to the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> metadata.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Borrow</code>

Potato callback for the legacy CoinMetadata borrowing.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a>&lt;<b>phantom</b> T&gt;
</code>

<summary>Fields</summary>

<dl>
</dl>

Struct <code>Currency</code>

Currency stores metadata such as name, symbol, decimals, icon_url and description,
as well as supply states (optional) and regulatory status.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;<b>phantom</b> T&gt; <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: u8</code>
</dt>
<dd>
 Number of decimal places the coin uses for display purposes.
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Human-readable name for the coin.
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Short symbol/ticker for the coin.
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Detailed description of the coin.
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 URL for the coin's icon/logo.
</dd>
<dt>
<code>supply: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/coin_registry#sui_coin_registry_SupplyState">sui::coin_registry::SupplyState</a>&lt;T&gt;&gt;</code>
</dt>
<dd>
 Current supply state of the coin (fixed supply or unknown)
 Note: We're using <code>Option</code> because <code><a href="../sui_sui/coin_registry#sui_coin_registry_SupplyState">SupplyState</a></code> does not have drop,
 meaning we cannot swap out its value at a later state.
</dd>
<dt>
<code>regulated: <a href="../sui_sui/coin_registry#sui_coin_registry_RegulatedState">sui::coin_registry::RegulatedState</a></code>
</dt>
<dd>
 Regulatory status of the coin (regulated with deny cap or unknown)
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;</code>
</dt>
<dd>
 ID of the treasury cap for this coin type, if registered.
</dd>
<dt>
<code><a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>: <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCapState">sui::coin_registry::MetadataCapState</a></code>
</dt>
<dd>
 ID of the metadata capability for this coin type, if claimed.
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_ExtraField">sui::coin_registry::ExtraField</a>&gt;</code>
</dt>
<dd>
 Additional fields for extensibility.
</dd>
</dl>

Struct <code>CurrencyInitializer</code>

Hot potato wrapper to enforce registration after "new_currency" data creation.
Destroyed in the <a href="../sui_sui/coin_registry#sui_coin_registry_finalize">finalize</a> call and either transferred to the <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>
(in case of an OTW registration) or shared directly (for dynamically created
currencies).

<code><b>public</b> <b>struct</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;<b>phantom</b> T&gt;
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>currency: <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
</dd>
<dt>
<code>is_otw: bool</code>
</dt>
<dd>
</dd>
</dl>

Enum <code>SupplyState</code>

Supply state marks the type of Currency Supply, which can be
- Fixed: no minting or burning;
- BurnOnly: no minting, burning is allowed;
- Unknown: flexible (supply is controlled by its TreasuryCap);

<code><b>public</b> <b>enum</b> <a href="../sui_sui/coin_registry#sui_coin_registry_SupplyState">SupplyState</a>&lt;<b>phantom</b> T&gt; <b>has</b> store
</code>

<summary>Variants</summary>

<dl>
<dt>
Variant <code>Fixed</code>
</dt>
<dd>
 Coin has a fixed supply with the given Supply object.
</dd>

<dl>
<dt>
<code>0: <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
</dl>

<dt>
Variant <code>BurnOnly</code>
</dt>
<dd>
 Coin has a supply that can ONLY decrease.
</dd>

<dl>
<dt>
<code>0: <a href="../sui_sui/balance#sui_balance_Supply">sui::balance::Supply</a>&lt;T&gt;</code>
</dt>
<dd>
</dd>
</dl>

<dt>
Variant <code>Unknown</code>
</dt>
<dd>
 Supply information is not yet known or registered.
</dd>
</dl>

Enum <code>RegulatedState</code>

Regulated state of a coin type.
- Regulated: DenyCap exists or a RegulatedCoinMetadata used to mark currency as regulated;
- Unregulated: the currency was created without deny list;
- Unknown: the regulatory status is unknown.

<code><b>public</b> <b>enum</b> <a href="../sui_sui/coin_registry#sui_coin_registry_RegulatedState">RegulatedState</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Variants</summary>

<dl>
<dt>
Variant <code>Regulated</code>
</dt>
<dd>
 Coin is regulated with a deny cap for address restrictions.
 <code>allow_global_pause</code> is <code>None</code> if the information is unknown (has not been migrated from <code>DenyCapV2</code>).
</dd>

<dl>
<dt>
<code>cap: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

<dl>
<dt>
<code>allow_global_pause: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;bool&gt;</code>
</dt>
<dd>
</dd>
</dl>

<dl>
<dt>
<code>variant: u8</code>
</dt>
<dd>
</dd>
</dl>

<dt>
Variant <code>Unregulated</code>
</dt>
<dd>
 The coin has been created without deny list.
</dd>
<dt>
Variant <code>Unknown</code>
</dt>
<dd>
 Regulatory status is unknown.
 Result of a legacy migration for that coin (from <code><a href="../sui_sui/coin#sui_coin">coin</a>.<b>move</b></code> constructors)
</dd>
</dl>

Enum <code>MetadataCapState</code>

State of the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> for a single <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>enum</b> <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCapState">MetadataCapState</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Variants</summary>

<dl>
<dt>
Variant <code>Claimed</code>
</dt>
<dd>
 The metadata cap has been claimed.
</dd>

<dl>
<dt>
<code>0: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

<dt>
Variant <code>Unclaimed</code>
</dt>
<dd>
 The metadata cap has not been claimed.
</dd>
<dt>
Variant <code>Deleted</code>
</dt>
<dd>
 The metadata cap has been claimed and then deleted.
</dd>
</dl>

Constants

Metadata cap already claimed

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EMetadataCapAlreadyClaimed">EMetadataCapAlreadyClaimed</a>: vector&lt;u8&gt; = b"Metadata cap already claimed";
</code>

Only the system address can create the registry

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ENotSystemAddress">ENotSystemAddress</a>: vector&lt;u8&gt; = b"Only the system can <a href="../sui_sui/coin_registry#sui_coin_registry_create">create</a> the registry.";
</code>

Currency for this coin type already exists

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ECurrencyAlreadyExists">ECurrencyAlreadyExists</a>: vector&lt;u8&gt; = b"<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> <b>for</b> this <a href="../sui_sui/coin#sui_coin">coin</a> type already <a href="../sui_sui/coin_registry#sui_coin_registry_exists">exists</a>.";
</code>

Attempt to set the deny list state permissionlessly while it has already been set.

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EDenyListStateAlreadySet">EDenyListStateAlreadySet</a>: vector&lt;u8&gt; = b"Cannot set the deny list state <b>as</b> it <b>has</b> already been set.";
</code>

Attempt to update <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> with legacy metadata after the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> has
been claimed. Updates are only allowed if the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> has not yet been
claimed or deleted.

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ECannotUpdateManagedMetadata">ECannotUpdateManagedMetadata</a>: vector&lt;u8&gt; = b"Cannot update metadata whose <span className="code-inline"><a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a></span> <b>has</b> already been claimed";
</code>

Attempt to set the symbol to a non-ASCII printable character

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EInvalidSymbol">EInvalidSymbol</a>: vector&lt;u8&gt; = b"Symbol <b>has</b> to be ASCII printable";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EDenyCapAlreadyCreated">EDenyCapAlreadyCreated</a>: vector&lt;u8&gt; = b"Cannot claim the deny cap twice";
</code>

Attempt to migrate legacy metadata for a <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> that already exists.

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ECurrencyAlreadyRegistered">ECurrencyAlreadyRegistered</a>: vector&lt;u8&gt; = b"<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> already registered";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EEmptySupply">EEmptySupply</a>: vector&lt;u8&gt; = b"Supply cannot be empty";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ESupplyNotBurnOnly">ESupplyNotBurnOnly</a>: vector&lt;u8&gt; = b"Cannot <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a> on a non <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a>-only supply";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EInvariantViolation">EInvariantViolation</a>: vector&lt;u8&gt; = b"Code <b>invariant</b> violation";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EDeletionNotSupported">EDeletionNotSupported</a>: vector&lt;u8&gt; = b"Deleting legacy metadata is not supported";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_ENotOneTimeWitness">ENotOneTimeWitness</a>: vector&lt;u8&gt; = b"Type is expected to be OTW";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EBorrowLegacyMetadata">EBorrowLegacyMetadata</a>: vector&lt;u8&gt; = b"Cannot <a href="../sui_sui/borrow#sui_borrow">borrow</a> legacy metadata <b>for</b> migrated currency";
</code>

<code>#[error]
<b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EDuplicateBorrow">EDuplicateBorrow</a>: vector&lt;u8&gt; = b"Attempt to <b>return</b> duplicate borrowed CoinMetadata";
</code>

Incremental identifier for regulated coin versions in the deny list.
We start from 0 in the new system, which aligns with the state of DenyCapV2.

<code><b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_REGULATED_COIN_VERSION">REGULATED_COIN_VERSION</a>: u8 = 0;
</code>

Marker used in metadata to indicate that the currency is not migrated.

<code><b>const</b> <a href="../sui_sui/coin_registry#sui_coin_registry_NEW_CURRENCY_MARKER">NEW_CURRENCY_MARKER</a>: vector&lt;u8&gt; = vector[105, 115, 95, 110, 101, 119, 95, 99, 117, 114, 114, 101, 110, 99, 121];
</code>

Function <code>new_currency</code>

Creates a new currency.

Note: This constructor has no long term difference from <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency_with_otw">new_currency_with_otw</a>.
This can be called from the module that defines T any time after it has been published.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency">new_currency</a>&lt;T: key&gt;(registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">sui::coin_registry::CoinRegistry</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: u8, <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency">new_currency</a>&lt;T: /* internal */ key&gt;(
    registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>,
    <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: u8,
    <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: String,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;, TreasuryCap&lt;T&gt;) {
    <b>assert</b>!(!registry.<a href="../sui_sui/coin_registry#sui_coin_registry_exists">exists</a>&lt;T&gt;(), <a href="../sui_sui/coin_registry#sui_coin_registry_ECurrencyAlreadyExists">ECurrencyAlreadyExists</a>);
    <b>assert</b>!(<a href="../sui_sui/coin_registry#sui_coin_registry_is_ascii_printable">is_ascii_printable</a>!(&<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>), <a href="../sui_sui/coin_registry#sui_coin_registry_EInvalidSymbol">EInvalidSymbol</a>);
    <b>let</b> treasury_cap = <a href="../sui_sui/coin#sui_coin_new_treasury_cap">coin::new_treasury_cap</a>(ctx);
    <b>let</b> currency = <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt; {
        id: <a href="../sui_sui/derived_object#sui_derived_object_claim">derived_object::claim</a>(&<b>mut</b> registry.id, <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyKey">CurrencyKey</a>&lt;T&gt;()),
        <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>,
        supply: option::some(SupplyState::Unknown),
        regulated: RegulatedState::Unregulated,
        <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>: option::some(<a href="../sui_sui/object#sui_object_id">object::id</a>(&treasury_cap)),
        <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>: MetadataCapState::Unclaimed,
        extra_fields: <a href="../sui_sui/vec_map#sui_vec_map_empty">vec_map::empty</a>(),
    };
    (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a> { currency, is_otw: <b>false</b>, extra_fields: <a href="../sui_sui/bag#sui_bag_new">bag::new</a>(ctx) }, treasury_cap)
}
</code></pre>

Function <code>new_currency_with_otw</code>

Creates a new currency with using an OTW as proof of uniqueness.

This is a two-step operation:
1. <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> is constructed in the init function and sent to the <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>;
2. <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> is promoted to a shared object in the <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_registration">finalize_registration</a> call;

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency_with_otw">new_currency_with_otw</a>&lt;T: drop&gt;(otw: T, <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: u8, <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency_with_otw">new_currency_with_otw</a>&lt;T: drop&gt;(
    otw: T,
    <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: u8,
    <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: String,
    <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: String,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;, TreasuryCap&lt;T&gt;) {
    <b>assert</b>!(<a href="../sui_sui/types#sui_types_is_one_time_witness">sui::types::is_one_time_witness</a>(&otw), <a href="../sui_sui/coin_registry#sui_coin_registry_ENotOneTimeWitness">ENotOneTimeWitness</a>);
    <b>assert</b>!(<a href="../sui_sui/coin_registry#sui_coin_registry_is_ascii_printable">is_ascii_printable</a>!(&<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>), <a href="../sui_sui/coin_registry#sui_coin_registry_EInvalidSymbol">EInvalidSymbol</a>);
    <b>let</b> treasury_cap = <a href="../sui_sui/coin#sui_coin_new_treasury_cap">coin::new_treasury_cap</a>(ctx);
    <b>let</b> currency = <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt; {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>,
        supply: option::some(SupplyState::Unknown),
        regulated: RegulatedState::Unregulated,
        <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>: option::some(<a href="../sui_sui/object#sui_object_id">object::id</a>(&treasury_cap)),
        <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>: MetadataCapState::Unclaimed,
        extra_fields: <a href="../sui_sui/vec_map#sui_vec_map_empty">vec_map::empty</a>(),
    };
    (<a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a> { currency, is_otw: <b>true</b>, extra_fields: <a href="../sui_sui/bag#sui_bag_new">bag::new</a>(ctx) }, treasury_cap)
}
</code></pre>

Function <code>claim_metadata_cap</code>

Claim a <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> for a coin type.
Only allowed from the owner of TreasuryCap, and only once.

Aborts if the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> has already been claimed.
Deleted <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> cannot be reclaimed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_claim_metadata_cap">claim_metadata_cap</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_claim_metadata_cap">claim_metadata_cap</a>&lt;T&gt;(
    currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;,
    _: &TreasuryCap&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt; {
    <b>assert</b>!(!currency.<a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_claimed">is_metadata_cap_claimed</a>(), <a href="../sui_sui/coin_registry#sui_coin_registry_EMetadataCapAlreadyClaimed">EMetadataCapAlreadyClaimed</a>);
    <b>let</b> id = <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx);
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a> = MetadataCapState::Claimed(id.to_inner());
    <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> { id }
}
</code></pre>

Function <code>make_regulated</code>

Allows converting a currency, on init, to regulated, which creates
a DenyCapV2 object, and a denylist entry. Sets regulated state to
Regulated.

This action is irreversible.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_regulated">make_regulated</a>&lt;T&gt;(init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, allow_global_pause: bool, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_regulated">make_regulated</a>&lt;T&gt;(
    init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;,
    allow_global_pause: bool,
    ctx: &<b>mut</b> TxContext,
): DenyCapV2&lt;T&gt; {
    <b>assert</b>!(init.currency.regulated == RegulatedState::Unregulated, <a href="../sui_sui/coin_registry#sui_coin_registry_EDenyCapAlreadyCreated">EDenyCapAlreadyCreated</a>);
    <b>let</b> deny_cap = <a href="../sui_sui/coin#sui_coin_new_deny_cap_v2">coin::new_deny_cap_v2</a>&lt;T&gt;(allow_global_pause, ctx);
    init.currency.regulated =
        RegulatedState::Regulated {
            cap: <a href="../sui_sui/object#sui_object_id">object::id</a>(&deny_cap),
            allow_global_pause: option::some(allow_global_pause),
            variant: <a href="../sui_sui/coin_registry#sui_coin_registry_REGULATED_COIN_VERSION">REGULATED_COIN_VERSION</a>,
        };
    deny_cap
}
</code></pre>

Function <code>make_supply_fixed_init</code>

Initializer function to make the supply fixed.
Aborts if Supply is 0 to enforce minting during initialization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_fixed_init">make_supply_fixed_init</a>&lt;T&gt;(init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, cap: <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_fixed_init">make_supply_fixed_init</a>&lt;T&gt;(init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;, cap: TreasuryCap&lt;T&gt;) {
    <b>assert</b>!(cap.<a href="../sui_sui/coin_registry#sui_coin_registry_total_supply">total_supply</a>() &gt; 0, <a href="../sui_sui/coin_registry#sui_coin_registry_EEmptySupply">EEmptySupply</a>);
    init.currency.<a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_fixed">make_supply_fixed</a>(cap)
}
</code></pre>

Function <code>make_supply_burn_only_init</code>

Initializer function to make the supply burn-only.
Aborts if Supply is 0 to enforce minting during initialization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_burn_only_init">make_supply_burn_only_init</a>&lt;T&gt;(init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, cap: <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_burn_only_init">make_supply_burn_only_init</a>&lt;T&gt;(init: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;, cap: TreasuryCap&lt;T&gt;) {
    <b>assert</b>!(cap.<a href="../sui_sui/coin_registry#sui_coin_registry_total_supply">total_supply</a>() &gt; 0, <a href="../sui_sui/coin_registry#sui_coin_registry_EEmptySupply">EEmptySupply</a>);
    init.currency.<a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_burn_only">make_supply_burn_only</a>(cap)
}
</code></pre>

Function <code>make_supply_fixed</code>

Freeze the supply by destroying the TreasuryCap and storing it in the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_fixed">make_supply_fixed</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, cap: <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_fixed">make_supply_fixed</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, cap: TreasuryCap&lt;T&gt;) {
    match (currency.supply.swap(SupplyState::Fixed(cap.into_supply()))) {
        // Impossible: We cannot fix a supply or make a supply <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a>-only twice.
        SupplyState::Fixed(_supply) | SupplyState::BurnOnly(_supply) =&gt; <b>abort</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EInvariantViolation">EInvariantViolation</a>,
        // We replaced "unknown" with fixed supply.
        SupplyState::Unknown =&gt; (),
    };
}
</code></pre>

Function <code>make_supply_burn_only</code>

Make the supply BurnOnly by giving up the TreasuryCap, and allowing
burning of Coins through the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_burn_only">make_supply_burn_only</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, cap: <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_make_supply_burn_only">make_supply_burn_only</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, cap: TreasuryCap&lt;T&gt;) {
    match (currency.supply.swap(SupplyState::BurnOnly(cap.into_supply()))) {
        // Impossible: We cannot fix a supply or make a supply <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a>-only twice.
        SupplyState::Fixed(_supply) | SupplyState::BurnOnly(_supply) =&gt; <b>abort</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EInvariantViolation">EInvariantViolation</a>,
        // We replaced "unknown" with frozen supply.
        SupplyState::Unknown =&gt; (),
    };
}
</code></pre>

Function <code>finalize</code>

Finalize the coin initialization, returning <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize">finalize</a>&lt;T&gt;(builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize">finalize</a>&lt;T&gt;(builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt; {
    <b>let</b> is_otw = builder.is_otw;
    <b>let</b> (currency, metadata_cap) = <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_impl">finalize_impl</a>!(builder, ctx);
    // Either share directly (<span className="code-inline"><a href="../sui_sui/coin_registry#sui_coin_registry_new_currency">new_currency</a></span> scenario), or <a href="../sui_sui/transfer#sui_transfer">transfer</a> <b>as</b> TTO to <span className="code-inline"><a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a></span>.
    <b>if</b> (is_otw) <a href="../sui_sui/transfer#sui_transfer_transfer">transfer::transfer</a>(currency, <a href="../sui_sui/object#sui_object_sui_coin_registry_address">object::sui_coin_registry_address</a>())
    <b>else</b> <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(currency);
    metadata_cap
}
</code></pre>

Function <code>finalize_and_delete_metadata_cap</code>

Does the same as <a href="../sui_sui/coin_registry#sui_coin_registry_finalize">finalize</a>, but also deletes the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> after finalization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_and_delete_metadata_cap">finalize_and_delete_metadata_cap</a>&lt;T&gt;(builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_and_delete_metadata_cap">finalize_and_delete_metadata_cap</a>&lt;T&gt;(
    builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> is_otw = builder.is_otw;
    <b>let</b> (<b>mut</b> currency, metadata_cap) = <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_impl">finalize_impl</a>!(builder, ctx);
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_delete_metadata_cap">delete_metadata_cap</a>(metadata_cap);
    // Either share directly (<span className="code-inline"><a href="../sui_sui/coin_registry#sui_coin_registry_new_currency">new_currency</a></span> scenario), or <a href="../sui_sui/transfer#sui_transfer">transfer</a> <b>as</b> TTO to <span className="code-inline"><a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a></span>.
    <b>if</b> (is_otw) <a href="../sui_sui/transfer#sui_transfer_transfer">transfer::transfer</a>(currency, <a href="../sui_sui/object#sui_object_sui_coin_registry_address">object::sui_coin_registry_address</a>())
    <b>else</b> <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(currency);
}
</code></pre>

Function <code>finalize_registration</code>

The second step in the "otw" initialization of coin metadata, that takes in
the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt; that was transferred from init, and transforms it in to a
"derived address" shared object.

Can be performed by anyone.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_registration">finalize_registration</a>&lt;T&gt;(registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">sui::coin_registry::CoinRegistry</a>, currency: <a href="../sui_sui/transfer#sui_transfer_Receiving">sui::transfer::Receiving</a>&lt;<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_registration">finalize_registration</a>&lt;T&gt;(
    registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>,
    currency: Receiving&lt;<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;&gt;,
    _ctx: &<b>mut</b> TxContext,
) {
    // 1. Consume <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>
    // 2. Re-<a href="../sui_sui/coin_registry#sui_coin_registry_create">create</a> it with a "derived" <b>address</b>.
    <b>let</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> {
        id,
        <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>,
        supply,
        regulated,
        <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>,
        extra_fields,
    } = <a href="../sui_sui/transfer#sui_transfer_receive">transfer::receive</a>(&<b>mut</b> registry.id, currency);
    id.delete();
    // Now, <a href="../sui_sui/coin_registry#sui_coin_registry_create">create</a> the derived version of the <a href="../sui_sui/coin#sui_coin">coin</a> currency.
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> {
        id: <a href="../sui_sui/derived_object#sui_derived_object_claim">derived_object::claim</a>(&<b>mut</b> registry.id, <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyKey">CurrencyKey</a>&lt;T&gt;()),
        <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>,
        supply,
        regulated,
        <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>,
        <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>,
        extra_fields,
    })
}
</code></pre>

Function <code>delete_metadata_cap</code>

Delete the metadata cap making further updates of <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> metadata impossible.
This action is IRREVERSIBLE, and the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> can no longer be claimed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_delete_metadata_cap">delete_metadata_cap</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, cap: <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_delete_metadata_cap">delete_metadata_cap</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, cap: <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> { id } = cap;
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a> = MetadataCapState::Deleted;
    id.delete();
}
</code></pre>

Function <code>burn</code>

Burn the Coin if the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> has a BurnOnly supply state.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_burn">burn</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: Coin&lt;T&gt;) {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_burn_balance">burn_balance</a>(<a href="../sui_sui/coin#sui_coin">coin</a>.into_balance());
}
</code></pre>

Function <code>burn_balance</code>

Burn the Balance if the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> has a BurnOnly supply state.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_burn_balance">burn_balance</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_burn_balance">burn_balance</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, <a href="../sui_sui/balance#sui_balance">balance</a>: Balance&lt;T&gt;) {
    <b>assert</b>!(currency.<a href="../sui_sui/coin_registry#sui_coin_registry_is_supply_burn_only">is_supply_burn_only</a>(), <a href="../sui_sui/coin_registry#sui_coin_registry_ESupplyNotBurnOnly">ESupplyNotBurnOnly</a>);
    match (currency.supply.borrow_mut()) {
        SupplyState::BurnOnly(supply) =&gt; { supply.decrease_supply(<a href="../sui_sui/balance#sui_balance">balance</a>); },
        _ =&gt; <b>abort</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EInvariantViolation">EInvariantViolation</a>, // unreachable
    }
}
</code></pre>

Function <code>set_name</code>

Update the name of the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_name">set_name</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_name">set_name</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: String) {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a> = <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>;
}
</code></pre>

Function <code>set_description</code>

Update the description of the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_description">set_description</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_description">set_description</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: String) {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a> = <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>;
}
</code></pre>

Function <code>set_icon_url</code>

Update the icon URL of the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_icon_url">set_icon_url</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_icon_url">set_icon_url</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, _: &<a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: String) {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a> = <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>;
}
</code></pre>

Function <code>set_treasury_cap_id</code>

Register the treasury cap ID for a migrated <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>. All currencies created with
<a href="../sui_sui/coin_registry#sui_coin_registry_new_currency">new_currency</a> or <a href="../sui_sui/coin_registry#sui_coin_registry_new_currency_with_otw">new_currency_with_otw</a> have their treasury cap ID set during
initialization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_treasury_cap_id">set_treasury_cap_id</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, cap: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_set_treasury_cap_id">set_treasury_cap_id</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, cap: &TreasuryCap&lt;T&gt;) {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>.fill(<a href="../sui_sui/object#sui_object_id">object::id</a>(cap));
}
</code></pre>

Function <code>migrate_legacy_metadata</code>

Register CoinMetadata in the <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>. This can happen only once, if the
<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> did not exist yet. Further updates are possible through
<a href="../sui_sui/coin_registry#sui_coin_registry_update_from_legacy_metadata">update_from_legacy_metadata</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_legacy_metadata">migrate_legacy_metadata</a>&lt;T&gt;(registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">sui::coin_registry::CoinRegistry</a>, legacy: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_legacy_metadata">migrate_legacy_metadata</a>&lt;T&gt;(
    registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>,
    legacy: &CoinMetadata&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> currency = <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_legacy_metadata_impl">migrate_legacy_metadata_impl</a>!(registry, legacy);
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(currency);
}
</code></pre>

Function <code>update_from_legacy_metadata</code>

Update <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> from CoinMetadata if the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> is not claimed. After
the <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a> is claimed, updates can only be made through set_* functions.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_update_from_legacy_metadata">update_from_legacy_metadata</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, legacy: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_update_from_legacy_metadata">update_from_legacy_metadata</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, legacy: &CoinMetadata&lt;T&gt;) {
    <b>assert</b>!(!currency.<a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_claimed">is_metadata_cap_claimed</a>(), <a href="../sui_sui/coin_registry#sui_coin_registry_ECannotUpdateManagedMetadata">ECannotUpdateManagedMetadata</a>);
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a> = legacy.get_name();
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a> = legacy.get_symbol().to_string();
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a> = legacy.get_description();
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a> = legacy.get_decimals();
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a> =
        legacy.get_icon_url().map!(|<a href="../sui_sui/url#sui_url">url</a>| <a href="../sui_sui/url#sui_url">url</a>.inner_url().to_string()).destroy_or!(b"".to_string());
}
</code></pre>

Function <code>delete_migrated_legacy_metadata</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_delete_migrated_legacy_metadata">delete_migrated_legacy_metadata</a>&lt;T&gt;(_: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, _: <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_delete_migrated_legacy_metadata">delete_migrated_legacy_metadata</a>&lt;T&gt;(_: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, _: CoinMetadata&lt;T&gt;) {
    <b>abort</b> <a href="../sui_sui/coin_registry#sui_coin_registry_EDeletionNotSupported">EDeletionNotSupported</a>
}
</code></pre>

Function <code>migrate_regulated_state_by_metadata</code>

Allow migrating the regulated state by access to RegulatedCoinMetadata frozen object.
This is a permissionless operation which can be performed only once.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_regulated_state_by_metadata">migrate_regulated_state_by_metadata</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, metadata: &<a href="../sui_sui/coin#sui_coin_RegulatedCoinMetadata">sui::coin::RegulatedCoinMetadata</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_regulated_state_by_metadata">migrate_regulated_state_by_metadata</a>&lt;T&gt;(
    currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;,
    metadata: &RegulatedCoinMetadata&lt;T&gt;,
) {
    // Only allow <b>if</b> this hasn't been migrated before.
    <b>assert</b>!(currency.regulated == RegulatedState::Unknown, <a href="../sui_sui/coin_registry#sui_coin_registry_EDenyListStateAlreadySet">EDenyListStateAlreadySet</a>);
    currency.regulated =
        RegulatedState::Regulated {
            cap: metadata.<a href="../sui_sui/coin_registry#sui_coin_registry_deny_cap_id">deny_cap_id</a>(),
            allow_global_pause: option::none(),
            variant: <a href="../sui_sui/coin_registry#sui_coin_registry_REGULATED_COIN_VERSION">REGULATED_COIN_VERSION</a>,
        };
}
</code></pre>

Function <code>migrate_regulated_state_by_cap</code>

Mark regulated state by showing the DenyCapV2 object for the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_regulated_state_by_cap">migrate_regulated_state_by_cap</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, cap: &<a href="../sui_sui/coin#sui_coin_DenyCapV2">sui::coin::DenyCapV2</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_regulated_state_by_cap">migrate_regulated_state_by_cap</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, cap: &DenyCapV2&lt;T&gt;) {
    currency.regulated =
        RegulatedState::Regulated {
            cap: <a href="../sui_sui/object#sui_object_id">object::id</a>(cap),
            allow_global_pause: option::some(cap.allow_global_pause()),
            variant: <a href="../sui_sui/coin_registry#sui_coin_registry_REGULATED_COIN_VERSION">REGULATED_COIN_VERSION</a>,
        };
}
</code></pre>

Function <code>borrow_legacy_metadata</code>

Borrow the legacy CoinMetadata from a new <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>. To preserve the ID
of the legacy CoinMetadata, we create it on request and then store it as a
dynamic field for future borrows.

<a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a>&lt;T&gt; ensures that the CoinMetadata is returned in the same transaction.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_borrow_legacy_metadata">borrow_legacy_metadata</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">sui::coin_registry::Borrow</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_borrow_legacy_metadata">borrow_legacy_metadata</a>&lt;T&gt;(
    currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
): (CoinMetadata&lt;T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a>&lt;T&gt;) {
    <b>assert</b>!(!currency.<a href="../sui_sui/coin_registry#sui_coin_registry_is_migrated_from_legacy">is_migrated_from_legacy</a>(), <a href="../sui_sui/coin_registry#sui_coin_registry_EBorrowLegacyMetadata">EBorrowLegacyMetadata</a>);
    <b>if</b> (!df::exists_(&currency.id, <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a>())) {
        <b>let</b> legacy = currency.<a href="../sui_sui/coin_registry#sui_coin_registry_to_legacy_metadata">to_legacy_metadata</a>(ctx);
        df::add(&<b>mut</b> currency.id, <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a>(), legacy);
    };
    <b>let</b> <b>mut</b> legacy: CoinMetadata&lt;T&gt; = df::remove(&<b>mut</b> currency.id, <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a>());
    legacy.update_coin_metadata(
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>.to_ascii(),
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>.to_ascii(),
    );
    (legacy, <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a> {})
}
</code></pre>

Function <code>return_borrowed_legacy_metadata</code>

Return the borrowed CoinMetadata and the <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a> potato to the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

Note to self: Borrow requirement prevents deletion through this method.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_return_borrowed_legacy_metadata">return_borrowed_legacy_metadata</a>&lt;T&gt;(currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, legacy: <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;, <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">sui::coin_registry::Borrow</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_return_borrowed_legacy_metadata">return_borrowed_legacy_metadata</a>&lt;T&gt;(
    currency: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;,
    <b>mut</b> legacy: CoinMetadata&lt;T&gt;,
    <a href="../sui_sui/borrow#sui_borrow">borrow</a>: <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a>&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(!df::exists_(&currency.id, <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a>()), <a href="../sui_sui/coin_registry#sui_coin_registry_EDuplicateBorrow">EDuplicateBorrow</a>);
    <b>let</b> <a href="../sui_sui/coin_registry#sui_coin_registry_Borrow">Borrow</a> {} = <a href="../sui_sui/borrow#sui_borrow">borrow</a>;
    // Always store up to date value.
    legacy.update_coin_metadata(
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>.to_ascii(),
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>.to_ascii(),
    );
    df::add(&<b>mut</b> currency.id, <a href="../sui_sui/coin_registry#sui_coin_registry_LegacyMetadataKey">LegacyMetadataKey</a>(), legacy);
}
</code></pre>

Function <code>decimals</code>

Get the number of decimal places for the coin type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): u8 { currency.<a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a> }
</code></pre>

Function <code>name</code>

Get the human-readable name of the coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): String { currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a> }
</code></pre>

Function <code>symbol</code>

Get the symbol/ticker of the coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): String { currency.<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a> }
</code></pre>

Function <code>description</code>

Get the description of the coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): String { currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a> }
</code></pre>

Function <code>icon_url</code>

Get the icon URL for the coin.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): String { currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a> }
</code></pre>

Function <code>is_metadata_cap_claimed</code>

Check if the metadata capability has been claimed for this <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_claimed">is_metadata_cap_claimed</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_claimed">is_metadata_cap_claimed</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    match (currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>) {
        MetadataCapState::Claimed(_) | MetadataCapState::Deleted =&gt; <b>true</b>,
        _ =&gt; <b>false</b>,
    }
}
</code></pre>

Function <code>is_metadata_cap_deleted</code>

Check if the metadata capability has been deleted for this <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> type.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_deleted">is_metadata_cap_deleted</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_metadata_cap_deleted">is_metadata_cap_deleted</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    match (currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>) {
        MetadataCapState::Deleted =&gt; <b>true</b>,
        _ =&gt; <b>false</b>,
    }
}
</code></pre>

Function <code>metadata_cap_id</code>

Get the metadata cap ID, or none if it has not been claimed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): Option&lt;ID&gt; {
    match (currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>) {
        MetadataCapState::Claimed(id) =&gt; option::some(id),
        _ =&gt; option::none(),
    }
}
</code></pre>

Function <code>treasury_cap_id</code>

Get the treasury cap ID for this coin type, if registered.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): Option&lt;ID&gt; {
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>
}
</code></pre>

Function <code>deny_cap_id</code>

Get the deny cap ID for this coin type, if it's a regulated coin.
Returns None if:
- The <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> is not regulated;
- The <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a> is migrated from legacy, and its regulated state has not been set;

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_deny_cap_id">deny_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_deny_cap_id">deny_cap_id</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): Option&lt;ID&gt; {
    match (currency.regulated) {
        RegulatedState::Regulated { cap, .. } =&gt; option::some(cap),
        RegulatedState::Unregulated | RegulatedState::Unknown =&gt; option::none(),
    }
}
</code></pre>

Function <code>is_supply_fixed</code>

Check if the supply is fixed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_supply_fixed">is_supply_fixed</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_supply_fixed">is_supply_fixed</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    match (currency.supply.<a href="../sui_sui/borrow#sui_borrow">borrow</a>()) {
        SupplyState::Fixed(_) =&gt; <b>true</b>,
        _ =&gt; <b>false</b>,
    }
}
</code></pre>

Function <code>is_supply_burn_only</code>

Check if the supply is burn-only.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_supply_burn_only">is_supply_burn_only</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_supply_burn_only">is_supply_burn_only</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    match (currency.supply.<a href="../sui_sui/borrow#sui_borrow">borrow</a>()) {
        SupplyState::BurnOnly(_) =&gt; <b>true</b>,
        _ =&gt; <b>false</b>,
    }
}
</code></pre>

Function <code>is_regulated</code>

Check if the currency is regulated.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_regulated">is_regulated</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_regulated">is_regulated</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    match (currency.regulated) {
        RegulatedState::Regulated { .. } =&gt; <b>true</b>,
        _ =&gt; <b>false</b>,
    }
}
</code></pre>

Function <code>total_supply</code>

Get the total supply for the <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt; if the Supply is in fixed or
burn-only state. Returns None if the SupplyState is Unknown.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_total_supply">total_supply</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_total_supply">total_supply</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): Option&lt;u64&gt; {
    match (currency.supply.<a href="../sui_sui/borrow#sui_borrow">borrow</a>()) {
        SupplyState::Fixed(supply) =&gt; option::some(supply.value()),
        SupplyState::BurnOnly(supply) =&gt; option::some(supply.value()),
        SupplyState::Unknown =&gt; option::none(),
    }
}
</code></pre>

Function <code>exists</code>

Check if coin data exists for the given type T in the registry.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_exists">exists</a>&lt;T&gt;(registry: &<a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">sui::coin_registry::CoinRegistry</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_exists">exists</a>&lt;T&gt;(registry: &<a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>): bool {
    <a href="../sui_sui/derived_object#sui_derived_object_exists">derived_object::exists</a>(&registry.id, <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyKey">CurrencyKey</a>&lt;T&gt;())
}
</code></pre>

Function <code>is_migrated_from_legacy</code>

Whether the currency is migrated from legacy.

<code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_migrated_from_legacy">is_migrated_from_legacy</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_migrated_from_legacy">is_migrated_from_legacy</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;): bool {
    !currency.extra_fields.contains(&<a href="../sui_sui/coin_registry#sui_coin_registry_NEW_CURRENCY_MARKER">NEW_CURRENCY_MARKER</a>.to_string())
}
</code></pre>

Function <code>to_legacy_metadata</code>

Create a new legacy CoinMetadata from a <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>.

<code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_to_legacy_metadata">to_legacy_metadata</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_to_legacy_metadata">to_legacy_metadata</a>&lt;T&gt;(currency: &<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;T&gt;, ctx: &<b>mut</b> TxContext): CoinMetadata&lt;T&gt; {
    <a href="../sui_sui/coin#sui_coin_new_coin_metadata">coin::new_coin_metadata</a>(
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>.to_ascii(),
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>,
        currency.<a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>.to_ascii(),
        ctx,
    )
}
</code></pre>

Function <code>create</code>

Create and share the singleton <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a> -- this function is
called exactly once, during the upgrade epoch.
Only the system address (0x0) can create the registry.

<code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_create">create</a>(ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_create">create</a>(ctx: &TxContext) {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/coin_registry#sui_coin_registry_ENotSystemAddress">ENotSystemAddress</a>);
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(<a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a> {
        id: <a href="../sui_sui/object#sui_object_sui_coin_registry_object_id">object::sui_coin_registry_object_id</a>(),
    });
}
</code></pre>

Macro function <code>finalize_impl</code>

Internal macro to keep implementation between build and test modes.

<code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_impl">finalize_impl</a>&lt;$T&gt;($builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">sui::coin_registry::CurrencyInitializer</a>&lt;$T&gt;, $ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;$T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">sui::coin_registry::MetadataCap</a>&lt;$T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_finalize_impl">finalize_impl</a>&lt;$T&gt;(
    $builder: <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a>&lt;$T&gt;,
    $ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;$T&gt;, <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;$T&gt;) {
    <b>let</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyInitializer">CurrencyInitializer</a> { <b>mut</b> currency, extra_fields, is_otw: _ } = $builder;
    extra_fields.destroy_empty();
    <b>let</b> id = <a href="../sui_sui/object#sui_object_new">object::new</a>($ctx);
    currency.<a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a> = MetadataCapState::Claimed(id.to_inner());
    // Mark the currency <b>as</b> new, so in the future we can support borrowing of the
    // legacy metadata.
    currency
        .extra_fields
        .insert(
            <a href="../sui_sui/coin_registry#sui_coin_registry_NEW_CURRENCY_MARKER">NEW_CURRENCY_MARKER</a>.to_string(),
            <a href="../sui_sui/coin_registry#sui_coin_registry_ExtraField">ExtraField</a>(type_name::with_original_ids&lt;bool&gt;(), <a href="../sui_sui/coin_registry#sui_coin_registry_NEW_CURRENCY_MARKER">NEW_CURRENCY_MARKER</a>),
        );
    (currency, <a href="../sui_sui/coin_registry#sui_coin_registry_MetadataCap">MetadataCap</a>&lt;$T&gt; { id })
}
</code></pre>

Macro function <code>migrate_legacy_metadata_impl</code>

Internal macro to keep implementation between build and test modes.

<code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_legacy_metadata_impl">migrate_legacy_metadata_impl</a>&lt;$T&gt;($registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">sui::coin_registry::CoinRegistry</a>, $legacy: &<a href="../sui_sui/coin#sui_coin_CoinMetadata">sui::coin::CoinMetadata</a>&lt;$T&gt;): <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">sui::coin_registry::Currency</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_migrate_legacy_metadata_impl">migrate_legacy_metadata_impl</a>&lt;$T&gt;(
    $registry: &<b>mut</b> <a href="../sui_sui/coin_registry#sui_coin_registry_CoinRegistry">CoinRegistry</a>,
    $legacy: &CoinMetadata&lt;$T&gt;,
): <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;$T&gt; {
    <b>let</b> registry = $registry;
    <b>let</b> legacy = $legacy;
    <b>assert</b>!(!registry.<a href="../sui_sui/coin_registry#sui_coin_registry_exists">exists</a>&lt;$T&gt;(), <a href="../sui_sui/coin_registry#sui_coin_registry_ECurrencyAlreadyRegistered">ECurrencyAlreadyRegistered</a>);
    <b>assert</b>!(<a href="../sui_sui/coin_registry#sui_coin_registry_is_ascii_printable">is_ascii_printable</a>!(&legacy.get_symbol().to_string()), <a href="../sui_sui/coin_registry#sui_coin_registry_EInvalidSymbol">EInvalidSymbol</a>);
    <a href="../sui_sui/coin_registry#sui_coin_registry_Currency">Currency</a>&lt;$T&gt; {
        id: <a href="../sui_sui/derived_object#sui_derived_object_claim">derived_object::claim</a>(&<b>mut</b> registry.id, <a href="../sui_sui/coin_registry#sui_coin_registry_CurrencyKey">CurrencyKey</a>&lt;$T&gt;()),
        <a href="../sui_sui/coin_registry#sui_coin_registry_decimals">decimals</a>: legacy.get_decimals(),
        <a href="../sui_sui/coin_registry#sui_coin_registry_name">name</a>: legacy.get_name(),
        <a href="../sui_sui/coin_registry#sui_coin_registry_symbol">symbol</a>: legacy.get_symbol().to_string(),
        <a href="../sui_sui/coin_registry#sui_coin_registry_description">description</a>: legacy.get_description(),
        <a href="../sui_sui/coin_registry#sui_coin_registry_icon_url">icon_url</a>: legacy
            .get_icon_url()
            .map!(|<a href="../sui_sui/url#sui_url">url</a>| <a href="../sui_sui/url#sui_url">url</a>.inner_url().to_string())
            .destroy_or!(b"".to_string()),
        supply: option::some(SupplyState::Unknown),
        regulated: RegulatedState::Unknown,
        <a href="../sui_sui/coin_registry#sui_coin_registry_treasury_cap_id">treasury_cap_id</a>: option::none(),
        <a href="../sui_sui/coin_registry#sui_coin_registry_metadata_cap_id">metadata_cap_id</a>: MetadataCapState::Unclaimed,
        extra_fields: <a href="../sui_sui/vec_map#sui_vec_map_empty">vec_map::empty</a>(),
    }
}
</code></pre>

Macro function <code>is_ascii_printable</code>

Nit: consider adding this function to <a href="../sui_std/string#std_string">std::string</a> in the future.

<code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_ascii_printable">is_ascii_printable</a>($s: &<a href="../sui_std/string#std_string_String">std::string::String</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui/coin_registry#sui_coin_registry_is_ascii_printable">is_ascii_printable</a>($s: &String): bool {
    <b>let</b> s = $s;
    s.as_bytes().all!(|b| ascii::is_printable_char(*b))
}
</code></pre>