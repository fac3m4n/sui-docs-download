-  [Constants](#@Constants_0)
-  [Function secp256r1_ecrecover](#sui_ecdsa_r1_secp256r1_ecrecover)
-  [Function secp256r1_verify](#sui_ecdsa_r1_secp256r1_verify)

<code></code>

Constants

Error if the public key cannot be recovered from the signature.

<code><b>const</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_EFailToRecoverPubKey">EFailToRecoverPubKey</a>: u64 = 0;
</code>

Error if the signature is invalid.

<code><b>const</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_EInvalidSignature">EInvalidSignature</a>: u64 = 1;
</code>

Hash function name that are valid for ecrecover and secp256k1_verify.

<code><b>const</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_KECCAK256">KECCAK256</a>: u8 = 0;
</code>

<code><b>const</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_SHA256">SHA256</a>: u8 = 1;
</code>

Function <code>secp256r1_ecrecover</code>

@param signature: A 65-bytes signature in form (r, s, v) that is signed using
Secp256r1. Reference implementation on signature generation using RFC6979:
https://github.com/MystenLabs/fastcrypto/blob/74aec4886e62122a5b769464c2bea5f803cf8ecc/fastcrypto/src/secp256r1/mod.rs
The accepted v values are {0, 1, 2, 3}.
@param msg: The message that the signature is signed against, this is raw message without hashing.
@param hash: The u8 representing the name of hash function used to hash the message when signing.

If the signature is valid, return the corresponding recovered Secpk256r1 public
key, otherwise throw error. This is similar to ecrecover in Ethereum, can only be
applied to Secp256r1 signatures. May fail with <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_EFailToRecoverPubKey">EFailToRecoverPubKey</a> or <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_EInvalidSignature">EInvalidSignature</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_secp256r1_ecrecover">secp256r1_ecrecover</a>(signature: &vector&lt;u8&gt;, msg: &vector&lt;u8&gt;, <a href="../sui_sui/hash#sui_hash">hash</a>: u8): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_secp256r1_ecrecover">secp256r1_ecrecover</a>(
    signature: &vector&lt;u8&gt;,
    msg: &vector&lt;u8&gt;,
    <a href="../sui_sui/hash#sui_hash">hash</a>: u8,
): vector&lt;u8&gt;;
</code></pre>

Function <code>secp256r1_verify</code>

@param signature: A 64-bytes signature in form (r, s) that is signed using
Secp256r1. This is an non-recoverable signature without recovery id.
Reference implementation on signature generation using RFC6979:
https://github.com/MystenLabs/fastcrypto/blob/74aec4886e62122a5b769464c2bea5f803cf8ecc/fastcrypto/src/secp256r1/mod.rs
@param public_key: The public key to verify the signature against
@param msg: The message that the signature is signed against, this is raw message without hashing.
@param hash: The u8 representing the name of hash function used to hash the message when signing.

If the signature is valid to the pubkey and hashed message, return true. Else false.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_secp256r1_verify">secp256r1_verify</a>(signature: &vector&lt;u8&gt;, public_key: &vector&lt;u8&gt;, msg: &vector&lt;u8&gt;, <a href="../sui_sui/hash#sui_hash">hash</a>: u8): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/ecdsa_r1#sui_ecdsa_r1_secp256r1_verify">secp256r1_verify</a>(
    signature: &vector&lt;u8&gt;,
    public_key: &vector&lt;u8&gt;,
    msg: &vector&lt;u8&gt;,
    <a href="../sui_sui/hash#sui_hash">hash</a>: u8,
): bool;
</code></pre>