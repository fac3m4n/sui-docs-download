-  [Struct VotingPowerInfo](#sui_system_voting_power_VotingPowerInfo)
-  [Struct VotingPowerInfoV2](#sui_system_voting_power_VotingPowerInfoV2)
-  [Constants](#@Constants_0)
-  [Function set_voting_power](#sui_system_voting_power_set_voting_power)
-  [Function init_voting_power_info](#sui_system_voting_power_init_voting_power_info)
-  [Function derive_raw_voting_power](#sui_system_voting_power_derive_raw_voting_power)
-  [Function insert](#sui_system_voting_power_insert)
-  [Function adjust_voting_power](#sui_system_voting_power_adjust_voting_power)
-  [Function update_voting_power](#sui_system_voting_power_update_voting_power)
-  [Function check_invariants](#sui_system_voting_power_check_invariants)
-  [Function total_voting_power](#sui_system_voting_power_total_voting_power)
-  [Function quorum_threshold](#sui_system_voting_power_quorum_threshold)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/internal#std_internal">std::internal</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/u128#std_u128">std::u128</a>;
<b>use</b> <a href="../sui_std/u64#std_u64">std::u64</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/accumulator#sui_accumulator">sui::accumulator</a>;
<b>use</b> <a href="../sui_sui/accumulator_settlement#sui_accumulator_settlement">sui::accumulator_settlement</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/bag#sui_bag">sui::bag</a>;
<b>use</b> <a href="../sui_sui/balance#sui_balance">sui::balance</a>;
<b>use</b> <a href="../sui_sui/bcs#sui_bcs">sui::bcs</a>;
<b>use</b> <a href="../sui_sui/coin#sui_coin">sui::coin</a>;
<b>use</b> <a href="../sui_sui/config#sui_config">sui::config</a>;
<b>use</b> <a href="../sui_sui/deny_list#sui_deny_list">sui::deny_list</a>;
<b>use</b> <a href="../sui_sui/dynamic_field#sui_dynamic_field">sui::dynamic_field</a>;
<b>use</b> <a href="../sui_sui/dynamic_object_field#sui_dynamic_object_field">sui::dynamic_object_field</a>;
<b>use</b> <a href="../sui_sui/event#sui_event">sui::event</a>;
<b>use</b> <a href="../sui_sui/funds_accumulator#sui_funds_accumulator">sui::funds_accumulator</a>;
<b>use</b> <a href="../sui_sui/hash#sui_hash">sui::hash</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/sui#sui_sui">sui::sui</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
<b>use</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">sui_system::staking_pool</a>;
<b>use</b> <a href="../sui_sui_system/validator#sui_system_validator">sui_system::validator</a>;
<b>use</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap">sui_system::validator_cap</a>;
</code>

Struct <code>VotingPowerInfo</code>

Deprecated. Use VotingPowerInfoV2 instead.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfo">VotingPowerInfo</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>validator_index: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>VotingPowerInfoV2</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a> <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>validator_index: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake: u64</code>
</dt>
<dd>
</dd>
</dl>

Constants

Set total_voting_power as 10_000 by convention. Individual voting powers can be interpreted
as easily understandable basis points (e.g., voting_power: 100 = 1%, voting_power: 1 = 0.01%) rather than
opaque quantities whose meaning changes from epoch to epoch as the total amount staked shifts.
Fixing the total voting power allows clients to hardcode the quorum threshold and total_voting power rather
than recomputing these.

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a>: u64 = 10000;
</code>

Quorum threshold for our fixed voting power--any message signed by this much voting power can be trusted
up to BFT assumptions

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_QUORUM_THRESHOLD">QUORUM_THRESHOLD</a>: u64 = 6667;
</code>

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_MAX_VOTING_POWER">MAX_VOTING_POWER</a>: u64 = 1000;
</code>

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_ETotalPowerMismatch">ETotalPowerMismatch</a>: u64 = 1;
</code>

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_ERelativePowerMismatch">ERelativePowerMismatch</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_EVotingPowerOverThreshold">EVotingPowerOverThreshold</a>: u64 = 3;
</code>

<code><b>const</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_EInvalidVotingPower">EInvalidVotingPower</a>: u64 = 4;
</code>

Function <code>set_voting_power</code>

Set the voting power of all validators.
Each validator's voting power is initialized using their stake. We then attempt to cap their voting power
at <a href="../sui_sui_system/voting_power#sui_system_voting_power_MAX_VOTING_POWER">MAX_VOTING_POWER</a>. If <a href="../sui_sui_system/voting_power#sui_system_voting_power_MAX_VOTING_POWER">MAX_VOTING_POWER</a> is not a feasible cap, we pick the lowest possible cap.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_set_voting_power">set_voting_power</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, total_stake: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_set_voting_power">set_voting_power</a>(validators: &<b>mut</b> vector&lt;Validator&gt;, total_stake: u64) {
    // If threshold_pct is too small, it's possible that even when all validators reach the threshold we still don't
    // have 100%. So we bound the threshold_pct to be always enough to find a solution.
    <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">total_voting_power</a> = <a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a>;
    <b>let</b> average_voting_power = <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">total_voting_power</a>.divide_and_round_up(validators.length());
    <b>let</b> threshold = <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">total_voting_power</a>.min(<a href="../sui_sui_system/voting_power#sui_system_voting_power_MAX_VOTING_POWER">MAX_VOTING_POWER</a>.max(average_voting_power));
    <b>let</b> (<b>mut</b> info_list, remaining_power) = <a href="../sui_sui_system/voting_power#sui_system_voting_power_init_voting_power_info">init_voting_power_info</a>(
        validators,
        threshold,
        total_stake,
    );
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_adjust_voting_power">adjust_voting_power</a>(&<b>mut</b> info_list, threshold, remaining_power);
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_update_voting_power">update_voting_power</a>(validators, info_list);
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_check_invariants">check_invariants</a>(validators);
}
</code></pre>

Function <code>init_voting_power_info</code>

Create the initial voting power of each validator, set using their stake, but capped using threshold.
We also perform insertion sort while creating the voting power list, by maintaining the list in
descending order using voting power.
Anything beyond the threshold is added to the remaining_power, which is also returned.

<code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_init_voting_power_info">init_voting_power_info</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, threshold: u64, total_stake: u64): (vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">sui_system::voting_power::VotingPowerInfoV2</a>&gt;, u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_init_voting_power_info">init_voting_power_info</a>(
    validators: &vector&lt;Validator&gt;,
    threshold: u64,
    total_stake: u64,
): (vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a>&gt;, u64) {
    <b>let</b> <b>mut</b> total_power = 0;
    <b>let</b> <b>mut</b> result = vector[];
    validators.length().do!(|i| {
        <b>let</b> stake = validators[i].total_stake();
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">derive_raw_voting_power</a>(stake, total_stake).min(threshold);
        <a href="../sui_sui_system/voting_power#sui_system_voting_power_insert">insert</a>(&<b>mut</b> result, <a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a> { validator_index: i, <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>, stake });
        total_power = total_power + <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>;
    });
    (result, <a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a> - total_power)
}
</code></pre>

Function <code>derive_raw_voting_power</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">derive_raw_voting_power</a>(stake: u64, total_stake: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">derive_raw_voting_power</a>(stake: u64, total_stake: u64): u64 {
    ((stake <b>as</b> u128 * (<a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a> <b>as</b> u128) / (total_stake <b>as</b> u128)) <b>as</b> u64)
}
</code></pre>

Function <code>insert</code>

Insert new_info to info_list as part of insertion sort, such that info_list is always sorted
using stake, in descending order.

<code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_insert">insert</a>(info_list: &<b>mut</b> vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">sui_system::voting_power::VotingPowerInfoV2</a>&gt;, new_info: <a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">sui_system::voting_power::VotingPowerInfoV2</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_insert">insert</a>(info_list: &<b>mut</b> vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a>&gt;, new_info: <a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a>) {
    <b>let</b> len = info_list.length();
    <b>let</b> idx = info_list.find_index!(|info| new_info.stake &gt;= info.stake);
    info_list.<a href="../sui_sui_system/voting_power#sui_system_voting_power_insert">insert</a>(new_info, idx.destroy_or!(len));
}
</code></pre>

Function <code>adjust_voting_power</code>

Distribute remaining_power to validators that are not capped at threshold.

<code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_adjust_voting_power">adjust_voting_power</a>(info_list: &<b>mut</b> vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">sui_system::voting_power::VotingPowerInfoV2</a>&gt;, threshold: u64, remaining_power: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_adjust_voting_power">adjust_voting_power</a>(
    info_list: &<b>mut</b> vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a>&gt;,
    threshold: u64,
    <b>mut</b> remaining_power: u64,
) {
    <b>let</b> <b>mut</b> i = 0;
    <b>let</b> len = info_list.length();
    <b>while</b> (i &lt; len && remaining_power &gt; 0) {
        <b>let</b> v = &<b>mut</b> info_list[i];
        // planned is the amount of extra power we want to distribute to this <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> planned = remaining_power.divide_and_round_up(len - i);
        // target is the targeting power this <a href="../sui_sui_system/validator#sui_system_validator">validator</a> will reach, capped by threshold.
        <b>let</b> target = threshold.min(v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> + planned);
        // actual is the actual amount of power we will be distributing to this <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> actual = remaining_power.min(target - v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>);
        v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> + actual;
        <b>assert</b>!(v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> &lt;= threshold, <a href="../sui_sui_system/voting_power#sui_system_voting_power_EVotingPowerOverThreshold">EVotingPowerOverThreshold</a>);
        remaining_power = remaining_power - actual;
        i = i + 1;
    };
    <b>assert</b>!(remaining_power == 0, <a href="../sui_sui_system/voting_power#sui_system_voting_power_ETotalPowerMismatch">ETotalPowerMismatch</a>);
}
</code></pre>

Function <code>update_voting_power</code>

Update validators with the decided voting power.

<code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_update_voting_power">update_voting_power</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, info_list: vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">sui_system::voting_power::VotingPowerInfoV2</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_update_voting_power">update_voting_power</a>(validators: &<b>mut</b> vector&lt;Validator&gt;, info_list: vector&lt;<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a>&gt;) {
    info_list.destroy!(|<a href="../sui_sui_system/voting_power#sui_system_voting_power_VotingPowerInfoV2">VotingPowerInfoV2</a> { validator_index, <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>, .. }| {
        validators[validator_index].<a href="../sui_sui_system/voting_power#sui_system_voting_power_set_voting_power">set_voting_power</a>(<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>);
    });
}
</code></pre>

Function <code>check_invariants</code>

Check a few invariants that must hold after setting the voting power.

<code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_check_invariants">check_invariants</a>(v: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_check_invariants">check_invariants</a>(v: &vector&lt;Validator&gt;) {
    <b>let</b> <b>mut</b> total = 0;
    v.do_ref!(|v| {
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
        <b>assert</b>!(<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> &gt; 0, <a href="../sui_sui_system/voting_power#sui_system_voting_power_EInvalidVotingPower">EInvalidVotingPower</a>);
        total = total + <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>;
    });
    <b>assert</b>!(total == <a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a>, <a href="../sui_sui_system/voting_power#sui_system_voting_power_ETotalPowerMismatch">ETotalPowerMismatch</a>);
    // Second check that <b>if</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> A's stake is larger than B's stake, A's
    // voting power must be no less than B's voting power; similarly, <b>if</b> A's
    // stake is less than B's stake, A's voting power must be no larger than
    // B's voting power.
    <b>let</b> length = v.length();
    length.do!(|a| {
        (a + 1).range_do!(length, |b| {
            <b>let</b> validator_a = &v[a];
            <b>let</b> validator_b = &v[b];
            <b>let</b> stake_a = validator_a.total_stake();
            <b>let</b> stake_b = validator_b.total_stake();
            <b>let</b> power_a = validator_a.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
            <b>let</b> power_b = validator_b.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
            <b>if</b> (stake_a &gt; stake_b) {
                <b>assert</b>!(power_a &gt;= power_b, <a href="../sui_sui_system/voting_power#sui_system_voting_power_ERelativePowerMismatch">ERelativePowerMismatch</a>);
            };
            <b>if</b> (stake_a &lt; stake_b) {
                <b>assert</b>!(power_a &lt;= power_b, <a href="../sui_sui_system/voting_power#sui_system_voting_power_ERelativePowerMismatch">ERelativePowerMismatch</a>);
            };
        })
    });
}
</code></pre>

Function <code>total_voting_power</code>

Return the (constant) total voting power

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">total_voting_power</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">total_voting_power</a>(): u64 {
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_TOTAL_VOTING_POWER">TOTAL_VOTING_POWER</a>
}
</code></pre>

Function <code>quorum_threshold</code>

Return the (constant) quorum threshold

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_quorum_threshold">quorum_threshold</a>(): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power_quorum_threshold">quorum_threshold</a>(): u64 {
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_QUORUM_THRESHOLD">QUORUM_THRESHOLD</a>
}
</code></pre>