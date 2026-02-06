Defines a Display struct which defines the way an Object
should be displayed. The intention is to keep data as independent
from its display as possible, protecting the development process
and keeping it separate from the ecosystem agreements.

Each of the fields of the Display object should allow for pattern
substitution and filling-in the pieces using the data from the object T.

More entry functions might be added in the future depending on the use cases.

-  [Struct Display](#sui_display_Display)
-  [Struct DisplayCreated](#sui_display_DisplayCreated)
-  [Struct VersionUpdated](#sui_display_VersionUpdated)
-  [Constants](#@Constants_0)
-  [Function new](#sui_display_new)
-  [Function new_with_fields](#sui_display_new_with_fields)
-  [Function create_and_keep](#sui_display_create_and_keep)
-  [Function update_version](#sui_display_update_version)
-  [Function add](#sui_display_add)
-  [Function add_multiple](#sui_display_add_multiple)
-  [Function edit](#sui_display_edit)
-  [Function remove](#sui_display_remove)
-  [Function is_authorized](#sui_display_is_authorized)
-  [Function version](#sui_display_version)
-  [Function fields](#sui_display_fields)
-  [Function create_internal](#sui_display_create_internal)
-  [Function add_internal](#sui_display_add_internal)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/accumulator#sui_accumulator">sui::accumulator</a>;
<b>use</b> <a href="../sui_sui/accumulator_settlement#sui_accumulator_settlement">sui::accumulator_settlement</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/bcs#sui_bcs">sui::bcs</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/event#sui_event">sui::event</a>;
<b>use</b> <a href="../sui_sui/hash#sui_hash">sui::hash</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/package#sui_package">sui::package</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Display</code>

The Display<T> object. Defines the way a T instance should be
displayed. Display object can only be created and modified with
a PublisherCap, making sure that the rules are set by the owner
of the type.

Each of the display properties should support patterns outside
of the system, making it simpler to customize Display based
on the property values of an Object.
```
// Example of a display object
Display<0x...::capy::Capy> {
fields:
<name, "Capy { genes }">
<link, "https://capy.art/capy/{ id }">
<image, "https://api.capy.art/capy/{ id }/svg">
<description, "Lovely Capy, one of many">
}
```

Uses only String type due to external-facing nature of the object,
the property names have a priority over their types.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;<b>phantom</b> T: key&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/display#sui_display_fields">fields</a>: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
 Contains fields for display. Currently supported
 fields are: name, link, image and description.
</dd>
<dt>
<code><a href="../sui_sui/display#sui_display_version">version</a>: u16</code>
</dt>
<dd>
 Version that can only be updated manually by the Publisher.
</dd>
</dl>

Struct <code>DisplayCreated</code>

Event: emitted when a new Display object has been created for type T.
Type signature of the event corresponds to the type while id serves for
the discovery.

Since Sui RPC supports querying events by type, finding a Display for the T
would be as simple as looking for the first event with <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/display#sui_display_DisplayCreated">DisplayCreated</a>&lt;<b>phantom</b> T: key&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>VersionUpdated</code>

Version of Display got updated -

<code><b>public</b> <b>struct</b> <a href="../sui_sui/display#sui_display_VersionUpdated">VersionUpdated</a>&lt;<b>phantom</b> T: key&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/display#sui_display_version">version</a>: u16</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/display#sui_display_fields">fields</a>: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

For when T does not belong to the package Publisher.

<code><b>const</b> <a href="../sui_sui/display#sui_display_ENotOwner">ENotOwner</a>: u64 = 0;
</code>

For when vectors passed into one of the multiple insert functions
don't match in their lengths.

<code><b>const</b> <a href="../sui_sui/display#sui_display_EVecLengthMismatch">EVecLengthMismatch</a>: u64 = 1;
</code>

Function <code>new</code>

Create an empty Display object. It can either be shared empty or filled
with data right away via cheaper set_owned method.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_new">new</a>&lt;T: key&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_new">new</a>&lt;T: key&gt;(pub: &Publisher, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt; {
    <b>assert</b>!(<a href="../sui_sui/display#sui_display_is_authorized">is_authorized</a>&lt;T&gt;(pub), <a href="../sui_sui/display#sui_display_ENotOwner">ENotOwner</a>);
    <a href="../sui_sui/display#sui_display_create_internal">create_internal</a>(ctx)
}
</code></pre>

Function <code>new_with_fields</code>

Create a new Display<T> object with a set of fields.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_new_with_fields">new_with_fields</a>&lt;T: key&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>, <a href="../sui_sui/display#sui_display_fields">fields</a>: vector&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;, values: vector&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_new_with_fields">new_with_fields</a>&lt;T: key&gt;(
    pub: &Publisher,
    <a href="../sui_sui/display#sui_display_fields">fields</a>: vector&lt;String&gt;,
    values: vector&lt;String&gt;,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt; {
    <b>let</b> len = <a href="../sui_sui/display#sui_display_fields">fields</a>.length();
    <b>assert</b>!(len == values.length(), <a href="../sui_sui/display#sui_display_EVecLengthMismatch">EVecLengthMismatch</a>);
    <b>let</b> <b>mut</b> <a href="../sui_sui/display#sui_display">display</a> = <a href="../sui_sui/display#sui_display_new">new</a>&lt;T&gt;(pub, ctx);
    <a href="../sui_sui/display#sui_display_fields">fields</a>.zip_do!(values, |field, value| <a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_add_internal">add_internal</a>(field, value));
    <a href="../sui_sui/display#sui_display">display</a>
}
</code></pre>

Function <code>create_and_keep</code>

Create a new empty Display<T> object and keep it.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_create_and_keep">create_and_keep</a>&lt;T: key&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_create_and_keep">create_and_keep</a>&lt;T: key&gt;(pub: &Publisher, ctx: &<b>mut</b> TxContext) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">transfer::public_transfer</a>(<a href="../sui_sui/display#sui_display_new">new</a>&lt;T&gt;(pub, ctx), ctx.sender())
}
</code></pre>

Function <code>update_version</code>

Manually bump the version and emit an event with the updated version's contents.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_update_version">update_version</a>&lt;T: key&gt;(<a href="../sui_sui/display#sui_display">display</a>: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_update_version">update_version</a>&lt;T: key&gt;(<a href="../sui_sui/display#sui_display">display</a>: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;) {
    <a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_version">version</a> = <a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_version">version</a> + 1;
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/display#sui_display_VersionUpdated">VersionUpdated</a>&lt;T&gt; {
        <a href="../sui_sui/display#sui_display_version">version</a>: <a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_version">version</a>,
        <a href="../sui_sui/display#sui_display_fields">fields</a>: *&<a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_fields">fields</a>,
        id: <a href="../sui_sui/display#sui_display">display</a>.id.to_inner(),
    })
}
</code></pre>

Function <code>add</code>

Sets a custom name field with the value.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_add">add</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>, value: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_add">add</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;, name: String, value: String) {
    self.<a href="../sui_sui/display#sui_display_add_internal">add_internal</a>(name, value)
}
</code></pre>

Function <code>add_multiple</code>

Sets multiple <a href="../sui_sui/display#sui_display_fields">fields</a> with values.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_add_multiple">add_multiple</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;, <a href="../sui_sui/display#sui_display_fields">fields</a>: vector&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;, values: vector&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_add_multiple">add_multiple</a>&lt;T: key&gt;(
    self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;,
    <a href="../sui_sui/display#sui_display_fields">fields</a>: vector&lt;String&gt;,
    values: vector&lt;String&gt;,
) {
    <b>let</b> len = <a href="../sui_sui/display#sui_display_fields">fields</a>.length();
    <b>assert</b>!(len == values.length(), <a href="../sui_sui/display#sui_display_EVecLengthMismatch">EVecLengthMismatch</a>);
    <a href="../sui_sui/display#sui_display_fields">fields</a>.zip_do!(values, |field, value| self.<a href="../sui_sui/display#sui_display_add_internal">add_internal</a>(field, value));
}
</code></pre>

Function <code>edit</code>

Change the value of the field.
TODO (long run): version changes;

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_edit">edit</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>, value: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_edit">edit</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;, name: String, value: String) {
    <b>let</b> (_, _) = self.<a href="../sui_sui/display#sui_display_fields">fields</a>.<a href="../sui_sui/display#sui_display_remove">remove</a>(&name);
    self.<a href="../sui_sui/display#sui_display_add_internal">add_internal</a>(name, value)
}
</code></pre>

Function <code>remove</code>

Remove the key from the Display.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_remove">remove</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/display#sui_display_remove">remove</a>&lt;T: key&gt;(self: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;, name: String) {
    self.<a href="../sui_sui/display#sui_display_fields">fields</a>.<a href="../sui_sui/display#sui_display_remove">remove</a>(&name);
}
</code></pre>

Function <code>is_authorized</code>

Authorization check; can be performed externally to implement protection rules for Display.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_is_authorized">is_authorized</a>&lt;T: key&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_is_authorized">is_authorized</a>&lt;T: key&gt;(pub: &Publisher): bool {
    pub.from_package&lt;T&gt;()
}
</code></pre>

Function <code>version</code>

Read the <a href="../sui_sui/display#sui_display_version">version</a> field.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_version">version</a>&lt;T: key&gt;(d: &<a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;): u16
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_version">version</a>&lt;T: key&gt;(d: &<a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;): u16 {
    d.<a href="../sui_sui/display#sui_display_version">version</a>
}
</code></pre>

Function <code>fields</code>

Read the <a href="../sui_sui/display#sui_display_fields">fields</a> field.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_fields">fields</a>&lt;T: key&gt;(d: &<a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;): &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/display#sui_display_fields">fields</a>&lt;T: key&gt;(d: &<a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;): &VecMap&lt;String, String&gt; {
    &d.<a href="../sui_sui/display#sui_display_fields">fields</a>
}
</code></pre>

Function <code>create_internal</code>

Internal function to create a new <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;.

<code><b>fun</b> <a href="../sui_sui/display#sui_display_create_internal">create_internal</a>&lt;T: key&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/display#sui_display_create_internal">create_internal</a>&lt;T: key&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt; {
    <b>let</b> uid = <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx);
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/display#sui_display_DisplayCreated">DisplayCreated</a>&lt;T&gt; {
        id: uid.to_inner(),
    });
    <a href="../sui_sui/display#sui_display_Display">Display</a> {
        id: uid,
        <a href="../sui_sui/display#sui_display_fields">fields</a>: <a href="../sui_sui/vec_map#sui_vec_map_empty">vec_map::empty</a>(),
        <a href="../sui_sui/display#sui_display_version">version</a>: 0,
    }
}
</code></pre>

Function <code>add_internal</code>

Private method for inserting fields without security checks.

<code><b>fun</b> <a href="../sui_sui/display#sui_display_add_internal">add_internal</a>&lt;T: key&gt;(<a href="../sui_sui/display#sui_display">display</a>: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">sui::display::Display</a>&lt;T&gt;, name: <a href="../sui_std/string#std_string_String">std::string::String</a>, value: <a href="../sui_std/string#std_string_String">std::string::String</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/display#sui_display_add_internal">add_internal</a>&lt;T: key&gt;(<a href="../sui_sui/display#sui_display">display</a>: &<b>mut</b> <a href="../sui_sui/display#sui_display_Display">Display</a>&lt;T&gt;, name: String, value: String) {
    <a href="../sui_sui/display#sui_display">display</a>.<a href="../sui_sui/display#sui_display_fields">fields</a>.insert(name, value)
}
</code></pre>