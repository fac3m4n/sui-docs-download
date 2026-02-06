-  [Struct VecMap](#sui_vec_map_VecMap)
-  [Struct Entry](#sui_vec_map_Entry)
-  [Constants](#@Constants_0)
-  [Function empty](#sui_vec_map_empty)
-  [Function insert](#sui_vec_map_insert)
-  [Function remove](#sui_vec_map_remove)
-  [Function pop](#sui_vec_map_pop)
-  [Function get_mut](#sui_vec_map_get_mut)
-  [Function get](#sui_vec_map_get)
-  [Function try_get](#sui_vec_map_try_get)
-  [Function contains](#sui_vec_map_contains)
-  [Function length](#sui_vec_map_length)
-  [Function is_empty](#sui_vec_map_is_empty)
-  [Function destroy_empty](#sui_vec_map_destroy_empty)
-  [Function into_keys_values](#sui_vec_map_into_keys_values)
-  [Function from_keys_values](#sui_vec_map_from_keys_values)
-  [Function keys](#sui_vec_map_keys)
-  [Function get_idx_opt](#sui_vec_map_get_idx_opt)
-  [Function get_idx](#sui_vec_map_get_idx)
-  [Function get_entry_by_idx](#sui_vec_map_get_entry_by_idx)
-  [Function get_entry_by_idx_mut](#sui_vec_map_get_entry_by_idx_mut)
-  [Function remove_entry_by_idx](#sui_vec_map_remove_entry_by_idx)
-  [Function size](#sui_vec_map_size)

<code><b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>VecMap</code>

A map data structure backed by a vector. The map is guaranteed not to contain duplicate keys, but entries
are *not* sorted by key--entries are included in insertion order.
All operations are O(N) in the size of the map--the intention of this data structure is only to provide
the convenience of programming against a map API.
Large maps should use handwritten parent/child relationships instead.
Maps that need sorted iteration rather than insertion order iteration should also be handwritten.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K: <b>copy</b>, V&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>contents: vector&lt;<a href="../sui_sui/vec_map#sui_vec_map_Entry">sui::vec_map::Entry</a>&lt;K, V&gt;&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Entry</code>

An entry in the map

<code><b>public</b> <b>struct</b> <a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a>&lt;K: <b>copy</b>, V&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>key: K</code>
</dt>
<dd>
</dd>
<dt>
<code>value: V</code>
</dt>
<dd>
</dd>
</dl>

Constants

This key already exists in the map

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EKeyAlreadyExists">EKeyAlreadyExists</a>: u64 = 0;
</code>

This key does not exist in the map

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EKeyDoesNotExist">EKeyDoesNotExist</a>: u64 = 1;
</code>

Trying to destroy a map that is not empty

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EMapNotEmpty">EMapNotEmpty</a>: u64 = 2;
</code>

Trying to access an element of the map at an invalid index

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EIndexOutOfBounds">EIndexOutOfBounds</a>: u64 = 3;
</code>

Trying to pop from a map that is empty

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EMapEmpty">EMapEmpty</a>: u64 = 4;
</code>

Trying to construct a map from keys and values of different lengths

<code><b>const</b> <a href="../sui_sui/vec_map#sui_vec_map_EUnequalLengths">EUnequalLengths</a>: u64 = 5;
</code>

Function <code>empty</code>

Create an empty <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_empty">empty</a>&lt;K: <b>copy</b>, V&gt;(): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_empty">empty</a>&lt;K: <b>copy</b>, V&gt;(): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt; {
    <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a> { contents: vector[] }
}
</code></pre>

Function <code>insert</code>

Insert the entry key |-> value into self.
Aborts if key is already bound in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_insert">insert</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: K, value: V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_insert">insert</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: K, value: V) {
    <b>assert</b>!(!self.<a href="../sui_sui/vec_map#sui_vec_map_contains">contains</a>(&key), <a href="../sui_sui/vec_map#sui_vec_map_EKeyAlreadyExists">EKeyAlreadyExists</a>);
    self.contents.push_back(<a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, value })
}
</code></pre>

Function <code>remove</code>

Remove the entry key |-> value from self. Aborts if key is not bound in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_remove">remove</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): (K, V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_remove">remove</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): (K, V) {
    <b>let</b> idx = self.<a href="../sui_sui/vec_map#sui_vec_map_get_idx">get_idx</a>(key);
    <b>let</b> <a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, value } = self.contents.<a href="../sui_sui/vec_map#sui_vec_map_remove">remove</a>(idx);
    (key, value)
}
</code></pre>

Function <code>pop</code>

Pop the most recently inserted entry from the map. Aborts if the map is empty.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_pop">pop</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): (K, V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_pop">pop</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): (K, V) {
    <b>assert</b>!(self.contents.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>() != 0, <a href="../sui_sui/vec_map#sui_vec_map_EMapEmpty">EMapEmpty</a>);
    <b>let</b> <a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, value } = self.contents.pop_back();
    (key, value)
}
</code></pre>

Function <code>get_mut</code>

Get a mutable reference to the value bound to key in self.
Aborts if key is not bound in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_mut">get_mut</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): &<b>mut</b> V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_mut">get_mut</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): &<b>mut</b> V {
    <b>let</b> idx = self.<a href="../sui_sui/vec_map#sui_vec_map_get_idx">get_idx</a>(key);
    <b>let</b> <b>entry</b> = &<b>mut</b> self.contents[idx];
    &<b>mut</b> <b>entry</b>.value
}
</code></pre>

Function <code>get</code>

Get a reference to the value bound to key in self.
Aborts if key is not bound in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get">get</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): &V
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get">get</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): &V {
    <b>let</b> idx = self.<a href="../sui_sui/vec_map#sui_vec_map_get_idx">get_idx</a>(key);
    <b>let</b> <b>entry</b> = &self.contents[idx];
    &<b>entry</b>.value
}
</code></pre>

Function <code>try_get</code>

Safely try borrow a value bound to key in self.
Return Some(V) if the value exists, None otherwise.
Only works for a "copyable" value as references cannot be stored in vector.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_try_get">try_get</a>&lt;K: <b>copy</b>, V: <b>copy</b>&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_try_get">try_get</a>&lt;K: <b>copy</b>, V: <b>copy</b>&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): Option&lt;V&gt; {
    <b>if</b> (self.<a href="../sui_sui/vec_map#sui_vec_map_contains">contains</a>(key)) {
        option::some(self[key])
    } <b>else</b> {
        option::none()
    }
}
</code></pre>

Function <code>contains</code>

Return true if self contains an entry for key, false otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_contains">contains</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_contains">contains</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): bool {
    <a href="../sui_sui/vec_map#sui_vec_map_get_idx_opt">get_idx_opt</a>(self, key).is_some()
}
</code></pre>

Function <code>length</code>

Return the number of entries in self

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_length">length</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_length">length</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): u64 {
    self.contents.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>()
}
</code></pre>

Function <code>is_empty</code>

Return true if self has 0 elements, false otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_is_empty">is_empty</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_is_empty">is_empty</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): bool {
    self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>() == 0
}
</code></pre>

Function <code>destroy_empty</code>

Destroy an empty map. Aborts if self is not empty

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b>, V&gt;(self: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_destroy_empty">destroy_empty</a>&lt;K: <b>copy</b>, V&gt;(self: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;) {
    <b>let</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a> { contents } = self;
    <b>assert</b>!(contents.<a href="../sui_sui/vec_map#sui_vec_map_is_empty">is_empty</a>(), <a href="../sui_sui/vec_map#sui_vec_map_EMapNotEmpty">EMapNotEmpty</a>);
    contents.<a href="../sui_sui/vec_map#sui_vec_map_destroy_empty">destroy_empty</a>()
}
</code></pre>

Function <code>into_keys_values</code>

Unpack self into vectors of its keys and values.
The output keys and values are stored in insertion order, *not* sorted by key.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_into_keys_values">into_keys_values</a>&lt;K: <b>copy</b>, V&gt;(self: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): (vector&lt;K&gt;, vector&lt;V&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_into_keys_values">into_keys_values</a>&lt;K: <b>copy</b>, V&gt;(self: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): (vector&lt;K&gt;, vector&lt;V&gt;) {
    <b>let</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a> { contents } = self;
    <b>let</b> <b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a> = vector[];
    <b>let</b> <b>mut</b> values = vector[];
    contents.do!(|<a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, value }| {
        <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>.push_back(key);
        values.push_back(value);
    });
    (<a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>, values)
}
</code></pre>

Function <code>from_keys_values</code>

Construct a new <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a> from two vectors, one for keys and one for values.
The key value pairs are associated via their indices in the vectors, e.g. the key at index i
in <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a> is associated with the value at index i in values.
The key value pairs are stored in insertion order (the original vectors ordering)
and are *not* sorted.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_from_keys_values">from_keys_values</a>&lt;K: <b>copy</b>, V&gt;(<a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>: vector&lt;K&gt;, values: vector&lt;V&gt;): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_from_keys_values">from_keys_values</a>&lt;K: <b>copy</b>, V&gt;(<a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>: vector&lt;K&gt;, values: vector&lt;V&gt;): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt; {
    <b>assert</b>!(<a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>() == values.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>(), <a href="../sui_sui/vec_map#sui_vec_map_EUnequalLengths">EUnequalLengths</a>);
    <b>let</b> <b>mut</b> contents = <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a> { contents: vector[] };
    <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>.zip_do!(values, |key, value| contents.<a href="../sui_sui/vec_map#sui_vec_map_insert">insert</a>(key, value));
    contents
}
</code></pre>

Function <code>keys</code>

Returns a list of keys in the map.
Do not assume any particular ordering.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): vector&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_keys">keys</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): vector&lt;K&gt; {
    self.contents.map_ref!(|<a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, .. }| *key)
}
</code></pre>

Function <code>get_idx_opt</code>

Find the index of key in self. Return None if key is not in self.
Note that map entries are stored in insertion order, *not* sorted by key.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_idx_opt">get_idx_opt</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_idx_opt">get_idx_opt</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): Option&lt;u64&gt; {
    self.contents.find_index!(|<a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key: k, .. }| k == key)
}
</code></pre>

Function <code>get_idx</code>

Find the index of key in self. Aborts if key is not in self.
Note that map entries are stored in insertion order, *not* sorted by key.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_idx">get_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, key: &K): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_idx">get_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, key: &K): u64 {
    self.contents.find_index!(|<a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key: k, .. }| k == key).destroy_or!(<b>abort</b> <a href="../sui_sui/vec_map#sui_vec_map_EKeyDoesNotExist">EKeyDoesNotExist</a>)
}
</code></pre>

Function <code>get_entry_by_idx</code>

Return a reference to the idxth entry of self. This gives direct access into the backing array of the map--use with caution.
Note that map entries are stored in insertion order, *not* sorted by key.
Aborts if idx is greater than or equal to self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>()

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_entry_by_idx">get_entry_by_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, idx: u64): (&K, &V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_entry_by_idx">get_entry_by_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, idx: u64): (&K, &V) {
    <b>assert</b>!(idx &lt; self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>(), <a href="../sui_sui/vec_map#sui_vec_map_EIndexOutOfBounds">EIndexOutOfBounds</a>);
    <b>let</b> <b>entry</b> = &self.contents[idx];
    (&<b>entry</b>.key, &<b>entry</b>.value)
}
</code></pre>

Function <code>get_entry_by_idx_mut</code>

Return a mutable reference to the idxth entry of self. This gives direct access into the backing array of the map--use with caution.
Note that map entries are stored in insertion order, *not* sorted by key.
Aborts if idx is greater than or equal to self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>()

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_entry_by_idx_mut">get_entry_by_idx_mut</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, idx: u64): (&K, &<b>mut</b> V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_get_entry_by_idx_mut">get_entry_by_idx_mut</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, idx: u64): (&K, &<b>mut</b> V) {
    <b>assert</b>!(idx &lt; self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>(), <a href="../sui_sui/vec_map#sui_vec_map_EIndexOutOfBounds">EIndexOutOfBounds</a>);
    <b>let</b> <b>entry</b> = &<b>mut</b> self.contents[idx];
    (&<b>entry</b>.key, &<b>mut</b> <b>entry</b>.value)
}
</code></pre>

Function <code>remove_entry_by_idx</code>

Remove the entry at index idx from self.
Aborts if idx is greater than or equal to self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>()

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_remove_entry_by_idx">remove_entry_by_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;, idx: u64): (K, V)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_remove_entry_by_idx">remove_entry_by_idx</a>&lt;K: <b>copy</b>, V&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;, idx: u64): (K, V) {
    <b>assert</b>!(idx &lt; self.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>(), <a href="../sui_sui/vec_map#sui_vec_map_EIndexOutOfBounds">EIndexOutOfBounds</a>);
    <b>let</b> <a href="../sui_sui/vec_map#sui_vec_map_Entry">Entry</a> { key, value } = self.contents.<a href="../sui_sui/vec_map#sui_vec_map_remove">remove</a>(idx);
    (key, value)
}
</code></pre>

Function <code>size</code>

Return the number of entries in self

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_size">size</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;K, V&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_map#sui_vec_map_size">size</a>&lt;K: <b>copy</b>, V&gt;(self: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">VecMap</a>&lt;K, V&gt;): u64 {
    self.contents.<a href="../sui_sui/vec_map#sui_vec_map_length">length</a>()
}
</code></pre>