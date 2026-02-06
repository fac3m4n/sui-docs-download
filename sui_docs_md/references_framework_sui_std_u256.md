-  [Function bitwise_not](#std_u256_bitwise_not)
-  [Function max](#std_u256_max)
-  [Function min](#std_u256_min)
-  [Function diff](#std_u256_diff)
-  [Function divide_and_round_up](#std_u256_divide_and_round_up)
-  [Function pow](#std_u256_pow)
-  [Function try_as_u8](#std_u256_try_as_u8)
-  [Function try_as_u16](#std_u256_try_as_u16)
-  [Function try_as_u32](#std_u256_try_as_u32)
-  [Function try_as_u64](#std_u256_try_as_u64)
-  [Function try_as_u128](#std_u256_try_as_u128)
-  [Function to_string](#std_u256_to_string)
-  [Function checked_add](#std_u256_checked_add)
-  [Function checked_sub](#std_u256_checked_sub)
-  [Function checked_mul](#std_u256_checked_mul)
-  [Function checked_div](#std_u256_checked_div)
-  [Function saturating_add](#std_u256_saturating_add)
-  [Function saturating_sub](#std_u256_saturating_sub)
-  [Function saturating_mul](#std_u256_saturating_mul)
-  [Function lossless_shl](#std_u256_lossless_shl)
-  [Function lossless_shr](#std_u256_lossless_shr)
-  [Function lossless_div](#std_u256_lossless_div)
-  [Macro function max_value](#std_u256_max_value)
-  [Macro function range_do](#std_u256_range_do)
-  [Macro function range_do_eq](#std_u256_range_do_eq)
-  [Macro function do](#std_u256_do)
-  [Macro function do_eq](#std_u256_do_eq)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Function <code>bitwise_not</code>

Returns the bitwise not of the value.
Each bit that is 1 becomes 0. Each bit that is 0 becomes 1.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_bitwise_not">bitwise_not</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_bitwise_not">bitwise_not</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    x ^ <a href="../sui_std/u256#std_u256_max_value">max_value</a>!()
}
</code></pre>

Function <code>max</code>

Return the larger of x and y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_max">max</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_max">max</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_max">std::macros::num_max</a>!(x, y)
}
</code></pre>

Function <code>min</code>

Return the smaller of x and y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_min">min</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_min">min</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_min">std::macros::num_min</a>!(x, y)
}
</code></pre>

Function <code>diff</code>

Return the absolute value of x - y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_diff">diff</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_diff">diff</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_diff">std::macros::num_diff</a>!(x, y)
}
</code></pre>

Function <code>divide_and_round_up</code>

Calculate x / y, but round up the result.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_divide_and_round_up">divide_and_round_up</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_divide_and_round_up">divide_and_round_up</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_divide_and_round_up">std::macros::num_divide_and_round_up</a>!(x, y)
}
</code></pre>

Function <code>pow</code>

Return the value of a base raised to a power

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_pow">pow</a>(base: <a href="../sui_std/u256#std_u256">u256</a>, exponent: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_pow">pow</a>(base: <a href="../sui_std/u256#std_u256">u256</a>, exponent: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_pow">std::macros::num_pow</a>!(base, exponent)
}
</code></pre>

Function <code>try_as_u8</code>

Try to convert a <a href="../sui_std/u256#std_u256">u256</a> to a <a href="../sui_std/u8#std_u8">u8</a>. Returns None if the value is too large.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u8">try_as_u8</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u8">try_as_u8</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_try_as_u8">std::macros::try_as_u8</a>!(x)
}
</code></pre>

Function <code>try_as_u16</code>

Try to convert a <a href="../sui_std/u256#std_u256">u256</a> to a <a href="../sui_std/u16#std_u16">u16</a>. Returns None if the value is too large.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u16">try_as_u16</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u16#std_u16">u16</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u16">try_as_u16</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u16#std_u16">u16</a>&gt; {
    <a href="../sui_std/macros#std_macros_try_as_u16">std::macros::try_as_u16</a>!(x)
}
</code></pre>

Function <code>try_as_u32</code>

Try to convert a <a href="../sui_std/u256#std_u256">u256</a> to a <a href="../sui_std/u32#std_u32">u32</a>. Returns None if the value is too large.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u32">try_as_u32</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u32#std_u32">u32</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u32">try_as_u32</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u32#std_u32">u32</a>&gt; {
    <a href="../sui_std/macros#std_macros_try_as_u32">std::macros::try_as_u32</a>!(x)
}
</code></pre>

Function <code>try_as_u64</code>

Try to convert a <a href="../sui_std/u256#std_u256">u256</a> to a <a href="../sui_std/u64#std_u64">u64</a>. Returns None if the value is too large.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u64">try_as_u64</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u64#std_u64">u64</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u64">try_as_u64</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u64#std_u64">u64</a>&gt; {
    <a href="../sui_std/macros#std_macros_try_as_u64">std::macros::try_as_u64</a>!(x)
}
</code></pre>

Function <code>try_as_u128</code>

Try to convert a <a href="../sui_std/u256#std_u256">u256</a> to a <a href="../sui_std/u128#std_u128">u128</a>. Returns None if the value is too large.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u128">try_as_u128</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u128#std_u128">u128</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_try_as_u128">try_as_u128</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u128#std_u128">u128</a>&gt; {
    <a href="../sui_std/macros#std_macros_try_as_u128">std::macros::try_as_u128</a>!(x)
}
</code></pre>

Function <code>to_string</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_to_string">to_string</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_to_string">to_string</a>(x: <a href="../sui_std/u256#std_u256">u256</a>): String {
    <a href="../sui_std/macros#std_macros_num_to_string">std::macros::num_to_string</a>!(x)
}
</code></pre>

Function <code>checked_add</code>

Try to add x and y.
Returns None if the addition would overflow.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_add">checked_add</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_add">checked_add</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_add">std::macros::num_checked_add</a>!(x, y, <a href="../sui_std/u256#std_u256_max_value">max_value</a>!())
}
</code></pre>

Function <code>checked_sub</code>

Try to subtract y from x.
Returns None if y &gt; x.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_sub">checked_sub</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_sub">checked_sub</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_sub">std::macros::num_checked_sub</a>!(x, y)
}
</code></pre>

Function <code>checked_mul</code>

Try to multiply x and y.
Returns None if the multiplication would overflow.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_mul">checked_mul</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_mul">checked_mul</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_mul">std::macros::num_checked_mul</a>!(x, y, <a href="../sui_std/u256#std_u256_max_value">max_value</a>!())
}
</code></pre>

Function <code>checked_div</code>

Try to divide x by y.
Returns None if y is zero.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_div">checked_div</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_checked_div">checked_div</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_div">std::macros::num_checked_div</a>!(x, y)
}
</code></pre>

Function <code>saturating_add</code>

Add x and y, saturating at the maximum value instead of overflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_add">saturating_add</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_add">saturating_add</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_add">std::macros::num_saturating_add</a>!(x, y, <a href="../sui_std/u256#std_u256_max_value">max_value</a>!())
}
</code></pre>

Function <code>saturating_sub</code>

Subtract y from x, saturating at 0 instead of underflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_sub">saturating_sub</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_sub">saturating_sub</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_sub">std::macros::num_saturating_sub</a>!(x, y)
}
</code></pre>

Function <code>saturating_mul</code>

Multiply x and y, saturating at the maximum value instead of overflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_mul">saturating_mul</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_saturating_mul">saturating_mul</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/u256#std_u256">u256</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_mul">std::macros::num_saturating_mul</a>!(x, y, <a href="../sui_std/u256#std_u256_max_value">max_value</a>!())
}
</code></pre>

Function <code>lossless_shl</code>

Shifts x left by shift bits.
Returns None if the shift would lose any bits (if the operation is not reversible).

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_shl">lossless_shl</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_shl">lossless_shl</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <b>let</b> result = x &lt;&lt; shift;
    <b>if</b> (result &gt;&gt; shift == x) <a href="../sui_std/option#std_option_some">option::some</a>(result) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
}
</code></pre>

Function <code>lossless_shr</code>

Shifts x right by shift bits.
Returns None if the shift would lose any bits (if the operation is not reversible).

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_shr">lossless_shr</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_shr">lossless_shr</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <b>let</b> result = x &gt;&gt; shift;
    <b>if</b> (result &lt;&lt; shift == x) <a href="../sui_std/option#std_option_some">option::some</a>(result) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
}
</code></pre>

Function <code>lossless_div</code>

Divides x by y.
Returns None if y is zero or if there is a non-zero remainder (if x % y != 0). In other
words, it returns None if the operation is not reversible.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_div">lossless_div</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u256#std_u256_lossless_div">lossless_div</a>(x: <a href="../sui_std/u256#std_u256">u256</a>, y: <a href="../sui_std/u256#std_u256">u256</a>): Option&lt;<a href="../sui_std/u256#std_u256">u256</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_lossless_div">std::macros::num_lossless_div</a>!(x, y)
}
</code></pre>

Macro function <code>max_value</code>

Maximum value for a <a href="../sui_std/u256#std_u256">u256</a>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_max_value">max_value</a>(): <a href="../sui_std/u256#std_u256">u256</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_max_value">max_value</a>(): <a href="../sui_std/u256#std_u256">u256</a> {
    0xFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF
}
</code></pre>

Macro function <code>range_do</code>

Loops applying $f to each number from $start to $stop (exclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_range_do">range_do</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u256#std_u256">u256</a>, $stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_range_do">range_do</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u256#std_u256">u256</a>, $stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do">std::macros::range_do</a>!($start, $stop, $f)
}
</code></pre>

Macro function <code>range_do_eq</code>

Loops applying $f to each number from $start to $stop (inclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_range_do_eq">range_do_eq</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u256#std_u256">u256</a>, $stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_range_do_eq">range_do_eq</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u256#std_u256">u256</a>, $stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do_eq">std::macros::range_do_eq</a>!($start, $stop, $f)
}
</code></pre>

Macro function <code>do</code>

Loops applying $f to each number from 0 to $stop (exclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_do">do</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_do">do</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_do">std::macros::do</a>!($stop, $f)
}
</code></pre>

Macro function <code>do_eq</code>

Loops applying $f to each number from 0 to $stop (inclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_do_eq">do_eq</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u256#std_u256_do_eq">do_eq</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u256#std_u256">u256</a>, $f: |<a href="../sui_std/u256#std_u256">u256</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_do_eq">std::macros::do_eq</a>!($stop, $f)
}
</code></pre>