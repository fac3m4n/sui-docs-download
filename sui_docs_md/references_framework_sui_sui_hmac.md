-  [Function hmac_sha3_256](#sui_hmac_hmac_sha3_256)

<code></code>

Function <code>hmac_sha3_256</code>

@param key: HMAC key, arbitrary bytes.
@param msg: message to sign, arbitrary bytes.
Returns the 32 bytes digest of HMAC-SHA3-256(key, msg).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/hmac#sui_hmac_hmac_sha3_256">hmac_sha3_256</a>(key: &vector&lt;u8&gt;, msg: &vector&lt;u8&gt;): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/hmac#sui_hmac_hmac_sha3_256">hmac_sha3_256</a>(key: &vector&lt;u8&gt;, msg: &vector&lt;u8&gt;): vector&lt;u8&gt;;
</code></pre>