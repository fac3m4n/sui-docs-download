Defines an unsigned, fixed-point numeric type with a 64-bit integer part and a 64-bit fractional
part. The notation <a href="../sui_std/uq64_64#std_uq64_64">uq64_64</a> and <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> is based on
[Q notation](https://en.wikipedia.org/wiki/Q_(number_format)). q indicates it a fixed-point
number. The u prefix indicates it is unsigned. The 64_64 suffix indicates the number of
bits, where the first number indicates the number of bits in the integer part, and the second
the number of bits in the fractional part--in this case 64 bits for each.

-  [Struct UQ64_64](#std_uq64_64_UQ64_64)
-  [Constants](#@Constants_0)
-  [Function from_quotient](#std_uq64_64_from_quotient)
-  [Function from_int](#std_uq64_64_from_int)
-  [Function add](#std_uq64_64_add)
-  [Function sub](#std_uq64_64_sub)
-  [Function mul](#std_uq64_64_mul)
-  [Function div](#std_uq64_64_div)
-  [Function to_int](#std_uq64_64_to_int)
-  [Function int_mul](#std_uq64_64_int_mul)
-  [Function int_div](#std_uq64_64_int_div)
-  [Function le](#std_uq64_64_le)
-  [Function lt](#std_uq64_64_lt)
-  [Function ge](#std_uq64_64_ge)
-  [Function gt](#std_uq64_64_gt)
-  [Function to_raw](#std_uq64_64_to_raw)
-  [Function from_raw](#std_uq64_64_from_raw)

<code></code>

Struct <code>UQ64_64</code>

A fixed-point numeric type with 64 integer bits and 64 fractional bits, represented by an
underlying 128 bit value. This is a binary representation, so decimal values may not be exactly
representable, but it provides more than 19 decimal digits of precision both before and after
the decimal point (38 digits total).

<code><b>public</b> <b>struct</b> <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>0: <a href="../sui_std/u128#std_u128">u128</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

<code>#[error]
<b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_EDenominator">EDenominator</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; = b"Quotient specified with a zero denominator";
</code>

<code>#[error]
<b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_EQuotientTooSmall">EQuotientTooSmall</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; = b"Quotient specified is too small, and is outside of the supported range";
</code>

<code>#[error]
<b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_EQuotientTooLarge">EQuotientTooLarge</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; = b"Quotient specified is too large, and is outside of the supported range";
</code>

<code>#[error]
<b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_EOverflow">EOverflow</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; = b"Overflow from an arithmetic operation";
</code>

<code>#[error]
<b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_EDivisionByZero">EDivisionByZero</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; = b"Division by zero";
</code>

The total number of bits in the fixed-point number. Used in <b>macro</b> invocations.

<code><b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_TOTAL_BITS">TOTAL_BITS</a>: <a href="../sui_std/u8#std_u8">u8</a> = 128;
</code>

The number of fractional bits in the fixed-point number. Used in <b>macro</b> invocations.

<code><b>const</b> <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>: <a href="../sui_std/u8#std_u8">u8</a> = 64;
</code>

Function <code>from_quotient</code>

Create a fixed-point value from a quotient specified by its numerator and denominator.
<a href="../sui_std/uq64_64#std_uq64_64_from_quotient">from_quotient</a> and <a href="../sui_std/uq64_64#std_uq64_64_from_int">from_int</a> should be preferred over using <a href="../sui_std/uq64_64#std_uq64_64_from_raw">from_raw</a>.
Unless the denominator is a power of two, fractions can not be represented accurately,
so be careful about rounding errors.
Aborts if the denominator is zero.
Aborts if the input is non-zero but so small that it will be represented as zero, e.g. smaller
than 2^{-64}.
Aborts if the input is too large, e.g. larger than or equal to 2^64.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_quotient">from_quotient</a>(numerator: <a href="../sui_std/u128#std_u128">u128</a>, denominator: <a href="../sui_std/u128#std_u128">u128</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_quotient">from_quotient</a>(numerator: <a href="../sui_std/u128#std_u128">u128</a>, denominator: <a href="../sui_std/u128#std_u128">u128</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(
        <a href="../sui_std/macros#std_macros_uq_from_quotient">std::macros::uq_from_quotient</a>!&lt;<a href="../sui_std/u128#std_u128">u128</a>, <a href="../sui_std/u256#std_u256">u256</a>&gt;(
            numerator,
            denominator,
            <a href="../sui_std/u128#std_u128_max_value">std::u128::max_value</a>!(),
            <a href="../sui_std/uq64_64#std_uq64_64_TOTAL_BITS">TOTAL_BITS</a>,
            <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>,
            <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EDenominator">EDenominator</a>,
            <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EQuotientTooSmall">EQuotientTooSmall</a>,
            <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EQuotientTooLarge">EQuotientTooLarge</a>,
        ),
    )
}
</code></pre>

Function <code>from_int</code>

Create a fixed-point value from an integer.
<a href="../sui_std/uq64_64#std_uq64_64_from_int">from_int</a> and <a href="../sui_std/uq64_64#std_uq64_64_from_quotient">from_quotient</a> should be preferred over using <a href="../sui_std/uq64_64#std_uq64_64_from_raw">from_raw</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_int">from_int</a>(integer: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_int">from_int</a>(integer: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(<a href="../sui_std/macros#std_macros_uq_from_int">std::macros::uq_from_int</a>!(integer, <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>))
}
</code></pre>

Function <code>add</code>

Add two fixed-point numbers, a + b.
Aborts if the sum overflows.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_add">add</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_add">add</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(<a href="../sui_std/macros#std_macros_uq_add">std::macros::uq_add</a>!&lt;<a href="../sui_std/u128#std_u128">u128</a>, <a href="../sui_std/u256#std_u256">u256</a>&gt;(a.0, b.0, <a href="../sui_std/u128#std_u128_max_value">std::u128::max_value</a>!(), <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EOverflow">EOverflow</a>))
}
</code></pre>

Function <code>sub</code>

Subtract two fixed-point numbers, a - b.
Aborts if a &lt; b.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_sub">sub</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_sub">sub</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(<a href="../sui_std/macros#std_macros_uq_sub">std::macros::uq_sub</a>!(a.0, b.0, <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EOverflow">EOverflow</a>))
}
</code></pre>

Function <code>mul</code>

Multiply two fixed-point numbers, truncating any fractional part of the product.
Aborts if the product overflows.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_mul">mul</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_mul">mul</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(<a href="../sui_std/uq64_64#std_uq64_64_int_mul">int_mul</a>(a.0, b))
}
</code></pre>

Function <code>div</code>

Divide two fixed-point numbers, truncating any fractional part of the quotient.
Aborts if the divisor is zero.
Aborts if the quotient overflows.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_div">div</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_div">div</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(<a href="../sui_std/uq64_64#std_uq64_64_int_div">int_div</a>(a.0, b))
}
</code></pre>

Function <code>to_int</code>

Convert a fixed-point number to an integer, truncating any fractional part.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_to_int">to_int</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_to_int">to_int</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    <a href="../sui_std/macros#std_macros_uq_to_int">std::macros::uq_to_int</a>!(a.0, <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>)
}
</code></pre>

Function <code>int_mul</code>

Multiply a <a href="../sui_std/u128#std_u128">u128</a> integer by a fixed-point number, truncating any fractional part of the product.
Aborts if the product overflows.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_int_mul">int_mul</a>(val: <a href="../sui_std/u128#std_u128">u128</a>, multiplier: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_int_mul">int_mul</a>(val: <a href="../sui_std/u128#std_u128">u128</a>, multiplier: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a> {
    <a href="../sui_std/macros#std_macros_uq_int_mul">std::macros::uq_int_mul</a>!&lt;<a href="../sui_std/u128#std_u128">u128</a>, <a href="../sui_std/u256#std_u256">u256</a>&gt;(
        val,
        multiplier.0,
        <a href="../sui_std/u128#std_u128_max_value">std::u128::max_value</a>!(),
        <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>,
        <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EOverflow">EOverflow</a>,
    )
}
</code></pre>

Function <code>int_div</code>

Divide a <a href="../sui_std/u128#std_u128">u128</a> integer by a fixed-point number, truncating any fractional part of the quotient.
Aborts if the divisor is zero.
Aborts if the quotient overflows.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_int_div">int_div</a>(val: <a href="../sui_std/u128#std_u128">u128</a>, divisor: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_int_div">int_div</a>(val: <a href="../sui_std/u128#std_u128">u128</a>, divisor: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a> {
    <a href="../sui_std/macros#std_macros_uq_int_div">std::macros::uq_int_div</a>!&lt;<a href="../sui_std/u128#std_u128">u128</a>, <a href="../sui_std/u256#std_u256">u256</a>&gt;(
        val,
        divisor.0,
        <a href="../sui_std/u128#std_u128_max_value">std::u128::max_value</a>!(),
        <a href="../sui_std/uq64_64#std_uq64_64_FRACTIONAL_BITS">FRACTIONAL_BITS</a>,
        <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EDivisionByZero">EDivisionByZero</a>,
        <b>abort</b> <a href="../sui_std/uq64_64#std_uq64_64_EOverflow">EOverflow</a>,
    )
}
</code></pre>

Function <code>le</code>

Less than or equal to. Returns <b>true</b> if and only if a &lt;= b.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_le">le</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_le">le</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    a.0 &lt;= b.0
}
</code></pre>

Function <code>lt</code>

Less than. Returns <b>true</b> if and only if a &lt; b.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_lt">lt</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_lt">lt</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    a.0 &lt; b.0
}
</code></pre>

Function <code>ge</code>

Greater than or equal to. Returns <b>true</b> if and only if a &gt;= b.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_ge">ge</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_ge">ge</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    a.0 &gt;= b.0
}
</code></pre>

Function <code>gt</code>

Greater than. Returns <b>true</b> if and only if a &gt; b.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_gt">gt</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_gt">gt</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>, b: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    a.0 &gt; b.0
}
</code></pre>

Function <code>to_raw</code>

Accessor for the raw u128 value. Can be paired with <a href="../sui_std/uq64_64#std_uq64_64_from_raw">from_raw</a> to perform less common operations
on the raw values directly.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_to_raw">to_raw</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_to_raw">to_raw</a>(a: <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>): <a href="../sui_std/u128#std_u128">u128</a> {
    a.0
}
</code></pre>

Function <code>from_raw</code>

Accessor for the raw u128 value. Can be paired with <a href="../sui_std/uq64_64#std_uq64_64_to_raw">to_raw</a> to perform less common operations
on the raw values directly.

<code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_raw">from_raw</a>(raw_value: <a href="../sui_std/u128#std_u128">u128</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">std::uq64_64::UQ64_64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/uq64_64#std_uq64_64_from_raw">from_raw</a>(raw_value: <a href="../sui_std/u128#std_u128">u128</a>): <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a> {
    <a href="../sui_std/uq64_64#std_uq64_64_UQ64_64">UQ64_64</a>(raw_value)
}
</code></pre>