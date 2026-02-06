Module which defines hash functions. Note that Sha-256 and Sha3-256 is available in the std::hash module in the
standard library.

-  [Function blake2b256](#sui_hash_blake2b256)
-  [Function keccak256](#sui_hash_keccak256)

<code></code>

Function <code>blake2b256</code>

@param data: Arbitrary binary data to hash
Hash the input bytes using Blake2b-256 and returns 32 bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/hash#sui_hash_blake2b256">blake2b256</a>(data: &vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/hash#sui_hash_blake2b256">blake2b256</a>(data: &vector&lt;u8&gt;): vector&lt;u8&gt;;
</code></pre>

Function <code>keccak256</code>

@param data: Arbitrary binary data to hash
Hash the input bytes using keccak256 and returns 32 bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/hash#sui_hash_keccak256">keccak256</a>(data: &vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/hash#sui_hash_keccak256">keccak256</a>(data: &vector&lt;u8&gt;): vector&lt;u8&gt;;
</code></pre>