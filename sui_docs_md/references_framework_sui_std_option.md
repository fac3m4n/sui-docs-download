This module defines the Option type and its methods to represent and handle an optional value.

-  [Struct Option](#std_option_Option)
-  [Constants](#@Constants_0)
-  [Function none](#std_option_none)
-  [Function some](#std_option_some)
-  [Function is_none](#std_option_is_none)
-  [Function is_some](#std_option_is_some)
-  [Function contains](#std_option_contains)
-  [Function borrow](#std_option_borrow)
-  [Function borrow_with_default](#std_option_borrow_with_default)
-  [Function get_with_default](#std_option_get_with_default)
-  [Function fill](#std_option_fill)
-  [Function extract](#std_option_extract)
-  [Function borrow_mut](#std_option_borrow_mut)
-  [Function swap](#std_option_swap)
-  [Function swap_or_fill](#std_option_swap_or_fill)
-  [Function destroy_with_default](#std_option_destroy_with_default)
-  [Function destroy_some](#std_option_destroy_some)
-  [Function destroy_none](#std_option_destroy_none)
-  [Function to_vec](#std_option_to_vec)
-  [Macro function destroy](#std_option_destroy)
-  [Macro function do](#std_option_do)
-  [Macro function do_ref](#std_option_do_ref)
-  [Macro function do_mut](#std_option_do_mut)
-  [Macro function or](#std_option_or)
-  [Macro function and](#std_option_and)
-  [Macro function and_ref](#std_option_and_ref)
-  [Macro function map](#std_option_map)
-  [Macro function map_ref](#std_option_map_ref)
-  [Macro function filter](#std_option_filter)
-  [Macro function is_some_and](#std_option_is_some_and)
-  [Macro function extract_or](#std_option_extract_or)
-  [Macro function destroy_or](#std_option_destroy_or)

<code><b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>Option</code>

Abstraction of a value that may or may not be present. Implemented with a vector of size
zero or one because Move bytecode does not have ADTs.

<code><b>public</b> <b>struct</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>vec: <a href="../sui_std/vector#std_vector">vector</a>&lt;Element&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

The <a href="../sui_std/option#std_option_Option">Option</a> is in an invalid state for the operation attempted.
The <a href="../sui_std/option#std_option_Option">Option</a> is Some while it should be None.

<code><b>const</b> <a href="../sui_std/option#std_option_EOPTION_IS_SET">EOPTION_IS_SET</a>: <a href="../sui_std/u64#std_u64">u64</a> = 262144;
</code>

The <a href="../sui_std/option#std_option_Option">Option</a> is in an invalid state for the operation attempted.
The <a href="../sui_std/option#std_option_Option">Option</a> is None while it should be Some.

<code><b>const</b> <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>: <a href="../sui_std/u64#std_u64">u64</a> = 262145;
</code>

Function <code>none</code>

Return an empty <a href="../sui_std/option#std_option_Option">Option</a>

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_none">none</a>&lt;Element&gt;(): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_none">none</a>&lt;Element&gt;(): <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt; {
    <a href="../sui_std/option#std_option_Option">Option</a> { vec: <a href="../sui_std/vector#std_vector_empty">vector::empty</a>() }
}
</code></pre>

Function <code>some</code>

Return an <a href="../sui_std/option#std_option_Option">Option</a> containing e

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_some">some</a>&lt;Element&gt;(e: Element): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_some">some</a>&lt;Element&gt;(e: Element): <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt; {
    <a href="../sui_std/option#std_option_Option">Option</a> { vec: <a href="../sui_std/vector#std_vector_singleton">vector::singleton</a>(e) }
}
</code></pre>

Function <code>is_none</code>

Return true if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_is_none">is_none</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_is_none">is_none</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): <a href="../sui_std/bool#std_bool">bool</a> {
    t.vec.is_empty()
}
</code></pre>

Function <code>is_some</code>

Return true if t holds a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_is_some">is_some</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_is_some">is_some</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): <a href="../sui_std/bool#std_bool">bool</a> {
    !t.vec.is_empty()
}
</code></pre>

Function <code>contains</code>

Return true if the value in t is equal to e_ref
Always returns <b>false</b> if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_contains">contains</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, e_ref: &Element): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_contains">contains</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, e_ref: &Element): <a href="../sui_std/bool#std_bool">bool</a> {
    t.vec.<a href="../sui_std/option#std_option_contains">contains</a>(e_ref)
}
</code></pre>

Function <code>borrow</code>

Return an immutable reference to the value inside t
Aborts if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow">borrow</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): &Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow">borrow</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): &Element {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_some">is_some</a>(), <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>);
    &t.vec[0]
}
</code></pre>

Function <code>borrow_with_default</code>

Return a reference to the value inside t if it holds one
Return default_ref if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow_with_default">borrow_with_default</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, default_ref: &Element): &Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow_with_default">borrow_with_default</a>&lt;Element&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, default_ref: &Element): &Element {
    <b>let</b> vec_ref = &t.vec;
    <b>if</b> (vec_ref.is_empty()) default_ref <b>else</b> &vec_ref[0]
}
</code></pre>

Function <code>get_with_default</code>

Return the value inside t if it holds one
Return default if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_get_with_default">get_with_default</a>&lt;Element: <b>copy</b>, drop&gt;(t: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, default: Element): Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_get_with_default">get_with_default</a>&lt;Element: <b>copy</b> + drop&gt;(t: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, default: Element): Element {
    <b>let</b> vec_ref = &t.vec;
    <b>if</b> (vec_ref.is_empty()) default <b>else</b> vec_ref[0]
}
</code></pre>

Function <code>fill</code>

Convert the none option t to a some option by adding e.
Aborts if t already holds a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_fill">fill</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, e: Element)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_fill">fill</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, e: Element) {
    <b>let</b> vec_ref = &<b>mut</b> t.vec;
    <b>if</b> (vec_ref.is_empty()) vec_ref.push_back(e) <b>else</b> <b>abort</b> <a href="../sui_std/option#std_option_EOPTION_IS_SET">EOPTION_IS_SET</a>
}
</code></pre>

Function <code>extract</code>

Convert a <a href="../sui_std/option#std_option_some">some</a> option to a <a href="../sui_std/option#std_option_none">none</a> by removing and returning the value stored inside t
Aborts if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_extract">extract</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_extract">extract</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): Element {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_some">is_some</a>(), <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>);
    t.vec.pop_back()
}
</code></pre>

Function <code>borrow_mut</code>

Return a mutable reference to the value inside t
Aborts if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow_mut">borrow_mut</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): &<b>mut</b> Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_borrow_mut">borrow_mut</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): &<b>mut</b> Element {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_some">is_some</a>(), <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>);
    &<b>mut</b> t.vec[0]
}
</code></pre>

Function <code>swap</code>

Swap the old value inside t with e and return the old value
Aborts if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_swap">swap</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, e: Element): Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_swap">swap</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, e: Element): Element {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_some">is_some</a>(), <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>);
    <b>let</b> vec_ref = &<b>mut</b> t.vec;
    <b>let</b> old_value = vec_ref.pop_back();
    vec_ref.push_back(e);
    old_value
}
</code></pre>

Function <code>swap_or_fill</code>

Swap the old value inside t with e and return the old value;
or if there is no old value, fill it with e.
Different from swap(), swap_or_fill() allows for t not holding a value.

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_swap_or_fill">swap_or_fill</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, e: Element): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_swap_or_fill">swap_or_fill</a>&lt;Element&gt;(t: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, e: Element): <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt; {
    <b>let</b> vec_ref = &<b>mut</b> t.vec;
    <b>let</b> old_value = <b>if</b> (vec_ref.is_empty()) <a href="../sui_std/option#std_option_none">none</a>() <b>else</b> <a href="../sui_std/option#std_option_some">some</a>(vec_ref.pop_back());
    vec_ref.push_back(e);
    old_value
}
</code></pre>

Function <code>destroy_with_default</code>

Destroys t. If t holds a value, return it. Returns default otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_with_default">destroy_with_default</a>&lt;Element: drop&gt;(t: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;, default: Element): Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_with_default">destroy_with_default</a>&lt;Element: drop&gt;(t: <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;, default: Element): Element {
    <b>let</b> <a href="../sui_std/option#std_option_Option">Option</a> { <b>mut</b> vec } = t;
    <b>if</b> (vec.is_empty()) default <b>else</b> vec.pop_back()
}
</code></pre>

Function <code>destroy_some</code>

Unpack t and return its contents
Aborts if t does not hold a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_some">destroy_some</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): Element
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_some">destroy_some</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): Element {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_some">is_some</a>(), <a href="../sui_std/option#std_option_EOPTION_NOT_SET">EOPTION_NOT_SET</a>);
    <b>let</b> <a href="../sui_std/option#std_option_Option">Option</a> { <b>mut</b> vec } = t;
    <b>let</b> elem = vec.pop_back();
    vec.destroy_empty();
    elem
}
</code></pre>

Function <code>destroy_none</code>

Unpack t
Aborts if t holds a value

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_none">destroy_none</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_none">destroy_none</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;) {
    <b>assert</b>!(t.<a href="../sui_std/option#std_option_is_none">is_none</a>(), <a href="../sui_std/option#std_option_EOPTION_IS_SET">EOPTION_IS_SET</a>);
    <b>let</b> <a href="../sui_std/option#std_option_Option">Option</a> { vec } = t;
    vec.destroy_empty()
}
</code></pre>

Function <code>to_vec</code>

Convert t into a vector of length 1 if it is Some,
and an empty vector otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_to_vec">to_vec</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;Element&gt;): <a href="../sui_std/vector#std_vector">vector</a>&lt;Element&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/option#std_option_to_vec">to_vec</a>&lt;Element&gt;(t: <a href="../sui_std/option#std_option_Option">Option</a>&lt;Element&gt;): <a href="../sui_std/vector#std_vector">vector</a>&lt;Element&gt; {
    <b>let</b> <a href="../sui_std/option#std_option_Option">Option</a> { vec } = t;
    vec
}
</code></pre>

Macro function <code>destroy</code>

Destroy <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; and call the closure f on the value inside if it holds one.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy">destroy</a>&lt;$T, $R: drop&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy">destroy</a>&lt;$T, $R: drop&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |$T| -&gt; $R) {
    <b>let</b> o = $o;
    o.<a href="../sui_std/option#std_option_do">do</a>!($f);
}
</code></pre>

Macro function <code>do</code>

Destroy <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; and call the closure f on the value inside if it holds one.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do">do</a>&lt;$T, $R: drop&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do">do</a>&lt;$T, $R: drop&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |$T| -&gt; $R) {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) { $f(o.<a href="../sui_std/option#std_option_destroy_some">destroy_some</a>()); } <b>else</b> o.<a href="../sui_std/option#std_option_destroy_none">destroy_none</a>()
}
</code></pre>

Macro function <code>do_ref</code>

Execute a closure on the value inside t if it holds one.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do_ref">do_ref</a>&lt;$T, $R: drop&gt;($o: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&$T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do_ref">do_ref</a>&lt;$T, $R: drop&gt;($o: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&$T| -&gt; $R) {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) { $f(o.<a href="../sui_std/option#std_option_borrow">borrow</a>()); }
}
</code></pre>

Macro function <code>do_mut</code>

Execute a closure on the mutable reference to the value inside t if it holds one.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do_mut">do_mut</a>&lt;$T, $R: drop&gt;($o: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&<b>mut</b> $T| -&gt; $R)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_do_mut">do_mut</a>&lt;$T, $R: drop&gt;($o: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&<b>mut</b> $T| -&gt; $R) {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) { $f(o.<a href="../sui_std/option#std_option_borrow_mut">borrow_mut</a>()); }
}
</code></pre>

Macro function <code>or</code>

Select the first Some value from the two options, or None if both are None.
Equivalent to Rust's a.<a href="../sui_std/option#std_option_or">or</a>(b).

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_or">or</a>&lt;$T&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $default: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_or">or</a>&lt;$T&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $default: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) {
        o
    } <b>else</b> {
        o.<a href="../sui_std/option#std_option_destroy_none">destroy_none</a>();
        $default
    }
}
</code></pre>

Macro function <code>and</code>

If the value is Some, call the closure f on it. Otherwise, return None.
Equivalent to Rust's t.and_then(f).

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_and">and</a>&lt;$T, $U&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |$T| -&gt; <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_and">and</a>&lt;$T, $U&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |$T| -&gt; <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt;): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) {
        $f(o.<a href="../sui_std/option#std_option_destroy_some">destroy_some</a>())
    } <b>else</b> {
        o.<a href="../sui_std/option#std_option_destroy_none">destroy_none</a>();
        <a href="../sui_std/option#std_option_none">none</a>()
    }
}
</code></pre>

Macro function <code>and_ref</code>

If the value is Some, call the closure f on it. Otherwise, return None.
Equivalent to Rust's t.and_then(f).

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_and_ref">and_ref</a>&lt;$T, $U&gt;($o: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_and_ref">and_ref</a>&lt;$T, $U&gt;($o: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt;): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) $f(o.<a href="../sui_std/option#std_option_borrow">borrow</a>()) <b>else</b> <a href="../sui_std/option#std_option_none">none</a>()
}
</code></pre>

Macro function <code>map</code>

Map an <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; to <a href="../sui_std/option#std_option_Option">Option</a>&lt;U&gt; by applying a function to a contained value.
Equivalent to Rust's t.<a href="../sui_std/option#std_option_map">map</a>(f).

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_map">map</a>&lt;$T, $U&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |$T| -&gt; $U): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_map">map</a>&lt;$T, $U&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |$T| -&gt; $U): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) {
        <a href="../sui_std/option#std_option_some">some</a>($f(o.<a href="../sui_std/option#std_option_destroy_some">destroy_some</a>()))
    } <b>else</b> {
        o.<a href="../sui_std/option#std_option_destroy_none">destroy_none</a>();
        <a href="../sui_std/option#std_option_none">none</a>()
    }
}
</code></pre>

Macro function <code>map_ref</code>

Map an <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; value to <a href="../sui_std/option#std_option_Option">Option</a>&lt;U&gt; by applying a function to a contained value by reference.
Original <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; is preserved.
Equivalent to Rust's t.<a href="../sui_std/option#std_option_map">map</a>(f).

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_map_ref">map_ref</a>&lt;$T, $U&gt;($o: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&$T| -&gt; $U): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$U&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_map_ref">map_ref</a>&lt;$T, $U&gt;($o: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&$T| -&gt; $U): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$U&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) <a href="../sui_std/option#std_option_some">some</a>($f(o.<a href="../sui_std/option#std_option_borrow">borrow</a>())) <b>else</b> <a href="../sui_std/option#std_option_none">none</a>()
}
</code></pre>

Macro function <code>filter</code>

Return None if the value is None, otherwise return <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; if the predicate f returns true.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_filter">filter</a>&lt;$T: drop&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/bool#std_bool">bool</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_filter">filter</a>&lt;$T: drop&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/bool#std_bool">bool</a>): <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt; {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>() && $f(o.<a href="../sui_std/option#std_option_borrow">borrow</a>())) o <b>else</b> <a href="../sui_std/option#std_option_none">none</a>()
}
</code></pre>

