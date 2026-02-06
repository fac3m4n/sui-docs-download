URL: standard Uniform Resource Locator string

-  [Struct Url](#sui_url_Url)
-  [Function new_unsafe](#sui_url_new_unsafe)
-  [Function new_unsafe_from_bytes](#sui_url_new_unsafe_from_bytes)
-  [Function inner_url](#sui_url_inner_url)
-  [Function update](#sui_url_update)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>Url</code>

Standard Uniform Resource Locator (URL) string.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/url#sui_url_Url">Url</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/url#sui_url">url</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a></code>
</dt>
<dd>
</dd>
</dl>

Function <code>new_unsafe</code>

Create a <a href="../sui_sui/url#sui_url_Url">Url</a>, with no validation

<code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_new_unsafe">new_unsafe</a>(<a href="../sui_sui/url#sui_url">url</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>): <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_new_unsafe">new_unsafe</a>(<a href="../sui_sui/url#sui_url">url</a>: String): <a href="../sui_sui/url#sui_url_Url">Url</a> {
    <a href="../sui_sui/url#sui_url_Url">Url</a> { <a href="../sui_sui/url#sui_url">url</a> }
}
</code></pre>

Function <code>new_unsafe_from_bytes</code>

Create a <a href="../sui_sui/url#sui_url_Url">Url</a> with no validation from bytes
Note: this will abort if bytes is not valid ASCII

<code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_new_unsafe_from_bytes">new_unsafe_from_bytes</a>(bytes: vector&lt;u8&gt;): <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_new_unsafe_from_bytes">new_unsafe_from_bytes</a>(bytes: vector&lt;u8&gt;): <a href="../sui_sui/url#sui_url_Url">Url</a> {
    <b>let</b> <a href="../sui_sui/url#sui_url">url</a> = bytes.to_ascii_string();
    <a href="../sui_sui/url#sui_url_Url">Url</a> { <a href="../sui_sui/url#sui_url">url</a> }
}
</code></pre>

Function <code>inner_url</code>

Get inner URL

<code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_inner_url">inner_url</a>(self: &<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_inner_url">inner_url</a>(self: &<a href="../sui_sui/url#sui_url_Url">Url</a>): String {
    self.<a href="../sui_sui/url#sui_url">url</a>
}
</code></pre>

Function <code>update</code>

Update the inner URL

<code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_update">update</a>(self: &<b>mut</b> <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>, <a href="../sui_sui/url#sui_url">url</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/url#sui_url_update">update</a>(self: &<b>mut</b> <a href="../sui_sui/url#sui_url_Url">Url</a>, <a href="../sui_sui/url#sui_url">url</a>: String) {
    self.<a href="../sui_sui/url#sui_url">url</a> = <a href="../sui_sui/url#sui_url">url</a>;
}
</code></pre>