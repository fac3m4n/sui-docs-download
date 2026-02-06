The <a href="../sui_std/string#std_string">string</a> module defines the <a href="../sui_std/string#std_string_String">String</a> type which represents UTF8 encoded
strings.

-  [Struct String](#std_string_String)
-  [Constants](#@Constants_0)
-  [Function utf8](#std_string_utf8)
-  [Function from_ascii](#std_string_from_ascii)
-  [Function to_ascii](#std_string_to_ascii)
-  [Function try_utf8](#std_string_try_utf8)
-  [Function as_bytes](#std_string_as_bytes)
-  [Function into_bytes](#std_string_into_bytes)
-  [Function is_empty](#std_string_is_empty)
-  [Function length](#std_string_length)
-  [Function append](#std_string_append)
-  [Function append_utf8](#std_string_append_utf8)
-  [Function insert](#std_string_insert)
-  [Function substring](#std_string_substring)
-  [Function index_of](#std_string_index_of)
-  [Function internal_check_utf8](#std_string_internal_check_utf8)
-  [Function internal_is_char_boundary](#std_string_internal_is_char_boundary)
-  [Function internal_sub_string](#std_string_internal_sub_string)
-  [Function internal_index_of](#std_string_internal_index_of)
-  [Function bytes](#std_string_bytes)
-  [Function sub_string](#std_string_sub_string)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>String</code>

A <a href="../sui_std/string#std_string_String">String</a> holds a sequence of bytes which is guaranteed to be in utf8
format.

<code><b>public</b> <b>struct</b> <a href="../sui_std/string#std_string_String">String</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

An invalid UTF8 encoding.

<code><b>const</b> <a href="../sui_std/string#std_string_EInvalidUTF8">EInvalidUTF8</a>: <a href="../sui_std/u64#std_u64">u64</a> = 1;
</code>

Index out of range.

<code><b>const</b> <a href="../sui_std/string#std_string_EInvalidIndex">EInvalidIndex</a>: <a href="../sui_std/u64#std_u64">u64</a> = 2;
</code>

Function <code>utf8</code>

Creates a new string from a sequence of bytes. Aborts if the bytes do
not represent valid utf8.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_utf8">utf8</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_utf8">utf8</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/string#std_string_String">String</a> {
    <b>assert</b>!(<a href="../sui_std/string#std_string_internal_check_utf8">internal_check_utf8</a>(&<a href="../sui_std/string#std_string_bytes">bytes</a>), <a href="../sui_std/string#std_string_EInvalidUTF8">EInvalidUTF8</a>);
    <a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a> }
}
</code></pre>

Function <code>from_ascii</code>

Convert an ASCII string to a UTF8 string

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_from_ascii">from_ascii</a>(s: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_from_ascii">from_ascii</a>(s: <a href="../sui_std/ascii#std_ascii_String">ascii::String</a>): <a href="../sui_std/string#std_string_String">String</a> {
    <a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a>: s.<a href="../sui_std/string#std_string_into_bytes">into_bytes</a>() }
}
</code></pre>

Function <code>to_ascii</code>

Convert an UTF8 string to an ASCII string.
Aborts if s is not valid ASCII

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_to_ascii">to_ascii</a>(s: <a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_to_ascii">to_ascii</a>(s: <a href="../sui_std/string#std_string_String">String</a>): <a href="../sui_std/ascii#std_ascii_String">ascii::String</a> {
    <b>let</b> <a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a> } = s;
    <a href="../sui_std/string#std_string_bytes">bytes</a>.to_ascii_string()
}
</code></pre>

Function <code>try_utf8</code>

Tries to create a new string from a sequence of bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_try_utf8">try_utf8</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_try_utf8">try_utf8</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): Option&lt;<a href="../sui_std/string#std_string_String">String</a>&gt; {
    <b>if</b> (<a href="../sui_std/string#std_string_internal_check_utf8">internal_check_utf8</a>(&<a href="../sui_std/string#std_string_bytes">bytes</a>)) <a href="../sui_std/option#std_option_some">option::some</a>(<a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a> }) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
}
</code></pre>

Function <code>as_bytes</code>

Returns a reference to the underlying byte vector.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_as_bytes">as_bytes</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_as_bytes">as_bytes</a>(s: &<a href="../sui_std/string#std_string_String">String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    &s.<a href="../sui_std/string#std_string_bytes">bytes</a>
}
</code></pre>

Function <code>into_bytes</code>

Unpack the <a href="../sui_std/string#std_string">string</a> to get its underlying bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_into_bytes">into_bytes</a>(s: <a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_into_bytes">into_bytes</a>(s: <a href="../sui_std/string#std_string_String">String</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <b>let</b> <a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a> } = s;
    <a href="../sui_std/string#std_string_bytes">bytes</a>
}
</code></pre>

Function <code>is_empty</code>

Checks whether this string is empty.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_is_empty">is_empty</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_is_empty">is_empty</a>(s: &<a href="../sui_std/string#std_string_String">String</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    s.<a href="../sui_std/string#std_string_bytes">bytes</a>.<a href="../sui_std/string#std_string_is_empty">is_empty</a>()
}
</code></pre>

Function <code>length</code>

Returns the length of this string, in bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_length">length</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_length">length</a>(s: &<a href="../sui_std/string#std_string_String">String</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    s.<a href="../sui_std/string#std_string_bytes">bytes</a>.<a href="../sui_std/string#std_string_length">length</a>()
}
</code></pre>

Function <code>append</code>

Appends a string.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_append">append</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">std::string::String</a>, r: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_append">append</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">String</a>, r: <a href="../sui_std/string#std_string_String">String</a>) {
    s.<a href="../sui_std/string#std_string_bytes">bytes</a>.<a href="../sui_std/string#std_string_append">append</a>(r.<a href="../sui_std/string#std_string_bytes">bytes</a>)
}
</code></pre>

Function <code>append_utf8</code>

Appends bytes which must be in valid utf8 format.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_append_utf8">append_utf8</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_append_utf8">append_utf8</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">String</a>, <a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;) {
    s.<a href="../sui_std/string#std_string_append">append</a>(<a href="../sui_std/string#std_string_utf8">utf8</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>))
}
</code></pre>

Function <code>insert</code>

Insert the other string at the byte index in given string. The index
must be at a valid utf8 char boundary.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_insert">insert</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">std::string::String</a>, at: <a href="../sui_std/u64#std_u64">u64</a>, o: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_insert">insert</a>(s: &<b>mut</b> <a href="../sui_std/string#std_string_String">String</a>, at: <a href="../sui_std/u64#std_u64">u64</a>, o: <a href="../sui_std/string#std_string_String">String</a>) {
    <b>let</b> <a href="../sui_std/string#std_string_bytes">bytes</a> = &s.<a href="../sui_std/string#std_string_bytes">bytes</a>;
    <b>assert</b>!(at &lt;= <a href="../sui_std/string#std_string_bytes">bytes</a>.<a href="../sui_std/string#std_string_length">length</a>() && <a href="../sui_std/string#std_string_internal_is_char_boundary">internal_is_char_boundary</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>, at), <a href="../sui_std/string#std_string_EInvalidIndex">EInvalidIndex</a>);
    <b>let</b> l = s.<a href="../sui_std/string#std_string_length">length</a>();
    <b>let</b> <b>mut</b> front = s.<a href="../sui_std/string#std_string_substring">substring</a>(0, at);
    <b>let</b> end = s.<a href="../sui_std/string#std_string_substring">substring</a>(at, l);
    front.<a href="../sui_std/string#std_string_append">append</a>(o);
    front.<a href="../sui_std/string#std_string_append">append</a>(end);
    *s = front;
}
</code></pre>

Function <code>substring</code>

Returns a sub-string using the given byte indices, where i is the first
byte position and j is the start of the first byte not included (or the
length of the string). The indices must be at valid utf8 char boundaries,
guaranteeing that the result is valid utf8.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_substring">substring</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_substring">substring</a>(s: &<a href="../sui_std/string#std_string_String">String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/string#std_string_String">String</a> {
    <b>let</b> <a href="../sui_std/string#std_string_bytes">bytes</a> = &s.<a href="../sui_std/string#std_string_bytes">bytes</a>;
    <b>let</b> l = <a href="../sui_std/string#std_string_bytes">bytes</a>.<a href="../sui_std/string#std_string_length">length</a>();
    <b>assert</b>!(
        j &lt;= l &&
            i &lt;= j &&
            <a href="../sui_std/string#std_string_internal_is_char_boundary">internal_is_char_boundary</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>, i) &&
            <a href="../sui_std/string#std_string_internal_is_char_boundary">internal_is_char_boundary</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>, j),
        <a href="../sui_std/string#std_string_EInvalidIndex">EInvalidIndex</a>,
    );
    <a href="../sui_std/string#std_string_String">String</a> { <a href="../sui_std/string#std_string_bytes">bytes</a>: <a href="../sui_std/string#std_string_internal_sub_string">internal_sub_string</a>(<a href="../sui_std/string#std_string_bytes">bytes</a>, i, j) }
}
</code></pre>

Function <code>index_of</code>

Computes the index of the first occurrence of a string. Returns s.<a href="../sui_std/string#std_string_length">length</a>()
if no occurrence found.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_index_of">index_of</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>, r: &<a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_index_of">index_of</a>(s: &<a href="../sui_std/string#std_string_String">String</a>, r: &<a href="../sui_std/string#std_string_String">String</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    <a href="../sui_std/string#std_string_internal_index_of">internal_index_of</a>(&s.<a href="../sui_std/string#std_string_bytes">bytes</a>, &r.<a href="../sui_std/string#std_string_bytes">bytes</a>)
}
</code></pre>

Function <code>internal_check_utf8</code>

<code><b>fun</b> <a href="../sui_std/string#std_string_internal_check_utf8">internal_check_utf8</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_std/string#std_string_internal_check_utf8">internal_check_utf8</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/bool#std_bool">bool</a>;
</code></pre>

Function <code>internal_is_char_boundary</code>

<code><b>fun</b> <a href="../sui_std/string#std_string_internal_is_char_boundary">internal_is_char_boundary</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, i: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_std/string#std_string_internal_is_char_boundary">internal_is_char_boundary</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, i: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bool#std_bool">bool</a>;
</code></pre>

Function <code>internal_sub_string</code>

<code><b>fun</b> <a href="../sui_std/string#std_string_internal_sub_string">internal_sub_string</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_std/string#std_string_internal_sub_string">internal_sub_string</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;;
</code></pre>

Function <code>internal_index_of</code>

<code><b>fun</b> <a href="../sui_std/string#std_string_internal_index_of">internal_index_of</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, r: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>native</b> <b>fun</b> <a href="../sui_std/string#std_string_internal_index_of">internal_index_of</a>(v: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;, r: &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/u64#std_u64">u64</a>;
</code></pre>

Function <code>bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_bytes">bytes</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_bytes">bytes</a>(s: &<a href="../sui_std/string#std_string_String">String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; { s.<a href="../sui_std/string#std_string_as_bytes">as_bytes</a>() }
</code></pre>

Function <code>sub_string</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_sub_string">sub_string</a>(s: &<a href="../sui_std/string#std_string_String">std::string::String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string_sub_string">sub_string</a>(s: &<a href="../sui_std/string#std_string_String">String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/string#std_string_String">String</a> {
    s.<a href="../sui_std/string#std_string_substring">substring</a>(i, j)
}
</code></pre>