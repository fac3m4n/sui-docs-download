-  [Struct VerifiedIssuer](#sui_zklogin_verified_issuer_VerifiedIssuer)
-  [Constants](#@Constants_0)
-  [Function owner](#sui_zklogin_verified_issuer_owner)
-  [Function issuer](#sui_zklogin_verified_issuer_issuer)
-  [Function delete](#sui_zklogin_verified_issuer_delete)
-  [Function verify_zklogin_issuer](#sui_zklogin_verified_issuer_verify_zklogin_issuer)
-  [Function check_zklogin_issuer](#sui_zklogin_verified_issuer_check_zklogin_issuer)
-  [Function check_zklogin_issuer_internal](#sui_zklogin_verified_issuer_check_zklogin_issuer_internal)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>VerifiedIssuer</code>

Possession of a VerifiedIssuer proves that the user's address was created using zklogin and with the given issuer
(identity provider).

<code><b>public</b> <b>struct</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
 The ID of this VerifiedIssuer
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>: <b>address</b></code>
</dt>
<dd>
 The address this VerifiedID is associated with
</dd>
<dt>
<code><a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The issuer
</dd>
</dl>

Constants

Error if the proof consisting of the inputs provided to the verification function is invalid.

<code><b>const</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_EInvalidInput">EInvalidInput</a>: u64 = 0;
</code>

Error if the proof consisting of the inputs provided to the verification function is invalid.

<code><b>const</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_EInvalidProof">EInvalidProof</a>: u64 = 1;
</code>

Function <code>owner</code>

Returns the address associated with the given VerifiedIssuer

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>(verified_issuer: &<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">sui::zklogin_verified_issuer::VerifiedIssuer</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>(verified_issuer: &<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a>): <b>address</b> {
    verified_issuer.<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>
}
</code></pre>

Function <code>issuer</code>

Returns the issuer associated with the given VerifiedIssuer

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>(verified_issuer: &<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">sui::zklogin_verified_issuer::VerifiedIssuer</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>(verified_issuer: &<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a>): &String {
    &verified_issuer.<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>
}
</code></pre>

Function <code>delete</code>

Delete a VerifiedIssuer

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_delete">delete</a>(verified_issuer: <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">sui::zklogin_verified_issuer::VerifiedIssuer</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_delete">delete</a>(verified_issuer: <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a>) {
    <b>let</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a> { id, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>: _, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: _ } = verified_issuer;
    id.<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_delete">delete</a>();
}
</code></pre>

Function <code>verify_zklogin_issuer</code>

Verify that the caller's address was created using zklogin with the given issuer. If so, a VerifiedIssuer object
with the issuers id transferred to the caller.

Aborts with <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_EInvalidProof">EInvalidProof</a> if the verification fails.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_verify_zklogin_issuer">verify_zklogin_issuer</a>(address_seed: u256, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_verify_zklogin_issuer">verify_zklogin_issuer</a>(address_seed: u256, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: String, ctx: &<b>mut</b> TxContext) {
    <b>let</b> sender = ctx.sender();
    <b>assert</b>!(<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer">check_zklogin_issuer</a>(sender, address_seed, &<a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>), <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_EInvalidProof">EInvalidProof</a>);
    <a href="../sui_sui/transfer#sui_transfer_transfer">transfer::transfer</a>(
        <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_VerifiedIssuer">VerifiedIssuer</a> {
            id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
            <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_owner">owner</a>: sender,
            <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>,
        },
        sender,
    )
}
</code></pre>

Function <code>check_zklogin_issuer</code>

Returns true if <b>address</b> was created using zklogin with the given issuer and address seed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer">check_zklogin_issuer</a>(<b>address</b>: <b>address</b>, address_seed: u256, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: &<a href="../sui_std/string#std_string_String">std::string::String</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer">check_zklogin_issuer</a>(<b>address</b>: <b>address</b>, address_seed: u256, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: &String): bool {
    <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer_internal">check_zklogin_issuer_internal</a>(<b>address</b>, address_seed, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>.as_bytes())
}
</code></pre>

Function <code>check_zklogin_issuer_internal</code>

Returns true if <b>address</b> was created using zklogin with the given issuer and address seed.

Aborts with <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_EInvalidInput">EInvalidInput</a> if the iss input is not a valid UTF-8 string.

<code><b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer_internal">check_zklogin_issuer_internal</a>(<b>address</b>: <b>address</b>, address_seed: u256, <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: &vector&lt;u8&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_check_zklogin_issuer_internal">check_zklogin_issuer_internal</a>(
    <b>address</b>: <b>address</b>,
    address_seed: u256,
    <a href="../sui_sui/zklogin_verified_issuer#sui_zklogin_verified_issuer_issuer">issuer</a>: &vector&lt;u8&gt;,
): bool;
</code></pre>