APIs for accessing time from move calls, via the <a href="../sui_sui/clock#sui_clock_Clock">Clock</a>: a unique
shared object that is created at 0x6 during genesis.

-  [Struct Clock](#sui_clock_Clock)
-  [Constants](#@Constants_0)
-  [Function timestamp_ms](#sui_clock_timestamp_ms)
-  [Function create](#sui_clock_create)
-  [Function consensus_commit_prologue](#sui_clock_consensus_commit_prologue)

<code><b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Clock</code>

Singleton shared object that exposes time to Move calls.  This
object is found at address 0x6, and can only be read (accessed
via an immutable reference) by entry functions.

Entry Functions that attempt to accept <a href="../sui_sui/clock#sui_clock_Clock">Clock</a> by mutable
reference or value will fail to verify, and honest validators
will not sign or execute transactions that use <a href="../sui_sui/clock#sui_clock_Clock">Clock</a> as an
input parameter, unless it is passed by immutable reference.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/clock#sui_clock_Clock">Clock</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>: u64</code>
</dt>
<dd>
 The clock's timestamp, which is set automatically by a
 system transaction every time consensus commits a
 schedule, or by <code>sui::clock::increment_for_testing</code> during
 testing.
</dd>
</dl>

Constants

Sender is not @0x0 the system address.

<code><b>const</b> <a href="../sui_sui/clock#sui_clock_ENotSystemAddress">ENotSystemAddress</a>: u64 = 0;
</code>

Function <code>timestamp_ms</code>

The <a href="../sui_sui/clock#sui_clock">clock</a>'s current timestamp as a running total of
milliseconds since an arbitrary point in the past.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>(<a href="../sui_sui/clock#sui_clock">clock</a>: &<a href="../sui_sui/clock#sui_clock_Clock">sui::clock::Clock</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>(<a href="../sui_sui/clock#sui_clock">clock</a>: &<a href="../sui_sui/clock#sui_clock_Clock">Clock</a>): u64 {
    <a href="../sui_sui/clock#sui_clock">clock</a>.<a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>
}
</code></pre>

Function <code>create</code>

Create and share the singleton Clock -- this function is
called exactly once, during genesis.

<code><b>fun</b> <a href="../sui_sui/clock#sui_clock_create">create</a>(ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/clock#sui_clock_create">create</a>(ctx: &TxContext) {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/clock#sui_clock_ENotSystemAddress">ENotSystemAddress</a>);
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(<a href="../sui_sui/clock#sui_clock_Clock">Clock</a> {
        id: <a href="../sui_sui/object#sui_object_clock">object::clock</a>(),
        // Initialised to zero, but set to a real timestamp by a
        // system transaction before it can be witnessed by a <b>move</b>
        // call.
        <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>: 0,
    })
}
</code></pre>

Function <code>consensus_commit_prologue</code>

<code><b>fun</b> <a href="../sui_sui/clock#sui_clock_consensus_commit_prologue">consensus_commit_prologue</a>(<a href="../sui_sui/clock#sui_clock">clock</a>: &<b>mut</b> <a href="../sui_sui/clock#sui_clock_Clock">sui::clock::Clock</a>, <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>: u64, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/clock#sui_clock_consensus_commit_prologue">consensus_commit_prologue</a>(<a href="../sui_sui/clock#sui_clock">clock</a>: &<b>mut</b> <a href="../sui_sui/clock#sui_clock_Clock">Clock</a>, <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>: u64, ctx: &TxContext) {
    // Validator will make a special system call with sender set <b>as</b> 0x0.
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui/clock#sui_clock_ENotSystemAddress">ENotSystemAddress</a>);
    <a href="../sui_sui/clock#sui_clock">clock</a>.<a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a> = <a href="../sui_sui/clock#sui_clock_timestamp_ms">timestamp_ms</a>
}
</code></pre>