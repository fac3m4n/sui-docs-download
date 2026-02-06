-  [Struct VerifiedID](#sui_zklogin_verified_id_VerifiedID)
-  [Constants](#@Constants_0)
-  [Function owner](#sui_zklogin_verified_id_owner)
-  [Function key_claim_name](#sui_zklogin_verified_id_key_claim_name)
-  [Function key_claim_value](#sui_zklogin_verified_id_key_claim_value)
-  [Function issuer](#sui_zklogin_verified_id_issuer)
-  [Function audience](#sui_zklogin_verified_id_audience)
-  [Function delete](#sui_zklogin_verified_id_delete)
-  [Function verify_zklogin_id](#sui_zklogin_verified_id_verify_zklogin_id)
-  [Function check_zklogin_id](#sui_zklogin_verified_id_check_zklogin_id)
-  [Function check_zklogin_id_internal](#sui_zklogin_verified_id_check_zklogin_id_internal)

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

Struct <code>VerifiedID</code>

Possession of a VerifiedID proves that the user's address was created using zklogin and the given parameters.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
 The ID of this VerifiedID
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_owner">owner</a>: <b>address</b></code>
</dt>
<dd>
 The address this VerifiedID is associated with
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The name of the key claim
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The value of the key claim
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The issuer
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The audience (wallet)
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_EFunctionDisabled">EFunctionDisabled</a>: u64 = 0;
</code>

Function <code>owner</code>

Returns the address associated with the given VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_owner">owner</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_owner">owner</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>): <b>address</b> {
    verified_id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_owner">owner</a>
}
</code></pre>

Function <code>key_claim_name</code>

Returns the name of the key claim associated with the given VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>): &String {
    &verified_id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>
}
</code></pre>

Function <code>key_claim_value</code>

Returns the value of the key claim associated with the given VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>): &String {
    &verified_id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>
}
</code></pre>

Function <code>issuer</code>

Returns the issuer associated with the given VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>): &String {
    &verified_id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>
}
</code></pre>

Function <code>audience</code>

Returns the audience (wallet) associated with the given VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>(verified_id: &<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>): &String {
    &verified_id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>
}
</code></pre>

Function <code>delete</code>

Delete a VerifiedID

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_delete">delete</a>(verified_id: <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">sui::zklogin_verified_id::VerifiedID</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_delete">delete</a>(verified_id: <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a>) {
    <b>let</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_VerifiedID">VerifiedID</a> { id, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_owner">owner</a>: _, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>: _, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>: _, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>: _, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>: _ } =
        verified_id;
    id.<a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_delete">delete</a>();
}
</code></pre>

Function <code>verify_zklogin_id</code>

This function has been disabled.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_verify_zklogin_id">verify_zklogin_id</a>(_key_claim_name: <a href="../sui_std/string#std_string_String">std::string::String</a>, _key_claim_value: <a href="../sui_std/string#std_string_String">std::string::String</a>, _issuer: <a href="../sui_std/string#std_string_String">std::string::String</a>, _audience: <a href="../sui_std/string#std_string_String">std::string::String</a>, _pin_hash: u256, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_verify_zklogin_id">verify_zklogin_id</a>(
    _key_claim_name: String,
    _key_claim_value: String,
    _issuer: String,
    _audience: String,
    _pin_hash: u256,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<b>false</b>, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_EFunctionDisabled">EFunctionDisabled</a>);
}
</code></pre>

Function <code>check_zklogin_id</code>

This function has been disabled.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_check_zklogin_id">check_zklogin_id</a>(_address: <b>address</b>, _key_claim_name: &<a href="../sui_std/string#std_string_String">std::string::String</a>, _key_claim_value: &<a href="../sui_std/string#std_string_String">std::string::String</a>, _issuer: &<a href="../sui_std/string#std_string_String">std::string::String</a>, _audience: &<a href="../sui_std/string#std_string_String">std::string::String</a>, _pin_hash: u256): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_check_zklogin_id">check_zklogin_id</a>(
    _address: <b>address</b>,
    _key_claim_name: &String,
    _key_claim_value: &String,
    _issuer: &String,
    _audience: &String,
    _pin_hash: u256,
): bool {
    <b>assert</b>!(<b>false</b>, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_EFunctionDisabled">EFunctionDisabled</a>);
    <b>false</b>
}
</code></pre>

Function <code>check_zklogin_id_internal</code>

Returns true if <b>address</b> was created using zklogin and the given parameters.

Aborts with EInvalidInput if any of kc_name, kc_value, iss and aud is not a properly encoded UTF-8
string or if the inputs are longer than the allowed upper bounds: kc_name must be at most 32 characters,
kc_value must be at most 115 characters and aud must be at most 145 characters.

<code><b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_check_zklogin_id_internal">check_zklogin_id_internal</a>(<b>address</b>: <b>address</b>, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>: &vector&lt;u8&gt;, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>: &vector&lt;u8&gt;, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>: &vector&lt;u8&gt;, <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>: &vector&lt;u8&gt;, pin_hash: u256): bool
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_check_zklogin_id_internal">check_zklogin_id_internal</a>(
    <b>address</b>: <b>address</b>,
    <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_name">key_claim_name</a>: &vector&lt;u8&gt;,
    <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_key_claim_value">key_claim_value</a>: &vector&lt;u8&gt;,
    <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_issuer">issuer</a>: &vector&lt;u8&gt;,
    <a href="../sui_sui/zklogin_verified_id#sui_zklogin_verified_id_audience">audience</a>: &vector&lt;u8&gt;,
    pin_hash: u256,
): bool;
</code></pre>