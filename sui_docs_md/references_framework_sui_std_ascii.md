The ASCII module defines basic string and char newtypes in Move that verify
that characters are valid ASCII, and that strings consist of only valid ASCII characters.

-  [Struct String](#std_ascii_String)
-  [Struct Char](#std_ascii_Char)
-  [Constants](#@Constants_0)
-  [Function char](#std_ascii_char)
-  [Function string](#std_ascii_string)
-  [Function try_string](#std_ascii_try_string)
-  [Function all_characters_printable](#std_ascii_all_characters_printable)
-  [Function push_char](#std_ascii_push_char)
-  [Function pop_char](#std_ascii_pop_char)
-  [Function length](#std_ascii_length)
-  [Function append](#std_ascii_append)
-  [Function insert](#std_ascii_insert)
-  [Function substring](#std_ascii_substring)
-  [Function as_bytes](#std_ascii_as_bytes)
-  [Function into_bytes](#std_ascii_into_bytes)
-  [Function byte](#std_ascii_byte)
-  [Function is_valid_char](#std_ascii_is_valid_char)
-  [Function is_printable_char](#std_ascii_is_printable_char)
-  [Function is_empty](#std_ascii_is_empty)
-  [Function to_uppercase](#std_ascii_to_uppercase)
-  [Function to_lowercase](#std_ascii_to_lowercase)
-  [Function index_of](#std_ascii_index_of)
-  [Function char_to_uppercase](#std_ascii_char_to_uppercase)
-  [Function char_to_lowercase](#std_ascii_char_to_lowercase)

<code><b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>String</code>

The <a href="../sui_std/ascii#std_ascii_String">String</a> struct holds a vector of bytes that all represent
valid ASCII characters. Note that these ASCII characters may not all
be printable. To determine if a <a href="../sui_std/ascii#std_ascii_String">String</a> contains only "printable"
characters you should use the <a href="../sui_std/ascii#std_ascii_all_characters_printable">all_characters_printable</a> predicate
defined in this module.

<code><b>public</b> <b>struct</b> <a href="../sui_std/ascii#std_ascii_String">String</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>bytes: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Char</code>

An ASCII character.

<code><b>public</b> <b>struct</b> <a href="../sui_std/ascii#std_ascii_Char">Char</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a></code>
</dt>
<dd>
</dd>
</dl>

Constants

An invalid ASCII character was encountered when creating an ASCII string.

<code><b>const</b> <a href="../sui_std/ascii#std_ascii_EInvalidASCIICharacter">EInvalidASCIICharacter</a>: <a href="../sui_std/u64#std_u64">u64</a> = 65536;
</code>

An invalid index was encountered when creating a substring.

<code><b>const</b> <a href="../sui_std/ascii#std_ascii_EInvalidIndex">EInvalidIndex</a>: <a href="../sui_std/u64#std_u64">u64</a> = 65537;
</code>

Function <code>char</code>

Convert a <a href="../sui_std/ascii#std_ascii_byte">byte</a> into a <a href="../sui_std/ascii#std_ascii_Char">Char</a> that is checked to make sure it is valid ASCII.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_char">char</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/ascii#std_ascii_Char">std::ascii::Char</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_char">char</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/ascii#std_ascii_Char">Char</a> {
    <b>assert</b>!(<a href="../sui_std/ascii#std_ascii_is_valid_char">is_valid_char</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>), <a href="../sui_std/ascii#std_ascii_EInvalidASCIICharacter">EInvalidASCIICharacter</a>);
    <a href="../sui_std/ascii#std_ascii_Char">Char</a> { <a href="../sui_std/ascii#std_ascii_byte">byte</a> }
}
</code></pre>

Function <code>string</code>

Convert a vector of bytes bytes into an <a href="../sui_std/ascii#std_ascii_String">String</a>. Aborts if
bytes contains non-ASCII characters.

<code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string">string</a>(bytes: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/string#std_string">string</a>(bytes: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/ascii#std_ascii_String">String</a> {
    <b>let</b> x = <a href="../sui_std/ascii#std_ascii_try_string">try_string</a>(bytes);
    <b>assert</b>!(x.is_some(), <a href="../sui_std/ascii#std_ascii_EInvalidASCIICharacter">EInvalidASCIICharacter</a>);
    x.destroy_some()
}
</code></pre>

Function <code>try_string</code>

Convert a vector of bytes bytes into an <a href="../sui_std/ascii#std_ascii_String">String</a>. Returns
Some(&lt;ascii_string&gt;) if the bytes contains all valid ASCII
characters. Otherwise returns None.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_try_string">try_string</a>(bytes: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_try_string">try_string</a>(bytes: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;): Option&lt;<a href="../sui_std/ascii#std_ascii_String">String</a>&gt; {
    <b>let</b> is_valid = bytes.all!(|<a href="../sui_std/ascii#std_ascii_byte">byte</a>| <a href="../sui_std/ascii#std_ascii_is_valid_char">is_valid_char</a>(*<a href="../sui_std/ascii#std_ascii_byte">byte</a>));
    <b>if</b> (is_valid) <a href="../sui_std/option#std_option_some">option::some</a>(<a href="../sui_std/ascii#std_ascii_String">String</a> { bytes }) <b>else</b> <a href="../sui_std/option#std_option_none">option::none</a>()
}
</code></pre>

Function <code>all_characters_printable</code>

Returns <b>true</b> if all characters in <a href="../sui_std/string#std_string">string</a> are printable characters
Returns <b>false</b> otherwise. Not all <a href="../sui_std/ascii#std_ascii_String">String</a>s are printable strings.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_all_characters_printable">all_characters_printable</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_all_characters_printable">all_characters_printable</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <a href="../sui_std/string#std_string">string</a>.bytes.all!(|<a href="../sui_std/ascii#std_ascii_byte">byte</a>| <a href="../sui_std/ascii#std_ascii_is_printable_char">is_printable_char</a>(*<a href="../sui_std/ascii#std_ascii_byte">byte</a>))
}
</code></pre>

Function <code>push_char</code>

Push a <a href="../sui_std/ascii#std_ascii_Char">Char</a> to the end of the <a href="../sui_std/string#std_string">string</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_push_char">push_char</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, <a href="../sui_std/ascii#std_ascii_char">char</a>: <a href="../sui_std/ascii#std_ascii_Char">std::ascii::Char</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_push_char">push_char</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">String</a>, <a href="../sui_std/ascii#std_ascii_char">char</a>: <a href="../sui_std/ascii#std_ascii_Char">Char</a>) {
    <a href="../sui_std/string#std_string">string</a>.bytes.push_back(<a href="../sui_std/ascii#std_ascii_char">char</a>.<a href="../sui_std/ascii#std_ascii_byte">byte</a>);
}
</code></pre>

Function <code>pop_char</code>

Pop a <a href="../sui_std/ascii#std_ascii_Char">Char</a> from the end of the <a href="../sui_std/string#std_string">string</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_pop_char">pop_char</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/ascii#std_ascii_Char">std::ascii::Char</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_pop_char">pop_char</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/ascii#std_ascii_Char">Char</a> {
    <a href="../sui_std/ascii#std_ascii_Char">Char</a> { <a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/string#std_string">string</a>.bytes.pop_back() }
}
</code></pre>

Function <code>length</code>

Returns the length of the <a href="../sui_std/string#std_string">string</a> in bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_length">length</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_length">length</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    <a href="../sui_std/string#std_string">string</a>.<a href="../sui_std/ascii#std_ascii_as_bytes">as_bytes</a>().<a href="../sui_std/ascii#std_ascii_length">length</a>()
}
</code></pre>

Function <code>append</code>

Append the other string to the end of <a href="../sui_std/string#std_string">string</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_append">append</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, other: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_append">append</a>(<a href="../sui_std/string#std_string">string</a>: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">String</a>, other: <a href="../sui_std/ascii#std_ascii_String">String</a>) {
    <a href="../sui_std/string#std_string">string</a>.bytes.<a href="../sui_std/ascii#std_ascii_append">append</a>(other.<a href="../sui_std/ascii#std_ascii_into_bytes">into_bytes</a>())
}
</code></pre>

Function <code>insert</code>

Insert the other string at the at index of <a href="../sui_std/string#std_string">string</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_insert">insert</a>(s: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, at: <a href="../sui_std/u64#std_u64">u64</a>, o: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_insert">insert</a>(s: &<b>mut</b> <a href="../sui_std/ascii#std_ascii_String">String</a>, at: <a href="../sui_std/u64#std_u64">u64</a>, o: <a href="../sui_std/ascii#std_ascii_String">String</a>) {
    <b>assert</b>!(at &lt;= s.<a href="../sui_std/ascii#std_ascii_length">length</a>(), <a href="../sui_std/ascii#std_ascii_EInvalidIndex">EInvalidIndex</a>);
    o.<a href="../sui_std/ascii#std_ascii_into_bytes">into_bytes</a>().destroy!(|e| s.bytes.<a href="../sui_std/ascii#std_ascii_insert">insert</a>(e, at));
}
</code></pre>

Function <code>substring</code>

Copy the slice of the <a href="../sui_std/string#std_string">string</a> from i to j into a new <a href="../sui_std/ascii#std_ascii_String">String</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_substring">substring</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_substring">substring</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>, i: <a href="../sui_std/u64#std_u64">u64</a>, j: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/ascii#std_ascii_String">String</a> {
    <b>assert</b>!(i &lt;= j && j &lt;= <a href="../sui_std/string#std_string">string</a>.<a href="../sui_std/ascii#std_ascii_length">length</a>(), <a href="../sui_std/ascii#std_ascii_EInvalidIndex">EInvalidIndex</a>);
    <b>let</b> <b>mut</b> bytes = <a href="../sui_std/vector#std_vector">vector</a>[];
    i.range_do!(j, |i| bytes.push_back(<a href="../sui_std/string#std_string">string</a>.bytes[i]));
    <a href="../sui_std/ascii#std_ascii_String">String</a> { bytes }
}
</code></pre>

Function <code>as_bytes</code>

Get the inner bytes of the <a href="../sui_std/string#std_string">string</a> as a reference

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_as_bytes">as_bytes</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_as_bytes">as_bytes</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): &<a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    &<a href="../sui_std/string#std_string">string</a>.bytes
}
</code></pre>

Function <code>into_bytes</code>

Unpack the <a href="../sui_std/string#std_string">string</a> to get its backing bytes

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_into_bytes">into_bytes</a>(<a href="../sui_std/string#std_string">string</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_into_bytes">into_bytes</a>(<a href="../sui_std/string#std_string">string</a>: <a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt; {
    <b>let</b> <a href="../sui_std/ascii#std_ascii_String">String</a> { bytes } = <a href="../sui_std/string#std_string">string</a>;
    bytes
}
</code></pre>

Function <code>byte</code>

Unpack the <a href="../sui_std/ascii#std_ascii_char">char</a> into its underlying bytes.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_byte">byte</a>(<a href="../sui_std/ascii#std_ascii_char">char</a>: <a href="../sui_std/ascii#std_ascii_Char">std::ascii::Char</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_byte">byte</a>(<a href="../sui_std/ascii#std_ascii_char">char</a>: <a href="../sui_std/ascii#std_ascii_Char">Char</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <b>let</b> <a href="../sui_std/ascii#std_ascii_Char">Char</a> { <a href="../sui_std/ascii#std_ascii_byte">byte</a> } = <a href="../sui_std/ascii#std_ascii_char">char</a>;
    <a href="../sui_std/ascii#std_ascii_byte">byte</a>
}
</code></pre>

Function <code>is_valid_char</code>

Returns <b>true</b> if b is a valid ASCII character.
Returns <b>false</b> otherwise.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_valid_char">is_valid_char</a>(b: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_valid_char">is_valid_char</a>(b: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    b &lt;= 0x7F
}
</code></pre>

Function <code>is_printable_char</code>

Returns <b>true</b> if <a href="../sui_std/ascii#std_ascii_byte">byte</a> is a printable ASCII character.
Returns <b>false</b> otherwise.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_printable_char">is_printable_char</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_printable_char">is_printable_char</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <a href="../sui_std/ascii#std_ascii_byte">byte</a> &gt;= 0x20 && // Disallow metacharacters
        <a href="../sui_std/ascii#std_ascii_byte">byte</a> &lt;= 0x7E // Don't allow DEL metacharacter
}
</code></pre>

Function <code>is_empty</code>

Returns <b>true</b> if <a href="../sui_std/string#std_string">string</a> is empty.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_empty">is_empty</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_is_empty">is_empty</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <a href="../sui_std/string#std_string">string</a>.bytes.<a href="../sui_std/ascii#std_ascii_is_empty">is_empty</a>()
}
</code></pre>

Function <code>to_uppercase</code>

Convert a <a href="../sui_std/string#std_string">string</a> to its uppercase equivalent.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_to_uppercase">to_uppercase</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_to_uppercase">to_uppercase</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/ascii#std_ascii_String">String</a> {
    <b>let</b> bytes = <a href="../sui_std/string#std_string">string</a>.<a href="../sui_std/ascii#std_ascii_as_bytes">as_bytes</a>().map_ref!(|<a href="../sui_std/ascii#std_ascii_byte">byte</a>| <a href="../sui_std/ascii#std_ascii_char_to_uppercase">char_to_uppercase</a>(*<a href="../sui_std/ascii#std_ascii_byte">byte</a>));
    <a href="../sui_std/ascii#std_ascii_String">String</a> { bytes }
}
</code></pre>

Function <code>to_lowercase</code>

Convert a <a href="../sui_std/string#std_string">string</a> to its lowercase equivalent.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_to_lowercase">to_lowercase</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_to_lowercase">to_lowercase</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/ascii#std_ascii_String">String</a> {
    <b>let</b> bytes = <a href="../sui_std/string#std_string">string</a>.<a href="../sui_std/ascii#std_ascii_as_bytes">as_bytes</a>().map_ref!(|<a href="../sui_std/ascii#std_ascii_byte">byte</a>| <a href="../sui_std/ascii#std_ascii_char_to_lowercase">char_to_lowercase</a>(*<a href="../sui_std/ascii#std_ascii_byte">byte</a>));
    <a href="../sui_std/ascii#std_ascii_String">String</a> { bytes }
}
</code></pre>

Function <code>index_of</code>

Computes the index of the first occurrence of the substr in the <a href="../sui_std/string#std_string">string</a>.
Returns the length of the <a href="../sui_std/string#std_string">string</a> if the substr is not found.
Returns 0 if the substr is empty.

<code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_index_of">index_of</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>, substr: &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/ascii#std_ascii_index_of">index_of</a>(<a href="../sui_std/string#std_string">string</a>: &<a href="../sui_std/ascii#std_ascii_String">String</a>, substr: &<a href="../sui_std/ascii#std_ascii_String">String</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    <b>let</b> <b>mut</b> i = 0;
    <b>let</b> (n, m) = (<a href="../sui_std/string#std_string">string</a>.<a href="../sui_std/ascii#std_ascii_length">length</a>(), substr.<a href="../sui_std/ascii#std_ascii_length">length</a>());
    <b>if</b> (n &lt; m) <b>return</b> n;
    <b>while</b> (i &lt;= n - m) {
        <b>let</b> <b>mut</b> j = 0;
        <b>while</b> (j &lt; m && <a href="../sui_std/string#std_string">string</a>.bytes[i + j] == substr.bytes[j]) j = j + 1;
        <b>if</b> (j == m) <b>return</b> i;
        i = i + 1;
    };
    n
}
</code></pre>

Function <code>char_to_uppercase</code>

Convert a <a href="../sui_std/ascii#std_ascii_char">char</a> to its lowercase equivalent.

<code><b>fun</b> <a href="../sui_std/ascii#std_ascii_char_to_uppercase">char_to_uppercase</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_std/ascii#std_ascii_char_to_uppercase">char_to_uppercase</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <b>if</b> (<a href="../sui_std/ascii#std_ascii_byte">byte</a> &gt;= 0x61 && <a href="../sui_std/ascii#std_ascii_byte">byte</a> &lt;= 0x7A) <a href="../sui_std/ascii#std_ascii_byte">byte</a> - 0x20 <b>else</b> <a href="../sui_std/ascii#std_ascii_byte">byte</a>
}
</code></pre>

Function <code>char_to_lowercase</code>

Convert a <a href="../sui_std/ascii#std_ascii_char">char</a> to its lowercase equivalent.

<code><b>fun</b> <a href="../sui_std/ascii#std_ascii_char_to_lowercase">char_to_lowercase</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_std/ascii#std_ascii_char_to_lowercase">char_to_lowercase</a>(<a href="../sui_std/ascii#std_ascii_byte">byte</a>: <a href="../sui_std/u8#std_u8">u8</a>): <a href="../sui_std/u8#std_u8">u8</a> {
    <b>if</b> (<a href="../sui_std/ascii#std_ascii_byte">byte</a> &gt;= 0x41 && <a href="../sui_std/ascii#std_ascii_byte">byte</a> &lt;= 0x5A) <a href="../sui_std/ascii#std_ascii_byte">byte</a> + 0x20 <b>else</b> <a href="../sui_std/ascii#std_ascii_byte">byte</a>
}
</code></pre>