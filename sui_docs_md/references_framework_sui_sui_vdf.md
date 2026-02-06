-  [Constants](#@Constants_0)
-  [Function hash_to_input](#sui_vdf_hash_to_input)
-  [Function hash_to_input_internal](#sui_vdf_hash_to_input_internal)
-  [Function vdf_verify](#sui_vdf_vdf_verify)
-  [Function vdf_verify_internal](#sui_vdf_vdf_verify_internal)

<code></code>

Constants

<code><b>const</b> <a href="../sui_sui/vdf#sui_vdf_EInvalidInput">EInvalidInput</a>: u64 = 0;
</code>

Function <code>hash_to_input</code>

Hash an arbitrary binary message to a class group element to be used as input for <a href="../sui_sui/vdf#sui_vdf_vdf_verify">vdf_verify</a>.

This function is currently only enabled on Devnet.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_hash_to_input">hash_to_input</a>(message: &vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_hash_to_input">hash_to_input</a>(message: &vector&lt;u8&gt;): vector&lt;u8&gt; {
    <a href="../sui_sui/vdf#sui_vdf_hash_to_input_internal">hash_to_input_internal</a>(message)
}
</code></pre>

Function <code>hash_to_input_internal</code>

The internal functions for <a href="../sui_sui/vdf#sui_vdf_hash_to_input">hash_to_input</a>.

<code><b>fun</b> <a href="../sui_sui/vdf#sui_vdf_hash_to_input_internal">hash_to_input_internal</a>(message: &vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_hash_to_input_internal">hash_to_input_internal</a>(message: &vector&lt;u8&gt;): vector&lt;u8&gt;;
</code></pre>

Function <code>vdf_verify</code>

Verify the output and proof of a VDF with the given number of iterations. The input, output and proof
are all class group elements represented by triples (a,b,c) such that b^2 - 4ac = discriminant. The are expected
to be encoded as a BCS encoding of a triple of byte arrays, each being the big-endian twos-complement encoding of
a, b and c in that order.

This uses Wesolowski's VDF construction over imaginary class groups as described in Wesolowski (2020),
'Efficient Verifiable Delay Functions.', J. Cryptol. 33, and is compatible with the VDF implementation in
fastcrypto.

The discriminant for the class group is pre-computed and fixed. See how this was generated in the fastcrypto-vdf
crate. The final selection of the discriminant for Mainnet will be computed and announced under a nothing-up-my-sleeve
process.

This function is currently only enabled on Devnet.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_vdf_verify">vdf_verify</a>(input: &vector&lt;u8&gt;, output: &vector&lt;u8&gt;, proof: &vector&lt;u8&gt;, iterations: u64): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_vdf_verify">vdf_verify</a>(
    input: &vector&lt;u8&gt;,
    output: &vector&lt;u8&gt;,
    proof: &vector&lt;u8&gt;,
    iterations: u64,
): bool {
    <a href="../sui_sui/vdf#sui_vdf_vdf_verify_internal">vdf_verify_internal</a>(input, output, proof, iterations)
}
</code></pre>

Function <code>vdf_verify_internal</code>

The internal functions for <a href="../sui_sui/vdf#sui_vdf_vdf_verify_internal">vdf_verify_internal</a>.

<code><b>fun</b> <a href="../sui_sui/vdf#sui_vdf_vdf_verify_internal">vdf_verify_internal</a>(input: &vector&lt;u8&gt;, output: &vector&lt;u8&gt;, proof: &vector&lt;u8&gt;, iterations: u64): bool
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_sui/vdf#sui_vdf_vdf_verify_internal">vdf_verify_internal</a>(
    input: &vector&lt;u8&gt;,
    output: &vector&lt;u8&gt;,
    proof: &vector&lt;u8&gt;,
    iterations: u64,
): bool;
</code></pre>