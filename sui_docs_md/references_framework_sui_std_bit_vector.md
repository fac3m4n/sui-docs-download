-  [Struct BitVector](#std_bit_vector_BitVector)
-  [Constants](#@Constants_0)
-  [Function new](#std_bit_vector_new)
-  [Function set](#std_bit_vector_set)
-  [Function unset](#std_bit_vector_unset)
-  [Function shift_left](#std_bit_vector_shift_left)
-  [Function is_index_set](#std_bit_vector_is_index_set)
-  [Function length](#std_bit_vector_length)
-  [Function longest_set_sequence_starting_at](#std_bit_vector_longest_set_sequence_starting_at)

<code></code>

Struct <code>BitVector</code>

<code><b>public</b> <b>struct</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_std/bit_vector#std_bit_vector_length">length</a>: <a href="../sui_std/u64#std_u64">u64</a></code>
</dt>
<dd>
</dd>
<dt>
<code>bit_field: <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/bool#std_bool">bool</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Constants

The provided index is out of bounds

<code><b>const</b> <a href="../sui_std/bit_vector#std_bit_vector_EINDEX">EINDEX</a>: <a href="../sui_std/u64#std_u64">u64</a> = 131072;
</code>

An invalid length of bitvector was given

<code><b>const</b> <a href="../sui_std/bit_vector#std_bit_vector_ELENGTH">ELENGTH</a>: <a href="../sui_std/u64#std_u64">u64</a> = 131073;
</code>

<code><b>const</b> <a href="../sui_std/bit_vector#std_bit_vector_WORD_SIZE">WORD_SIZE</a>: <a href="../sui_std/u64#std_u64">u64</a> = 1;
</code>

The maximum allowed bitvector size

<code><b>const</b> <a href="../sui_std/bit_vector#std_bit_vector_MAX_SIZE">MAX_SIZE</a>: <a href="../sui_std/u64#std_u64">u64</a> = 1024;
</code>

Function <code>new</code>

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_new">new</a>(<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_new">new</a>(<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a> {
    <b>assert</b>!(<a href="../sui_std/bit_vector#std_bit_vector_length">length</a> &gt; 0, <a href="../sui_std/bit_vector#std_bit_vector_ELENGTH">ELENGTH</a>);
    <b>assert</b>!(<a href="../sui_std/bit_vector#std_bit_vector_length">length</a> &lt; <a href="../sui_std/bit_vector#std_bit_vector_MAX_SIZE">MAX_SIZE</a>, <a href="../sui_std/bit_vector#std_bit_vector_ELENGTH">ELENGTH</a>);
    <b>let</b> <b>mut</b> counter = 0;
    <b>let</b> <b>mut</b> bit_field = <a href="../sui_std/vector#std_vector_empty">vector::empty</a>();
    <b>while</b> (counter &lt; <a href="../sui_std/bit_vector#std_bit_vector_length">length</a>) {
        bit_field.push_back(<b>false</b>);
        counter = counter + 1;
    };
    <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a> {
        <a href="../sui_std/bit_vector#std_bit_vector_length">length</a>,
        bit_field,
    }
}
</code></pre>

Function <code>set</code>

Set the bit at bit_index in the bitvector regardless of its previous state.

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_set">set</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_set">set</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>) {
    <b>assert</b>!(bit_index &lt; bitvector.bit_field.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>(), <a href="../sui_std/bit_vector#std_bit_vector_EINDEX">EINDEX</a>);
    <b>let</b> x = &<b>mut</b> bitvector.bit_field[bit_index];
    *x = <b>true</b>;
}
</code></pre>

Function <code>unset</code>

Unset the bit at bit_index in the bitvector regardless of its previous state.

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_unset">unset</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_unset">unset</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>) {
    <b>assert</b>!(bit_index &lt; bitvector.bit_field.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>(), <a href="../sui_std/bit_vector#std_bit_vector_EINDEX">EINDEX</a>);
    <b>let</b> x = &<b>mut</b> bitvector.bit_field[bit_index];
    *x = <b>false</b>;
}
</code></pre>

Function <code>shift_left</code>

Shift the bitvector left by amount. If amount is greater than the
bitvector's length the bitvector will be zeroed out.

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_shift_left">shift_left</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>, amount: <a href="../sui_std/u64#std_u64">u64</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_shift_left">shift_left</a>(bitvector: &<b>mut</b> <a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>, amount: <a href="../sui_std/u64#std_u64">u64</a>) {
    <b>if</b> (amount &gt;= bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>) {
        <b>let</b> len = bitvector.bit_field.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>();
        <b>let</b> <b>mut</b> i = 0;
        <b>while</b> (i &lt; len) {
            <b>let</b> elem = &<b>mut</b> bitvector.bit_field[i];
            *elem = <b>false</b>;
            i = i + 1;
        };
    } <b>else</b> {
        <b>let</b> <b>mut</b> i = amount;
        <b>while</b> (i &lt; bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>) {
            <b>if</b> (bitvector.<a href="../sui_std/bit_vector#std_bit_vector_is_index_set">is_index_set</a>(i)) bitvector.<a href="../sui_std/bit_vector#std_bit_vector_set">set</a>(i - amount)
            <b>else</b> bitvector.<a href="../sui_std/bit_vector#std_bit_vector_unset">unset</a>(i - amount);
            i = i + 1;
        };
        i = bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a> - amount;
        <b>while</b> (i &lt; bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>) {
            <a href="../sui_std/bit_vector#std_bit_vector_unset">unset</a>(bitvector, i);
            i = i + 1;
        };
    }
}
</code></pre>

Function <code>is_index_set</code>

Return the value of the bit at bit_index in the bitvector. <b>true</b>
represents "1" and <b>false</b> represents a 0

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_is_index_set">is_index_set</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bool#std_bool">bool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_is_index_set">is_index_set</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>, bit_index: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/bool#std_bool">bool</a> {
    <b>assert</b>!(bit_index &lt; bitvector.bit_field.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>(), <a href="../sui_std/bit_vector#std_bit_vector_EINDEX">EINDEX</a>);
    bitvector.bit_field[bit_index]
}
</code></pre>

Function <code>length</code>

Return the length (number of usable bits) of this bitvector

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_length">length</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_length">length</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    bitvector.bit_field.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>()
}
</code></pre>

Function <code>longest_set_sequence_starting_at</code>

Returns the length of the longest sequence of set bits starting at (and
including) start_index in the bitvector. If there is no such
sequence, then 0 is returned.

<code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_longest_set_sequence_starting_at">longest_set_sequence_starting_at</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">std::bit_vector::BitVector</a>, start_index: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/bit_vector#std_bit_vector_longest_set_sequence_starting_at">longest_set_sequence_starting_at</a>(bitvector: &<a href="../sui_std/bit_vector#std_bit_vector_BitVector">BitVector</a>, start_index: <a href="../sui_std/u64#std_u64">u64</a>): <a href="../sui_std/u64#std_u64">u64</a> {
    <b>assert</b>!(start_index &lt; bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>, <a href="../sui_std/bit_vector#std_bit_vector_EINDEX">EINDEX</a>);
    <b>let</b> <b>mut</b> index = start_index;
    // Find the greatest index in the <a href="../sui_std/vector#std_vector">vector</a> such that all indices less than it are <a href="../sui_std/bit_vector#std_bit_vector_set">set</a>.
    <b>while</b> (index &lt; bitvector.<a href="../sui_std/bit_vector#std_bit_vector_length">length</a>) {
        <b>if</b> (!bitvector.<a href="../sui_std/bit_vector#std_bit_vector_is_index_set">is_index_set</a>(index)) <b>break</b>;
        index = index + 1;
    };
    index - start_index
}
</code></pre>