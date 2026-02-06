-  [Struct StakingPool](#sui_system_staking_pool_StakingPool)
-  [Struct PoolTokenExchangeRate](#sui_system_staking_pool_PoolTokenExchangeRate)
-  [Struct StakedSui](#sui_system_staking_pool_StakedSui)
-  [Struct FungibleStakedSui](#sui_system_staking_pool_FungibleStakedSui)
-  [Struct FungibleStakedSuiData](#sui_system_staking_pool_FungibleStakedSuiData)
-  [Struct FungibleStakedSuiDataKey](#sui_system_staking_pool_FungibleStakedSuiDataKey)
-  [Struct UnderflowSuiBalance](#sui_system_staking_pool_UnderflowSuiBalance)
-  [Constants](#@Constants_0)
-  [Function new](#sui_system_staking_pool_new)
-  [Function request_add_stake](#sui_system_staking_pool_request_add_stake)
-  [Function request_withdraw_stake](#sui_system_staking_pool_request_withdraw_stake)
-  [Function redeem_fungible_staked_sui](#sui_system_staking_pool_redeem_fungible_staked_sui)
-  [Function calculate_fungible_staked_sui_withdraw_amount](#sui_system_staking_pool_calculate_fungible_staked_sui_withdraw_amount)
-  [Function convert_to_fungible_staked_sui](#sui_system_staking_pool_convert_to_fungible_staked_sui)
-  [Function withdraw_from_principal](#sui_system_staking_pool_withdraw_from_principal)
-  [Function unwrap_staked_sui](#sui_system_staking_pool_unwrap_staked_sui)
-  [Function deposit_rewards](#sui_system_staking_pool_deposit_rewards)
-  [Function process_pending_stakes_and_withdraws](#sui_system_staking_pool_process_pending_stakes_and_withdraws)
-  [Function process_pending_stake_withdraw](#sui_system_staking_pool_process_pending_stake_withdraw)
-  [Function process_pending_stake](#sui_system_staking_pool_process_pending_stake)
-  [Function withdraw_rewards](#sui_system_staking_pool_withdraw_rewards)
-  [Function activate_staking_pool](#sui_system_staking_pool_activate_staking_pool)
-  [Function deactivate_staking_pool](#sui_system_staking_pool_deactivate_staking_pool)
-  [Function sui_balance](#sui_system_staking_pool_sui_balance)
-  [Function pool_id](#sui_system_staking_pool_pool_id)
-  [Function fungible_staked_sui_pool_id](#sui_system_staking_pool_fungible_staked_sui_pool_id)
-  [Function staked_sui_amount](#sui_system_staking_pool_staked_sui_amount)
-  [Function stake_activation_epoch](#sui_system_staking_pool_stake_activation_epoch)
-  [Function is_preactive](#sui_system_staking_pool_is_preactive)
-  [Function activation_epoch](#sui_system_staking_pool_activation_epoch)
-  [Function is_inactive](#sui_system_staking_pool_is_inactive)
-  [Function fungible_staked_sui_value](#sui_system_staking_pool_fungible_staked_sui_value)
-  [Function split_fungible_staked_sui](#sui_system_staking_pool_split_fungible_staked_sui)
-  [Function join_fungible_staked_sui](#sui_system_staking_pool_join_fungible_staked_sui)
-  [Function split](#sui_system_staking_pool_split)
-  [Function split_staked_sui](#sui_system_staking_pool_split_staked_sui)
-  [Function join_staked_sui](#sui_system_staking_pool_join_staked_sui)
-  [Function is_equal_staking_metadata](#sui_system_staking_pool_is_equal_staking_metadata)
-  [Function pool_token_exchange_rate_at_epoch](#sui_system_staking_pool_pool_token_exchange_rate_at_epoch)
-  [Function pending_stake_amount](#sui_system_staking_pool_pending_stake_amount)
-  [Function pending_stake_withdraw_amount](#sui_system_staking_pool_pending_stake_withdraw_amount)
-  [Function exchange_rates](#sui_system_staking_pool_exchange_rates)
-  [Function sui_amount](#sui_system_staking_pool_sui_amount)
-  [Function pool_token_amount](#sui_system_staking_pool_pool_token_amount)
-  [Function is_preactive_at_epoch](#sui_system_staking_pool_is_preactive_at_epoch)
-  [Function get_sui_amount](#sui_system_staking_pool_get_sui_amount)
-  [Function get_token_amount](#sui_system_staking_pool_get_token_amount)
-  [Function initial_exchange_rate](#sui_system_staking_pool_initial_exchange_rate)
-  [Function check_balance_invariants](#sui_system_staking_pool_check_balance_invariants)
-  [Macro function mul_div](#sui_system_staking_pool_mul_div)
-  [Function calculate_rewards](#sui_system_staking_pool_calculate_rewards)

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
</code>

Struct <code>StakingPool</code>

A staking pool embedded in each validator struct in the system state object.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;</code>
</dt>
<dd>
 The epoch at which this pool became active.
 The value is <code>None</code> if the pool is pre-active and <code>Some(&lt;epoch_number&gt;)</code> if active or inactive.
</dd>
<dt>
<code>deactivation_epoch: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;</code>
</dt>
<dd>
 The epoch at which this staking pool ceased to be active. <code>None</code> = {pre-active, active},
 <code>Some(&lt;epoch_number&gt;)</code> if in-active, and it was de-activated at epoch <code>&lt;epoch_number&gt;</code>.
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>: u64</code>
</dt>
<dd>
 The total number of SUI tokens in this pool, including the SUI in the rewards_pool, as well as in all the principal
 in the <code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a></code> object, updated at epoch boundaries.
</dd>
<dt>
<code>rewards_pool: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
 The epoch stake rewards will be added here at the end of each epoch.
</dd>
<dt>
<code>pool_token_balance: u64</code>
</dt>
<dd>
 Total number of pool tokens issued by the pool.
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;u64, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>&gt;</code>
</dt>
<dd>
 Exchange rate history of previous epochs. Key is the epoch number.
 The entries start from the <code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a></code> of this pool and contains exchange rates at the beginning of each epoch,
 i.e., right after the rewards for the previous epoch have been deposited into the pool.
</dd>
<dt>
<code>pending_stake: u64</code>
</dt>
<dd>
 Pending stake amount for this epoch, emptied at epoch boundaries.
</dd>
<dt>
<code>pending_total_sui_withdraw: u64</code>
</dt>
<dd>
 Pending stake withdrawn during the current epoch, emptied at epoch boundaries.
 This includes both the principal and rewards SUI withdrawn.
</dd>
<dt>
<code>pending_pool_token_withdraw: u64</code>
</dt>
<dd>
 Pending pool token withdrawn during the current epoch, emptied at epoch boundaries.
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
 Any extra fields that's not defined statically.
</dd>
</dl>

Struct <code>PoolTokenExchangeRate</code>

Struct representing the exchange rate of the stake pool token to SUI.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>StakedSui</code>

A self-custodial object holding the staked SUI tokens.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 ID of the staking pool we are staking with.
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>: u64</code>
</dt>
<dd>
 The epoch at which the stake becomes active.
</dd>
<dt>
<code>principal: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
 The staked SUI tokens.
</dd>
</dl>

Struct <code>FungibleStakedSui</code>

An alternative to <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> that holds the pool token amount instead of the SUI balance.
StakedSui objects can be converted to FungibleStakedSuis after the initial warmup period.
The advantage of this is that you can now merge multiple StakedSui objects from different
activation epochs into a single FungibleStakedSui object.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 ID of the staking pool we are staking with.
</dd>
<dt>
<code>value: u64</code>
</dt>
<dd>
 The pool token amount.
</dd>
</dl>

Struct <code>FungibleStakedSuiData</code>

Holds useful information

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiData">FungibleStakedSuiData</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>total_supply: u64</code>
</dt>
<dd>
 fungible_staked_sui supply
</dd>
<dt>
<code>principal: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
 principal balance. Rewards are withdrawn from the reward pool
</dd>
</dl>

Struct <code>FungibleStakedSuiDataKey</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiDataKey">FungibleStakedSuiDataKey</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Struct <code>UnderflowSuiBalance</code>

Holds the amount of SUI that was underflowed when withdrawing from the pool
post safe mode. Cleaned up in the same transaction.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_UnderflowSuiBalance">UnderflowSuiBalance</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

StakedSui objects cannot be split to below this amount.

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>: u64 = 1000000000;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInsufficientPoolTokenBalance">EInsufficientPoolTokenBalance</a>: u64 = 0;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongPool">EWrongPool</a>: u64 = 1;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWithdrawAmountCannotBeZero">EWithdrawAmountCannotBeZero</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInsufficientSuiTokenBalance">EInsufficientSuiTokenBalance</a>: u64 = 3;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInsufficientRewardsPoolBalance">EInsufficientRewardsPoolBalance</a>: u64 = 4;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDestroyNonzeroBalance">EDestroyNonzeroBalance</a>: u64 = 5;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_ETokenTimeLockIsSome">ETokenTimeLockIsSome</a>: u64 = 6;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongDelegation">EWrongDelegation</a>: u64 = 7;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EPendingDelegationDoesNotExist">EPendingDelegationDoesNotExist</a>: u64 = 8;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_ETokenBalancesDoNotMatchExchangeRate">ETokenBalancesDoNotMatchExchangeRate</a>: u64 = 9;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDelegationToInactivePool">EDelegationToInactivePool</a>: u64 = 10;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDeactivationOfInactivePool">EDeactivationOfInactivePool</a>: u64 = 11;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EIncompatibleStakedSui">EIncompatibleStakedSui</a>: u64 = 12;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWithdrawalInSameEpoch">EWithdrawalInSameEpoch</a>: u64 = 13;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EPoolAlreadyActive">EPoolAlreadyActive</a>: u64 = 14;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EPoolPreactiveOrInactive">EPoolPreactiveOrInactive</a>: u64 = 15;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EActivationOfInactivePool">EActivationOfInactivePool</a>: u64 = 16;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDelegationOfZeroSui">EDelegationOfZeroSui</a>: u64 = 17;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EStakedSuiBelowThreshold">EStakedSuiBelowThreshold</a>: u64 = 18;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_ECannotMintFungibleStakedSuiYet">ECannotMintFungibleStakedSuiYet</a>: u64 = 19;
</code>

<code><b>const</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInvariantFailure">EInvariantFailure</a>: u64 = 20;
</code>

Function <code>new</code>

Create a new, empty staking pool.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_new">new</a>(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_new">new</a>(ctx: &<b>mut</b> TxContext): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a> {
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a> {
        id: object::new(ctx),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>: option::none(),
        deactivation_epoch: option::none(),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>: 0,
        rewards_pool: balance::zero(),
        pool_token_balance: 0,
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>: table::new(ctx),
        pending_stake: 0,
        pending_total_sui_withdraw: 0,
        pending_pool_token_withdraw: 0,
        extra_fields: bag::new(ctx),
    }
}
</code></pre>

Function <code>request_add_stake</code>

Request to stake to a staking pool. The stake starts counting at the beginning of the next epoch,

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_request_add_stake">request_add_stake</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, stake: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_request_add_stake">request_add_stake</a>(
    pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    stake: Balance&lt;SUI&gt;,
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>: u64,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> {
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a> = stake.value();
    <b>assert</b>!(!pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDelegationToInactivePool">EDelegationToInactivePool</a>);
    <b>assert</b>!(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a> &gt; 0, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDelegationOfZeroSui">EDelegationOfZeroSui</a>);
    pool.pending_stake = pool.pending_stake + <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>;
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> {
        id: object::new(ctx),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>: object::id(pool),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>,
        principal: stake,
    }
}
</code></pre>

Function <code>request_withdraw_stake</code>

Request to withdraw the given stake plus rewards from a staking pool.
Both the principal and corresponding rewards in SUI are withdrawn.
A proportional amount of pool token withdraw is recorded and processed at epoch change time.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_request_withdraw_stake">request_withdraw_stake</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_request_withdraw_stake">request_withdraw_stake</a>(
    pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    // stake is inactive and the pool is not preactive - allow direct withdraw
    // the reason why we exclude preactive pools is to avoid potential underflow
    // on subtraction, and we need to enforce <span className="code-inline">pending_stake_withdraw</span> call.
    <b>if</b> (staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a> &gt; ctx.epoch() && !pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>()) {
        <b>let</b> principal = staked_sui.into_balance();
        pool.pending_stake = pool.pending_stake - principal.value();
        <b>return</b> principal
    };
    <b>let</b> (pool_token_withdraw_amount, <b>mut</b> principal_withdraw) = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_from_principal">withdraw_from_principal</a>(
        staked_sui,
    );
    <b>let</b> principal_withdraw_amount = principal_withdraw.value();
    <b>let</b> rewards_withdraw = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_rewards">withdraw_rewards</a>(
        principal_withdraw_amount,
        pool_token_withdraw_amount,
        ctx.epoch(),
    );
    <b>let</b> total_sui_withdraw_amount = principal_withdraw_amount + rewards_withdraw.value();
    pool.pending_total_sui_withdraw = pool.pending_total_sui_withdraw + total_sui_withdraw_amount;
    pool.pending_pool_token_withdraw =
        pool.pending_pool_token_withdraw + pool_token_withdraw_amount;
    // If the pool is inactive or preactive, we immediately process the withdrawal.
    <b>if</b> (pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>() || pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>()) pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake_withdraw">process_pending_stake_withdraw</a>();
    // TODO: implement withdraw bonding period here.
    principal_withdraw.join(rewards_withdraw);
    principal_withdraw
}
</code></pre>

Function <code>redeem_fungible_staked_sui</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, fungible_staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(
    pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    fungible_staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> { id, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>, value } = fungible_staked_sui;
    <b>assert</b>!(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> == object::id(pool), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongPool">EWrongPool</a>);
    id.delete();
    <b>let</b> latest_exchange_rate = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(ctx.epoch());
    <b>let</b> fungible_staked_sui_data: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiData">FungibleStakedSuiData</a> =
        &<b>mut</b> pool.extra_fields[<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiDataKey">FungibleStakedSuiDataKey</a> {}];
    <b>let</b> (
        principal_amount,
        rewards_amount,
    ) = latest_exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_calculate_fungible_staked_sui_withdraw_amount">calculate_fungible_staked_sui_withdraw_amount</a>(
        value,
        fungible_staked_sui_data.principal.value(),
        fungible_staked_sui_data.total_supply,
    );
    fungible_staked_sui_data.total_supply = fungible_staked_sui_data.total_supply - value;
    <b>let</b> <b>mut</b> sui_out = fungible_staked_sui_data.principal.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(principal_amount);
    sui_out.join(pool.rewards_pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(rewards_amount));
    pool.pending_total_sui_withdraw = pool.pending_total_sui_withdraw + sui_out.value();
    pool.pending_pool_token_withdraw = pool.pending_pool_token_withdraw + value;
    sui_out
}
</code></pre>

Function <code>calculate_fungible_staked_sui_withdraw_amount</code>

written in separate function so i can test with random values
returns (principal_withdraw_amount, rewards_withdraw_amount)

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_calculate_fungible_staked_sui_withdraw_amount">calculate_fungible_staked_sui_withdraw_amount</a>(latest_exchange_rate: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>: u64, fungible_staked_sui_data_principal_amount: u64, fungible_staked_sui_data_total_supply: u64): (u64, u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_calculate_fungible_staked_sui_withdraw_amount">calculate_fungible_staked_sui_withdraw_amount</a>(
    latest_exchange_rate: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>,
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>: u64,
    fungible_staked_sui_data_principal_amount: u64, // fungible_staked_sui_data.principal.value()
    fungible_staked_sui_data_total_supply: u64, // fungible_staked_sui_data.total_supply
): (u64, u64) {
    // 1. <b>if</b> the entire <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiData">FungibleStakedSuiData</a> supply is redeemed, how much sui should we receive?
    <b>let</b> total_sui_amount = latest_exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(
        fungible_staked_sui_data_total_supply,
    );
    // min with total_sui_amount to prevent underflow
    <b>let</b> fungible_staked_sui_data_principal_amount = fungible_staked_sui_data_principal_amount.min(
        total_sui_amount,
    );
    // 2. how much do we need to withdraw from the rewards pool?
    <b>let</b> total_rewards = total_sui_amount - fungible_staked_sui_data_principal_amount;
    // 3. proportionally withdraw from both wrt the <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>.
    <b>let</b> principal_withdraw_amount = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>!(
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>,
        fungible_staked_sui_data_principal_amount,
        fungible_staked_sui_data_total_supply,
    );
    <b>let</b> rewards_withdraw_amount = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>!(
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>,
        total_rewards,
        fungible_staked_sui_data_total_supply,
    );
    // <b>invariant</b> check, just in case
    <b>let</b> expected_sui_amount = latest_exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>);
    <b>assert</b>!(
        principal_withdraw_amount + rewards_withdraw_amount &lt;= expected_sui_amount,
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInvariantFailure">EInvariantFailure</a>,
    );
    (principal_withdraw_amount, rewards_withdraw_amount)
}
</code></pre>

Function <code>convert_to_fungible_staked_sui</code>

Convert the given staked SUI to an FungibleStakedSui object

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(
    pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> {
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> { id, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>, principal } = staked_sui;
    <b>assert</b>!(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> == object::id(pool), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongPool">EWrongPool</a>);
    <b>assert</b>!(ctx.epoch() &gt;= <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_ECannotMintFungibleStakedSuiYet">ECannotMintFungibleStakedSuiYet</a>);
    <b>assert</b>!(!pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>() && !pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EPoolPreactiveOrInactive">EPoolPreactiveOrInactive</a>);
    id.delete();
    <b>let</b> exchange_rate_at_staking_epoch = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>,
    );
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a> = exchange_rate_at_staking_epoch.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(principal.value());
    <b>let</b> key = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiDataKey">FungibleStakedSuiDataKey</a> {};
    <b>if</b> (!pool.extra_fields.contains(key)) {
        pool
            .extra_fields
            .add(
                key,
                <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiData">FungibleStakedSuiData</a> {
                    id: object::new(ctx),
                    total_supply: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>,
                    principal,
                },
            );
    } <b>else</b> {
        <b>let</b> fungible_staked_sui_data: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSuiData">FungibleStakedSuiData</a> = &<b>mut</b> pool.extra_fields[key];
        fungible_staked_sui_data.total_supply =
            fungible_staked_sui_data.total_supply + <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>;
        fungible_staked_sui_data.principal.join(principal);
    };
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> {
        id: object::new(ctx),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>,
        value: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>,
    }
}
</code></pre>

Function <code>withdraw_from_principal</code>

Withdraw the principal SUI stored in the StakedSui object, and calculate the corresponding amount of pool
tokens using exchange rate at staking epoch.
Returns values are amount of pool tokens withdrawn and withdrawn principal portion of SUI.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_from_principal">withdraw_from_principal</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): (u64, <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_from_principal">withdraw_from_principal</a>(
    pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>,
): (u64, Balance&lt;SUI&gt;) {
    // Check that the stake information matches the pool.
    <b>assert</b>!(staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> == object::id(pool), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongPool">EWrongPool</a>);
    <b>let</b> exchange_rate_at_staking_epoch = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>);
    <b>let</b> principal_withdraw = staked_sui.into_balance();
    <b>let</b> pool_token_withdraw_amount = exchange_rate_at_staking_epoch.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(principal_withdraw.value());
    (pool_token_withdraw_amount, principal_withdraw)
}
</code></pre>

Function <code>unwrap_staked_sui</code>

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_unwrap_staked_sui">unwrap_staked_sui</a>(staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_unwrap_staked_sui">unwrap_staked_sui</a>(staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>): Balance&lt;SUI&gt; {
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> { id, principal, .. } = staked_sui;
    id.delete();
    principal
}
</code></pre>

Function <code>deposit_rewards</code>

Called at epoch advancement times to add rewards (in SUI) to the staking pool.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_deposit_rewards">deposit_rewards</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, rewards: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_deposit_rewards">deposit_rewards</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, rewards: Balance&lt;SUI&gt;) {
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> + rewards.value();
    pool.rewards_pool.join(rewards);
}
</code></pre>

Function <code>process_pending_stakes_and_withdraws</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, ctx: &TxContext) {
    <b>let</b> new_epoch = ctx.epoch() + 1;
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake_withdraw">process_pending_stake_withdraw</a>();
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake">process_pending_stake</a>();
    pool
        .<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>
        .add(
            new_epoch,
            <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> {
                <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>,
                <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>: pool.pool_token_balance,
            },
        );
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_check_balance_invariants">check_balance_invariants</a>(new_epoch);
}
</code></pre>

Function <code>process_pending_stake_withdraw</code>

Called at epoch boundaries to process pending stake withdraws requested during the epoch.
Also called immediately upon withdrawal if the pool is inactive.

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake_withdraw">process_pending_stake_withdraw</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake_withdraw">process_pending_stake_withdraw</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>) {
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> = <b>if</b> (pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> &gt;= pool.pending_total_sui_withdraw) {
        pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> - pool.pending_total_sui_withdraw
    } <b>else</b> {
        // the diff will be applied in the <span className="code-inline"><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake">process_pending_stake</a></span> function.
        <b>let</b> diff = pool.pending_total_sui_withdraw - pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>;
        pool.extra_fields.add(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_UnderflowSuiBalance">UnderflowSuiBalance</a> {}, diff);
        0
    };
    pool.pool_token_balance = <b>if</b> (pool.pool_token_balance &gt;= pool.pending_pool_token_withdraw) {
        pool.pool_token_balance - pool.pending_pool_token_withdraw
    } <b>else</b> {
        0
    };
    pool.pending_total_sui_withdraw = 0;
    pool.pending_pool_token_withdraw = 0;
}
</code></pre>

Function <code>process_pending_stake</code>

Called at epoch boundaries to process the pending stake.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake">process_pending_stake</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_process_pending_stake">process_pending_stake</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>) {
    // Use the most up to date exchange rate with the rewards deposited and withdraws effectuated.
    <b>let</b> latest_exchange_rate = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> {
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>,
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>: pool.pool_token_balance,
    };
    // This key is only present <b>if</b> the <span className="code-inline"><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a></span> underflowed, hence, the current value of <span className="code-inline"><a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a></span>
    // is <span className="code-inline">0</span>. Pool token balance will be recalculated automatically <b>for</b> <span className="code-inline">0</span> value.
    <b>let</b> sui_diff = {
        <b>let</b> key = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_UnderflowSuiBalance">UnderflowSuiBalance</a> {};
        <b>if</b> (pool.extra_fields.contains(key)) pool.extra_fields.remove(key) <b>else</b> 0
    };
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> + pool.pending_stake - sui_diff;
    pool.pool_token_balance = latest_exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>);
    pool.pending_stake = 0;
}
</code></pre>

Function <code>withdraw_rewards</code>

This function does the following:
1. Calculates the total amount of SUI (including principal and rewards) that the provided pool tokens represent
at the current exchange rate.
2. Using the above number and the given principal_withdraw_amount, calculates the rewards portion of the
stake we should withdraw.
3. Withdraws the rewards portion from the rewards pool at the current exchange rate. We only withdraw the rewards
portion because the principal portion was already taken out of the staker's self custodied StakedSui.

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_rewards">withdraw_rewards</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, principal_withdraw_amount: u64, pool_token_withdraw_amount: u64, epoch: u64): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_withdraw_rewards">withdraw_rewards</a>(
    pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    principal_withdraw_amount: u64,
    pool_token_withdraw_amount: u64,
    epoch: u64,
): Balance&lt;SUI&gt; {
    <b>let</b> exchange_rate = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(epoch);
    <b>let</b> total_sui_withdraw_amount = exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(pool_token_withdraw_amount);
    <b>let</b> <b>mut</b> reward_withdraw_amount = <b>if</b> (total_sui_withdraw_amount &gt;= principal_withdraw_amount) {
        total_sui_withdraw_amount - principal_withdraw_amount
    } <b>else</b> 0;
    // This may happen when we are withdrawing everything from the pool and
    // the rewards pool balance may be less than reward_withdraw_amount.
    // TODO: FIGURE OUT EXACTLY WHY THIS CAN HAPPEN.
    reward_withdraw_amount = reward_withdraw_amount.min(pool.rewards_pool.value());
    pool.rewards_pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(reward_withdraw_amount)
}
</code></pre>

Function <code>activate_staking_pool</code>

Called by <a href="../sui_sui_system/validator#sui_system_validator">validator</a> module to activate a staking pool.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activate_staking_pool">activate_staking_pool</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activate_staking_pool">activate_staking_pool</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>: u64) {
    // Add the initial exchange rate to the table.
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>.add(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_initial_exchange_rate">initial_exchange_rate</a>());
    // Check that the pool is preactive and not inactive.
    <b>assert</b>!(pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EPoolAlreadyActive">EPoolAlreadyActive</a>);
    <b>assert</b>!(!pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EActivationOfInactivePool">EActivationOfInactivePool</a>);
    // Fill in the active epoch.
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>.fill(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>);
}
</code></pre>

Function <code>deactivate_staking_pool</code>

Deactivate a staking pool by setting the deactivation_epoch. After
this pool deactivation, the pool stops earning rewards. Only stake
withdraws can be made to the pool.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_deactivate_staking_pool">deactivate_staking_pool</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, deactivation_epoch: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_deactivate_staking_pool">deactivate_staking_pool</a>(pool: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, deactivation_epoch: u64) {
    // We can't deactivate an already deactivated pool.
    <b>assert</b>!(!pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EDeactivationOfInactivePool">EDeactivationOfInactivePool</a>);
    pool.deactivation_epoch = option::some(deactivation_epoch);
}
</code></pre>

Function <code>sui_balance</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): u64 { pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a> }
</code></pre>

Function <code>pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>): ID { staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> }
</code></pre>

Function <code>fungible_staked_sui_pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_pool_id">fungible_staked_sui_pool_id</a>(fungible_staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_pool_id">fungible_staked_sui_pool_id</a>(fungible_staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>): ID {
    fungible_staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>
}
</code></pre>

Function <code>staked_sui_amount</code>

Returns the principal amount of <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_staked_sui_amount">staked_sui_amount</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_staked_sui_amount">staked_sui_amount</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>): u64 { staked_sui.principal.value() }
</code></pre>

Function <code>stake_activation_epoch</code>

Returns the activation epoch of <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>(staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>): u64 {
    staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>
}
</code></pre>

Function <code>is_preactive</code>

Returns true if the input staking pool is preactive.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): bool {
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>.is_none()
}
</code></pre>

Function <code>activation_epoch</code>

Returns the activation epoch of the <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>. For validator candidates,
or pending validators, the value returned is None. For active validators,
the value is the epoch before the validator was activated.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): Option&lt;u64&gt; {
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>
}
</code></pre>

Function <code>is_inactive</code>

Returns true if the input staking pool is inactive.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_inactive">is_inactive</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): bool {
    pool.deactivation_epoch.is_some()
}
</code></pre>

Function <code>fungible_staked_sui_value</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>(fungible_staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_fungible_staked_sui_value">fungible_staked_sui_value</a>(fungible_staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>): u64 {
    fungible_staked_sui.value
}
</code></pre>

Function <code>split_fungible_staked_sui</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split_fungible_staked_sui">split_fungible_staked_sui</a>(fungible_staked_sui: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, split_amount: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split_fungible_staked_sui">split_fungible_staked_sui</a>(
    fungible_staked_sui: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>,
    split_amount: u64,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> {
    <b>assert</b>!(split_amount &lt;= fungible_staked_sui.value, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInsufficientPoolTokenBalance">EInsufficientPoolTokenBalance</a>);
    fungible_staked_sui.value = fungible_staked_sui.value - split_amount;
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> {
        id: object::new(ctx),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>: fungible_staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>,
        value: split_amount,
    }
}
</code></pre>

Function <code>join_fungible_staked_sui</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_join_fungible_staked_sui">join_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, other: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_join_fungible_staked_sui">join_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>, other: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a>) {
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">FungibleStakedSui</a> { id, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>, value } = other;
    <b>assert</b>!(self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> == <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EWrongPool">EWrongPool</a>);
    id.delete();
    self.value = self.value + value;
}
</code></pre>

Function <code>split</code>

Split StakedSui self to two parts, one with principal split_amount,
and the remaining principal is left in self.
All the other parameters of the StakedSui like <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a> or <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> remain the same.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, split_amount: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>, split_amount: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> {
    <b>let</b> original_amount = self.principal.value();
    <b>assert</b>!(split_amount &lt;= original_amount, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EInsufficientSuiTokenBalance">EInsufficientSuiTokenBalance</a>);
    <b>let</b> remaining_amount = original_amount - split_amount;
    // Both resulting parts should have at least <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>.
    <b>assert</b>!(remaining_amount &gt;= <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EStakedSuiBelowThreshold">EStakedSuiBelowThreshold</a>);
    <b>assert</b>!(split_amount &gt;= <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EStakedSuiBelowThreshold">EStakedSuiBelowThreshold</a>);
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> {
        id: object::new(ctx),
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>: self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>,
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>: self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>,
        principal: self.principal.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(split_amount),
    }
}
</code></pre>

Function <code>split_staked_sui</code>

Split the given StakedSui to the two parts, one with principal split_amount,
transfer the newly split part to the sender address.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split_staked_sui">split_staked_sui</a>(stake: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, split_amount: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split_staked_sui">split_staked_sui</a>(stake: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>, split_amount: u64, ctx: &<b>mut</b> TxContext) {
    transfer::transfer(stake.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_split">split</a>(split_amount, ctx), ctx.sender());
}
</code></pre>

Function <code>join_staked_sui</code>

Consume the staked sui other and add its value to self.
Aborts if some of the staking parameters are incompatible (pool id, stake activation epoch, etc.)

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_join_staked_sui">join_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, other: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_join_staked_sui">join_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>, other: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>) {
    <b>assert</b>!(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_equal_staking_metadata">is_equal_staking_metadata</a>(self, &other), <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_EIncompatibleStakedSui">EIncompatibleStakedSui</a>);
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a> { id, principal, .. } = other;
    id.delete();
    self.principal.join(principal);
}
</code></pre>

Function <code>is_equal_staking_metadata</code>

Returns true if all the staking parameters of the staked sui except the principal are identical

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_equal_staking_metadata">is_equal_staking_metadata</a>(self: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, other: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_equal_staking_metadata">is_equal_staking_metadata</a>(self: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>, other: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>): bool {
    (self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a> == other.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_id">pool_id</a>) &&
    (self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a> == other.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>)
}
</code></pre>

Function <code>pool_token_exchange_rate_at_epoch</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, epoch: u64): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(
    pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    epoch: u64,
): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> {
    // If the pool is preactive then the exchange rate is always 1:1.
    <b>if</b> (pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive_at_epoch">is_preactive_at_epoch</a>(epoch)) {
        <b>return</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_initial_exchange_rate">initial_exchange_rate</a>()
    };
    <b>let</b> clamped_epoch = pool.deactivation_epoch.get_with_default(epoch);
    <b>let</b> <b>mut</b> epoch = clamped_epoch.min(epoch);
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a> = *pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>.borrow();
    // Find the latest epoch that's earlier than the given epoch with an <b>entry</b> in the table
    <b>while</b> (epoch &gt;= <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>) {
        <b>if</b> (pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>.contains(epoch)) {
            <b>return</b> pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>[epoch]
        };
        epoch = epoch - 1;
    };
    // This line really should be unreachable. Do we want an <b>assert</b> <b>false</b> here?
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_initial_exchange_rate">initial_exchange_rate</a>()
}
</code></pre>

Function <code>pending_stake_amount</code>

Returns the total value of the pending staking requests for this staking pool.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pending_stake_amount">pending_stake_amount</a>(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pending_stake_amount">pending_stake_amount</a>(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): u64 {
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.pending_stake
}
</code></pre>

Function <code>pending_stake_withdraw_amount</code>

Returns the total withdrawal from the staking pool this epoch.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pending_stake_withdraw_amount">pending_stake_withdraw_amount</a>(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pending_stake_withdraw_amount">pending_stake_withdraw_amount</a>(<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): u64 {
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.pending_total_sui_withdraw
}
</code></pre>

Function <code>exchange_rates</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>): &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;u64, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>): &Table&lt;u64, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>&gt; {
    &pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_exchange_rates">exchange_rates</a>
}
</code></pre>

Function <code>sui_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>): u64 {
    exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>
}
</code></pre>

Function <code>pool_token_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>): u64 {
    exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>
}
</code></pre>

Function <code>is_preactive_at_epoch</code>

Returns true if the provided staking pool is preactive at the provided epoch.

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive_at_epoch">is_preactive_at_epoch</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, epoch: u64): bool
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive_at_epoch">is_preactive_at_epoch</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, epoch: u64): bool {
    // Either the pool is currently preactive or the pool's starting epoch is later than the provided epoch.
    pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_is_preactive">is_preactive</a>() || (*pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_activation_epoch">activation_epoch</a>.borrow() &gt; epoch)
}
</code></pre>

Function <code>get_sui_amount</code>

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>, token_amount: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>, token_amount: u64): u64 {
    // When either amount is 0, that means we have no stakes with this pool.
    // The other amount might be non-zero when there's dust left in the pool.
    <b>if</b> (exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a> == 0 || exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a> == 0) {
        <b>return</b> token_amount
    };
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>!(exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>, token_amount, exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>)
}
</code></pre>

Function <code>get_token_amount</code>

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(exchange_rate: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: u64): u64 {
    // When either amount is 0, that means we have no stakes with this pool.
    // The other amount might be non-zero when there's dust left in the pool.
    <b>if</b> (exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a> == 0 || exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a> == 0) {
        <b>return</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>
    };
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>!(exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>, exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>)
}
</code></pre>

Function <code>initial_exchange_rate</code>

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_initial_exchange_rate">initial_exchange_rate</a>(): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_initial_exchange_rate">initial_exchange_rate</a>(): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> {
    <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">PoolTokenExchangeRate</a> { <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_amount">sui_amount</a>: 0, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_amount">pool_token_amount</a>: 0 }
}
</code></pre>

Function <code>check_balance_invariants</code>

<code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_check_balance_invariants">check_balance_invariants</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, epoch: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_check_balance_invariants">check_balance_invariants</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>, epoch: u64) {
    <b>let</b> exchange_rate = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(epoch);
    // check that the pool token balance and sui balance ratio matches the exchange rate stored.
    <b>let</b> expected = exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_sui_balance">sui_balance</a>);
    <b>let</b> actual = pool.pool_token_balance;
    <b>assert</b>!(expected == actual, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_ETokenBalancesDoNotMatchExchangeRate">ETokenBalancesDoNotMatchExchangeRate</a>)
}
</code></pre>

Macro function <code>mul_div</code>

<code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>($a: u64, $b: u64, $c: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_mul_div">mul_div</a>($a: u64, $b: u64, $c: u64): u64 {
    (($a <b>as</b> u128) * ($b <b>as</b> u128) / ($c <b>as</b> u128)) <b>as</b> u64
}
</code></pre>

Function <code>calculate_rewards</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_calculate_rewards">calculate_rewards</a>(pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>, staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, current_epoch: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_calculate_rewards">calculate_rewards</a>(
    pool: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">StakingPool</a>,
    staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">StakedSui</a>,
    current_epoch: u64,
): u64 {
    <b>let</b> staked_amount = staked_sui.amount();
    <b>let</b> pool_token_withdraw_amount = {
        <b>let</b> exchange_rate_at_staking_epoch = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(staked_sui.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_stake_activation_epoch">stake_activation_epoch</a>);
        exchange_rate_at_staking_epoch.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_token_amount">get_token_amount</a>(staked_amount)
    };
    <b>let</b> new_epoch_exchange_rate = pool.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(current_epoch);
    <b>let</b> total_sui_withdraw_amount = new_epoch_exchange_rate.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_get_sui_amount">get_sui_amount</a>(
        pool_token_withdraw_amount,
    );
    <b>let</b> <b>mut</b> reward_withdraw_amount = <b>if</b> (total_sui_withdraw_amount &gt;= staked_amount) {
        total_sui_withdraw_amount - staked_amount
    } <b>else</b> 0;
    reward_withdraw_amount = reward_withdraw_amount.min(pool.rewards_pool.value());
    reward_withdraw_amount
}
</code></pre>