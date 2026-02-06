Functionality for converting Move types into values. Use with care!

-  [Struct TypeName](#std_type_name_TypeName)
-  [Constants](#@Constants_0)
-  [Function with_defining_ids](#std_type_name_with_defining_ids)
-  [Function with_original_ids](#std_type_name_with_original_ids)
-  [Function defining_id](#std_type_name_defining_id)
-  [Function original_id](#std_type_name_original_id)
-  [Function is_primitive](#std_type_name_is_primitive)
-  [Function as_string](#std_type_name_as_string)
-  [Function address_string](#std_type_name_address_string)
-  [Function module_string](#std_type_name_module_string)
-  [Function datatype_string](#std_type_name_datatype_string)
-  [Function into_string](#std_type_name_into_string)
-  [Function get](#std_type_name_get)
-  [Function get_with_original_ids](#std_type_name_get_with_original_ids)
-  [Function borrow_string](#std_type_name_borrow_string)
-  [Function get_address](#std_type_name_get_address)
-  [Function get_module](#std_type_name_get_module)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>TypeName</code>

<code><b>public</b> <b>struct</b> <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>name: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a></code>
</dt>
<dd>
 String representation of the type. All types are represented
 using their source syntax:
 "u8", "u64", "bool", "address", "vector", and so on for primitive types.
 Struct types are represented as fully qualified type names; e.g.
 <code>00000000000000000000000000000001::string::String</code> or
 <code>0000000000000000000000000000000a::module_name1::type_name1&lt;0000000000000000000000000000000a::module_name2::type_name2&lt;<a href="../sui_std/u64#std_u64">u64</a>&gt;&gt;</code>
 Addresses are hex-encoded lowercase values of length ADDRESS_LENGTH (16, 20, or 32 depending on the Move platform)
</dd>
</dl>

Constants

ASCII Character code for the : (colon) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_COLON">ASCII_COLON</a>: <a href="../sui_std/u8#std_u8">u8</a> = 58;
</code>

ASCII Character code for the &lt; (less than) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_LESS_THAN">ASCII_LESS_THAN</a>: <a href="../sui_std/u8#std_u8">u8</a> = 60;
</code>

ASCII Character code for the v (lowercase v) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_V">ASCII_V</a>: <a href="../sui_std/u8#std_u8">u8</a> = 118;
</code>

ASCII Character code for the e (lowercase e) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_E">ASCII_E</a>: <a href="../sui_std/u8#std_u8">u8</a> = 101;
</code>

ASCII Character code for the c (lowercase c) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_C">ASCII_C</a>: <a href="../sui_std/u8#std_u8">u8</a> = 99;
</code>

ASCII Character code for the t (lowercase t) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_T">ASCII_T</a>: <a href="../sui_std/u8#std_u8">u8</a> = 116;
</code>

ASCII Character code for the o (lowercase o) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_O">ASCII_O</a>: <a href="../sui_std/u8#std_u8">u8</a> = 111;
</code>

ASCII Character code for the r (lowercase r) symbol.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ASCII_R">ASCII_R</a>: <a href="../sui_std/u8#std_u8">u8</a> = 114;
</code>

The type is not from a package/module. It is a primitive type.

<code><b>const</b> <a href="../sui_std/type_name#std_type_name_ENonModuleType">ENonModuleType</a>: <a href="../sui_std/u64#std_u64">u64</a> = 0;
</code>

Function <code>with_defining_ids</code>

Return a value representation of the type T. Package IDs that appear in fully qualified type
names in the output from this function are defining IDs (the ID of the package in storage that
first introduced the type).

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_with_defining_ids">with_defining_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_with_defining_ids">with_defining_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>;
</code></pre>

Function <code>with_original_ids</code>

Return a value representation of the type T. Package IDs that appear in fully qualified type
names in the output from this function are original IDs (the ID of the first version of
the package, even if the type in question was introduced in a later upgrade).

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_with_original_ids">with_original_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_with_original_ids">with_original_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>;
</code></pre>

Function <code>defining_id</code>

Like <a href="../sui_std/type_name#std_type_name_with_defining_ids">with_defining_ids</a>, this accesses the package ID that original defined the type T.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_defining_id">defining_id</a>&lt;T&gt;(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_defining_id">defining_id</a>&lt;T&gt;(): <b>address</b>;
</code></pre>

Function <code>original_id</code>

Like <a href="../sui_std/type_name#std_type_name_with_original_ids">with_original_ids</a>, this accesses the original ID of the package that defines type T,
even if the type was introduced in a later version of the package.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_original_id">original_id</a>&lt;T&gt;(): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_original_id">original_id</a>&lt;T&gt;(): <b>address</b>;
</code></pre>

Function <code>is_primitive</code>

Returns true iff the TypeName represents a primitive type, i.e. one of
u8, u16, u32, u64, u128, u256, bool, address, vector.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_is_primitive">is_primitive</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_is_primitive">is_primitive</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <b>let</b> bytes = self.name.as_bytes();
    bytes == &b"<a href="../sui_std/bool#std_bool">bool</a>" ||
        bytes == &b"<a href="../sui_std/u8#std_u8">u8</a>" ||
        bytes == &b"<a href="../sui_std/u16#std_u16">u16</a>" ||
        bytes == &b"<a href="../sui_std/u32#std_u32">u32</a>" ||
        bytes == &b"<a href="../sui_std/u64#std_u64">u64</a>" ||
        bytes == &b"<a href="../sui_std/u128#std_u128">u128</a>" ||
        bytes == &b"<a href="../sui_std/u256#std_u256">u256</a>" ||
        bytes == &b"<b>address</b>" ||
        (
            bytes.length() &gt;= 6 &&
            bytes[0] == <a href="../sui_std/type_name#std_type_name_ASCII_V">ASCII_V</a> &&
            bytes[1] == <a href="../sui_std/type_name#std_type_name_ASCII_E">ASCII_E</a> &&
            bytes[2] == <a href="../sui_std/type_name#std_type_name_ASCII_C">ASCII_C</a> &&
            bytes[3] == <a href="../sui_std/type_name#std_type_name_ASCII_T">ASCII_T</a> &&
            bytes[4] == <a href="../sui_std/type_name#std_type_name_ASCII_O">ASCII_O</a> &&
            bytes[5] == <a href="../sui_std/type_name#std_type_name_ASCII_R">ASCII_R</a>,
        )
}
</code></pre>

Function <code>as_string</code>

Get the String representation of self

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_as_string">as_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_as_string">as_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): &String {
    &self.name
}
</code></pre>

Function <code>address_string</code>

Get Address string (Base16 encoded), first part of the TypeName.
Aborts if given a primitive type.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_address_string">address_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_address_string">address_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    <b>assert</b>!(!self.<a href="../sui_std/type_name#std_type_name_is_primitive">is_primitive</a>(), <a href="../sui_std/type_name#std_type_name_ENonModuleType">ENonModuleType</a>);
    // Base16 (<a href="../sui_std/string#std_string">string</a>) representation of an <b>address</b> <b>has</b> 2 symbols per byte.
    <b>let</b> len = <a href="../sui_std/address#std_address_length">address::length</a>() * 2;
    <b>let</b> str_bytes = self.name.as_bytes();
    <b>let</b> <b>mut</b> addr_bytes = <a href="../sui_std/vector#std_vector">vector</a>[];
    <b>let</b> <b>mut</b> i = 0;
    // Read <span className="code-inline">len</span> bytes from the type name and push them to addr_bytes.
    <b>while</b> (i &lt; len) {
        addr_bytes.push_back(str_bytes[i]);
        i = i + 1;
    };
    <a href="../sui_std/ascii#std_ascii_string">ascii::string</a>(addr_bytes)
}
</code></pre>

Function <code>module_string</code>

Get name of the module.
Aborts if given a primitive type.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_module_string">module_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_module_string">module_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    <b>assert</b>!(!self.<a href="../sui_std/type_name#std_type_name_is_primitive">is_primitive</a>(), <a href="../sui_std/type_name#std_type_name_ENonModuleType">ENonModuleType</a>);
    // Starts after <b>address</b> and a double colon: <span className="code-inline">&lt;addr <b>as</b> HEX&gt;::</span>
    <b>let</b> <b>mut</b> i = <a href="../sui_std/address#std_address_length">address::length</a>() * 2 + 2;
    <b>let</b> str_bytes = self.name.as_bytes();
    <b>let</b> <b>mut</b> module_name = <a href="../sui_std/vector#std_vector">vector</a>[];
    <b>let</b> colon = <a href="../sui_std/type_name#std_type_name_ASCII_COLON">ASCII_COLON</a>;
    <b>loop</b> {
        <b>let</b> char = &str_bytes[i];
        <b>if</b> (char != &colon) {
            module_name.push_back(*char);
            i = i + 1;
        } <b>else</b> {
            <b>break</b>
        }
    };
    <a href="../sui_std/ascii#std_ascii_string">ascii::string</a>(module_name)
}
</code></pre>

Function <code>datatype_string</code>

Get name of the datatype (struct or enum).
Aborts if given a primitive type.

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_datatype_string">datatype_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_datatype_string">datatype_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    <b>assert</b>!(!self.<a href="../sui_std/type_name#std_type_name_is_primitive">is_primitive</a>(), <a href="../sui_std/type_name#std_type_name_ENonModuleType">ENonModuleType</a>);
    // Starts after <b>address</b> and a double colon: <span className="code-inline">&lt;addr <b>as</b> HEX&gt;::</span>
    <b>let</b> <b>mut</b> i = <a href="../sui_std/address#std_address_length">address::length</a>() * 2 + 2;
    <b>let</b> str_bytes = self.name.as_bytes();
    <b>let</b> str_bytes_len = str_bytes.length();
    <b>let</b> colon = <a href="../sui_std/type_name#std_type_name_ASCII_COLON">ASCII_COLON</a>;
    // Skip past the <span className="code-inline">&lt;module_name&gt;::</span> to the datatype name.
    // The asserts should never fail, since all non-primitive types should have two colons.
    <b>while</b> (&str_bytes[i] != &colon) i = i + 1;
    i = i + 1;
    <b>assert</b>!(&str_bytes[i] == &colon);
    i = i + 1;
    <b>assert</b>!(&str_bytes[i] != &colon);
    // Take all characters until the type parameters start at <span className="code-inline">&lt;</span>, or until the end of the <a href="../sui_std/string#std_string">string</a>.
    <b>let</b> <b>mut</b> datatype_name = <a href="../sui_std/vector#std_vector">vector</a>[];
    <b>let</b> lt = <a href="../sui_std/type_name#std_type_name_ASCII_LESS_THAN">ASCII_LESS_THAN</a>;
    <b>loop</b> {
        <b>let</b> char = &str_bytes[i];
        <b>if</b> (char == &lt) <b>break</b>;
        datatype_name.push_back(*char);
        i = i + 1;
        <b>if</b> (i &gt;= str_bytes_len) <b>break</b>;
    };
    <a href="../sui_std/ascii#std_ascii_string">ascii::string</a>(datatype_name)
}
</code></pre>

Function <code>into_string</code>

Convert self into its inner String

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_into_string">into_string</a>(self: <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_into_string">into_string</a>(self: <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    self.name
}
</code></pre>

Function <code>get</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get">get</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get">get</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a> {
    <a href="../sui_std/type_name#std_type_name_with_defining_ids">with_defining_ids</a>&lt;T&gt;()
}
</code></pre>

Function <code>get_with_original_ids</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_with_original_ids">get_with_original_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_with_original_ids">get_with_original_ids</a>&lt;T&gt;(): <a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a> {
    <a href="../sui_std/type_name#std_type_name_with_original_ids">with_original_ids</a>&lt;T&gt;()
}
</code></pre>

Function <code>borrow_string</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_borrow_string">borrow_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_borrow_string">borrow_string</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): &String {
    self.<a href="../sui_std/type_name#std_type_name_as_string">as_string</a>()
}
</code></pre>

Function <code>get_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_address">get_address</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_address">get_address</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    self.<a href="../sui_std/type_name#std_type_name_address_string">address_string</a>()
}
</code></pre>

Function <code>get_module</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_module">get_module</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>): <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/type_name#std_type_name_get_module">get_module</a>(self: &<a href="../sui_std/type_name#std_type_name_TypeName">TypeName</a>): String {
    self.<a href="../sui_std/type_name#std_type_name_module_string">module_string</a>()
}
</code></pre>