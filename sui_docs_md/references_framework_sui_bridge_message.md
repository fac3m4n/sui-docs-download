-  [Struct BridgeMessage](#bridge_message_BridgeMessage)
-  [Struct BridgeMessageKey](#bridge_message_BridgeMessageKey)
-  [Struct TokenTransferPayload](#bridge_message_TokenTransferPayload)
-  [Struct TokenTransferPayloadV2](#bridge_message_TokenTransferPayloadV2)
-  [Struct EmergencyOp](#bridge_message_EmergencyOp)
-  [Struct Blocklist](#bridge_message_Blocklist)
-  [Struct UpdateBridgeLimit](#bridge_message_UpdateBridgeLimit)
-  [Struct UpdateAssetPrice](#bridge_message_UpdateAssetPrice)
-  [Struct AddTokenOnSui](#bridge_message_AddTokenOnSui)
-  [Struct ParsedTokenTransferMessage](#bridge_message_ParsedTokenTransferMessage)
-  [Constants](#@Constants_0)
-  [Function extract_token_bridge_payload](#bridge_message_extract_token_bridge_payload)
-  [Function extract_token_bridge_payload_v2](#bridge_message_extract_token_bridge_payload_v2)
-  [Function to_token_payload_v1](#bridge_message_to_token_payload_v1)
-  [Function extract_emergency_op_payload](#bridge_message_extract_emergency_op_payload)
-  [Function extract_blocklist_payload](#bridge_message_extract_blocklist_payload)
-  [Function extract_update_bridge_limit](#bridge_message_extract_update_bridge_limit)
-  [Function extract_update_asset_price](#bridge_message_extract_update_asset_price)
-  [Function extract_add_tokens_on_sui](#bridge_message_extract_add_tokens_on_sui)
-  [Function serialize_message](#bridge_message_serialize_message)
-  [Function create_token_bridge_message](#bridge_message_create_token_bridge_message)
-  [Function create_token_bridge_message_v2](#bridge_message_create_token_bridge_message_v2)
-  [Function create_emergency_op_message](#bridge_message_create_emergency_op_message)
-  [Function create_blocklist_message](#bridge_message_create_blocklist_message)
-  [Function create_update_bridge_limit_message](#bridge_message_create_update_bridge_limit_message)
-  [Function create_update_asset_price_message](#bridge_message_create_update_asset_price_message)
-  [Function create_add_tokens_on_sui_message](#bridge_message_create_add_tokens_on_sui_message)
-  [Function create_key](#bridge_message_create_key)
-  [Function key](#bridge_message_key)
-  [Function message_version](#bridge_message_message_version)
-  [Function message_type](#bridge_message_message_type)
-  [Function seq_num](#bridge_message_seq_num)
-  [Function source_chain](#bridge_message_source_chain)
-  [Function payload](#bridge_message_payload)
-  [Function token_target_chain](#bridge_message_token_target_chain)
-  [Function token_target_address](#bridge_message_token_target_address)
-  [Function token_type](#bridge_message_token_type)
-  [Function token_amount](#bridge_message_token_amount)
-  [Function timestamp_ms](#bridge_message_timestamp_ms)
-  [Function emergency_op_type](#bridge_message_emergency_op_type)
-  [Function blocklist_type](#bridge_message_blocklist_type)
-  [Function blocklist_validator_addresses](#bridge_message_blocklist_validator_addresses)
-  [Function update_bridge_limit_payload_sending_chain](#bridge_message_update_bridge_limit_payload_sending_chain)
-  [Function update_bridge_limit_payload_receiving_chain](#bridge_message_update_bridge_limit_payload_receiving_chain)
-  [Function update_bridge_limit_payload_limit](#bridge_message_update_bridge_limit_payload_limit)
-  [Function update_asset_price_payload_token_id](#bridge_message_update_asset_price_payload_token_id)
-  [Function update_asset_price_payload_new_price](#bridge_message_update_asset_price_payload_new_price)
-  [Function is_native](#bridge_message_is_native)
-  [Function token_ids](#bridge_message_token_ids)
-  [Function token_type_names](#bridge_message_token_type_names)
-  [Function token_prices](#bridge_message_token_prices)
-  [Function emergency_op_pause](#bridge_message_emergency_op_pause)
-  [Function emergency_op_unpause](#bridge_message_emergency_op_unpause)
-  [Function required_voting_power](#bridge_message_required_voting_power)
-  [Function to_parsed_token_transfer_message](#bridge_message_to_parsed_token_transfer_message)
-  [Function token_transfer_message_version](#bridge_message_token_transfer_message_version)
-  [Function reverse_bytes](#bridge_message_reverse_bytes)
-  [Function peel_u64_be](#bridge_message_peel_u64_be)

<code><b>use</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids">bridge::chain_ids</a>;
<b>use</b> <a href="../sui_bridge/message_types#bridge_message_types">bridge::message_types</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/bcs#sui_bcs">sui::bcs</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
</code>

Struct <code>BridgeMessage</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_payload">payload</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>BridgeMessageKey</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">BridgeMessageKey</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>bridge_seq_num: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenTransferPayload</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>sender_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>target_chain: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>target_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>amount: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenTransferPayloadV2</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">TokenTransferPayloadV2</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>sender_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>target_chain: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>target_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>amount: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a>: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>EmergencyOp</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_EmergencyOp">EmergencyOp</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>op_type: u8</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Blocklist</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_Blocklist">Blocklist</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_eth_addresses: vector&lt;vector&lt;u8&gt;&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>UpdateBridgeLimit</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>receiving_chain: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>sending_chain: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>limit: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>UpdateAssetPrice</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">UpdateAssetPrice</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>token_id: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>new_price: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>AddTokenOnSui</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>native_token: bool</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>: vector&lt;<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>: vector&lt;u64&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ParsedTokenTransferMessage</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/message#bridge_message_ParsedTokenTransferMessage">ParsedTokenTransferMessage</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_bridge/message#bridge_message_payload">payload</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>parsed_payload: <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>: u8 = 1;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_TOKEN_TRANSFER_MESSAGE_VERSION_V2">TOKEN_TRANSFER_MESSAGE_VERSION_V2</a>: u8 = 2;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_ECDSA_ADDRESS_LENGTH">ECDSA_ADDRESS_LENGTH</a>: u64 = 20;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>: u64 = 0;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EInvalidAddressLength">EInvalidAddressLength</a>: u64 = 1;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EEmptyList">EEmptyList</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EInvalidMessageType">EInvalidMessageType</a>: u64 = 3;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EInvalidEmergencyOpType">EInvalidEmergencyOpType</a>: u64 = 4;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EInvalidPayloadLength">EInvalidPayloadLength</a>: u64 = 5;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EMustBeTokenMessage">EMustBeTokenMessage</a>: u64 = 6;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_EInvalidMessageVersion">EInvalidMessageVersion</a>: u64 = 7;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_PAUSE">PAUSE</a>: u8 = 0;
</code>

<code><b>const</b> <a href="../sui_bridge/message#bridge_message_UNPAUSE">UNPAUSE</a>: u8 = 1;
</code>

Function <code>extract_token_bridge_payload</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload">extract_token_bridge_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload">extract_token_bridge_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a> {
    <b>assert</b>!(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_message_version">message_version</a>() == 1, <a href="../sui_bridge/message#bridge_message_EInvalidMessageVersion">EInvalidMessageVersion</a>);
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> sender_address = bcs.peel_vec_u8();
    <b>let</b> target_chain = bcs.peel_u8();
    <b>let</b> target_address = bcs.peel_vec_u8();
    <b>let</b> <a href="../sui_bridge/message#bridge_message_token_type">token_type</a> = bcs.peel_u8();
    <b>let</b> amount = <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(&<b>mut</b> bcs);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(target_chain);
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a> {
        sender_address,
        target_chain,
        target_address,
        <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>,
        amount,
    }
}
</code></pre>

Function <code>extract_token_bridge_payload_v2</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload_v2">extract_token_bridge_payload_v2</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">bridge::message::TokenTransferPayloadV2</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload_v2">extract_token_bridge_payload_v2</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">TokenTransferPayloadV2</a> {
    <b>assert</b>!(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_message_version">message_version</a>() == 2, <a href="../sui_bridge/message#bridge_message_EInvalidMessageVersion">EInvalidMessageVersion</a>);
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> sender_address = bcs.peel_vec_u8();
    <b>let</b> target_chain = bcs.peel_u8();
    <b>let</b> target_address = bcs.peel_vec_u8();
    <b>let</b> <a href="../sui_bridge/message#bridge_message_token_type">token_type</a> = bcs.peel_u8();
    <b>let</b> amount = <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(&<b>mut</b> bcs);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(target_chain);
    <b>let</b> <a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a> = <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(&<b>mut</b> bcs);
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">TokenTransferPayloadV2</a> {
        sender_address,
        target_chain,
        target_address,
        <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>,
        amount,
        <a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a>,
    }
}
</code></pre>

Function <code>to_token_payload_v1</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_bridge/message#bridge_message_to_token_payload_v1">to_token_payload_v1</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">bridge::message::TokenTransferPayloadV2</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_bridge/message#bridge_message_to_token_payload_v1">to_token_payload_v1</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">TokenTransferPayloadV2</a>): <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a> {
    <a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a> {
        sender_address: self.sender_address,
        target_chain: self.target_chain,
        target_address: self.target_address,
        <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: self.<a href="../sui_bridge/message#bridge_message_token_type">token_type</a>,
        amount: self.amount,
    }
}
</code></pre>

Function <code>extract_emergency_op_payload</code>

Emergency op payload is just a single byte

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_emergency_op_payload">extract_emergency_op_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_EmergencyOp">bridge::message::EmergencyOp</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_emergency_op_payload">extract_emergency_op_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_EmergencyOp">EmergencyOp</a> {
    <b>assert</b>!(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>.length() == 1, <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_EmergencyOp">EmergencyOp</a> { op_type: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>[0] }
}
</code></pre>

Function <code>extract_blocklist_payload</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_blocklist_payload">extract_blocklist_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_Blocklist">bridge::message::Blocklist</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_blocklist_payload">extract_blocklist_payload</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_Blocklist">Blocklist</a> {
    // blocklist <a href="../sui_bridge/message#bridge_message_payload">payload</a> should consist of one byte blocklist type, and list of 20 bytes evm addresses
    // derived from ECDSA <b>public</b> keys
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a> = bcs.peel_u8();
    <b>let</b> <b>mut</b> address_count = bcs.peel_u8();
    <b>assert</b>!(address_count != 0, <a href="../sui_bridge/message#bridge_message_EEmptyList">EEmptyList</a>);
    <b>let</b> <b>mut</b> validator_eth_addresses = vector[];
    <b>while</b> (address_count &gt; 0) {
        <b>let</b> (<b>mut</b> <b>address</b>, <b>mut</b> i) = (vector[], 0);
        <b>while</b> (i &lt; <a href="../sui_bridge/message#bridge_message_ECDSA_ADDRESS_LENGTH">ECDSA_ADDRESS_LENGTH</a>) {
            <b>address</b>.push_back(bcs.peel_u8());
            i = i + 1;
        };
        validator_eth_addresses.push_back(<b>address</b>);
        address_count = address_count - 1;
    };
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_Blocklist">Blocklist</a> {
        <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>,
        validator_eth_addresses,
    }
}
</code></pre>

Function <code>extract_update_bridge_limit</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_update_bridge_limit">extract_update_bridge_limit</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">bridge::message::UpdateBridgeLimit</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_update_bridge_limit">extract_update_bridge_limit</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a> {
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> sending_chain = bcs.peel_u8();
    <b>let</b> limit = <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(&<b>mut</b> bcs);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(sending_chain);
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a> {
        receiving_chain: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        sending_chain,
        limit,
    }
}
</code></pre>

Function <code>extract_update_asset_price</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_update_asset_price">extract_update_asset_price</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">bridge::message::UpdateAssetPrice</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_update_asset_price">extract_update_asset_price</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">UpdateAssetPrice</a> {
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> token_id = bcs.peel_u8();
    <b>let</b> new_price = <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(&<b>mut</b> bcs);
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">UpdateAssetPrice</a> {
        token_id,
        new_price,
    }
}
</code></pre>

Function <code>extract_add_tokens_on_sui</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_add_tokens_on_sui">extract_add_tokens_on_sui</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_AddTokenOnSui">bridge::message::AddTokenOnSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_extract_add_tokens_on_sui">extract_add_tokens_on_sui</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a> {
    <b>let</b> <b>mut</b> bcs = bcs::new(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <b>let</b> native_token = bcs.peel_bool();
    <b>let</b> <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a> = bcs.peel_vec_u8();
    <b>let</b> token_type_names_bytes = bcs.peel_vec_vec_u8();
    <b>let</b> <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a> = bcs.peel_vec_u64();
    <b>let</b> <b>mut</b> n = 0;
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a> = vector[];
    <b>while</b> (n &lt; token_type_names_bytes.length()) {
        <a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>.push_back(ascii::string(*token_type_names_bytes.borrow(n)));
        n = n + 1;
    };
    <b>assert</b>!(bcs.into_remainder_bytes().is_empty(), <a href="../sui_bridge/message#bridge_message_ETrailingBytes">ETrailingBytes</a>);
    <a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a> {
        native_token,
        <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>,
        <a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>,
        <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>,
    }
}
</code></pre>

Function <code>serialize_message</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_serialize_message">serialize_message</a>(<a href="../sui_bridge/message#bridge_message">message</a>: <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_serialize_message">serialize_message</a>(<a href="../sui_bridge/message#bridge_message">message</a>: <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): vector&lt;u8&gt; {
    <b>let</b> <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>,
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    } = <a href="../sui_bridge/message#bridge_message">message</a>;
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message">message</a> = vector[<a href="../sui_bridge/message#bridge_message_message_type">message_type</a>, <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>];
    // bcs serializes u64 <b>as</b> 8 bytes
    <a href="../sui_bridge/message#bridge_message">message</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&<a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>)));
    <a href="../sui_bridge/message#bridge_message">message</a>.push_back(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <a href="../sui_bridge/message#bridge_message">message</a>.append(<a href="../sui_bridge/message#bridge_message_payload">payload</a>);
    <a href="../sui_bridge/message#bridge_message">message</a>
}
</code></pre>

Function <code>create_token_bridge_message</code>

Token Transfer Message Format:
[message_type: u8]
[version:u8]
[nonce:u64]
[source_chain: u8]
[sender_address_length:u8]
[sender_address: byte[]]
[target_chain:u8]
[target_address_length:u8]
[target_address: byte[]]
[token_type:u8]
[amount:u64]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_token_bridge_message">create_token_bridge_message</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, sender_address: vector&lt;u8&gt;, target_chain: u8, target_address: vector&lt;u8&gt;, <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8, amount: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_token_bridge_message">create_token_bridge_message</a>(
    <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    sender_address: vector&lt;u8&gt;,
    target_chain: u8,
    target_address: vector&lt;u8&gt;,
    <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8,
    amount: u64,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(target_chain);
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = vector[];
    // sender <b>address</b> should be less than 255 bytes so can fit into u8
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back((vector::length(&sender_address) <b>as</b> u8));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(sender_address);
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back(target_chain);
    // target <b>address</b> should be less than 255 bytes so can fit into u8
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back((vector::length(&target_address) <b>as</b> u8));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(target_address);
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back(<a href="../sui_bridge/message#bridge_message_token_type">token_type</a>);
    // bcs serialzies u64 <b>as</b> 8 bytes
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&amount)));
    <b>assert</b>!(vector::length(&<a href="../sui_bridge/message#bridge_message_payload">payload</a>) == 64, <a href="../sui_bridge/message#bridge_message_EInvalidPayloadLength">EInvalidPayloadLength</a>);
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_token">message_types::token</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_token_bridge_message_v2</code>

Token Transfer Message Format:
[message_type: u8]
[version:u8]
[nonce:u64]
[source_chain: u8]
[sender_address_length:u8]
[sender_address: byte[]]
[target_chain:u8]
[target_address_length:u8]
[target_address: byte[]]
[token_type:u8]
[amount:u64]
[timestamp:u64]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_token_bridge_message_v2">create_token_bridge_message_v2</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, sender_address: vector&lt;u8&gt;, target_chain: u8, target_address: vector&lt;u8&gt;, <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8, amount: u64, timestamp: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_token_bridge_message_v2">create_token_bridge_message_v2</a>(
    <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    sender_address: vector&lt;u8&gt;,
    target_chain: u8,
    target_address: vector&lt;u8&gt;,
    <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>: u8,
    amount: u64,
    timestamp: u64,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(target_chain);
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = vector[];
    // sender <b>address</b> should be less than 255 bytes so can fit into u8
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back((vector::length(&sender_address) <b>as</b> u8));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(sender_address);
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back(target_chain);
    // target <b>address</b> should be less than 255 bytes so can fit into u8
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back((vector::length(&target_address) <b>as</b> u8));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(target_address);
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.push_back(<a href="../sui_bridge/message#bridge_message_token_type">token_type</a>);
    // bcs serialzies u64 <b>as</b> 8 bytes
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&amount)));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&timestamp)));
    <b>assert</b>!(vector::length(&<a href="../sui_bridge/message#bridge_message_payload">payload</a>) == 72, <a href="../sui_bridge/message#bridge_message_EInvalidPayloadLength">EInvalidPayloadLength</a>);
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_token">message_types::token</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_TOKEN_TRANSFER_MESSAGE_VERSION_V2">TOKEN_TRANSFER_MESSAGE_VERSION_V2</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_emergency_op_message</code>

Emergency Op Message Format:
[message_type: u8]
[version:u8]
[nonce:u64]
[chain_id: u8]
[op_type: u8]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_emergency_op_message">create_emergency_op_message</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, op_type: u8): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_emergency_op_message">create_emergency_op_message</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, op_type: u8): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_emergency_op">message_types::emergency_op</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>: vector[op_type],
    }
}
</code></pre>

Function <code>create_blocklist_message</code>

Blocklist Message Format:
[message_type: u8]
[version:u8]
[nonce:u64]
[chain_id: u8]
[blocklist_type: u8]
[validator_length: u8]
[validator_ecdsa_addresses: byte[][]]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_blocklist_message">create_blocklist_message</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>: u8, validator_ecdsa_addresses: vector&lt;vector&lt;u8&gt;&gt;): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_blocklist_message">create_blocklist_message</a>(
    <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    // 0: block, 1: unblock
    <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>: u8,
    validator_ecdsa_addresses: vector&lt;vector&lt;u8&gt;&gt;,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <b>let</b> address_length = validator_ecdsa_addresses.length();
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = vector[<a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>, (address_length <b>as</b> u8)];
    <b>let</b> <b>mut</b> i = 0;
    <b>while</b> (i &lt; address_length) {
        <b>let</b> <b>address</b> = validator_ecdsa_addresses[i];
        <b>assert</b>!(<b>address</b>.length() == <a href="../sui_bridge/message#bridge_message_ECDSA_ADDRESS_LENGTH">ECDSA_ADDRESS_LENGTH</a>, <a href="../sui_bridge/message#bridge_message_EInvalidAddressLength">EInvalidAddressLength</a>);
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<b>address</b>);
        i = i + 1;
    };
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_committee_blocklist">message_types::committee_blocklist</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_update_bridge_limit_message</code>

Update bridge limit Message Format:
[message_type: u8]
[version:u8]
[nonce:u64]
[receiving_chain_id: u8]
[sending_chain_id: u8]
[new_limit: u64]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_update_bridge_limit_message">create_update_bridge_limit_message</a>(receiving_chain: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, sending_chain: u8, new_limit: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_update_bridge_limit_message">create_update_bridge_limit_message</a>(
    receiving_chain: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    sending_chain: u8,
    new_limit: u64,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(receiving_chain);
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(sending_chain);
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = vector[sending_chain];
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&new_limit)));
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_update_bridge_limit">message_types::update_bridge_limit</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: receiving_chain,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_update_asset_price_message</code>

Update asset price message
[message_type: u8]
[version:u8]
[nonce:u64]
[chain_id: u8]
[token_id: u8]
[new_price:u64]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_update_asset_price_message">create_update_asset_price_message</a>(token_id: u8, <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, new_price: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_update_asset_price_message">create_update_asset_price_message</a>(
    token_id: u8,
    <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    new_price: u64,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = vector[token_id];
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(<a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bcs::to_bytes(&new_price)));
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_update_asset_price">message_types::update_asset_price</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_add_tokens_on_sui_message</code>

Update Sui token message
[message_type:u8]
[version:u8]
[nonce:u64]
[chain_id: u8]
[native_token:bool]
[token_ids:vector<u8>]
[token_type_name:vector<String>]
[token_prices:vector<u64>]

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_add_tokens_on_sui_message">create_add_tokens_on_sui_message</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64, native_token: bool, <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>: vector&lt;u8&gt;, type_names: vector&lt;<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>&gt;, <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>: vector&lt;u64&gt;): <a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_add_tokens_on_sui_message">create_add_tokens_on_sui_message</a>(
    <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8,
    <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: u64,
    native_token: bool,
    <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>: vector&lt;u8&gt;,
    type_names: vector&lt;String&gt;,
    <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>: vector&lt;u64&gt;,
): <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">chain_ids::assert_valid_chain_id</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>);
    <b>let</b> <b>mut</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = bcs::to_bytes(&native_token);
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(bcs::to_bytes(&<a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(bcs::to_bytes(&type_names));
    <a href="../sui_bridge/message#bridge_message_payload">payload</a>.append(bcs::to_bytes(&<a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>));
    <a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: <a href="../sui_bridge/message_types#bridge_message_types_add_tokens_on_sui">message_types::add_tokens_on_sui</a>(),
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message_CURRENT_MESSAGE_VERSION">CURRENT_MESSAGE_VERSION</a>,
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>,
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>,
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>,
    }
}
</code></pre>

Function <code>create_key</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_key">create_key</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: u8, bridge_seq_num: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">bridge::message::BridgeMessageKey</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_create_key">create_key</a>(<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: u8, <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>: u8, bridge_seq_num: u64): <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">BridgeMessageKey</a> {
    <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">BridgeMessageKey</a> { <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>, <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>, bridge_seq_num }
}
</code></pre>

Function <code>key</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_key">key</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">bridge::message::BridgeMessageKey</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_key">key</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_BridgeMessageKey">BridgeMessageKey</a> {
    <a href="../sui_bridge/message#bridge_message_create_key">create_key</a>(self.<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>, self.<a href="../sui_bridge/message#bridge_message_message_type">message_type</a>, self.<a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>)
}
</code></pre>

Function <code>message_version</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): u8 {
    self.<a href="../sui_bridge/message#bridge_message_message_version">message_version</a>
}
</code></pre>

Function <code>message_type</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): u8 {
    self.<a href="../sui_bridge/message#bridge_message_message_type">message_type</a>
}
</code></pre>

Function <code>seq_num</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): u64 {
    self.<a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>
}
</code></pre>

Function <code>source_chain</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): u8 {
    self.<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>
}
</code></pre>

Function <code>payload</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): vector&lt;u8&gt; {
    self.<a href="../sui_bridge/message#bridge_message_payload">payload</a>
}
</code></pre>

Function <code>token_target_chain</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_target_chain">token_target_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_target_chain">token_target_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a>): u8 {
    self.target_chain
}
</code></pre>

Function <code>token_target_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_target_address">token_target_address</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_target_address">token_target_address</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a>): vector&lt;u8&gt; {
    self.target_address
}
</code></pre>

Function <code>token_type</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_type">token_type</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a>): u8 {
    self.<a href="../sui_bridge/message#bridge_message_token_type">token_type</a>
}
</code></pre>

Function <code>token_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_amount">token_amount</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">bridge::message::TokenTransferPayload</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_amount">token_amount</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayload">TokenTransferPayload</a>): u64 {
    self.amount
}
</code></pre>

Function <code>timestamp_ms</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">bridge::message::TokenTransferPayloadV2</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a>(self: &<a href="../sui_bridge/message#bridge_message_TokenTransferPayloadV2">TokenTransferPayloadV2</a>): u64 {
    self.<a href="../sui_bridge/message#bridge_message_timestamp_ms">timestamp_ms</a>
}
</code></pre>

Function <code>emergency_op_type</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_type">emergency_op_type</a>(self: &<a href="../sui_bridge/message#bridge_message_EmergencyOp">bridge::message::EmergencyOp</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_type">emergency_op_type</a>(self: &<a href="../sui_bridge/message#bridge_message_EmergencyOp">EmergencyOp</a>): u8 {
    self.op_type
}
</code></pre>

Function <code>blocklist_type</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>(self: &<a href="../sui_bridge/message#bridge_message_Blocklist">bridge::message::Blocklist</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>(self: &<a href="../sui_bridge/message#bridge_message_Blocklist">Blocklist</a>): u8 {
    self.<a href="../sui_bridge/message#bridge_message_blocklist_type">blocklist_type</a>
}
</code></pre>

Function <code>blocklist_validator_addresses</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_blocklist_validator_addresses">blocklist_validator_addresses</a>(self: &<a href="../sui_bridge/message#bridge_message_Blocklist">bridge::message::Blocklist</a>): &vector&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_blocklist_validator_addresses">blocklist_validator_addresses</a>(self: &<a href="../sui_bridge/message#bridge_message_Blocklist">Blocklist</a>): &vector&lt;vector&lt;u8&gt;&gt; {
    &self.validator_eth_addresses
}
</code></pre>

Function <code>update_bridge_limit_payload_sending_chain</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_sending_chain">update_bridge_limit_payload_sending_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">bridge::message::UpdateBridgeLimit</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_sending_chain">update_bridge_limit_payload_sending_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a>): u8 {
    self.sending_chain
}
</code></pre>

Function <code>update_bridge_limit_payload_receiving_chain</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_receiving_chain">update_bridge_limit_payload_receiving_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">bridge::message::UpdateBridgeLimit</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_receiving_chain">update_bridge_limit_payload_receiving_chain</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a>): u8 {
    self.receiving_chain
}
</code></pre>

Function <code>update_bridge_limit_payload_limit</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_limit">update_bridge_limit_payload_limit</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">bridge::message::UpdateBridgeLimit</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_bridge_limit_payload_limit">update_bridge_limit_payload_limit</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateBridgeLimit">UpdateBridgeLimit</a>): u64 {
    self.limit
}
</code></pre>

Function <code>update_asset_price_payload_token_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_asset_price_payload_token_id">update_asset_price_payload_token_id</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">bridge::message::UpdateAssetPrice</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_asset_price_payload_token_id">update_asset_price_payload_token_id</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">UpdateAssetPrice</a>): u8 {
    self.token_id
}
</code></pre>

Function <code>update_asset_price_payload_new_price</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_asset_price_payload_new_price">update_asset_price_payload_new_price</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">bridge::message::UpdateAssetPrice</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_update_asset_price_payload_new_price">update_asset_price_payload_new_price</a>(self: &<a href="../sui_bridge/message#bridge_message_UpdateAssetPrice">UpdateAssetPrice</a>): u64 {
    self.new_price
}
</code></pre>

Function <code>is_native</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_is_native">is_native</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">bridge::message::AddTokenOnSui</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_is_native">is_native</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a>): bool {
    self.native_token
}
</code></pre>

Function <code>token_ids</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">bridge::message::AddTokenOnSui</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a>): vector&lt;u8&gt; {
    self.<a href="../sui_bridge/message#bridge_message_token_ids">token_ids</a>
}
</code></pre>

Function <code>token_type_names</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">bridge::message::AddTokenOnSui</a>): vector&lt;<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a>): vector&lt;String&gt; {
    self.<a href="../sui_bridge/message#bridge_message_token_type_names">token_type_names</a>
}
</code></pre>

Function <code>token_prices</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">bridge::message::AddTokenOnSui</a>): vector&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>(self: &<a href="../sui_bridge/message#bridge_message_AddTokenOnSui">AddTokenOnSui</a>): vector&lt;u64&gt; {
    self.<a href="../sui_bridge/message#bridge_message_token_prices">token_prices</a>
}
</code></pre>

Function <code>emergency_op_pause</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_pause">emergency_op_pause</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_pause">emergency_op_pause</a>(): u8 {
    <a href="../sui_bridge/message#bridge_message_PAUSE">PAUSE</a>
}
</code></pre>

Function <code>emergency_op_unpause</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_unpause">emergency_op_unpause</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_emergency_op_unpause">emergency_op_unpause</a>(): u8 {
    <a href="../sui_bridge/message#bridge_message_UNPAUSE">UNPAUSE</a>
}
</code></pre>

Function <code>required_voting_power</code>

Return the required signature threshold for the message, values are voting power in the scale of 10000

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_required_voting_power">required_voting_power</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_required_voting_power">required_voting_power</a>(self: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): u64 {
    <b>let</b> <a href="../sui_bridge/message#bridge_message_message_type">message_type</a> = <a href="../sui_bridge/message#bridge_message_message_type">message_type</a>(self);
    <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_token">message_types::token</a>()) {
        3334
    } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_emergency_op">message_types::emergency_op</a>()) {
        <b>let</b> <a href="../sui_bridge/message#bridge_message_payload">payload</a> = <a href="../sui_bridge/message#bridge_message_extract_emergency_op_payload">extract_emergency_op_payload</a>(self);
        <b>if</b> (<a href="../sui_bridge/message#bridge_message_payload">payload</a>.op_type == <a href="../sui_bridge/message#bridge_message_PAUSE">PAUSE</a>) {
            450
        } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_payload">payload</a>.op_type == <a href="../sui_bridge/message#bridge_message_UNPAUSE">UNPAUSE</a>) {
            5001
        } <b>else</b> {
            <b>abort</b> <a href="../sui_bridge/message#bridge_message_EInvalidEmergencyOpType">EInvalidEmergencyOpType</a>
        }
    } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_committee_blocklist">message_types::committee_blocklist</a>()) {
        5001
    } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_update_asset_price">message_types::update_asset_price</a>()) {
        5001
    } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_update_bridge_limit">message_types::update_bridge_limit</a>()) {
        5001
    } <b>else</b> <b>if</b> (<a href="../sui_bridge/message#bridge_message_message_type">message_type</a> == <a href="../sui_bridge/message_types#bridge_message_types_add_tokens_on_sui">message_types::add_tokens_on_sui</a>()) {
        5001
    } <b>else</b> {
        <b>abort</b> <a href="../sui_bridge/message#bridge_message_EInvalidMessageType">EInvalidMessageType</a>
    }
}
</code></pre>

Function <code>to_parsed_token_transfer_message</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_to_parsed_token_transfer_message">to_parsed_token_transfer_message</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">bridge::message::BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_ParsedTokenTransferMessage">bridge::message::ParsedTokenTransferMessage</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_to_parsed_token_transfer_message">to_parsed_token_transfer_message</a>(<a href="../sui_bridge/message#bridge_message">message</a>: &<a href="../sui_bridge/message#bridge_message_BridgeMessage">BridgeMessage</a>): <a href="../sui_bridge/message#bridge_message_ParsedTokenTransferMessage">ParsedTokenTransferMessage</a> {
    <b>assert</b>!(<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_message_type">message_type</a>() == <a href="../sui_bridge/message_types#bridge_message_types_token">message_types::token</a>(), <a href="../sui_bridge/message#bridge_message_EMustBeTokenMessage">EMustBeTokenMessage</a>);
    // Handle both V1 and V2 <a href="../sui_bridge/message#bridge_message">message</a> formats
    <b>let</b> parsed_payload = <b>if</b> (<a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_message_version">message_version</a>() == 2) {
        // V2 <a href="../sui_bridge/message#bridge_message_payload">payload</a> <b>has</b> timestamp - extract and convert to V1 format
        <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload_v2">extract_token_bridge_payload_v2</a>().<a href="../sui_bridge/message#bridge_message_to_token_payload_v1">to_token_payload_v1</a>()
    } <b>else</b> {
        // V1 <a href="../sui_bridge/message#bridge_message_payload">payload</a>
        <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_extract_token_bridge_payload">extract_token_bridge_payload</a>()
    };
    <a href="../sui_bridge/message#bridge_message_ParsedTokenTransferMessage">ParsedTokenTransferMessage</a> {
        <a href="../sui_bridge/message#bridge_message_message_version">message_version</a>: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_message_version">message_version</a>(),
        <a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_seq_num">seq_num</a>(),
        <a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_source_chain">source_chain</a>(),
        <a href="../sui_bridge/message#bridge_message_payload">payload</a>: <a href="../sui_bridge/message#bridge_message">message</a>.<a href="../sui_bridge/message#bridge_message_payload">payload</a>(),
        parsed_payload,
    }
}
</code></pre>

Function <code>token_transfer_message_version</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_transfer_message_version">token_transfer_message_version</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/message#bridge_message_token_transfer_message_version">token_transfer_message_version</a>(): u8 {
    <a href="../sui_bridge/message#bridge_message_TOKEN_TRANSFER_MESSAGE_VERSION_V2">TOKEN_TRANSFER_MESSAGE_VERSION_V2</a>
}
</code></pre>

Function <code>reverse_bytes</code>

<code><b>fun</b> <a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(bytes: vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_bridge/message#bridge_message_reverse_bytes">reverse_bytes</a>(<b>mut</b> bytes: vector&lt;u8&gt;): vector&lt;u8&gt; {
    vector::reverse(&<b>mut</b> bytes);
    bytes
}
</code></pre>

Function <code>peel_u64_be</code>

<code><b>fun</b> <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(bcs: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_bridge/message#bridge_message_peel_u64_be">peel_u64_be</a>(bcs: &<b>mut</b> BCS): u64 {
    <b>let</b> (<b>mut</b> value, <b>mut</b> i) = (0u64, 64u8);
    <b>while</b> (i &gt; 0) {
        i = i - 8;
        <b>let</b> byte = (bcs::peel_u8(bcs) <b>as</b> u64);
        value = value + (byte &lt;&lt; i);
    };
    value
}
</code></pre>