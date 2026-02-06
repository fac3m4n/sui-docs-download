-  [Constants](#@Constants_0)
-  [Function to_u256](#sui_address_to_u256)
-  [Function from_u256](#sui_address_from_u256)
-  [Function from_bytes](#sui_address_from_bytes)
-  [Function to_bytes](#sui_address_to_bytes)
-  [Function to_ascii_string](#sui_address_to_ascii_string)
-  [Function to_string](#sui_address_to_string)
-  [Function from_ascii_bytes](#sui_address_from_ascii_bytes)
-  [Function hex_char_value](#sui_address_hex_char_value)
-  [Function length](#sui_address_length)
-  [Function max](#sui_address_max)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
</code>

Constants

The length of an address, in bytes

<code><b>const</b> <a href="../sui_sui/address#sui_address_LENGTH">LENGTH</a>: u64 = 32;
</code>

<code><b>const</b> <a href="../sui_sui/address#sui_address_MAX">MAX</a>: u256 = 115792089237316195423570985008687907853269984665640564039457584007913129639935;
</code>

Error from <a href="../sui_sui/address#sui_address_from_bytes">from_bytes</a> when it is supplied too many or too few bytes.

<code><b>const</b> <a href="../sui_sui/address#sui_address_EAddressParseError">EAddressParseError</a>: u64 = 0;
</code>

Function <code>to_u256</code>

Convert a into a u256 by interpreting a as the bytes of a big-endian integer
(e.g., <a href="../sui_sui/address#sui_address_to_u256">to_u256</a>(0x1) == 1)

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_u256">to_u256</a>(a: <b>address</b>): u256
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_u256">to_u256</a>(a: <b>address</b>): u256;
</code></pre>

Function <code>from_u256</code>

Convert n into an address by encoding it as a big-endian integer (e.g., <a href="../sui_sui/address#sui_address_from_u256">from_u256</a>(1) = @0x1)
Aborts if n > MAX_ADDRESS

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_u256">from_u256</a>(n: u256): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_u256">from_u256</a>(n: u256): <b>address</b>;
</code></pre>

Function <code>from_bytes</code>

Convert bytes into an address.
Aborts with <a href="../sui_sui/address#sui_address_EAddressParseError">EAddressParseError</a> if the length of bytes is not 32

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_bytes">from_bytes</a>(bytes: vector&lt;u8&gt;): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_bytes">from_bytes</a>(bytes: vector&lt;u8&gt;): <b>address</b>;
</code></pre>

Function <code>to_bytes</code>

Convert a into BCS-encoded bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_bytes">to_bytes</a>(a: <b>address</b>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_bytes">to_bytes</a>(a: <b>address</b>): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>(&a)
}
</code></pre>

Function <code>to_ascii_string</code>

Convert a to a hex-encoded ASCII string

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_ascii_string">to_ascii_string</a>(a: <b>address</b>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_ascii_string">to_ascii_string</a>(a: <b>address</b>): ascii::String {
    <a href="../sui_sui/hex#sui_hex_encode">hex::encode</a>(<a href="../sui_sui/address#sui_address_to_bytes">to_bytes</a>(a)).<a href="../sui_sui/address#sui_address_to_ascii_string">to_ascii_string</a>()
}
</code></pre>

Function <code>to_string</code>

Convert a to a hex-encoded string

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_string">to_string</a>(a: <b>address</b>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_to_string">to_string</a>(a: <b>address</b>): string::String {
    <a href="../sui_sui/address#sui_address_to_ascii_string">to_ascii_string</a>(a).<a href="../sui_sui/address#sui_address_to_string">to_string</a>()
}
</code></pre>

Function <code>from_ascii_bytes</code>

Converts an ASCII string to an address, taking the numerical value for each character. The
string must be Base16 encoded, and thus exactly 64 characters long.
For example, the string "00000000000000000000000000000000000000000000000000000000DEADB33F"
will be converted to the address @0xDEADB33F.
Aborts with <a href="../sui_sui/address#sui_address_EAddressParseError">EAddressParseError</a> if the length of s is not 64,
or if an invalid character is encountered.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_ascii_bytes">from_ascii_bytes</a>(bytes: &vector&lt;u8&gt;): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_from_ascii_bytes">from_ascii_bytes</a>(bytes: &vector&lt;u8&gt;): <b>address</b> {
    <b>assert</b>!(bytes.<a href="../sui_sui/address#sui_address_length">length</a>() == 64, <a href="../sui_sui/address#sui_address_EAddressParseError">EAddressParseError</a>);
    <b>let</b> <b>mut</b> hex_bytes = vector[];
    <b>let</b> <b>mut</b> i = 0;
    <b>while</b> (i &lt; 64) {
        <b>let</b> hi = <a href="../sui_sui/address#sui_address_hex_char_value">hex_char_value</a>(bytes[i]);
        <b>let</b> lo = <a href="../sui_sui/address#sui_address_hex_char_value">hex_char_value</a>(bytes[i+1]);
        hex_bytes.push_back((hi &lt;&lt; 4) | lo);
        i = i + 2;
    };
    <a href="../sui_sui/address#sui_address_from_bytes">from_bytes</a>(hex_bytes)
}
</code></pre>

Function <code>hex_char_value</code>

<code><b>fun</b> <a href="../sui_sui/address#sui_address_hex_char_value">hex_char_value</a>(c: u8): u8
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/address#sui_address_hex_char_value">hex_char_value</a>(c: u8): u8 {
    <b>if</b> (c &gt;= 48 && c &lt;= 57) c - 48 // 0-9
    <b>else</b> <b>if</b> (c &gt;= 65 && c &lt;= 70) c - 55 // A-F
    <b>else</b> <b>if</b> (c &gt;= 97 && c &lt;= 102) c - 87 // a-f
    <b>else</b> <b>abort</b> <a href="../sui_sui/address#sui_address_EAddressParseError">EAddressParseError</a>
}
</code></pre>

Function <code>length</code>

Length of a Sui address in bytes

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_length">length</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_length">length</a>(): u64 {
    <a href="../sui_sui/address#sui_address_LENGTH">LENGTH</a>
}
</code></pre>

Function <code>max</code>

Largest possible address

<code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_max">max</a>(): u256
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/address#sui_address_max">max</a>(): u256 {
    <a href="../sui_sui/address#sui_address_MAX">MAX</a>
}
</code></pre>