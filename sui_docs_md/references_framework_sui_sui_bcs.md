This module implements BCS (de)serialization in Move.
Full specification can be found here: https://github.com/diem/bcs

Short summary (for Move-supported types):

- address - sequence of X bytes
- bool - byte with 0 or 1
- u8 - a single u8 byte
- u16 / u32 / u64 / u128 / u256 - LE bytes
- vector - ULEB128 length + LEN elements
- option - first byte bool: None (0) or Some (1), then value

Usage example:
```
/// This function reads u8 and u64 value from the input
/// and returns the rest of the bytes.
fun deserialize(bytes: vector<u8>): (u8, u64, vector<u8>) {
use sui::bcs::{Self, BCS};

let prepared: BCS = bcs::new(bytes);
let (u8_value, u64_value) = (
prepared.peel_u8(),
prepared.peel_u64()
);

// unpack bcs struct
let leftovers = prepared.into_remainder_bytes();

(u8_value, u64_value, leftovers)
}
```

-  [Struct BCS](#sui_bcs_BCS)
-  [Constants](#@Constants_0)
-  [Function to_bytes](#sui_bcs_to_bytes)
-  [Function new](#sui_bcs_new)
-  [Function into_remainder_bytes](#sui_bcs_into_remainder_bytes)
-  [Function peel_address](#sui_bcs_peel_address)
-  [Function peel_bool](#sui_bcs_peel_bool)
-  [Function peel_u8](#sui_bcs_peel_u8)
-  [Macro function peel_num](#sui_bcs_peel_num)
-  [Function peel_u16](#sui_bcs_peel_u16)
-  [Function peel_u32](#sui_bcs_peel_u32)
-  [Function peel_u64](#sui_bcs_peel_u64)
-  [Function peel_u128](#sui_bcs_peel_u128)
-  [Function peel_u256](#sui_bcs_peel_u256)
-  [Function peel_vec_length](#sui_bcs_peel_vec_length)
-  [Macro function peel_vec](#sui_bcs_peel_vec)
-  [Function peel_vec_address](#sui_bcs_peel_vec_address)
-  [Function peel_vec_bool](#sui_bcs_peel_vec_bool)
-  [Function peel_vec_u8](#sui_bcs_peel_vec_u8)
-  [Function peel_vec_vec_u8](#sui_bcs_peel_vec_vec_u8)
-  [Function peel_vec_u16](#sui_bcs_peel_vec_u16)
-  [Function peel_vec_u32](#sui_bcs_peel_vec_u32)
-  [Function peel_vec_u64](#sui_bcs_peel_vec_u64)
-  [Function peel_vec_u128](#sui_bcs_peel_vec_u128)
-  [Function peel_vec_u256](#sui_bcs_peel_vec_u256)
-  [Function peel_enum_tag](#sui_bcs_peel_enum_tag)
-  [Macro function peel_option](#sui_bcs_peel_option)
-  [Function peel_option_address](#sui_bcs_peel_option_address)
-  [Function peel_option_bool](#sui_bcs_peel_option_bool)
-  [Function peel_option_u8](#sui_bcs_peel_option_u8)
-  [Function peel_option_u16](#sui_bcs_peel_option_u16)
-  [Function peel_option_u32](#sui_bcs_peel_option_u32)
-  [Function peel_option_u64](#sui_bcs_peel_option_u64)
-  [Function peel_option_u128](#sui_bcs_peel_option_u128)
-  [Function peel_option_u256](#sui_bcs_peel_option_u256)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
</code>

Struct <code>BCS</code>

A helper struct that saves resources on operations. For better
vector performance, it stores reversed bytes of the BCS and
enables use of vector::pop_back.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>bytes: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

For when bytes length is less than required for deserialization.

<code><b>const</b> <a href="../sui_sui/bcs#sui_bcs_EOutOfRange">EOutOfRange</a>: u64 = 0;
</code>

For when the boolean value different than 0 or 1.

<code><b>const</b> <a href="../sui_sui/bcs#sui_bcs_ENotBool">ENotBool</a>: u64 = 1;
</code>

For when ULEB byte is out of range (or not found).

<code><b>const</b> <a href="../sui_sui/bcs#sui_bcs_ELenOutOfRange">ELenOutOfRange</a>: u64 = 2;
</code>

Function <code>to_bytes</code>

Get BCS serialized bytes for any value.
Re-exports stdlib <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_to_bytes">to_bytes</a>&lt;T&gt;(value: &T): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_to_bytes">to_bytes</a>&lt;T&gt;(value: &T): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs_to_bytes">bcs::to_bytes</a>(value)
}
</code></pre>

Function <code>new</code>

Creates a new instance of BCS wrapper that holds inversed
bytes for better performance.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_new">new</a>(bytes: vector&lt;u8&gt;): <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_new">new</a>(<b>mut</b> bytes: vector&lt;u8&gt;): <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a> {
    bytes.reverse();
    <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a> { bytes }
}
</code></pre>

Function <code>into_remainder_bytes</code>

Unpack the <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a> struct returning the leftover bytes.
Useful for passing the data further after partial deserialization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_into_remainder_bytes">into_remainder_bytes</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_into_remainder_bytes">into_remainder_bytes</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u8&gt; {
    <b>let</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a> { <b>mut</b> bytes } = <a href="../sui_sui/bcs#sui_bcs">bcs</a>;
    bytes.reverse();
    bytes
}
</code></pre>

Function <code>peel_address</code>

Read address from the bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_address">peel_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_address">peel_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): <b>address</b> {
    <b>assert</b>!(<a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.length() &gt;= <a href="../sui_sui/address#sui_address_length">address::length</a>(), <a href="../sui_sui/bcs#sui_bcs_EOutOfRange">EOutOfRange</a>);
    <a href="../sui_sui/address#sui_address_from_bytes">address::from_bytes</a>(vector::tabulate!(<a href="../sui_sui/address#sui_address_length">address::length</a>(), |_| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.pop_back()))
}
</code></pre>

Function <code>peel_bool</code>

Read a bool value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_bool">peel_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_bool">peel_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): bool {
    <b>let</b> value = <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u8">peel_u8</a>();
    <b>if</b> (value == 0) <b>false</b>
    <b>else</b> <b>if</b> (value == 1) <b>true</b>
    <b>else</b> <b>abort</b> <a href="../sui_sui/bcs#sui_bcs_ENotBool">ENotBool</a>
}
</code></pre>

Function <code>peel_u8</code>

Read u8 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u8">peel_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u8">peel_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u8 {
    <b>assert</b>!(<a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.length() &gt;= 1, <a href="../sui_sui/bcs#sui_bcs_EOutOfRange">EOutOfRange</a>);
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.pop_back()
}
</code></pre>

Macro function <code>peel_num</code>

<code><b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>&lt;$I, $T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>, $len: u64, $bits: $I): $T
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>&lt;$I, $T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>, $len: u64, $bits: $I): $T {
    <b>let</b> <a href="../sui_sui/bcs#sui_bcs">bcs</a> = $<a href="../sui_sui/bcs#sui_bcs">bcs</a>;
    <b>assert</b>!(<a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.length() &gt;= $len, <a href="../sui_sui/bcs#sui_bcs_EOutOfRange">EOutOfRange</a>);
    <b>let</b> <b>mut</b> value: $T = 0;
    <b>let</b> <b>mut</b> i: $I = 0;
    <b>let</b> bits = $bits;
    <b>while</b> (i &lt; bits) {
        <b>let</b> byte = <a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.pop_back() <b>as</b> $T;
        value = value + (byte &lt;&lt; (i <b>as</b> u8));
        i = i + 8;
    };
    value
}
</code></pre>

Function <code>peel_u16</code>

Read u16 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u16">peel_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u16
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u16">peel_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u16 {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>!(2, 16u8)
}
</code></pre>

Function <code>peel_u32</code>

Read u32 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u32">peel_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u32
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u32">peel_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u32 {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>!(4, 32u8)
}
</code></pre>

Function <code>peel_u64</code>

Read u64 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u64">peel_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u64">peel_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u64 {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>!(8, 64u8)
}
</code></pre>

Function <code>peel_u128</code>

Read u128 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u128">peel_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u128
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u128">peel_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u128 {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>!(16, 128u8)
}
</code></pre>

Function <code>peel_u256</code>

Read u256 value from bcs-serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u256">peel_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u256
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_u256">peel_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u256 {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_num">peel_num</a>!(32, 256u16)
}
</code></pre>

Function <code>peel_vec_length</code>

Read ULEB bytes expecting a vector length. Result should
then be used to perform peel_* operation LEN times.

In BCS vector length is implemented with ULEB128;
See more here: https://en.wikipedia.org/wiki/LEB128

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_length">peel_vec_length</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_length">peel_vec_length</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u64 {
    <b>let</b> (<b>mut</b> total, <b>mut</b> shift, <b>mut</b> len) = (0u64, 0u8, 0u64);
    <b>loop</b> {
        <b>assert</b>!(len &lt;= 4, <a href="../sui_sui/bcs#sui_bcs_ELenOutOfRange">ELenOutOfRange</a>);
        <b>let</b> byte = <a href="../sui_sui/bcs#sui_bcs">bcs</a>.bytes.pop_back() <b>as</b> u64;
        len = len + 1;
        total = total | ((byte & 0x7f) &lt;&lt; shift);
        <b>if</b> ((byte & 0x80) == 0) <b>break</b>;
        shift = shift + 7;
    };
    total
}
</code></pre>

Macro function <code>peel_vec</code>

Peel vector&lt;$T&gt; from serialized bytes, where $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>| -&gt; $T gives the
functionality of peeling each value.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>&lt;$T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>, $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>| -&gt; $T): vector&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>&lt;$T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>, $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>| -&gt; $T): vector&lt;$T&gt; {
    <b>let</b> <a href="../sui_sui/bcs#sui_bcs">bcs</a> = $<a href="../sui_sui/bcs#sui_bcs">bcs</a>;
    vector::tabulate!(<a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec_length">peel_vec_length</a>(), |_| $peel(<a href="../sui_sui/bcs#sui_bcs">bcs</a>))
}
</code></pre>

Function <code>peel_vec_address</code>

Peel a vector of <b>address</b> from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_address">peel_vec_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_address">peel_vec_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;<b>address</b>&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_address">peel_address</a>())
}
</code></pre>

Function <code>peel_vec_bool</code>

Peel a vector of <b>address</b> from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_bool">peel_vec_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;bool&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_bool">peel_vec_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;bool&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_bool">peel_bool</a>())
}
</code></pre>

Function <code>peel_vec_u8</code>

Peel a vector of u8 (eg string) from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u8">peel_vec_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u8">peel_vec_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u8">peel_u8</a>())
}
</code></pre>

Function <code>peel_vec_vec_u8</code>

Peel a vector&lt;vector&lt;u8&gt;&gt; (eg vec of string) from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_vec_u8">peel_vec_vec_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_vec_u8">peel_vec_vec_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;vector&lt;u8&gt;&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec_u8">peel_vec_u8</a>())
}
</code></pre>

Function <code>peel_vec_u16</code>

Peel a vector of u16 from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u16">peel_vec_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u16&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u16">peel_vec_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u16&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u16">peel_u16</a>())
}
</code></pre>

Function <code>peel_vec_u32</code>

Peel a vector of u32 from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u32">peel_vec_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u32&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u32">peel_vec_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u32&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u32">peel_u32</a>())
}
</code></pre>

Function <code>peel_vec_u64</code>

Peel a vector of u64 from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u64">peel_vec_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u64">peel_vec_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u64&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u64">peel_u64</a>())
}
</code></pre>

Function <code>peel_vec_u128</code>

Peel a vector of u128 from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u128">peel_vec_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u128&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u128">peel_vec_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u128&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u128">peel_u128</a>())
}
</code></pre>

Function <code>peel_vec_u256</code>

Peel a vector of u256 from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u256">peel_vec_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): vector&lt;u256&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_vec_u256">peel_vec_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): vector&lt;u256&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec">peel_vec</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u256">peel_u256</a>())
}
</code></pre>

Function <code>peel_enum_tag</code>

Peel enum from serialized bytes, where $f takes a tag value and returns
the corresponding enum variant. Move enums are limited to 127 variants,
however the tag can be any u32 value.

Example:
```rust
let my_enum = match (bcs.peel_enum_tag()) {
0 => Enum::Empty,
1 => Enum::U8(bcs.peel_u8()),
2 => Enum::U16(bcs.peel_u16()),
3 => Enum::Struct { a: bcs.peel_address(), b: bcs.peel_u8() },
_ => abort,
};
```

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_enum_tag">peel_enum_tag</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): u32
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_enum_tag">peel_enum_tag</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): u32 {
    <b>let</b> tag = <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_vec_length">peel_vec_length</a>();
    <b>assert</b>!(tag &lt;= <a href="../sui_std/u32#std_u32_max_value">std::u32::max_value</a>!() <b>as</b> u64, <a href="../sui_sui/bcs#sui_bcs_EOutOfRange">EOutOfRange</a>);
    tag <b>as</b> u32
}
</code></pre>

Macro function <code>peel_option</code>

Peel Option&lt;$T&gt; from serialized bytes, where $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>| -&gt; $T gives the
functionality of peeling the inner value.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>&lt;$T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>, $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>| -&gt; $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>&lt;$T&gt;($<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>, $peel: |&<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>| -&gt; $T): Option&lt;$T&gt; {
    <b>let</b> <a href="../sui_sui/bcs#sui_bcs">bcs</a> = $<a href="../sui_sui/bcs#sui_bcs">bcs</a>;
    <b>if</b> (<a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_bool">peel_bool</a>()) option::some($peel(<a href="../sui_sui/bcs#sui_bcs">bcs</a>)) <b>else</b> option::none()
}
</code></pre>

Function <code>peel_option_address</code>

Peel Option&lt;<b>address</b>&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_address">peel_option_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_address">peel_option_address</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;<b>address</b>&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_address">peel_address</a>())
}
</code></pre>

Function <code>peel_option_bool</code>

Peel Option&lt;bool&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_bool">peel_option_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;bool&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_bool">peel_option_bool</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;bool&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_bool">peel_bool</a>())
}
</code></pre>

Function <code>peel_option_u8</code>

Peel Option&lt;u8&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u8">peel_option_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u8">peel_option_u8</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u8&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u8">peel_u8</a>())
}
</code></pre>

Function <code>peel_option_u16</code>

Peel Option&lt;u16&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u16">peel_option_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u16&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u16">peel_option_u16</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u16&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u16">peel_u16</a>())
}
</code></pre>

Function <code>peel_option_u32</code>

Peel Option&lt;u32&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u32">peel_option_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u32&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u32">peel_option_u32</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u32&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u32">peel_u32</a>())
}
</code></pre>

Function <code>peel_option_u64</code>

Peel Option&lt;u64&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u64">peel_option_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u64">peel_option_u64</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u64&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u64">peel_u64</a>())
}
</code></pre>

Function <code>peel_option_u128</code>

Peel Option&lt;u128&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u128">peel_option_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u128&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u128">peel_option_u128</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u128&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u128">peel_u128</a>())
}
</code></pre>

Function <code>peel_option_u256</code>

Peel Option&lt;u256&gt; from serialized bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u256">peel_option_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">sui::bcs::BCS</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u256&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/bcs#sui_bcs_peel_option_u256">peel_option_u256</a>(<a href="../sui_sui/bcs#sui_bcs">bcs</a>: &<b>mut</b> <a href="../sui_sui/bcs#sui_bcs_BCS">BCS</a>): Option&lt;u256&gt; {
    <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_option">peel_option</a>!(|<a href="../sui_sui/bcs#sui_bcs">bcs</a>| <a href="../sui_sui/bcs#sui_bcs">bcs</a>.<a href="../sui_sui/bcs#sui_bcs_peel_u256">peel_u256</a>())
}
</code></pre>