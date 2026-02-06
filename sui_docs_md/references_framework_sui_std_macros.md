This module holds shared implementation of macros used in std

-  [Macro function num_max](#std_macros_num_max)
-  [Macro function num_min](#std_macros_num_min)
-  [Macro function num_diff](#std_macros_num_diff)
-  [Macro function num_divide_and_round_up](#std_macros_num_divide_and_round_up)
-  [Macro function num_pow](#std_macros_num_pow)
-  [Macro function num_sqrt](#std_macros_num_sqrt)
-  [Macro function num_to_string](#std_macros_num_to_string)
-  [Macro function num_checked_add](#std_macros_num_checked_add)
-  [Macro function num_checked_sub](#std_macros_num_checked_sub)
-  [Macro function num_checked_mul](#std_macros_num_checked_mul)
-  [Macro function num_checked_div](#std_macros_num_checked_div)
-  [Macro function num_saturating_add](#std_macros_num_saturating_add)
-  [Macro function num_saturating_sub](#std_macros_num_saturating_sub)
-  [Macro function num_saturating_mul](#std_macros_num_saturating_mul)
-  [Macro function num_checked_shl](#std_macros_num_checked_shl)
-  [Macro function num_checked_shr](#std_macros_num_checked_shr)
-  [Macro function num_lossless_shl](#std_macros_num_lossless_shl)
-  [Macro function num_lossless_shr](#std_macros_num_lossless_shr)
-  [Macro function num_lossless_div](#std_macros_num_lossless_div)
-  [Macro function range_do](#std_macros_range_do)
-  [Macro function range_do_eq](#std_macros_range_do_eq)
-  [Macro function do](#std_macros_do)
-  [Macro function do_eq](#std_macros_do_eq)
-  [Macro function try_as_u8](#std_macros_try_as_u8)
-  [Macro function try_as_u16](#std_macros_try_as_u16)
-  [Macro function try_as_u32](#std_macros_try_as_u32)
-  [Macro function try_as_u64](#std_macros_try_as_u64)
-  [Macro function try_as_u128](#std_macros_try_as_u128)
-  [Macro function uq_from_quotient](#std_macros_uq_from_quotient)
-  [Macro function uq_from_int](#std_macros_uq_from_int)
-  [Macro function uq_add](#std_macros_uq_add)
-  [Macro function uq_sub](#std_macros_uq_sub)
-  [Macro function uq_to_int](#std_macros_uq_to_int)
-  [Macro function uq_int_mul](#std_macros_uq_int_mul)
-  [Macro function uq_int_div](#std_macros_uq_int_div)

<code></code>

Macro function <code>num_max</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_max">num_max</a>&lt;$T&gt;($x: $T, $y: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_max">num_max</a>&lt;$T&gt;($x: $T, $y: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x &gt; y) x <b>else</b> y
}
</code></pre>

Macro function <code>num_min</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_min">num_min</a>&lt;$T&gt;($x: $T, $y: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_min">num_min</a>&lt;$T&gt;($x: $T, $y: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x &lt; y) x <b>else</b> y
}
</code></pre>

Macro function <code>num_diff</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_diff">num_diff</a>&lt;$T&gt;($x: $T, $y: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_diff">num_diff</a>&lt;$T&gt;($x: $T, $y: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x &gt; y) x - y <b>else</b> y - x
}
</code></pre>

Macro function <code>num_divide_and_round_up</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_divide_and_round_up">num_divide_and_round_up</a>&lt;$T&gt;($x: $T, $y: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_divide_and_round_up">num_divide_and_round_up</a>&lt;$T&gt;($x: $T, $y: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x % y == 0) x / y <b>else</b> x / y + 1
}
</code></pre>

Macro function <code>num_pow</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_pow">num_pow</a>($base: _, $exponent: <a href="../sui_std/u8#std_u8">u8</a>): _
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_pow">num_pow</a>($base: _, $exponent: <a href="../sui_std/u8#std_u8">u8</a>): _ {
    <b>let</b> <b>mut</b> base = $base;
    <b>let</b> <b>mut</b> exponent = $exponent;
    <b>let</b> <b>mut</b> res = 1;
    <b>while</b> (exponent &gt;= 1) {
        <b>if</b> (exponent % 2 == 0) {
            base = base * base;
            exponent = exponent / 2;
        } <b>else</b> {
            res = res * base;
            exponent = exponent - 1;
        }
    };
    res
}
</code></pre>

Macro function <code>num_sqrt</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_sqrt">num_sqrt</a>&lt;$T, $U&gt;($x: $T, $bitsize: <a href="../sui_std/u8#std_u8">u8</a>): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_sqrt">num_sqrt</a>&lt;$T, $U&gt;($x: $T, $bitsize: <a href="../sui_std/u8#std_u8">u8</a>): $T {
    <b>let</b> x = $x;
    <b>let</b> <b>mut</b> bit = (1: $U) &lt;&lt; $bitsize;
    <b>let</b> <b>mut</b> res = (0: $U);
    <b>let</b> <b>mut</b> x = x <b>as</b> $U;
    <b>while</b> (bit != 0) {
        <b>if</b> (x &gt;= res + bit) {
            x = x - (res + bit);
            res = (res &gt;&gt; 1) + bit;
        } <b>else</b> {
            res = res &gt;&gt; 1;
        };
        bit = bit &gt;&gt; 2;
    };
    res <b>as</b> $T
}
</code></pre>

Macro function <code>num_to_string</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_to_string">num_to_string</a>($x: _): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_to_string">num_to_string</a>($x: _): String {
    <b>let</b> <b>mut</b> x = $x;
    <b>if</b> (x == 0) {
        <b>return</b> b"0".to_string()
    };
    <b>let</b> <b>mut</b> buffer = <a href="../sui_std/vector#std_vector">vector</a>[];
    <b>while</b> (x != 0) {
        buffer.push_back(((48 + x % 10) <b>as</b> <a href="../sui_std/u8#std_u8">u8</a>));
        x = x / 10;
    };
    buffer.reverse();
    buffer.to_string()
}
</code></pre>

Macro function <code>num_checked_add</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_add">num_checked_add</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_add">num_checked_add</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>let</b> max_t = $max_t;
    <b>if</b> (y &gt; max_t - x) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x + y)
}
</code></pre>

Macro function <code>num_checked_sub</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_sub">num_checked_sub</a>&lt;$T&gt;($x: $T, $y: $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_sub">num_checked_sub</a>&lt;$T&gt;($x: $T, $y: $T): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x &lt; y) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x - y)
}
</code></pre>

Macro function <code>num_checked_mul</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_mul">num_checked_mul</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_mul">num_checked_mul</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>let</b> max_t = $max_t;
    <b>if</b> (x == 0 || y == 0) <a href="../sui_std/option#std_option_some">option::some</a>(0)
    <b>else</b> <b>if</b> (y &gt; max_t / x) <a href="../sui_std/option#std_option_none">option::none</a>()
    <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x * y)
}
</code></pre>

Macro function <code>num_checked_div</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_div">num_checked_div</a>&lt;$T&gt;($x: $T, $y: $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_div">num_checked_div</a>&lt;$T&gt;($x: $T, $y: $T): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (y == 0) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x / y)
}
</code></pre>

Macro function <code>num_saturating_add</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_add">num_saturating_add</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_add">num_saturating_add</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>let</b> max_t = $max_t;
    <b>if</b> (y &gt; max_t - x) max_t <b>else</b> x + y
}
</code></pre>

Macro function <code>num_saturating_sub</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_sub">num_saturating_sub</a>&lt;$T&gt;($x: $T, $y: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_sub">num_saturating_sub</a>&lt;$T&gt;($x: $T, $y: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (x &lt; y) 0 <b>else</b> x - y
}
</code></pre>

Macro function <code>num_saturating_mul</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_mul">num_saturating_mul</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_saturating_mul">num_saturating_mul</a>&lt;$T&gt;($x: $T, $y: $T, $max_t: $T): $T {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>let</b> max_t = $max_t;
    <b>if</b> (x == 0 || y == 0) 0
    <b>else</b> <b>if</b> (y &gt; max_t / x) max_t
    <b>else</b> x * y
}
</code></pre>

Macro function <code>num_checked_shl</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_shl">num_checked_shl</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_shl">num_checked_shl</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> shift = $shift;
    <b>let</b> bit_size = $bit_size;
    <b>if</b> (shift &gt;= bit_size) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x &lt;&lt; shift)
}
</code></pre>

Macro function <code>num_checked_shr</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_shr">num_checked_shr</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_checked_shr">num_checked_shr</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> shift = $shift;
    <b>let</b> bit_size = $bit_size;
    <b>if</b> (shift &gt;= bit_size) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x &gt;&gt; shift)
}
</code></pre>

Macro function <code>num_lossless_shl</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_shl">num_lossless_shl</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_shl">num_lossless_shl</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> shift = $shift;
    <b>let</b> bit_size = $bit_size;
    <b>if</b> (shift &gt;= bit_size) <a href="../sui_std/option#std_option_none">option::none</a>()
    <b>else</b> {
        <b>let</b> result = x &lt;&lt; shift;
        <b>if</b> (result &gt;&gt; shift == x) <a href="../sui_std/option#std_option_some">option::some</a>(result) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
    }
}
</code></pre>

Macro function <code>num_lossless_shr</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_shr">num_lossless_shr</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_shr">num_lossless_shr</a>&lt;$T&gt;($x: $T, $shift: <a href="../sui_std/u8#std_u8">u8</a>, $bit_size: <a href="../sui_std/u8#std_u8">u8</a>): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> shift = $shift;
    <b>let</b> bit_size = $bit_size;
    <b>if</b> (shift &gt;= bit_size) <a href="../sui_std/option#std_option_none">option::none</a>()
    <b>else</b> {
        <b>let</b> result = x &gt;&gt; shift;
        <b>if</b> (result &lt;&lt; shift == x) <a href="../sui_std/option#std_option_some">option::some</a>(result) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
    }
}
</code></pre>

Macro function <code>num_lossless_div</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_div">num_lossless_div</a>&lt;$T&gt;($x: $T, $y: $T): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_num_lossless_div">num_lossless_div</a>&lt;$T&gt;($x: $T, $y: $T): Option&lt;$T&gt; {
    <b>let</b> x = $x;
    <b>let</b> y = $y;
    <b>if</b> (y == 0) <a href="../sui_std/option#std_option_none">option::none</a>()
    <b>else</b> <b>if</b> (x % y == 0) <a href="../sui_std/option#std_option_some">option::some</a>(x / y)
    <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
}
</code></pre>

Macro function <code>range_do</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_range_do">range_do</a>&lt;$T, $R: drop&gt;($start: $T, $stop: $T, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_range_do">range_do</a>&lt;$T, $R: drop&gt;($start: $T, $stop: $T, $f: |$T| -&gt; $R) {
    <b>let</b> <b>mut</b> i = $start;
    <b>let</b> stop = $stop;
    <b>while</b> (i &lt; stop) {
        $f(i);
        i = i + 1;
    }
}
</code></pre>

Macro function <code>range_do_eq</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_range_do_eq">range_do_eq</a>&lt;$T, $R: drop&gt;($start: $T, $stop: $T, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_range_do_eq">range_do_eq</a>&lt;$T, $R: drop&gt;($start: $T, $stop: $T, $f: |$T| -&gt; $R) {
    <b>let</b> <b>mut</b> i = $start;
    <b>let</b> stop = $stop;
    // we check <span className="code-inline">i &gt;= stop</span> inside the <b>loop</b> instead of <span className="code-inline">i &lt;= stop</span> <b>as</b> <span className="code-inline"><b>while</b></span> condition to avoid
    // incrementing <span className="code-inline">i</span> past the MAX integer value.
    // Because of this, we need to check <b>if</b> <span className="code-inline">i &gt; stop</span> and <b>return</b> early--instead of letting the
    // <b>loop</b> bound handle it, like in the <span className="code-inline"><a href="../sui_std/macros#std_macros_range_do">range_do</a></span> <b>macro</b>.
    <b>if</b> (i &gt; stop) <b>return</b>;
    <b>loop</b> {
        $f(i);
        <b>if</b> (i &gt;= stop) <b>break</b>;
        i = i + 1;
    }
}
</code></pre>

Macro function <code>do</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_do">do</a>&lt;$T, $R: drop&gt;($stop: $T, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_do">do</a>&lt;$T, $R: drop&gt;($stop: $T, $f: |$T| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do">range_do</a>!(0, $stop, $f)
}
</code></pre>

Macro function <code>do_eq</code>

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_do_eq">do_eq</a>&lt;$T, $R: drop&gt;($stop: $T, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_do_eq">do_eq</a>&lt;$T, $R: drop&gt;($stop: $T, $f: |$T| -&gt; $R) {
    <a href="../sui_std/macros#std_macros_range_do_eq">range_do_eq</a>!(0, $stop, $f)
}
</code></pre>

Macro function <code>try_as_u8</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u8">try_as_u8</a>($x: _): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u8">try_as_u8</a>($x: _): Option&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <b>let</b> x = $x;
    <b>if</b> (x &gt; 0xFF) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x <b>as</b> <a href="../sui_std/u8#std_u8">u8</a>)
}
</code></pre>

Macro function <code>try_as_u16</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u16">try_as_u16</a>($x: _): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u16#std_u16">u16</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u16">try_as_u16</a>($x: _): Option&lt;<a href="../sui_std/u16#std_u16">u16</a>&gt; {
    <b>let</b> x = $x;
    <b>if</b> (x &gt; 0xFFFF) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x <b>as</b> <a href="../sui_std/u16#std_u16">u16</a>)
}
</code></pre>

Macro function <code>try_as_u32</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u32">try_as_u32</a>($x: _): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u32#std_u32">u32</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u32">try_as_u32</a>($x: _): Option&lt;<a href="../sui_std/u32#std_u32">u32</a>&gt; {
    <b>let</b> x = $x;
    <b>if</b> (x &gt; 0xFFFF_FFFF) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x <b>as</b> <a href="../sui_std/u32#std_u32">u32</a>)
}
</code></pre>

Macro function <code>try_as_u64</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u64">try_as_u64</a>($x: _): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u64#std_u64">u64</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u64">try_as_u64</a>($x: _): Option&lt;<a href="../sui_std/u64#std_u64">u64</a>&gt; {
    <b>let</b> x = $x;
    <b>if</b> (x &gt; 0xFFFF_FFFF_FFFF_FFFF) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x <b>as</b> <a href="../sui_std/u64#std_u64">u64</a>)
}
</code></pre>

Macro function <code>try_as_u128</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u128">try_as_u128</a>($x: _): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/u128#std_u128">u128</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_try_as_u128">try_as_u128</a>($x: _): Option&lt;<a href="../sui_std/u128#std_u128">u128</a>&gt; {
    <b>let</b> x = $x;
    <b>if</b> (x &gt; 0xFFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF_FFFF) <a href="../sui_std/option#std_option_none">option::none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">option::some</a>(x <b>as</b> <a href="../sui_std/u128#std_u128">u128</a>)
}
</code></pre>

Macro function <code>uq_from_quotient</code>

Creates a fixed-point value from a quotient specified by its numerator and denominator.
$T is the underlying integer type for the fixed-point value, where $T has $t_bits bits.
$U is the type used for intermediate calculations, where $U is the next larger integer type.
$max_t is the maximum value that can be represented by $T.
$t_bits (as mentioned above) is the total number of bits in the fixed-point value (integer
plus fractional).
$fractional_bits is the number of fractional bits in the fixed-point value.

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_from_quotient">uq_from_quotient</a>&lt;$T, $U&gt;($numerator: $T, $denominator: $T, $max_t: $T, $t_bits: <a href="../sui_std/u8#std_u8">u8</a>, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>, $abort_denominator: _, $abort_quotient_too_small: _, $abort_quotient_too_large: _): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_from_quotient">uq_from_quotient</a>&lt;$T, $U&gt;(
    $numerator: $T,
    $denominator: $T,
    $max_t: $T,
    $t_bits: <a href="../sui_std/u8#std_u8">u8</a>,
    $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>,
    $abort_denominator: _,
    $abort_quotient_too_small: _,
    $abort_quotient_too_large: _,
): $T {
    <b>let</b> numerator = $numerator;
    <b>let</b> denominator = $denominator;
    <b>if</b> (denominator == 0) $abort_denominator;
    // Scale the numerator to have <span className="code-inline">$t_bits</span> fractional bits and the denominator to have
    // <span className="code-inline">$t_bits - $fractional_bits</span> fractional bits, so that the quotient will have
    // <span className="code-inline">$fractional_bits</span> fractional bits.
    <b>let</b> scaled_numerator = numerator <b>as</b> $U &lt;&lt; $t_bits;
    <b>let</b> scaled_denominator = denominator <b>as</b> $U &lt;&lt; ($t_bits - $fractional_bits);
    <b>let</b> quotient = scaled_numerator / scaled_denominator;
    // The quotient can only be zero <b>if</b> the numerator is also zero.
    <b>if</b> (quotient == 0 && numerator != 0) $abort_quotient_too_small;
    // Return the quotient <b>as</b> a fixed-point number. We first need to check whether the cast
    // can succeed.
    <b>if</b> (quotient &gt; $max_t <b>as</b> $U) $abort_quotient_too_large;
    quotient <b>as</b> $T
}
</code></pre>

Macro function <code>uq_from_int</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_from_int">uq_from_int</a>&lt;$T, $U&gt;($integer: $T, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>): $U
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_from_int">uq_from_int</a>&lt;$T, $U&gt;($integer: $T, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>): $U {
    ($integer <b>as</b> $U) &lt;&lt; $fractional_bits
}
</code></pre>

Macro function <code>uq_add</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_add">uq_add</a>&lt;$T, $U&gt;($a: $T, $b: $T, $max_t: $T, $abort_overflow: _): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_add">uq_add</a>&lt;$T, $U&gt;($a: $T, $b: $T, $max_t: $T, $abort_overflow: _): $T {
    <b>let</b> sum = $a <b>as</b> $U + ($b <b>as</b> $U);
    <b>if</b> (sum &gt; $max_t <b>as</b> $U) $abort_overflow;
    sum <b>as</b> $T
}
</code></pre>

Macro function <code>uq_sub</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_sub">uq_sub</a>&lt;$T&gt;($a: $T, $b: $T, $abort_overflow: _): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_sub">uq_sub</a>&lt;$T&gt;($a: $T, $b: $T, $abort_overflow: _): $T {
    <b>let</b> a = $a;
    <b>let</b> b = $b;
    <b>if</b> (a &lt; b) $abort_overflow;
    a - b
}
</code></pre>

Macro function <code>uq_to_int</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_to_int">uq_to_int</a>&lt;$T, $U&gt;($a: $U, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_to_int">uq_to_int</a>&lt;$T, $U&gt;($a: $U, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>): $T {
    ($a &gt;&gt; $fractional_bits) <b>as</b> $T
}
</code></pre>

Macro function <code>uq_int_mul</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_int_mul">uq_int_mul</a>&lt;$T, $U&gt;($val: $T, $multiplier: $T, $max_t: $T, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>, $abort_overflow: _): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_int_mul">uq_int_mul</a>&lt;$T, $U&gt;(
    $val: $T,
    $multiplier: $T,
    $max_t: $T,
    $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>,
    $abort_overflow: _,
): $T {
    // The product of two <span className="code-inline">$T</span> bit values <b>has</b> the same number of bits <b>as</b> <span className="code-inline">$U</span>, so perform the
    // multiplication with <span className="code-inline">$U</span> types and keep the full <span className="code-inline">$U</span> bit product
    // to avoid losing accuracy.
    <b>let</b> unscaled_product = $val <b>as</b> $U * ($multiplier <b>as</b> $U);
    // The unscaled product <b>has</b> <span className="code-inline">$fractional_bits</span> fractional bits (from the multiplier)
    // so rescale it by shifting away the low bits.
    <b>let</b> product = unscaled_product &gt;&gt; $fractional_bits;
    // Check whether the value is too large.
    <b>if</b> (product &gt; $max_t <b>as</b> $U) $abort_overflow;
    product <b>as</b> $T
}
</code></pre>

Macro function <code>uq_int_div</code>

<code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_int_div">uq_int_div</a>&lt;$T, $U&gt;($val: $T, $divisor: $T, $max_t: $T, $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>, $abort_division_by_zero: _, $abort_overflow: _): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>macro</b> <b>fun</b> <a href="../sui_std/macros#std_macros_uq_int_div">uq_int_div</a>&lt;$T, $U&gt;(
    $val: $T,
    $divisor: $T,
    $max_t: $T,
    $fractional_bits: <a href="../sui_std/u8#std_u8">u8</a>,
    $abort_division_by_zero: _,
    $abort_overflow: _,
): $T {
    <b>let</b> val = $val;
    <b>let</b> divisor = $divisor;
    // Check <b>for</b> division by zero.
    <b>if</b> (divisor == 0) $abort_division_by_zero;
    // First convert to $U to increase the number of bits to the next integer size
    // and then shift left to add <span className="code-inline">$fractional_bits</span> fractional zero bits to the dividend.
    <b>let</b> scaled_value = val <b>as</b> $U &lt;&lt; $fractional_bits;
    <b>let</b> quotient = scaled_value / (divisor <b>as</b> $U);
    // Check whether the value is too large.
    <b>if</b> (quotient &gt; $max_t <b>as</b> $U) $abort_overflow;
    quotient <b>as</b> $T
}
</code></pre>