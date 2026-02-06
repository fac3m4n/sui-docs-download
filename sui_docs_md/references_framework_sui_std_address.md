Provides a way to get address length since it's a
platform-specific parameter.

-  [Function length](#std_address_length)

<code></code>

Function <code>length</code>

Should be converted to a native function.
Current implementation only works for Sui.

<code><b>public</b> <b>fun</b> <a href="../sui_std/address#std_address_length">length</a>(): <a href="../sui_std/u64#std_u64">u64</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/address#std_address_length">length</a>(): <a href="../sui_std/u64#std_u64">u64</a> {
    32
}
</code></pre>