Coin<SUI> is the token used to pay for gas in Sui.
It has 9 decimals, and the smallest unit (10^-9) is called "mist".

-  [Struct SUI](#sui_sui_SUI)
-  [Constants](#@Constants_0)
-  [Function new](#sui_sui_new)
-  [Function transfer](#sui_sui_transfer)

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

Struct <code>SUI</code>

Name of the coin

<code><b>public</b> <b>struct</b> <a href="../sui_sui/sui#sui_sui_SUI">SUI</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/sui#sui_sui_EAlreadyMinted">EAlreadyMinted</a>: u64 = 0;
</code>

Sender is not @0x0 the system address.

<code><b>const</b> <a href="../sui_sui/sui#sui_sui_ENotSystemAddress">ENotSystemAddress</a>: u64 = 1;
</code>

The amount of Mist per Sui token based on the fact that mist is
10^-9 of a Sui token

<code><b>const</b> <a href="../sui_sui/sui#sui_sui_MIST_PER_SUI">MIST_PER_SUI</a>: u64 = 1000000000;
</code>

The total supply of Sui denominated in whole Sui tokens (10 Billion)

<code><b>const</b> <a href="../sui_sui/sui#sui_sui_TOTAL_SUPPLY_SUI">TOTAL_SUPPLY_SUI</a>: u64 = 10000000000;
</code>

The total supply of Sui denominated in Mist (10 Billion * 10^9)

<code><b>const</b> <a href="../sui_sui/sui#sui_sui_TOTAL_SUPPLY_MIST">TOTAL_SUPPLY_MIST</a>: u64 = 10000000000000000000;
</code>

Function <code>new</code>

Register the <a href="../sui_sui/sui#sui_sui_SUI">SUI</a> Coin to acquire its Supply.
This should be called only once during genesis creation.

<code><b>fun</b> <a href="../sui_sui/sui#sui_sui_new">new</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/sui#sui_sui_new">new</a>(ctx: &<b>mut</b> TxContext): Balance&lt;<a href="../sui_sui/sui#sui_sui_SUI">SUI</a>&gt; {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/sui#sui_sui_ENotSystemAddress">ENotSystemAddress</a>);
    <b>assert</b>!(ctx.epoch() == 0, <a href="../sui_sui/sui#sui_sui_EAlreadyMinted">EAlreadyMinted</a>);
    <b>let</b> (treasury, metadata) = <a href="../sui_sui/coin#sui_coin_create_currency">coin::create_currency</a>(
        <a href="../sui_sui/sui#sui_sui_SUI">SUI</a> {},
        9,
        b"<a href="../sui_sui/sui#sui_sui_SUI">SUI</a>",
        b"Sui",
        // TODO: add appropriate description and logo <a href="../sui_sui/url#sui_url">url</a>
        b"",
        option::none(),
        ctx,
    );
    <a href="../sui_sui/transfer#sui_transfer_public_freeze_object">transfer::public_freeze_object</a>(metadata);
    <b>let</b> <b>mut</b> supply = treasury.treasury_into_supply();
    <b>let</b> total_sui = supply.increase_supply(<a href="../sui_sui/sui#sui_sui_TOTAL_SUPPLY_MIST">TOTAL_SUPPLY_MIST</a>);
    supply.destroy_supply();
    total_sui
}
</code></pre>

Function <code>transfer</code>

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>(c: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, recipient: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>(c: <a href="../sui_sui/coin#sui_coin_Coin">coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">SUI</a>&gt;, recipient: <b>address</b>) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(c, recipient)
}
</code></pre>