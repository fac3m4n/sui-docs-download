-  [Function bitwise_not](#std_u8_bitwise_not)
-  [Function max](#std_u8_max)
-  [Function min](#std_u8_min)
-  [Function diff](#std_u8_diff)
-  [Function divide_and_round_up](#std_u8_divide_and_round_up)
-  [Function pow](#std_u8_pow)
-  [Function sqrt](#std_u8_sqrt)
-  [Function to_string](#std_u8_to_string)
-  [Function checked_add](#std_u8_checked_add)
-  [Function checked_sub](#std_u8_checked_sub)
-  [Function checked_mul](#std_u8_checked_mul)
-  [Function checked_div](#std_u8_checked_div)
-  [Function saturating_add](#std_u8_saturating_add)
-  [Function saturating_sub](#std_u8_saturating_sub)
-  [Function saturating_mul](#std_u8_saturating_mul)
-  [Function checked_shl](#std_u8_checked_shl)
-  [Function checked_shr](#std_u8_checked_shr)
-  [Function lossless_shl](#std_u8_lossless_shl)
-  [Function lossless_shr](#std_u8_lossless_shr)
-  [Function lossless_div](#std_u8_lossless_div)
-  [Macro function max_value](#std_u8_max_value)
-  [Macro function range_do](#std_u8_range_do)
-  [Macro function range_do_eq](#std_u8_range_do_eq)
-  [Macro function do](#std_u8_do)
-  [Macro function do_eq](#std_u8_do_eq)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Function <code>bitwise_not</code>

Returns the bitwise not of the value.
Each bit that is 1 becomes 0. Each bit that is 0 becomes 1.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_bitwise_not">bitwise_not</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_bitwise_not">bitwise_not</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    x ^ <a href="../sui_std/u8#std_u8_max_value">max_value</a>!()
}
</code></pre>

Function <code>max</code>

Return the larger of x and y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_max">max</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_max">max</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_max">std::macros::num_max</a>!(x, y)
}
</code></pre>

Function <code>min</code>

Return the smaller of x and y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_min">min</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_min">min</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_min">std::macros::num_min</a>!(x, y)
}
</code></pre>

Function <code>diff</code>

Return the absolute value of x - y

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_diff">diff</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_diff">diff</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_diff">std::macros::num_diff</a>!(x, y)
}
</code></pre>

Function <code>divide_and_round_up</code>

Calculate x / y, but round up the result.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_divide_and_round_up">divide_and_round_up</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_divide_and_round_up">divide_and_round_up</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_divide_and_round_up">std::macros::num_divide_and_round_up</a>!(x, y)
}
</code></pre>

Function <code>pow</code>

Return the value of a base raised to a power

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_pow">pow</a>(base: <a href="../sui_std/u8#std_u8">u8</a>, exponent: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_pow">pow</a>(base: <a href="../sui_std/u8#std_u8">u8</a>, exponent: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_pow">std::macros::num_pow</a>!(base, exponent)
}
</code></pre>

Function <code>sqrt</code>

Get a nearest lower integer Square Root for x. Given that this
function can only operate with integers, it is impossible
to get perfect (or precise) integer square root for some numbers.

Example:
```
math::sqrt(9) => 3
math::sqrt(8) => 2 // the nearest lower square root is 4;
```

In integer math, one of the possible ways to get results with more
precision is to use higher values or temporarily multiply the
value by some bigger number. Ideally if this is a square of 10 or 100.

Example:
```
math::sqrt(8) => 2;
math::sqrt(8 * 10000) => 282;
// now we can use this value as if it was 2.82;
// but to get the actual result, this value needs
// to be divided by 100 (because sqrt(10000)).

math::sqrt(8 * 1000000) => 2828; // same as above, 2828 / 1000 (2.828)
```

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_sqrt">sqrt</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_sqrt">sqrt</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_sqrt">std::macros::num_sqrt</a>!&lt;<a href="../sui_std/u8#std_u8">u8</a>, <a href="../sui_std/u16#std_u16">u16</a>&gt;(x, 8)
}
</code></pre>

Function <code>to_string</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_to_string">to_string</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_to_string">to_string</a>(x: <a href="../sui_std/u8#std_u8">u8</a>): String {
    <a href="../sui_std/macros#std_macros_num_to_string">std::macros::num_to_string</a>!(x)
}
</code></pre>

Function <code>checked_add</code>

Try to add x and y.
Returns None if the addition would overflow.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_add">checked_add</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_add">checked_add</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_add">std::macros::num_checked_add</a>!(x, y, <a href="../sui_std/u8#std_u8_max_value">max_value</a>!())
}
</code></pre>

Function <code>checked_sub</code>

Try to subtract y from x.
Returns None if y &gt; x.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_sub">checked_sub</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_sub">checked_sub</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_sub">std::macros::num_checked_sub</a>!(x, y)
}
</code></pre>

Function <code>checked_mul</code>

Try to multiply x and y.
Returns None if the multiplication would overflow.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_mul">checked_mul</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_mul">checked_mul</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_mul">std::macros::num_checked_mul</a>!(x, y, <a href="../sui_std/u8#std_u8_max_value">max_value</a>!())
}
</code></pre>

Function <code>checked_div</code>

Try to divide x by y.
Returns None if y is zero.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_div">checked_div</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_div">checked_div</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_div">std::macros::num_checked_div</a>!(x, y)
}
</code></pre>

Function <code>saturating_add</code>

Add x and y, saturating at the maximum value instead of overflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_add">saturating_add</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_add">saturating_add</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_add">std::macros::num_saturating_add</a>!(x, y, <a href="../sui_std/u8#std_u8_max_value">max_value</a>!())
}
</code></pre>

Function <code>saturating_sub</code>

Subtract y from x, saturating at 0 instead of underflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_sub">saturating_sub</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_sub">saturating_sub</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_sub">std::macros::num_saturating_sub</a>!(x, y)
}
</code></pre>

Function <code>saturating_mul</code>

Multiply x and y, saturating at the maximum value instead of overflowing.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_mul">saturating_mul</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_saturating_mul">saturating_mul</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <a href="../sui_std/macros#std_macros_num_saturating_mul">std::macros::num_saturating_mul</a>!(x, y, <a href="../sui_std/u8#std_u8_max_value">max_value</a>!())
}
</code></pre>

Function <code>checked_shl</code>

Shifts x left by shift bits.
Returns None if the shift is greater than or equal to the bit size of 8.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_shl">checked_shl</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_shl">checked_shl</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_shl">std::macros::num_checked_shl</a>!(x, shift, 8)
}
</code></pre>

Function <code>checked_shr</code>

Shifts x right by shift bits.
Returns None if the shift is greater than or equal to the bit size of 8.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_shr">checked_shr</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_checked_shr">checked_shr</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_checked_shr">std::macros::num_checked_shr</a>!(x, shift, 8)
}
</code></pre>

Function <code>lossless_shl</code>

Shifts x left by shift bits.
Returns None if the shift is larger than or equal to the bit size of 8, or if the shift would
lose any bits (if the operation is not reversible).

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_shl">lossless_shl</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_shl">lossless_shl</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_lossless_shl">std::macros::num_lossless_shl</a>!(x, shift, 8)
}
</code></pre>

Function <code>lossless_shr</code>

Shifts x right by shift bits.
Returns None if the shift is larger than or equal to the bit size of 8, or if the shift would
lose any bits (if the operation is not reversible).

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_shr">lossless_shr</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_shr">lossless_shr</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, shift: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_lossless_shr">std::macros::num_lossless_shr</a>!(x, shift, 8)
}
</code></pre>

Function <code>lossless_div</code>

Divides x by y.
Returns None if y is zero or if there is a non-zero remainder (if x % y != 0). In other
words, it returns None if the operation is not reversible.

<code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_div">lossless_div</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/u8#std_u8_lossless_div">lossless_div</a>(x: <a href="../sui_std/u8#std_u8">u8</a>, y: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <a href="../sui_std/macros#std_macros_num_lossless_div">std::macros::num_lossless_div</a>!(x, y)
}
</code></pre>

Macro function <code>max_value</code>

Maximum value for a <a href="../sui_std/u8#std_u8">u8</a>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_max_value">max_value</a>(): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_max_value">max_value</a>(): <a href="../sui_std/u8#std_u8">u8</a> {
    0xFF
}
</code></pre>

Macro function <code>range_do</code>

Loops applying $f to each number from $start to $stop (exclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_range_do">range_do</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u8#std_u8">u8</a>, $stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_range_do">range_do</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u8#std_u8">u8</a>, $stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do">std::macros::range_do</a>!($start, $stop, $f)
}
</code></pre>

Macro function <code>range_do_eq</code>

Loops applying $f to each number from $start to $stop (inclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_range_do_eq">range_do_eq</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u8#std_u8">u8</a>, $stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_range_do_eq">range_do_eq</a>&lt;$R: drop&gt;($start: <a href="../sui_std/u8#std_u8">u8</a>, $stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do_eq">std::macros::range_do_eq</a>!($start, $stop, $f)
}
</code></pre>

Macro function <code>do</code>

Loops applying $f to each number from 0 to $stop (exclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_do">do</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_do">do</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_do">std::macros::do</a>!($stop, $f)
}
</code></pre>

Macro function <code>do_eq</code>

Loops applying $f to each number from 0 to $stop (inclusive)

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_do_eq">do_eq</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/u8#std_u8_do_eq">do_eq</a>&lt;$R: drop&gt;($stop: <a href="../sui_std/u8#std_u8">u8</a>, $f: |<a href="../sui_std/u8#std_u8">u8</a>| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_do_eq">std::macros::do_eq</a>!($stop, $f)
}
</code></pre>