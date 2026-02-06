-  [Function ed25519_verify](#sui_ed25519_ed25519_verify)

<code></code>

Function <code>ed25519_verify</code>

@param signature: 32-byte signature that is a point on the Ed25519 elliptic curve.
@param public_key: 32-byte signature that is a point on the Ed25519 elliptic curve.
@param msg: The message that we test the signature against.

If the signature is a valid Ed25519 signature of the message and public key, return true.
Otherwise, return false.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/ed25519#sui_ed25519_ed25519_verify">ed25519_verify</a>(signature: &vector&lt;u8&gt;, public_key: &vector&lt;u8&gt;, msg: &vector&lt;u8&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/ed25519#sui_ed25519_ed25519_verify">ed25519_verify</a>(
    signature: &vector&lt;u8&gt;,
    public_key: &vector&lt;u8&gt;,
    msg: &vector&lt;u8&gt;,
): bool;
</code></pre>