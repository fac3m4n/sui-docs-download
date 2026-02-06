-  [Struct VecSet](#sui_vec_set_VecSet)
-  [Constants](#@Constants_0)
-  [Function empty](#sui_vec_set_empty)
-  [Function singleton](#sui_vec_set_singleton)
-  [Function insert](#sui_vec_set_insert)
-  [Function remove](#sui_vec_set_remove)
-  [Function contains](#sui_vec_set_contains)
-  [Function length](#sui_vec_set_length)
-  [Function is_empty](#sui_vec_set_is_empty)
-  [Function into_keys](#sui_vec_set_into_keys)
-  [Function from_keys](#sui_vec_set_from_keys)
-  [Function keys](#sui_vec_set_keys)
-  [Function size](#sui_vec_set_size)

<code><b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>VecSet</code>

A set data structure backed by a vector. The set is guaranteed not to
contain duplicate keys. All operations are O(N) in the size of the set
- the intention of this data structure is only to provide the convenience
of programming against a set API. Sets that need sorted iteration rather
than insertion order iteration should be handwritten.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K: <b>copy</b>, drop&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>contents: vector&lt;K&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

This key already exists in the map

<code><b>const</b> <a href="../sui_sui/vec_set#sui_vec_set_EKeyAlreadyExists">EKeyAlreadyExists</a>: u64 = 0;
</code>

This key does not exist in the map

<code><b>const</b> <a href="../sui_sui/vec_set#sui_vec_set_EKeyDoesNotExist">EKeyDoesNotExist</a>: u64 = 1;
</code>

Function <code>empty</code>

Create an empty <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_empty">empty</a>&lt;K: <b>copy</b>, drop&gt;(): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_empty">empty</a>&lt;K: <b>copy</b> + drop&gt;(): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt; {
    <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> { contents: vector[] }
}
</code></pre>

Function <code>singleton</code>

Create a singleton <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> that only contains one element.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_singleton">singleton</a>&lt;K: <b>copy</b>, drop&gt;(key: K): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_singleton">singleton</a>&lt;K: <b>copy</b> + drop&gt;(key: K): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt; {
    <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> { contents: vector[key] }
}
</code></pre>

Function <code>insert</code>

Insert a key into self.
Aborts if key is already present in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_insert">insert</a>&lt;K: <b>copy</b>, drop&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;, key: K)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_insert">insert</a>&lt;K: <b>copy</b> + drop&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;, key: K) {
    <b>assert</b>!(!self.<a href="../sui_sui/vec_set#sui_vec_set_contains">contains</a>(&key), <a href="../sui_sui/vec_set#sui_vec_set_EKeyAlreadyExists">EKeyAlreadyExists</a>);
    self.contents.push_back(key)
}
</code></pre>

Function <code>remove</code>

Remove the entry key from self. Aborts if key is not present in self.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_remove">remove</a>&lt;K: <b>copy</b>, drop&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;, key: &K)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_remove">remove</a>&lt;K: <b>copy</b> + drop&gt;(self: &<b>mut</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;, key: &K) {
    <b>let</b> idx = self.contents.find_index!(|k| k == key).destroy_or!(<b>abort</b> <a href="../sui_sui/vec_set#sui_vec_set_EKeyDoesNotExist">EKeyDoesNotExist</a>);
    self.contents.<a href="../sui_sui/vec_set#sui_vec_set_remove">remove</a>(idx);
}
</code></pre>

Function <code>contains</code>

Return true if self contains an entry for key, false otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_contains">contains</a>&lt;K: <b>copy</b>, drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;, key: &K): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_contains">contains</a>&lt;K: <b>copy</b> + drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;, key: &K): bool {
    'search: {
        self.contents.do_ref!(|k| <b>if</b> (k == key) <b>return</b> 'search <b>true</b>);
        <b>false</b>
    }
}
</code></pre>

Function <code>length</code>

Return the number of entries in self

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_length">length</a>&lt;K: <b>copy</b>, drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_length">length</a>&lt;K: <b>copy</b> + drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;): u64 {
    self.contents.<a href="../sui_sui/vec_set#sui_vec_set_length">length</a>()
}
</code></pre>

Function <code>is_empty</code>

Return true if self has 0 elements, false otherwise

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_is_empty">is_empty</a>&lt;K: <b>copy</b>, drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_is_empty">is_empty</a>&lt;K: <b>copy</b> + drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;): bool {
    self.<a href="../sui_sui/vec_set#sui_vec_set_length">length</a>() == 0
}
</code></pre>

Function <code>into_keys</code>

Unpack self into vectors of keys.
The output keys are stored in insertion order, *not* sorted.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_into_keys">into_keys</a>&lt;K: <b>copy</b>, drop&gt;(self: <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;): vector&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_into_keys">into_keys</a>&lt;K: <b>copy</b> + drop&gt;(self: <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;): vector&lt;K&gt; {
    <b>let</b> <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> { contents } = self;
    contents
}
</code></pre>

Function <code>from_keys</code>

Construct a new <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> from a vector of keys.
The keys are stored in insertion order (the original <a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a> ordering)
and are *not* sorted.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_from_keys">from_keys</a>&lt;K: <b>copy</b>, drop&gt;(<a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a>: vector&lt;K&gt;): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_from_keys">from_keys</a>&lt;K: <b>copy</b> + drop&gt;(<a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a>: vector&lt;K&gt;): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt; {
    <b>let</b> <b>mut</b> set = <a href="../sui_sui/vec_set#sui_vec_set_empty">empty</a>();
    <a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a>.do!(|key| set.<a href="../sui_sui/vec_set#sui_vec_set_insert">insert</a>(key));
    set
}
</code></pre>

Function <code>keys</code>

Borrow the contents of the <a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a> to access content by index
without unpacking. The contents are stored in insertion order,
*not* sorted.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a>&lt;K: <b>copy</b>, drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;): &vector&lt;K&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_keys">keys</a>&lt;K: <b>copy</b> + drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;): &vector&lt;K&gt; {
    &self.contents
}
</code></pre>

Function <code>size</code>

Return the number of entries in self

<code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_size">size</a>&lt;K: <b>copy</b>, drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;K&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/vec_set#sui_vec_set_size">size</a>&lt;K: <b>copy</b> + drop&gt;(self: &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">VecSet</a>&lt;K&gt;): u64 {
    self.contents.<a href="../sui_sui/vec_set#sui_vec_set_length">length</a>()
}
</code></pre>