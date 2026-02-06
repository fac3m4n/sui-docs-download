-  [Constants](#@Constants_0)
-  [Function ecvrf_verify](#sui_ecvrf_ecvrf_verify)

<code></code>

Constants

<code><b>const</b> <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidHashLength">EInvalidHashLength</a>: u64 = 1;
</code>

<code><b>const</b> <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidPublicKeyEncoding">EInvalidPublicKeyEncoding</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidProofEncoding">EInvalidProofEncoding</a>: u64 = 3;
</code>

Function <code>ecvrf_verify</code>

@param hash: The hash/output from a ECVRF to be verified.
@param alpha_string: Input/seed to the ECVRF used to generate the output.
@param public_key: The public key corresponding to the private key used to generate the output.
@param proof: The proof of validity of the output.
Verify a proof for a Ristretto ECVRF. Returns true if the proof is valid and corresponds to the given output. May abort with <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidHashLength">EInvalidHashLength</a>, <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidPublicKeyEncoding">EInvalidPublicKeyEncoding</a> or <a href="../sui_sui/ecvrf#sui_ecvrf_EInvalidProofEncoding">EInvalidProofEncoding</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/ecvrf#sui_ecvrf_ecvrf_verify">ecvrf_verify</a>(<a href="../sui_sui/hash#sui_hash">hash</a>: &vector&lt;u8&gt;, alpha_string: &vector&lt;u8&gt;, public_key: &vector&lt;u8&gt;, proof: &vector&lt;u8&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/ecvrf#sui_ecvrf_ecvrf_verify">ecvrf_verify</a>(
    <a href="../sui_sui/hash#sui_hash">hash</a>: &vector&lt;u8&gt;,
    alpha_string: &vector&lt;u8&gt;,
    public_key: &vector&lt;u8&gt;,
    proof: &vector&lt;u8&gt;,
): bool;
</code></pre>