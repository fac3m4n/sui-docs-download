Utility for converting a Move value to its binary representation in BCS (Binary Canonical
Serialization). BCS is the binary encoding for Move resources and other non-module values
published on-chain. See https://github.com/diem/bcs#binary-canonical-serialization-bcs for more
details on BCS.

-  [Function to_bytes](#std_bcs_to_bytes)

<code></code>

Function <code>to_bytes</code>

Return the binary representation of v in BCS (Binary Canonical Serialization) format

<code><b>public</b> <b>fun</b> <a href="../sui_std/bcs#std_bcs_to_bytes">to_bytes</a>&lt;MoveValue&gt;(v: &MoveValue): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_std/bcs#std_bcs_to_bytes">to_bytes</a>&lt;MoveValue&gt;(v: &MoveValue): <a href="../sui_std/vector#std_vector">vector</a>&lt;<a href="../sui_std/u8#std_u8">u8</a>&gt;;
</code></pre>