Macro function <code>is_some_and</code>

Return <b>false</b> if the value is None, otherwise return the result of the predicate f.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_is_some_and">is_some_and</a>&lt;$T&gt;($o: &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/bool#std_bool">bool</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_is_some_and">is_some_and</a>&lt;$T&gt;($o: &<a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $f: |&$T| -&gt; <a href="../sui_std/bool#std_bool">bool</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <b>let</b> o = $o;
    o.<a href="../sui_std/option#std_option_is_some">is_some</a>() && $f(o.<a href="../sui_std/option#std_option_borrow">borrow</a>())
}
</code></pre>

Macro function <code>extract_or</code>

Extract the value inside <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; if it holds one, or default otherwise.
Similar to <a href="../sui_std/option#std_option_destroy_or">destroy_or</a>, but modifying the input <a href="../sui_std/option#std_option_Option">Option</a> via a mutable reference.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_extract_or">extract_or</a>&lt;$T&gt;($o: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $default: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_extract_or">extract_or</a>&lt;$T&gt;($o: &<b>mut</b> <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $default: $T): $T {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) o.<a href="../sui_std/option#std_option_extract">extract</a>() <b>else</b> $default
}
</code></pre>

Macro function <code>destroy_or</code>

Destroy <a href="../sui_std/option#std_option_Option">Option</a>&lt;T&gt; and return the value inside if it holds one, or default otherwise.
Equivalent to Rust's t.unwrap_or(default).

Note: this function is a more efficient version of <a href="../sui_std/option#std_option_destroy_with_default">destroy_with_default</a>, as it does not
evaluate the default value unless necessary. The <a href="../sui_std/option#std_option_destroy_with_default">destroy_with_default</a> function should be
deprecated in favor of this function.

<code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_or">destroy_or</a>&lt;$T&gt;($o: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $default: $T): $T
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>macro</b> <b>fun</b> <a href="../sui_std/option#std_option_destroy_or">destroy_or</a>&lt;$T&gt;($o: <a href="../sui_std/option#std_option_Option">Option</a>&lt;$T&gt;, $default: $T): $T {
    <b>let</b> o = $o;
    <b>if</b> (o.<a href="../sui_std/option#std_option_is_some">is_some</a>()) {
        o.<a href="../sui_std/option#std_option_destroy_some">destroy_some</a>()
    } <b>else</b> {
        o.<a href="../sui_std/option#std_option_destroy_none">destroy_none</a>();
        $default
    }
}
</code></pre>