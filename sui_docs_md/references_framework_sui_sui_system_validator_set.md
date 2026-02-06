-  [Struct ValidatorSet](#sui_system_validator_set_ValidatorSet)
-  [Struct ValidatorEpochInfoEvent](#sui_system_validator_set_ValidatorEpochInfoEvent)
-  [Struct ValidatorEpochInfoEventV2](#sui_system_validator_set_ValidatorEpochInfoEventV2)
-  [Struct ValidatorJoinEvent](#sui_system_validator_set_ValidatorJoinEvent)
-  [Struct ValidatorLeaveEvent](#sui_system_validator_set_ValidatorLeaveEvent)
-  [Struct VotingPowerAdmissionStartEpochKey](#sui_system_validator_set_VotingPowerAdmissionStartEpochKey)
-  [Constants](#@Constants_0)
-  [Function new](#sui_system_validator_set_new)
-  [Function request_add_validator_candidate](#sui_system_validator_set_request_add_validator_candidate)
-  [Function request_remove_validator_candidate](#sui_system_validator_set_request_remove_validator_candidate)
-  [Function request_add_validator](#sui_system_validator_set_request_add_validator)
-  [Function can_join](#sui_system_validator_set_can_join)
-  [Function get_voting_power_thresholds](#sui_system_validator_set_get_voting_power_thresholds)
-  [Function assert_no_pending_or_active_duplicates](#sui_system_validator_set_assert_no_pending_or_active_duplicates)
-  [Function request_remove_validator](#sui_system_validator_set_request_remove_validator)
-  [Function request_add_stake](#sui_system_validator_set_request_add_stake)
-  [Function request_withdraw_stake](#sui_system_validator_set_request_withdraw_stake)
-  [Function convert_to_fungible_staked_sui](#sui_system_validator_set_convert_to_fungible_staked_sui)
-  [Function redeem_fungible_staked_sui](#sui_system_validator_set_redeem_fungible_staked_sui)
-  [Function request_set_commission_rate](#sui_system_validator_set_request_set_commission_rate)
-  [Function advance_epoch](#sui_system_validator_set_advance_epoch)
-  [Function update_validator_positions_and_calculate_total_stake](#sui_system_validator_set_update_validator_positions_and_calculate_total_stake)
-  [Function effectuate_staged_metadata](#sui_system_validator_set_effectuate_staged_metadata)
-  [Function derive_reference_gas_price](#sui_system_validator_set_derive_reference_gas_price)
-  [Function total_stake](#sui_system_validator_set_total_stake)
-  [Function validator_total_stake_amount](#sui_system_validator_set_validator_total_stake_amount)
-  [Function validator_stake_amount](#sui_system_validator_set_validator_stake_amount)
-  [Function validator_voting_power](#sui_system_validator_set_validator_voting_power)
-  [Function validator_staking_pool_id](#sui_system_validator_set_validator_staking_pool_id)
-  [Function staking_pool_mappings](#sui_system_validator_set_staking_pool_mappings)
-  [Function validator_address_by_pool_id](#sui_system_validator_set_validator_address_by_pool_id)
-  [Function pool_exchange_rates](#sui_system_validator_set_pool_exchange_rates)
-  [Function validator_by_pool_id](#sui_system_validator_set_validator_by_pool_id)
-  [Function next_epoch_validator_count](#sui_system_validator_set_next_epoch_validator_count)
-  [Function is_active_validator_by_sui_address](#sui_system_validator_set_is_active_validator_by_sui_address)
-  [Function is_duplicate_with_active_validator](#sui_system_validator_set_is_duplicate_with_active_validator)
-  [Function is_duplicate_validator](#sui_system_validator_set_is_duplicate_validator)
-  [Function count_duplicates_vec](#sui_system_validator_set_count_duplicates_vec)
-  [Function is_duplicate_with_pending_validator](#sui_system_validator_set_is_duplicate_with_pending_validator)
-  [Function count_duplicates_tablevec](#sui_system_validator_set_count_duplicates_tablevec)
-  [Function get_candidate_or_active_validator_mut](#sui_system_validator_set_get_candidate_or_active_validator_mut)
-  [Function find_validator](#sui_system_validator_set_find_validator)
-  [Function find_validator_from_table_vec](#sui_system_validator_set_find_validator_from_table_vec)
-  [Function get_validator_indices](#sui_system_validator_set_get_validator_indices)
-  [Function get_validator_mut](#sui_system_validator_set_get_validator_mut)
-  [Function get_active_or_pending_or_candidate_validator_mut](#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut)
-  [Function get_validator_mut_with_verified_cap](#sui_system_validator_set_get_validator_mut_with_verified_cap)
-  [Function get_validator_mut_with_ctx](#sui_system_validator_set_get_validator_mut_with_ctx)
-  [Function get_validator_mut_with_ctx_including_candidates](#sui_system_validator_set_get_validator_mut_with_ctx_including_candidates)
-  [Function get_validator_ref](#sui_system_validator_set_get_validator_ref)
-  [Function get_active_or_pending_or_candidate_validator_ref](#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref)
-  [Function get_active_validator_ref](#sui_system_validator_set_get_active_validator_ref)
-  [Function get_pending_validator_ref](#sui_system_validator_set_get_pending_validator_ref)
-  [Function verify_cap](#sui_system_validator_set_verify_cap)
-  [Function process_pending_removals](#sui_system_validator_set_process_pending_removals)
-  [Function process_validator_departure](#sui_system_validator_set_process_validator_departure)
-  [Function clean_report_records_leaving_validator](#sui_system_validator_set_clean_report_records_leaving_validator)
-  [Function sort_removal_list](#sui_system_validator_set_sort_removal_list)
-  [Function process_pending_stakes_and_withdraws](#sui_system_validator_set_process_pending_stakes_and_withdraws)
-  [Function calculate_total_stakes](#sui_system_validator_set_calculate_total_stakes)
-  [Function adjust_stake_and_gas_price](#sui_system_validator_set_adjust_stake_and_gas_price)
-  [Function compute_reward_adjustments](#sui_system_validator_set_compute_reward_adjustments)
-  [Function compute_slashed_validators](#sui_system_validator_set_compute_slashed_validators)
-  [Function compute_unadjusted_reward_distribution](#sui_system_validator_set_compute_unadjusted_reward_distribution)
-  [Function compute_adjusted_reward_distribution](#sui_system_validator_set_compute_adjusted_reward_distribution)
-  [Function distribute_reward](#sui_system_validator_set_distribute_reward)
-  [Function emit_validator_epoch_events](#sui_system_validator_set_emit_validator_epoch_events)
-  [Function sum_voting_power_by_addresses](#sui_system_validator_set_sum_voting_power_by_addresses)
-  [Function active_validators](#sui_system_validator_set_active_validators)
-  [Function is_validator_candidate](#sui_system_validator_set_is_validator_candidate)
-  [Function is_active_validator](#sui_system_validator_set_is_active_validator)
-  [Function is_inactive_validator](#sui_system_validator_set_is_inactive_validator)
-  [Function is_at_risk_validator](#sui_system_validator_set_is_at_risk_validator)
-  [Function active_validator_addresses](#sui_system_validator_set_active_validator_addresses)
-  [Macro function mul_div](#sui_system_validator_set_mul_div)

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
<b>use</b> <a href="../sui_sui/priority_queue#sui_priority_queue">sui::priority_queue</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/sui#sui_sui">sui::sui</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/table_vec#sui_table_vec">sui::table_vec</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
<b>use</b> <a href="../sui_sui/versioned#sui_versioned">sui::versioned</a>;
<b>use</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">sui_system::staking_pool</a>;
<b>use</b> <a href="../sui_sui_system/validator#sui_system_validator">sui_system::validator</a>;
<b>use</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap">sui_system::validator_cap</a>;
<b>use</b> <a href="../sui_sui_system/validator_wrapper#sui_system_validator_wrapper">sui_system::validator_wrapper</a>;
<b>use</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">sui_system::voting_power</a>;
</code>

Struct <code>ValidatorSet</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>: u64</code>
</dt>
<dd>
 Total amount of stake from all active validators at the beginning of the epoch.
 Written only once per epoch, in <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_advance_epoch">advance_epoch</a></code> function.
</dd>
<dt>
<code><a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>: vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;</code>
</dt>
<dd>
 The current list of active validators.
</dd>
<dt>
<code>pending_active_validators: <a href="../sui_sui/table_vec#sui_table_vec_TableVec">sui::table_vec::TableVec</a>&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;</code>
</dt>
<dd>
 List of new validator candidates added during the current epoch.
 They will be processed at the end of the epoch.
</dd>
<dt>
<code>pending_removals: vector&lt;u64&gt;</code>
</dt>
<dd>
 Removal requests from the validators. Each element is an index
 pointing to <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a></code>.
</dd>
<dt>
<code><a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, <b>address</b>&gt;</code>
</dt>
<dd>
 Mappings from staking pool's ID to the sui address of a validator.
</dd>
<dt>
<code>inactive_validators: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, <a href="../sui_sui_system/validator_wrapper#sui_system_validator_wrapper_ValidatorWrapper">sui_system::validator_wrapper::ValidatorWrapper</a>&gt;</code>
</dt>
<dd>
 Mapping from a staking pool ID to the inactive validator that has that pool as its staking pool.
 When a validator is deactivated the validator is removed from <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a></code> it
 is added to this table so that stakers can continue to withdraw their stake from it.
</dd>
<dt>
<code>validator_candidates: <a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;<b>address</b>, <a href="../sui_sui_system/validator_wrapper#sui_system_validator_wrapper_ValidatorWrapper">sui_system::validator_wrapper::ValidatorWrapper</a>&gt;</code>
</dt>
<dd>
 Table storing preactive/candidate validators, mapping their addresses to their <code>Validator </code> structs.
 When an address calls <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator_candidate">request_add_validator_candidate</a></code>, they get added to this table and become a preactive
 validator.
 When the candidate has met the min stake requirement, they can call <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator">request_add_validator</a></code> to
 officially add them to the active validator set <code><a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a></code> next epoch.
</dd>
<dt>
<code>at_risk_validators: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, u64&gt;</code>
</dt>
<dd>
 Table storing the number of epochs during which a validator's stake has been below the low stake threshold.
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
 Any extra fields that's not defined statically.
</dd>
</dl>

Struct <code>ValidatorEpochInfoEvent</code>

Event containing staking and rewards related information of
each validator, emitted during epoch advancement.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorEpochInfoEvent">ValidatorEpochInfoEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>reference_gas_survey_quote: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>commission_rate: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>pool_staking_reward: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>storage_fund_staking_reward: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>pool_token_exchange_rate: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a></code>
</dt>
<dd>
</dd>
<dt>
<code>tallying_rule_reporters: vector&lt;<b>address</b>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>tallying_rule_global_score: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ValidatorEpochInfoEventV2</code>

V2 of ValidatorEpochInfoEvent containing more information about the validator.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorEpochInfoEventV2">ValidatorEpochInfoEventV2</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>reference_gas_survey_quote: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake: u64</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>commission_rate: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>pool_staking_reward: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>storage_fund_staking_reward: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>pool_token_exchange_rate: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a></code>
</dt>
<dd>
</dd>
<dt>
<code>tallying_rule_reporters: vector&lt;<b>address</b>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>tallying_rule_global_score: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ValidatorJoinEvent</code>

Event emitted every time a new validator joins the committee.
The epoch value corresponds to the first epoch this change takes place.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorJoinEvent">ValidatorJoinEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>staking_pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ValidatorLeaveEvent</code>

Event emitted every time a validator leaves the committee.
The epoch value corresponds to the first epoch this change takes place.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorLeaveEvent">ValidatorLeaveEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>staking_pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>is_voluntary: bool</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>VotingPowerAdmissionStartEpochKey</code>

Key for the extra_fields bag to store the start epoch of allowing admission
of new validators based on a minimum voting power rather than a minimum stake.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_VotingPowerAdmissionStartEpochKey">VotingPowerAdmissionStartEpochKey</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENonValidatorInReportRecords">ENonValidatorInReportRecords</a>: u64 = 0;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EInvalidStakeAdjustmentAmount">EInvalidStakeAdjustmentAmount</a>: u64 = 1;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EDuplicateValidator">EDuplicateValidator</a>: u64 = 2;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENoPoolFound">ENoPoolFound</a>: u64 = 3;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>: u64 = 4;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EMinJoiningStakeNotReached">EMinJoiningStakeNotReached</a>: u64 = 5;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EAlreadyValidatorCandidate">EAlreadyValidatorCandidate</a>: u64 = 6;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorNotCandidate">EValidatorNotCandidate</a>: u64 = 7;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotValidatorCandidate">ENotValidatorCandidate</a>: u64 = 8;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotActiveOrPendingValidator">ENotActiveOrPendingValidator</a>: u64 = 9;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EStakingBelowThreshold">EStakingBelowThreshold</a>: u64 = 10;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorAlreadyRemoved">EValidatorAlreadyRemoved</a>: u64 = 11;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAPendingValidator">ENotAPendingValidator</a>: u64 = 12;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorSetEmpty">EValidatorSetEmpty</a>: u64 = 13;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_EInvalidCap">EInvalidCap</a>: u64 = 101;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ACTIVE_VALIDATOR_ONLY">ACTIVE_VALIDATOR_ONLY</a>: u8 = 1;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ACTIVE_OR_PENDING_VALIDATOR">ACTIVE_OR_PENDING_VALIDATOR</a>: u8 = 2;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ANY_VALIDATOR">ANY_VALIDATOR</a>: u8 = 3;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_BASIS_POINT_DENOMINATOR">BASIS_POINT_DENOMINATOR</a>: u64 = 10000;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>: u64 = 1000000000;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_PHASE_LENGTH">PHASE_LENGTH</a>: u64 = 14;
</code>

Function <code>new</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_new">new</a>(init_active_validators: vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_new">new</a>(
    init_active_validators: vector&lt;Validator&gt;,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a> {
    <b>let</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_calculate_total_stakes">calculate_total_stakes</a>(&init_active_validators);
    <b>let</b> <b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a> = table::new(ctx);
    init_active_validators.do_ref!(|v| {
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.add(v.staking_pool_id(), v.sui_address());
    });
    <b>let</b> <b>mut</b> validators = <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a> {
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>,
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>: init_active_validators,
        pending_active_validators: table_vec::empty(ctx),
        pending_removals: vector[],
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>,
        inactive_validators: table::new(ctx),
        validator_candidates: table::new(ctx),
        at_risk_validators: vec_map::empty(),
        extra_fields: bag::new(ctx),
    };
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_set_voting_power">voting_power::set_voting_power</a>(&<b>mut</b> validators.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, <a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>);
    validators
}
</code></pre>

Function <code>request_add_validator_candidate</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> to add a new validator candidate.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator_candidate">request_add_validator_candidate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator_candidate">request_add_validator_candidate</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: Validator,
    ctx: &<b>mut</b> TxContext,
) {
    // The next assertions are not critical <b>for</b> the protocol, but they are here to catch problematic configs earlier.
    <b>assert</b>!(
        !self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_active_validator">is_duplicate_with_active_validator</a>(&<a href="../sui_sui_system/validator#sui_system_validator">validator</a>)
            && !self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_pending_validator">is_duplicate_with_pending_validator</a>(&<a href="../sui_sui_system/validator#sui_system_validator">validator</a>),
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_EDuplicateValidator">EDuplicateValidator</a>,
    );
    <b>let</b> validator_address = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address();
    <b>assert</b>!(!self.validator_candidates.contains(validator_address), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EAlreadyValidatorCandidate">EAlreadyValidatorCandidate</a>);
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.is_preactive(), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorNotCandidate">EValidatorNotCandidate</a>);
    // Add <a href="../sui_sui_system/validator#sui_system_validator">validator</a> to the candidates mapping and the pool id mappings so that users can start
    // staking with this candidate.
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.add(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id(), validator_address);
    self.validator_candidates.add(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address(), <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.wrap_v1(ctx));
}
</code></pre>

Function <code>request_remove_validator_candidate</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> to remove a validator candidate, and move them to inactive_validators.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_remove_validator_candidate">request_remove_validator_candidate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_remove_validator_candidate">request_remove_validator_candidate</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> validator_address = ctx.sender();
    <b>assert</b>!(self.validator_candidates.contains(validator_address), <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>let</b> <b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = self.validator_candidates.remove(validator_address).destroy();
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.is_preactive(), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorNotCandidate">EValidatorNotCandidate</a>);
    <b>let</b> staking_pool_id = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id();
    // Remove the <a href="../sui_sui_system/validator#sui_system_validator">validator</a>'s staking pool from mappings.
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.remove(staking_pool_id);
    // Deactivate the staking pool.
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.deactivate(ctx.epoch());
    // Add to the inactive tables.
    self.inactive_validators.add(staking_pool_id, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.wrap_v1(ctx));
}
</code></pre>

Function <code>request_add_validator</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> to add a new validator to pending_active_validators, which will be
processed at the end of epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator">request_add_validator</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator">request_add_validator</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, ctx: &TxContext) {
    <b>let</b> validator_address = ctx.sender();
    <b>assert</b>!(self.validator_candidates.contains(validator_address), <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = self.validator_candidates.remove(validator_address).destroy();
    <b>assert</b>!(
        !self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_active_validator">is_duplicate_with_active_validator</a>(&<a href="../sui_sui_system/validator#sui_system_validator">validator</a>)
            && !self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_pending_validator">is_duplicate_with_pending_validator</a>(&<a href="../sui_sui_system/validator#sui_system_validator">validator</a>),
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_EDuplicateValidator">EDuplicateValidator</a>,
    );
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.is_preactive(), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorNotCandidate">EValidatorNotCandidate</a>);
    <b>assert</b>!(self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_can_join">can_join</a>(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>(), ctx), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EMinJoiningStakeNotReached">EMinJoiningStakeNotReached</a>);
    self.pending_active_validators.push_back(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>);
}
</code></pre>

Function <code>can_join</code>

Return <b>true</b> if a  candidate validator with stake will have sufficeint voting power to join the validator set

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_can_join">can_join</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, stake: u64, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_can_join">can_join</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, stake: u64, ctx: &TxContext): bool {
    <b>let</b> (min_joining_voting_power, _, _) = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_voting_power_thresholds">get_voting_power_thresholds</a>(ctx);
    // <b>if</b> the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> will have at least <span className="code-inline">min_joining_voting_power</span> after joining, they can join.
    // this formula comes from SIP-39: https://github.com/sui-foundation/sips/blob/main/sips/sip-39.md
    <b>let</b> future_total_stake = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a> + stake;
    <b>let</b> future_validator_voting_power = <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">voting_power::derive_raw_voting_power</a>(
        stake,
        future_total_stake,
    );
    future_validator_voting_power &gt;= min_joining_voting_power
}
</code></pre>

Function <code>get_voting_power_thresholds</code>

return (min, low, very low voting power) thresholds

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_voting_power_thresholds">get_voting_power_thresholds</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (u64, u64, u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_voting_power_thresholds">get_voting_power_thresholds</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, ctx: &TxContext): (u64, u64, u64) {
    <b>let</b> start_epoch = {
        <b>let</b> key = <a href="../sui_sui_system/validator_set#sui_system_validator_set_VotingPowerAdmissionStartEpochKey">VotingPowerAdmissionStartEpochKey</a>();
        <b>if</b> (self.extra_fields.contains(key)) self.extra_fields[key]
        <b>else</b> ctx.epoch() + 1 // will give us the phase 1 values
    };
    // these numbers come from SIP-39: https://github.com/sui-foundation/sips/blob/main/sips/sip-39.md
    <b>let</b> curr_epoch = ctx.epoch();
    <b>if</b> (curr_epoch &lt; start_epoch + <a href="../sui_sui_system/validator_set#sui_system_validator_set_PHASE_LENGTH">PHASE_LENGTH</a>) (12, 8, 4) // phase 1
    <b>else</b> <b>if</b> (curr_epoch &lt; start_epoch + (2 * <a href="../sui_sui_system/validator_set#sui_system_validator_set_PHASE_LENGTH">PHASE_LENGTH</a>)) (6, 4, 2) // phase 2
    <b>else</b> (3, 2, 1) // phase 3
}
</code></pre>

Function <code>assert_no_pending_or_active_duplicates</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_assert_no_pending_or_active_duplicates">assert_no_pending_or_active_duplicates</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_assert_no_pending_or_active_duplicates">assert_no_pending_or_active_duplicates</a>(
    self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &Validator,
) {
    // Validator here must be active or pending, and thus must be identified <b>as</b> duplicate exactly once.
    <b>assert</b>!(
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_vec">count_duplicates_vec</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>) +
            <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_tablevec">count_duplicates_tablevec</a>(&self.pending_active_validators, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>) == 1,
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_EDuplicateValidator">EDuplicateValidator</a>,
    );
}
</code></pre>

Function <code>request_remove_validator</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a>, to remove a validator.
The index of the validator is added to pending_removals and
will be processed at the end of epoch.
Only an active validator can request to be removed.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_remove_validator">request_remove_validator</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_remove_validator">request_remove_validator</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, ctx: &TxContext) {
    <b>let</b> validator_address = ctx.sender();
    <b>let</b> validator_index = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(
        &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        validator_address,
    ).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>);
    <b>assert</b>!(!self.pending_removals.contains(&validator_index), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorAlreadyRemoved">EValidatorAlreadyRemoved</a>);
    self.pending_removals.push_back(validator_index);
}
</code></pre>

Function <code>request_add_stake</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a>, to add a new stake to the validator.
This request is added to the validator's staking pool's pending stake entries, processed at the end
of the epoch.
Aborts in case the staking amount is smaller than MIN_STAKING_THRESHOLD

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_stake">request_add_stake</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>, stake: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_stake">request_add_stake</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_address: <b>address</b>,
    stake: Balance&lt;SUI&gt;,
    ctx: &<b>mut</b> TxContext,
): StakedSui {
    <b>let</b> sui_amount = stake.value();
    <b>assert</b>!(sui_amount &gt;= <a href="../sui_sui_system/validator_set#sui_system_validator_set_MIN_STAKING_THRESHOLD">MIN_STAKING_THRESHOLD</a>, <a href="../sui_sui_system/validator_set#sui_system_validator_set_EStakingBelowThreshold">EStakingBelowThreshold</a>);
    self
        .<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(validator_address)
        .<a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_stake">request_add_stake</a>(stake, ctx.sender(), ctx)
}
</code></pre>

Function <code>request_withdraw_stake</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a>, to withdraw some share of a stake from the validator. The share to withdraw
is denoted by principal_withdraw_amount. One of two things occurs in this function:
1. If the staked_sui is staked with an active validator, the request is added to the validator's
staking pool's pending stake withdraw entries, processed at the end of the epoch.
2. If the staked_sui was staked with a validator that is no longer active,
the stake and any rewards corresponding to it will be immediately processed.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_withdraw_stake">request_withdraw_stake</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_withdraw_stake">request_withdraw_stake</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    staked_sui: StakedSui,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    <b>let</b> staking_pool_id = staked_sui.pool_id();
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(staking_pool_id)) {
        // This is an active <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> validator_address = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[staked_sui.pool_id()];
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(validator_address)
    } <b>else</b> {
        // This is an inactive pool.
        <b>assert</b>!(self.inactive_validators.contains(staking_pool_id), <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENoPoolFound">ENoPoolFound</a>);
        self.inactive_validators[staking_pool_id].load_validator_maybe_upgrade()
    };
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_request_withdraw_stake">request_withdraw_stake</a>(staked_sui, ctx)
}
</code></pre>

Function <code>convert_to_fungible_staked_sui</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    staked_sui: StakedSui,
    ctx: &<b>mut</b> TxContext,
): FungibleStakedSui {
    <b>let</b> staking_pool_id = staked_sui.pool_id();
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(staking_pool_id)) {
        // This is an active <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> validator_address = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[staking_pool_id];
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(validator_address)
    } <b>else</b> {
        // This is an inactive pool.
        <b>assert</b>!(self.inactive_validators.contains(staking_pool_id), <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENoPoolFound">ENoPoolFound</a>);
        self.inactive_validators[staking_pool_id].load_validator_maybe_upgrade()
    };
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(staked_sui, ctx)
}
</code></pre>

Function <code>redeem_fungible_staked_sui</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, fungible_staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    fungible_staked_sui: FungibleStakedSui,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    <b>let</b> staking_pool_id = fungible_staked_sui.pool_id();
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(staking_pool_id)) {
        // This is an active <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> validator_address = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[staking_pool_id];
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(validator_address)
    } <b>else</b> {
        // This is an inactive pool.
        <b>assert</b>!(self.inactive_validators.contains(staking_pool_id), <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENoPoolFound">ENoPoolFound</a>);
        self.inactive_validators[staking_pool_id].load_validator_maybe_upgrade()
    };
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(fungible_staked_sui, ctx)
}
</code></pre>

Function <code>request_set_commission_rate</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_set_commission_rate">request_set_commission_rate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, new_commission_rate: u64, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_set_commission_rate">request_set_commission_rate</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    new_commission_rate: u64,
    ctx: &TxContext,
) {
    <b>let</b> validator_address = ctx.sender();
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut">get_validator_mut</a>(&<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_request_set_commission_rate">request_set_commission_rate</a>(new_commission_rate);
}
</code></pre>

Function <code>advance_epoch</code>

Update the validator set at the end of epoch.
It does the following things:
1. Distribute stake award.
2. Process pending stake deposits and withdraws for each validator (adjust_stake).
3. Process pending stake deposits, and withdraws.
4. Process pending validator application and withdraws.
5. At the end, we calculate the total stake for the new epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_advance_epoch">advance_epoch</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, computation_reward: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, storage_fund_reward: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, validator_report_records: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, reward_slashing_rate: u64, low_stake_grace_period: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_advance_epoch">advance_epoch</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    computation_reward: &<b>mut</b> Balance&lt;SUI&gt;,
    storage_fund_reward: &<b>mut</b> Balance&lt;SUI&gt;,
    validator_report_records: &<b>mut</b> VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    reward_slashing_rate: u64,
    low_stake_grace_period: u64,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> new_epoch = ctx.epoch() + 1;
    <b>let</b> total_voting_power = <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">voting_power::total_voting_power</a>();
    // switch to using voting power based admission, <b>if</b> we are not already using it
    <b>let</b> key = <a href="../sui_sui_system/validator_set#sui_system_validator_set_VotingPowerAdmissionStartEpochKey">VotingPowerAdmissionStartEpochKey</a>();
    <b>if</b> (!self.extra_fields.contains(key)) self.extra_fields.add(key, ctx.epoch());
    // Compute the reward distribution without taking into account the tallying rule slashing.
    <b>let</b> (
        unadjusted_staking_reward_amounts,
        unadjusted_storage_fund_reward_amounts,
    ) = <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_unadjusted_reward_distribution">compute_unadjusted_reward_distribution</a>(
        &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        total_voting_power,
        computation_reward.value(),
        storage_fund_reward.value(),
    );
    // Use the tallying rule report records <b>for</b> the epoch to compute validators that will be
    // punished.
    <b>let</b> slashed_validators = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_slashed_validators">compute_slashed_validators</a>(*validator_report_records);
    <b>let</b> total_slashed_validator_voting_power = <a href="../sui_sui_system/validator_set#sui_system_validator_set_sum_voting_power_by_addresses">sum_voting_power_by_addresses</a>(
        &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        &slashed_validators,
    );
    // Compute the reward adjustments of slashed validators, to be taken into
    // account in adjusted reward computation.
    <b>let</b> (
        total_staking_reward_adjustment,
        individual_staking_reward_adjustments,
        total_storage_fund_reward_adjustment,
        individual_storage_fund_reward_adjustments,
    ) = <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_reward_adjustments">compute_reward_adjustments</a>(
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_indices">get_validator_indices</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, &slashed_validators),
        reward_slashing_rate,
        &unadjusted_staking_reward_amounts,
        &unadjusted_storage_fund_reward_amounts,
    );
    // Compute the adjusted amounts of stake each <a href="../sui_sui_system/validator#sui_system_validator">validator</a> should get given the tallying rule
    // reward adjustments we computed before.
    // <span className="code-inline"><a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_adjusted_reward_distribution">compute_adjusted_reward_distribution</a></span> must be called before <span className="code-inline"><a href="../sui_sui_system/validator_set#sui_system_validator_set_distribute_reward">distribute_reward</a></span> and <span className="code-inline"><a href="../sui_sui_system/validator_set#sui_system_validator_set_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a></span> to
    // make sure we are using the current epoch's stake information to compute reward distribution.
    <b>let</b> (
        adjusted_staking_reward_amounts,
        adjusted_storage_fund_reward_amounts,
    ) = <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_adjusted_reward_distribution">compute_adjusted_reward_distribution</a>(
        &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        total_voting_power,
        total_slashed_validator_voting_power,
        unadjusted_staking_reward_amounts,
        unadjusted_storage_fund_reward_amounts,
        total_staking_reward_adjustment,
        individual_staking_reward_adjustments,
        total_storage_fund_reward_adjustment,
        individual_storage_fund_reward_adjustments,
    );
    // Distribute the rewards before adjusting stake so that we immediately start compounding
    // the rewards <b>for</b> validators and stakers.
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_distribute_reward">distribute_reward</a>(
        &<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        &adjusted_staking_reward_amounts,
        &adjusted_storage_fund_reward_amounts,
        computation_reward,
        storage_fund_reward,
        ctx,
    );
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>(&<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>);
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(&<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, ctx);
    // Emit events after we have processed all the rewards distribution and pending stakes.
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_emit_validator_epoch_events">emit_validator_epoch_events</a>(
        new_epoch,
        &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
        &adjusted_staking_reward_amounts,
        &adjusted_storage_fund_reward_amounts,
        validator_report_records,
        &slashed_validators,
    );
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_removals">process_pending_removals</a>(validator_report_records, ctx);
    // kick low stake validators out.
    <b>let</b> new_total_stake = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_update_validator_positions_and_calculate_total_stake">update_validator_positions_and_calculate_total_stake</a>(
        low_stake_grace_period,
        validator_report_records,
        ctx,
    );
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a> = new_total_stake;
    <a href="../sui_sui_system/voting_power#sui_system_voting_power_set_voting_power">voting_power::set_voting_power</a>(&<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, new_total_stake);
    // At this point, self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a> are updated <b>for</b> next epoch.
    // Now we process the staged <a href="../sui_sui_system/validator#sui_system_validator">validator</a> metadata.
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_effectuate_staged_metadata">effectuate_staged_metadata</a>();
}
</code></pre>

Function <code>update_validator_positions_and_calculate_total_stake</code>

This function does the following:
- removes validators from at_risk group if their voting power is above the LOW threshold
- increments the number of epochs a validator has been below the LOW threshold but above the
VERY LOW threshold
- removes validators from the active set if they have been below the LOW threshold for more than
low_stake_grace_period epochs
- removes validators from the active set immediately if they are below the VERY LOW threshold
- activates pending validators if they have sufficient voting power

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_update_validator_positions_and_calculate_total_stake">update_validator_positions_and_calculate_total_stake</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, low_stake_grace_period: u64, validator_report_records: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_update_validator_positions_and_calculate_total_stake">update_validator_positions_and_calculate_total_stake</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    low_stake_grace_period: u64,
    validator_report_records: &<b>mut</b> VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    ctx: &<b>mut</b> TxContext,
): u64 {
    // take all pending validators out of the tablevec and put them in a local vector
    <b>let</b> pending_active_validators = vector::tabulate!(
        self.pending_active_validators.length(),
        |_| self.pending_active_validators.pop_back(),
    );
    // Note: we count the total stake of pending validators <b>as</b> well!
    <b>let</b> pending_total_stake = <a href="../sui_sui_system/validator_set#sui_system_validator_set_calculate_total_stakes">calculate_total_stakes</a>(&pending_active_validators);
    <b>let</b> initial_total_stake = <a href="../sui_sui_system/validator_set#sui_system_validator_set_calculate_total_stakes">calculate_total_stakes</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>) + pending_total_stake;
    <b>let</b> (
        min_joining_voting_power_threshold,
        low_voting_power_threshold,
        very_low_voting_power_threshold,
    ) = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_voting_power_thresholds">get_voting_power_thresholds</a>(ctx);
    // Iterate through all the active validators, record their low stake status, and kick them out <b>if</b> the condition is met.
    <b>let</b> <b>mut</b> total_removed_stake = 0; // amount of stake to remove due to departed_validators
    <b>let</b> <b>mut</b> i = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.length();
    <b>while</b> (i &gt; 0) {
        i = i - 1;
        <b>let</b> validator_ref = &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>[i];
        <b>let</b> validator_address = validator_ref.sui_address();
        <b>let</b> validator_stake = validator_ref.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>();
        // calculate the voting power <b>for</b> this <a href="../sui_sui_system/validator#sui_system_validator">validator</a> in the next epoch <b>if</b> no validators are removed
        // <b>if</b> one of more low stake validators are removed, it's possible this <a href="../sui_sui_system/validator#sui_system_validator">validator</a> will have higher voting power--that's ok.
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">voting_power::derive_raw_voting_power</a>(
            validator_stake,
            initial_total_stake,
        );
        // SIP-39: a <a href="../sui_sui_system/validator#sui_system_validator">validator</a> can remain indefinitely with a voting power ≥ LOW_VOTING_POWER_THRESHOLD
        <b>if</b> (<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> &gt;= low_voting_power_threshold) {
            // The <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is safe. We remove their <b>entry</b> from the at_risk map <b>if</b> there exists one.
            <b>if</b> (self.at_risk_validators.contains(&validator_address)) {
                self.at_risk_validators.remove(&validator_address);
            }
            // SIP-39: <b>as</b> soon <b>as</b> the <a href="../sui_sui_system/validator#sui_system_validator">validator</a>’s voting power falls to VERY_LOW_VOTING_POWER_THRESHOLD,
            //      they are on probation and must acquire sufficient stake to recover to voting power
        } <b>else</b> <b>if</b> (<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> &gt;= very_low_voting_power_threshold) {
            // The stake is a bit below the threshold so we increment the <b>entry</b> of the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> in the map.
            <b>let</b> new_low_stake_period = <b>if</b> (self.at_risk_validators.contains(&validator_address)) {
                <b>let</b> num_epochs = &<b>mut</b> self.at_risk_validators[&validator_address];
                *num_epochs = *num_epochs + 1;
                *num_epochs
            } <b>else</b> {
                self.at_risk_validators.insert(validator_address, 1);
                1
            };
            // If the grace period <b>has</b> passed, the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> <b>has</b> to leave us.
            <b>if</b> (new_low_stake_period &gt; low_stake_grace_period) {
                <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.remove(i);
                <b>let</b> removed_stake = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_process_validator_departure">process_validator_departure</a>(
                    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>,
                    validator_report_records,
                    <b>false</b>, // the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is kicked out involuntarily
                    ctx,
                );
                total_removed_stake = total_removed_stake + removed_stake;
            }
            // SIP-39: at the end of an epoch when <a href="../sui_sui_system/validator_set#sui_system_validator_set_new">new</a> voting powers are computed based on stake changes,
            //      any <a href="../sui_sui_system/validator#sui_system_validator">validator</a> with VOTING_POWER &lt; VERY_LOW_VOTING_POWER_THRESHOLD will be removed
        } <b>else</b> {
            // The <a href="../sui_sui_system/validator#sui_system_validator">validator</a>'s stake is lower than the very low threshold so we kick them out immediately.
            <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.remove(i);
            <b>let</b> removed_stake = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_process_validator_departure">process_validator_departure</a>(
                <a href="../sui_sui_system/validator#sui_system_validator">validator</a>,
                validator_report_records,
                <b>false</b>, // the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is kicked out involuntarily
                ctx,
            );
            total_removed_stake = total_removed_stake + removed_stake;
        }
    };
    // check that pending validators still have sufficient stake to be added. this was checked at
    // the time of <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator">request_add_validator</a>, but stake may have been withdrawn, or stakes of other
    // validators may have increased significantly
    pending_active_validators.do!(|<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a>| {
        <b>let</b> validator_stake = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>();
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = <a href="../sui_sui_system/voting_power#sui_system_voting_power_derive_raw_voting_power">voting_power::derive_raw_voting_power</a>(
            validator_stake,
            initial_total_stake,
        );
        <b>if</b> (<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> &gt;= min_joining_voting_power_threshold) {
            <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.activate(ctx.epoch());
            event::emit(<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorJoinEvent">ValidatorJoinEvent</a> {
                epoch: ctx.epoch(),
                validator_address: <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address(),
                staking_pool_id: <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id(),
            });
            self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.push_back(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>);
        } <b>else</b> {
            // <b>return</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> object to the candidate pool. want to do this directly instead of
            // calling <a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_validator_candidate">request_add_validator_candidate</a> because <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a> already <b>has</b> an
            // <b>entry</b> <b>for</b> this <a href="../sui_sui_system/validator#sui_system_validator">validator</a>, and the duplicate checks are redundant
            self
                .validator_candidates
                .add(
                    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address(),
                    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.wrap_v1(ctx),
                );
            total_removed_stake = total_removed_stake + validator_stake;
        }
    });
    // <a href="../sui_sui_system/validator_set#sui_system_validator_set_new">new</a> total stake is the initial total minus the amount removed via validators we kicked out
    initial_total_stake - total_removed_stake
}
</code></pre>

Function <code>effectuate_staged_metadata</code>

Effectuate pending next epoch metadata if they are staged.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_effectuate_staged_metadata">effectuate_staged_metadata</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_effectuate_staged_metadata">effectuate_staged_metadata</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>) {
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.do_mut!(|v| v.<a href="../sui_sui_system/validator_set#sui_system_validator_set_effectuate_staged_metadata">effectuate_staged_metadata</a>());
}
</code></pre>

Function <code>derive_reference_gas_price</code>

Called by <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system</a> to derive reference gas price for the new epoch.
Derive the reference gas price based on the gas price quote submitted by each validator.
The returned gas price should be greater than or equal to 2/3 of the validators submitted
gas price, weighted by stake.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_derive_reference_gas_price">derive_reference_gas_price</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_derive_reference_gas_price">derive_reference_gas_price</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): u64 {
    <b>let</b> entries = self
        .<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>
        .map_ref!(|v| pq::new_entry(v.gas_price(), v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>()));
    // Build a priority queue that will pop entries with gas price from the highest to the lowest.
    <b>let</b> <b>mut</b> pq = pq::new(entries);
    <b>let</b> <b>mut</b> sum = 0;
    <b>let</b> threshold = <a href="../sui_sui_system/voting_power#sui_system_voting_power_total_voting_power">voting_power::total_voting_power</a>() - <a href="../sui_sui_system/voting_power#sui_system_voting_power_quorum_threshold">voting_power::quorum_threshold</a>();
    <b>let</b> <b>mut</b> result = 0;
    <b>while</b> (sum &lt; threshold) {
        <b>let</b> (gas_price, <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>) = pq.pop_max();
        result = gas_price;
        sum = sum + <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>;
    };
    result
}
</code></pre>

Function <code>total_stake</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): u64 {
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>
}
</code></pre>

Function <code>validator_total_stake_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_total_stake_amount">validator_total_stake_amount</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_total_stake_amount">validator_total_stake_amount</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, validator_address: <b>address</b>): u64 {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>()
}
</code></pre>

Function <code>validator_stake_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_stake_amount">validator_stake_amount</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_stake_amount">validator_stake_amount</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, validator_address: <b>address</b>): u64 {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>()
}
</code></pre>

Function <code>validator_voting_power</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_voting_power">validator_voting_power</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_voting_power">validator_voting_power</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, validator_address: <b>address</b>): u64 {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>()
}
</code></pre>

Function <code>validator_staking_pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_staking_pool_id">validator_staking_pool_id</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_staking_pool_id">validator_staking_pool_id</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, validator_address: <b>address</b>): ID {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id()
}
</code></pre>

Function <code>staking_pool_mappings</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, <b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): &Table&lt;ID, <b>address</b>&gt; {
    &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>
}
</code></pre>

Function <code>validator_address_by_pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_address_by_pool_id">validator_address_by_pool_id</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, pool_id: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_address_by_pool_id">validator_address_by_pool_id</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, pool_id: &ID): <b>address</b> {
    // If the pool id is recorded in the mapping, then it must be either candidate or active.
    <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(*pool_id)) {
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[*pool_id]
    } <b>else</b> {
        // otherwise it's inactive
        self.inactive_validators[*pool_id].load_validator_maybe_upgrade().sui_address()
    }
}
</code></pre>

Function <code>pool_exchange_rates</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_pool_exchange_rates">pool_exchange_rates</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, pool_id: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;u64, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_pool_exchange_rates">pool_exchange_rates</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    pool_id: &ID,
): &Table&lt;u64, PoolTokenExchangeRate&gt; {
    // If the pool id is recorded in the mapping, then it must be either candidate or active.
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(*pool_id)) {
        <b>let</b> validator_address = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[*pool_id];
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref">get_active_or_pending_or_candidate_validator_ref</a>(validator_address, <a href="../sui_sui_system/validator_set#sui_system_validator_set_ANY_VALIDATOR">ANY_VALIDATOR</a>)
    } <b>else</b> {
        // otherwise it's inactive
        self.inactive_validators[*pool_id].load_validator_maybe_upgrade()
    };
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.get_staking_pool_ref().exchange_rates()
}
</code></pre>

Function <code>validator_by_pool_id</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_by_pool_id">validator_by_pool_id</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, pool_id: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_validator_by_pool_id">validator_by_pool_id</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, pool_id: &ID): &Validator {
    // If the pool id is recorded in the mapping, then it must be either candidate or active.
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.contains(*pool_id)) {
        <b>let</b> validator_address = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>[*pool_id];
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref">get_active_or_pending_or_candidate_validator_ref</a>(validator_address, <a href="../sui_sui_system/validator_set#sui_system_validator_set_ANY_VALIDATOR">ANY_VALIDATOR</a>)
    } <b>else</b> {
        // otherwise it's inactive
        self.inactive_validators[*pool_id].load_validator_maybe_upgrade()
    };
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>
}
</code></pre>

Function <code>next_epoch_validator_count</code>

Get the total number of validators in the next epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_next_epoch_validator_count">next_epoch_validator_count</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_next_epoch_validator_count">next_epoch_validator_count</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): u64 {
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.length() - self.pending_removals.length() + self.pending_active_validators.length()
}
</code></pre>

Function <code>is_active_validator_by_sui_address</code>

Returns true iff the address exists in active validators.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator_by_sui_address">is_active_validator_by_sui_address</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator_by_sui_address">is_active_validator_by_sui_address</a>(
    self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_address: <b>address</b>,
): bool {
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address).is_some()
}
</code></pre>

Function <code>is_duplicate_with_active_validator</code>

Checks whether new_validator is duplicate with any currently active validators.
It differs from <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator_by_sui_address">is_active_validator_by_sui_address</a> in that the former checks
only the sui address but this function looks at more metadata.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_active_validator">is_duplicate_with_active_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, new_validator: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_active_validator">is_duplicate_with_active_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, new_validator: &Validator): bool {
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_validator">is_duplicate_validator</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, new_validator)
}
</code></pre>

Function <code>is_duplicate_validator</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_validator">is_duplicate_validator</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, new_validator: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_validator">is_duplicate_validator</a>(
    validators: &vector&lt;Validator&gt;,
    new_validator: &Validator,
): bool {
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_vec">count_duplicates_vec</a>(validators, new_validator) &gt; 0
}
</code></pre>

Function <code>count_duplicates_vec</code>

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_vec">count_duplicates_vec</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_vec">count_duplicates_vec</a>(validators: &vector&lt;Validator&gt;, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &Validator): u64 {
    validators.count!(|v| v.is_duplicate(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>))
}
</code></pre>

Function <code>is_duplicate_with_pending_validator</code>

Checks whether new_validator is duplicate with any currently pending validators.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_pending_validator">is_duplicate_with_pending_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, new_validator: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_with_pending_validator">is_duplicate_with_pending_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, new_validator: &Validator): bool {
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_tablevec">count_duplicates_tablevec</a>(&self.pending_active_validators, new_validator) &gt; 0
}
</code></pre>

Function <code>count_duplicates_tablevec</code>

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_tablevec">count_duplicates_tablevec</a>(validators: &<a href="../sui_sui/table_vec#sui_table_vec_TableVec">sui::table_vec::TableVec</a>&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_count_duplicates_tablevec">count_duplicates_tablevec</a>(validators: &TableVec&lt;Validator&gt;, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: &Validator): u64 {
    <b>let</b> <b>mut</b> result = 0;
    validators.length().do!(|i| {
        <b>if</b> (validators[i].is_duplicate(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>)) {
            result = result + 1;
        };
    });
    result
}
</code></pre>

Function <code>get_candidate_or_active_validator_mut</code>

Get mutable reference to either a candidate or an active validator by address.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_candidate_or_active_validator_mut">get_candidate_or_active_validator_mut</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_address: <b>address</b>,
): &<b>mut</b> Validator {
    <b>if</b> (self.validator_candidates.contains(validator_address)) {
        self.validator_candidates[validator_address].load_validator_maybe_upgrade()
    } <b>else</b> {
        <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut">get_validator_mut</a>(&<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address)
    }
}
</code></pre>

Function <code>find_validator</code>

Find validator by validator_address, in validators.
Returns (true, index) if the validator is found, and the index is its index in the list.
If not found, returns (false, 0).

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, validator_address: <b>address</b>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(validators: &vector&lt;Validator&gt;, validator_address: <b>address</b>): Option&lt;u64&gt; {
    validators.find_index!(|v| v.sui_address() == validator_address)
}
</code></pre>

Function <code>find_validator_from_table_vec</code>

Find validator by validator_address, in validators.
Returns (true, index) if the validator is found, and the index is its index in the list.
If not found, returns (false, 0).

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator_from_table_vec">find_validator_from_table_vec</a>(validators: &<a href="../sui_sui/table_vec#sui_table_vec_TableVec">sui::table_vec::TableVec</a>&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, validator_address: <b>address</b>): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator_from_table_vec">find_validator_from_table_vec</a>(
    validators: &TableVec&lt;Validator&gt;,
    validator_address: <b>address</b>,
): Option&lt;u64&gt; {
    <b>let</b> length = validators.length();
    <b>let</b> <b>mut</b> i = 0;
    <b>while</b> (i &lt; length) {
        <b>let</b> v = &validators[i];
        <b>if</b> (v.sui_address() == validator_address) {
            <b>return</b> option::some(i)
        };
        i = i + 1;
    };
    option::none()
}
</code></pre>

Function <code>get_validator_indices</code>

Given a vector of validator addresses, return their indices in the validator set.
Aborts if any address isn't in the given validator set.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_indices">get_validator_indices</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, validator_addresses: &vector&lt;<b>address</b>&gt;): vector&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_indices">get_validator_indices</a>(
    validators: &vector&lt;Validator&gt;,
    validator_addresses: &vector&lt;<b>address</b>&gt;,
): vector&lt;u64&gt; {
    <b>let</b> <b>mut</b> res = vector[];
    validator_addresses.do_ref!(|addr| {
        <b>let</b> idx = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(validators, *addr).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>);
        res.push_back(idx);
    });
    res
}
</code></pre>

Function <code>get_validator_mut</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut">get_validator_mut</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, validator_address: <b>address</b>): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut">get_validator_mut</a>(
    validators: &<b>mut</b> vector&lt;Validator&gt;,
    validator_address: <b>address</b>,
): &<b>mut</b> Validator {
    <b>let</b> idx = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(validators, validator_address).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>);
    &<b>mut</b> validators[idx]
}
</code></pre>

Function <code>get_active_or_pending_or_candidate_validator_mut</code>

Get mutable reference to an active or (if active does not exist) pending or (if pending and
active do not exist) or candidate validator by address.
Note: this function should be called carefully, only after verifying the transaction
sender has the ability to modify the Validator.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut">get_active_or_pending_or_candidate_validator_mut</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>, include_candidate: bool): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut">get_active_or_pending_or_candidate_validator_mut</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_address: <b>address</b>,
    include_candidate: bool,
): &<b>mut</b> Validator {
    <b>let</b> <b>mut</b> validator_index_opt = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <b>if</b> (validator_index_opt.is_some()) {
        <b>let</b> validator_index = validator_index_opt.extract();
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = &<b>mut</b> self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>[validator_index];
        <b>return</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a>
    };
    <b>let</b> <b>mut</b> validator_index_opt = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator_from_table_vec">find_validator_from_table_vec</a>(
        &self.pending_active_validators,
        validator_address,
    );
    // consider both pending validators and the candidate ones
    <b>if</b> (validator_index_opt.is_some()) {
        <b>let</b> validator_index = validator_index_opt.extract();
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = &<b>mut</b> self.pending_active_validators[validator_index];
        <b>return</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a>
    };
    <b>assert</b>!(include_candidate, <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotActiveOrPendingValidator">ENotActiveOrPendingValidator</a>);
    self.validator_candidates[validator_address].load_validator_maybe_upgrade()
}
</code></pre>

Function <code>get_validator_mut_with_verified_cap</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_verified_cap">get_validator_mut_with_verified_cap</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, verified_cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>, include_candidate: bool): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_verified_cap">get_validator_mut_with_verified_cap</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    verified_cap: &ValidatorOperationCap,
    include_candidate: bool,
): &<b>mut</b> Validator {
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut">get_active_or_pending_or_candidate_validator_mut</a>(
        *verified_cap.verified_operation_cap_address(),
        include_candidate,
    )
}
</code></pre>

Function <code>get_validator_mut_with_ctx</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_ctx">get_validator_mut_with_ctx</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_ctx">get_validator_mut_with_ctx</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    ctx: &TxContext,
): &<b>mut</b> Validator {
    <b>let</b> validator_address = ctx.sender();
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut">get_active_or_pending_or_candidate_validator_mut</a>(validator_address, <b>false</b>)
}
</code></pre>

Function <code>get_validator_mut_with_ctx_including_candidates</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_ctx_including_candidates">get_validator_mut_with_ctx_including_candidates</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut_with_ctx_including_candidates">get_validator_mut_with_ctx_including_candidates</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    ctx: &TxContext,
): &<b>mut</b> Validator {
    <b>let</b> validator_address = ctx.sender();
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_mut">get_active_or_pending_or_candidate_validator_mut</a>(validator_address, <b>true</b>)
}
</code></pre>

Function <code>get_validator_ref</code>

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, validator_address: <b>address</b>): &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(validators: &vector&lt;Validator&gt;, validator_address: <b>address</b>): &Validator {
    <b>let</b> idx = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(validators, validator_address).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>);
    &validators[idx]
}
</code></pre>

Function <code>get_active_or_pending_or_candidate_validator_ref</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref">get_active_or_pending_or_candidate_validator_ref</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_address: <b>address</b>, which_validator: u8): &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref">get_active_or_pending_or_candidate_validator_ref</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_address: <b>address</b>,
    which_validator: u8,
): &Validator {
    <b>let</b> <b>mut</b> validator_index_opt = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, validator_address);
    <b>if</b> (validator_index_opt.is_some() || which_validator == <a href="../sui_sui_system/validator_set#sui_system_validator_set_ACTIVE_VALIDATOR_ONLY">ACTIVE_VALIDATOR_ONLY</a>) {
        <b>let</b> validator_index = validator_index_opt.extract();
        <b>return</b> &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>[validator_index]
    };
    <b>let</b> <b>mut</b> validator_index_opt = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator_from_table_vec">find_validator_from_table_vec</a>(
        &self.pending_active_validators,
        validator_address,
    );
    <b>if</b> (validator_index_opt.is_some() || which_validator == <a href="../sui_sui_system/validator_set#sui_system_validator_set_ACTIVE_OR_PENDING_VALIDATOR">ACTIVE_OR_PENDING_VALIDATOR</a>) {
        <b>let</b> validator_index = validator_index_opt.extract();
        <b>return</b> &self.pending_active_validators[validator_index]
    };
    self.validator_candidates[validator_address].load_validator_maybe_upgrade()
}
</code></pre>

Function <code>get_active_validator_ref</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_validator_ref">get_active_validator_ref</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, addr: <b>address</b>): &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_validator_ref">get_active_validator_ref</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, addr: <b>address</b>): &Validator {
    <b>let</b> idx = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator">find_validator</a>(&self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>, addr).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAValidator">ENotAValidator</a>);
    &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>[idx]
}
</code></pre>

Function <code>get_pending_validator_ref</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_pending_validator_ref">get_pending_validator_ref</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, addr: <b>address</b>): &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_pending_validator_ref">get_pending_validator_ref</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, addr: <b>address</b>): &Validator {
    <b>let</b> idx = <a href="../sui_sui_system/validator_set#sui_system_validator_set_find_validator_from_table_vec">find_validator_from_table_vec</a>(
        &self.pending_active_validators,
        addr,
    ).destroy_or!(<b>abort</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENotAPendingValidator">ENotAPendingValidator</a>);
    &self.pending_active_validators[idx]
}
</code></pre>

Function <code>verify_cap</code>

Verify the capability is valid for a Validator.
If active_validator_only is true, only verify the Cap for an active validator.
Otherwise, verify the Cap for au either active or pending validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_verify_cap">verify_cap</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>, which_validator: u8): <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_verify_cap">verify_cap</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    cap: &UnverifiedValidatorOperationCap,
    which_validator: u8,
): ValidatorOperationCap {
    <b>let</b> cap_address = *cap.unverified_operation_cap_address();
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <b>if</b> (which_validator == <a href="../sui_sui_system/validator_set#sui_system_validator_set_ACTIVE_VALIDATOR_ONLY">ACTIVE_VALIDATOR_ONLY</a>) {
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_validator_ref">get_active_validator_ref</a>(cap_address)
    } <b>else</b> {
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_get_active_or_pending_or_candidate_validator_ref">get_active_or_pending_or_candidate_validator_ref</a>(cap_address, which_validator)
    };
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>.operation_cap_id() == &object::id(cap), <a href="../sui_sui_system/validator_set#sui_system_validator_set_EInvalidCap">EInvalidCap</a>);
    cap.into_verified()
}
</code></pre>

Function <code>process_pending_removals</code>

Process the pending withdraw requests. For each pending request, the validator
is removed from validators and its staking pool is put into the inactive_validators table.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_removals">process_pending_removals</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_report_records: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_removals">process_pending_removals</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    validator_report_records: &<b>mut</b> VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_sort_removal_list">sort_removal_list</a>(&<b>mut</b> self.pending_removals);
    self.pending_removals.length().do!(|_| {
        <b>let</b> index = self.pending_removals.pop_back();
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.remove(index);
        self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_process_validator_departure">process_validator_departure</a>(
            <a href="../sui_sui_system/validator#sui_system_validator">validator</a>,
            validator_report_records,
            <b>true</b>, // the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> removes itself voluntarily
            ctx,
        );
    });
}
</code></pre>

Function <code>process_validator_departure</code>

Remove <a href="../sui_sui_system/validator#sui_system_validator">validator</a> from self and return the amount of stake that was removed

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_validator_departure">process_validator_departure</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, validator_report_records: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, is_voluntary: bool, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_validator_departure">process_validator_departure</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    <b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a>: Validator,
    validator_report_records: &<b>mut</b> VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    is_voluntary: bool,
    ctx: &<b>mut</b> TxContext,
): u64 {
    <b>let</b> new_epoch = ctx.epoch() + 1;
    <b>let</b> validator_address = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address();
    <b>let</b> validator_pool_id = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id();
    // Remove the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> from our tables.
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_staking_pool_mappings">staking_pool_mappings</a>.remove(validator_pool_id);
    <b>if</b> (self.at_risk_validators.contains(&validator_address)) {
        self.at_risk_validators.remove(&validator_address);
    };
    <a href="../sui_sui_system/validator_set#sui_system_validator_set_clean_report_records_leaving_validator">clean_report_records_leaving_validator</a>(validator_report_records, validator_address);
    event::emit(<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorLeaveEvent">ValidatorLeaveEvent</a> {
        epoch: new_epoch,
        validator_address,
        staking_pool_id: <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.staking_pool_id(),
        is_voluntary,
    });
    // Deactivate the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> and its staking pool
    <b>let</b> removed_stake = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>();
    <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.deactivate(new_epoch);
    self
        .inactive_validators
        .add(
            validator_pool_id,
            <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.wrap_v1(ctx),
        );
    removed_stake
}
</code></pre>

Function <code>clean_report_records_leaving_validator</code>

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_clean_report_records_leaving_validator">clean_report_records_leaving_validator</a>(validator_report_records: &<b>mut</b> <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, leaving_validator_addr: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_clean_report_records_leaving_validator">clean_report_records_leaving_validator</a>(
    validator_report_records: &<b>mut</b> VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    leaving_validator_addr: <b>address</b>,
) {
    // Remove the records about this <a href="../sui_sui_system/validator#sui_system_validator">validator</a>
    <b>if</b> (validator_report_records.contains(&leaving_validator_addr)) {
        validator_report_records.remove(&leaving_validator_addr);
    };
    // Remove the reports submitted by this <a href="../sui_sui_system/validator#sui_system_validator">validator</a>
    <b>let</b> reported_validators = validator_report_records.keys();
    reported_validators.length().do!(|i| {
        <b>let</b> reported_validator_addr = &reported_validators[i];
        <b>let</b> reporters = &<b>mut</b> validator_report_records[reported_validator_addr];
        <b>if</b> (reporters.contains(&leaving_validator_addr)) {
            reporters.remove(&leaving_validator_addr);
            <b>if</b> (reporters.is_empty()) {
                validator_report_records.remove(reported_validator_addr);
            };
        };
    });
}
</code></pre>

Function <code>sort_removal_list</code>

Sort all the pending removal indexes.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_sort_removal_list">sort_removal_list</a>(withdraw_list: &<b>mut</b> vector&lt;u64&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_sort_removal_list">sort_removal_list</a>(withdraw_list: &<b>mut</b> vector&lt;u64&gt;) {
    <b>let</b> length = withdraw_list.length();
    <b>let</b> <b>mut</b> i = 1;
    <b>while</b> (i &lt; length) {
        <b>let</b> cur = withdraw_list[i];
        <b>let</b> <b>mut</b> j = i;
        <b>while</b> (j &gt; 0) {
            j = j - 1;
            <b>if</b> (withdraw_list[j] &gt; cur) {
                withdraw_list.swap(j, j + 1);
            } <b>else</b> {
                <b>break</b>
            };
        };
        i = i + 1;
    };
}
</code></pre>

Function <code>process_pending_stakes_and_withdraws</code>

Process all active validators' pending stake deposits and withdraws.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(validators: &<b>mut</b> vector&lt;Validator&gt;, ctx: &TxContext) {
    validators.do_mut!(|v| v.<a href="../sui_sui_system/validator_set#sui_system_validator_set_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(ctx))
}
</code></pre>

Function <code>calculate_total_stakes</code>

Calculate the total active validator stake.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_calculate_total_stakes">calculate_total_stakes</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_calculate_total_stakes">calculate_total_stakes</a>(validators: &vector&lt;Validator&gt;): u64 {
    <b>let</b> <b>mut</b> stake = 0;
    validators.do_ref!(|v| stake = stake + v.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>());
    stake
}
</code></pre>

Function <code>adjust_stake_and_gas_price</code>

Process the pending stake changes for each validator.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>(validators: &<b>mut</b> vector&lt;Validator&gt;) {
    validators.do_mut!(|v| v.<a href="../sui_sui_system/validator_set#sui_system_validator_set_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>())
}
</code></pre>

Function <code>compute_reward_adjustments</code>

Compute both the individual reward adjustments and total reward adjustment for staking rewards
as well as storage fund rewards.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_reward_adjustments">compute_reward_adjustments</a>(slashed_validator_indices: vector&lt;u64&gt;, reward_slashing_rate: u64, unadjusted_staking_reward_amounts: &vector&lt;u64&gt;, unadjusted_storage_fund_reward_amounts: &vector&lt;u64&gt;): (u64, <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;u64, u64&gt;, u64, <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;u64, u64&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_reward_adjustments">compute_reward_adjustments</a>(
    slashed_validator_indices: vector&lt;u64&gt;,
    reward_slashing_rate: u64,
    unadjusted_staking_reward_amounts: &vector&lt;u64&gt;,
    unadjusted_storage_fund_reward_amounts: &vector&lt;u64&gt;,
): (
    u64, // sum of staking reward adjustments
    VecMap&lt;u64, u64&gt;, // mapping of individual <a href="../sui_sui_system/validator#sui_system_validator">validator</a>'s staking reward adjustment from index -&gt; amount
    u64, // sum of storage fund reward adjustments
    VecMap&lt;u64, u64&gt;, // mapping of individual <a href="../sui_sui_system/validator#sui_system_validator">validator</a>'s storage fund reward adjustment from index -&gt; amount
) {
    <b>let</b> <b>mut</b> total_staking_reward_adjustment = 0;
    <b>let</b> <b>mut</b> individual_staking_reward_adjustments = vec_map::empty();
    <b>let</b> <b>mut</b> total_storage_fund_reward_adjustment = 0;
    <b>let</b> <b>mut</b> individual_storage_fund_reward_adjustments = vec_map::empty();
    slashed_validator_indices.destroy!(|validator_index| {
        // Use the slashing rate to compute the amount of staking rewards slashed from this punished <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.
        <b>let</b> unadjusted_staking_reward = unadjusted_staking_reward_amounts[validator_index];
        <b>let</b> staking_reward_adjustment = <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>!(
            unadjusted_staking_reward,
            reward_slashing_rate,
            <a href="../sui_sui_system/validator_set#sui_system_validator_set_BASIS_POINT_DENOMINATOR">BASIS_POINT_DENOMINATOR</a>,
        );
        // Insert into individual mapping and record into the total adjustment sum.
        individual_staking_reward_adjustments.insert(validator_index, staking_reward_adjustment);
        total_staking_reward_adjustment =
            total_staking_reward_adjustment + staking_reward_adjustment;
        // Do the same thing <b>for</b> storage fund rewards.
        <b>let</b> unadjusted_storage_fund_reward = unadjusted_storage_fund_reward_amounts[
            validator_index,
        ];
        <b>let</b> storage_fund_reward_adjustment = <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>!(
            unadjusted_storage_fund_reward,
            reward_slashing_rate,
            <a href="../sui_sui_system/validator_set#sui_system_validator_set_BASIS_POINT_DENOMINATOR">BASIS_POINT_DENOMINATOR</a>,
        );
        individual_storage_fund_reward_adjustments.insert(
            validator_index,
            storage_fund_reward_adjustment,
        );
        total_storage_fund_reward_adjustment =
            total_storage_fund_reward_adjustment + storage_fund_reward_adjustment;
    });
    (
        total_staking_reward_adjustment,
        individual_staking_reward_adjustments,
        total_storage_fund_reward_adjustment,
        individual_storage_fund_reward_adjustments,
    )
}
</code></pre>

Function <code>compute_slashed_validators</code>

Process the validator report records of the epoch and return the addresses of the
non-performant validators according to the input threshold.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_slashed_validators">compute_slashed_validators</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, validator_report_records: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_slashed_validators">compute_slashed_validators</a>(
    self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>,
    <b>mut</b> validator_report_records: VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
): vector&lt;<b>address</b>&gt; {
    <b>let</b> <b>mut</b> slashed_validators = vector[];
    <b>while</b> (!validator_report_records.is_empty()) {
        <b>let</b> (validator_address, reporters) = validator_report_records.pop();
        <b>assert</b>!(
            self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator_by_sui_address">is_active_validator_by_sui_address</a>(validator_address),
            <a href="../sui_sui_system/validator_set#sui_system_validator_set_ENonValidatorInReportRecords">ENonValidatorInReportRecords</a>,
        );
        // Sum up the voting power of validators that have reported this <a href="../sui_sui_system/validator#sui_system_validator">validator</a> and check <b>if</b> it <b>has</b>
        // passed the slashing threshold.
        <b>let</b> reporter_votes = <a href="../sui_sui_system/validator_set#sui_system_validator_set_sum_voting_power_by_addresses">sum_voting_power_by_addresses</a>(
            &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>,
            &reporters.into_keys(),
        );
        <b>if</b> (reporter_votes &gt;= <a href="../sui_sui_system/voting_power#sui_system_voting_power_quorum_threshold">voting_power::quorum_threshold</a>()) {
            slashed_validators.push_back(validator_address);
        }
    };
    slashed_validators
}
</code></pre>

Function <code>compute_unadjusted_reward_distribution</code>

Given the current list of active validators, the total stake and total reward,
calculate the amount of reward each validator should get, without taking into
account the tallying rule results.
Returns the unadjusted amounts of staking reward and storage fund reward for each validator.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_unadjusted_reward_distribution">compute_unadjusted_reward_distribution</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, total_voting_power: u64, total_staking_reward: u64, total_storage_fund_reward: u64): (vector&lt;u64&gt;, vector&lt;u64&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_unadjusted_reward_distribution">compute_unadjusted_reward_distribution</a>(
    validators: &vector&lt;Validator&gt;,
    total_voting_power: u64,
    total_staking_reward: u64,
    total_storage_fund_reward: u64,
): (vector&lt;u64&gt;, vector&lt;u64&gt;) {
    <b>let</b> <b>mut</b> staking_reward_amounts = vector[];
    <b>let</b> <b>mut</b> storage_fund_reward_amounts = vector[];
    <b>let</b> length = validators.length();
    <b>let</b> storage_fund_reward_per_validator = total_storage_fund_reward / length;
    validators.do_ref!(|<a href="../sui_sui_system/validator#sui_system_validator">validator</a>| {
        // Integer divisions will truncate the results. Because of this, we expect that at the end
        // there will be some reward remaining in <span className="code-inline">total_staking_reward</span>.
        // Use u128 to avoid multiplication overflow.
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
        <b>let</b> reward_amount = <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>!(<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>, total_staking_reward, total_voting_power);
        staking_reward_amounts.push_back(reward_amount);
        // Storage fund's share of the rewards are equally distributed among validators.
        storage_fund_reward_amounts.push_back(storage_fund_reward_per_validator);
    });
    (staking_reward_amounts, storage_fund_reward_amounts)
}
</code></pre>

Function <code>compute_adjusted_reward_distribution</code>

Use the reward adjustment info to compute the adjusted rewards each validator should get.
Returns the staking rewards each validator gets and the storage fund rewards each validator gets.
The staking rewards are shared with the stakers while the storage fund ones are not.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_adjusted_reward_distribution">compute_adjusted_reward_distribution</a>(validators: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, total_voting_power: u64, total_slashed_validator_voting_power: u64, unadjusted_staking_reward_amounts: vector&lt;u64&gt;, unadjusted_storage_fund_reward_amounts: vector&lt;u64&gt;, total_staking_reward_adjustment: u64, individual_staking_reward_adjustments: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;u64, u64&gt;, total_storage_fund_reward_adjustment: u64, individual_storage_fund_reward_adjustments: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;u64, u64&gt;): (vector&lt;u64&gt;, vector&lt;u64&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_compute_adjusted_reward_distribution">compute_adjusted_reward_distribution</a>(
    validators: &vector&lt;Validator&gt;,
    total_voting_power: u64,
    total_slashed_validator_voting_power: u64,
    unadjusted_staking_reward_amounts: vector&lt;u64&gt;,
    unadjusted_storage_fund_reward_amounts: vector&lt;u64&gt;,
    total_staking_reward_adjustment: u64,
    individual_staking_reward_adjustments: VecMap&lt;u64, u64&gt;,
    total_storage_fund_reward_adjustment: u64,
    individual_storage_fund_reward_adjustments: VecMap&lt;u64, u64&gt;,
): (vector&lt;u64&gt;, vector&lt;u64&gt;) {
    <b>let</b> total_unslashed_validator_voting_power =
        total_voting_power - total_slashed_validator_voting_power;
    <b>let</b> <b>mut</b> adjusted_staking_reward_amounts = vector[];
    <b>let</b> <b>mut</b> adjusted_storage_fund_reward_amounts = vector[];
    <b>let</b> length = validators.length();
    <b>let</b> num_unslashed_validators = length - individual_staking_reward_adjustments.length();
    length.do!(|i| {
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = &validators[i];
        // Integer divisions will truncate the results. Because of this, we expect that at the end
        // there will be some reward remaining in <span className="code-inline">total_reward</span>.
        // Use u128 to avoid multiplication overflow.
        <b>let</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
        // Compute adjusted staking reward.
        <b>let</b> unadjusted_staking_reward_amount = unadjusted_staking_reward_amounts[i];
        // If the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is one of the slashed ones, then subtract the adjustment.
        <b>let</b> adjusted_staking_reward_amount = <b>if</b> (
            individual_staking_reward_adjustments.contains(&i)
        ) {
            <b>let</b> adjustment = individual_staking_reward_adjustments[&i];
            unadjusted_staking_reward_amount - adjustment
        } <b>else</b> {
            // Otherwise the slashed rewards should be distributed among the unslashed
            // validators so add the corresponding adjustment.
            <b>let</b> adjustment = <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>!(
                total_staking_reward_adjustment,
                <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>,
                total_unslashed_validator_voting_power,
            );
            unadjusted_staking_reward_amount + adjustment
        };
        adjusted_staking_reward_amounts.push_back(adjusted_staking_reward_amount);
        // Compute adjusted storage fund reward.
        <b>let</b> unadjusted_storage_fund_reward_amount = unadjusted_storage_fund_reward_amounts[i];
        // If the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is one of the slashed ones, then subtract the adjustment.
        <b>let</b> adjusted_storage_fund_reward_amount = <b>if</b> (
            individual_storage_fund_reward_adjustments.contains(&i)
        ) {
            <b>let</b> adjustment = individual_storage_fund_reward_adjustments[&i];
            unadjusted_storage_fund_reward_amount - adjustment
        } <b>else</b> {
            // Otherwise the slashed rewards should be equally distributed among the unslashed validators.
            <b>let</b> adjustment = total_storage_fund_reward_adjustment / num_unslashed_validators;
            unadjusted_storage_fund_reward_amount + adjustment
        };
        adjusted_storage_fund_reward_amounts.push_back(adjusted_storage_fund_reward_amount);
    });
    (adjusted_staking_reward_amounts, adjusted_storage_fund_reward_amounts)
}
</code></pre>

Function <code>distribute_reward</code>

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_distribute_reward">distribute_reward</a>(validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, adjusted_staking_reward_amounts: &vector&lt;u64&gt;, adjusted_storage_fund_reward_amounts: &vector&lt;u64&gt;, staking_rewards: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, storage_fund_reward: &<b>mut</b> <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_distribute_reward">distribute_reward</a>(
    validators: &<b>mut</b> vector&lt;Validator&gt;,
    adjusted_staking_reward_amounts: &vector&lt;u64&gt;,
    adjusted_storage_fund_reward_amounts: &vector&lt;u64&gt;,
    staking_rewards: &<b>mut</b> Balance&lt;SUI&gt;,
    storage_fund_reward: &<b>mut</b> Balance&lt;SUI&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> length = validators.length();
    <b>assert</b>!(length &gt; 0, <a href="../sui_sui_system/validator_set#sui_system_validator_set_EValidatorSetEmpty">EValidatorSetEmpty</a>);
    length.do!(|i| {
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = &<b>mut</b> validators[i];
        <b>let</b> staking_reward_amount = adjusted_staking_reward_amounts[i];
        <b>let</b> <b>mut</b> staker_reward = staking_rewards.split(staking_reward_amount);
        // Validator takes a cut of the rewards <b>as</b> commission.
        <b>let</b> validator_commission_amount = <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>!(
            staking_reward_amount,
            <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.commission_rate(),
            <a href="../sui_sui_system/validator_set#sui_system_validator_set_BASIS_POINT_DENOMINATOR">BASIS_POINT_DENOMINATOR</a>,
        );
        // The <a href="../sui_sui_system/validator#sui_system_validator">validator</a> reward = storage_fund_reward + commission.
        <b>let</b> <b>mut</b> validator_reward = staker_reward.split(validator_commission_amount <b>as</b> u64);
        // Add storage fund rewards to the <a href="../sui_sui_system/validator#sui_system_validator">validator</a>'s reward.
        validator_reward.join(storage_fund_reward.split(adjusted_storage_fund_reward_amounts[i]));
        // Add rewards to the <a href="../sui_sui_system/validator#sui_system_validator">validator</a>. Don't try and distribute rewards though <b>if</b> the payout is zero.
        <b>if</b> (validator_reward.value() &gt; 0) {
            <b>let</b> validator_address = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.sui_address();
            <b>let</b> rewards_stake = <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/validator_set#sui_system_validator_set_request_add_stake">request_add_stake</a>(
                validator_reward,
                validator_address,
                ctx,
            );
            transfer::public_transfer(rewards_stake, validator_address);
        } <b>else</b> {
            validator_reward.destroy_zero();
        };
        // Add rewards to stake staking pool to auto compound <b>for</b> stakers.
        <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.deposit_stake_rewards(staker_reward);
    });
}
</code></pre>

Function <code>emit_validator_epoch_events</code>

Emit events containing information of each validator for the epoch,
including stakes, rewards, performance, etc.

<code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_emit_validator_epoch_events">emit_validator_epoch_events</a>(new_epoch: u64, vs: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, pool_staking_reward_amounts: &vector&lt;u64&gt;, storage_fund_staking_reward_amounts: &vector&lt;u64&gt;, report_records: &<a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<b>address</b>&gt;&gt;, slashed_validators: &vector&lt;<b>address</b>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_emit_validator_epoch_events">emit_validator_epoch_events</a>(
    new_epoch: u64,
    vs: &vector&lt;Validator&gt;,
    pool_staking_reward_amounts: &vector&lt;u64&gt;,
    storage_fund_staking_reward_amounts: &vector&lt;u64&gt;,
    report_records: &VecMap&lt;<b>address</b>, VecSet&lt;<b>address</b>&gt;&gt;,
    slashed_validators: &vector&lt;<b>address</b>&gt;,
) {
    <b>let</b> length = vs.length();
    length.do!(|i| {
        <b>let</b> v = &vs[i];
        <b>let</b> validator_address = v.sui_address();
        <b>let</b> tallying_rule_reporters = <b>if</b> (report_records.contains(&validator_address)) {
            report_records[&validator_address].into_keys()
        } <b>else</b> {
            vector[]
        };
        <b>let</b> tallying_rule_global_score = <b>if</b> (slashed_validators.contains(&validator_address)) {
            0
        } <b>else</b> {
            1
        };
        event::emit(<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorEpochInfoEventV2">ValidatorEpochInfoEventV2</a> {
            epoch: new_epoch,
            validator_address,
            reference_gas_survey_quote: v.gas_price(),
            stake: v.<a href="../sui_sui_system/validator_set#sui_system_validator_set_total_stake">total_stake</a>(),
            <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: v.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>(),
            commission_rate: v.commission_rate(),
            pool_staking_reward: pool_staking_reward_amounts[i],
            storage_fund_staking_reward: storage_fund_staking_reward_amounts[i],
            pool_token_exchange_rate: v.pool_token_exchange_rate_at_epoch(new_epoch),
            tallying_rule_reporters,
            tallying_rule_global_score,
        });
    });
}
</code></pre>

Function <code>sum_voting_power_by_addresses</code>

Sum up the total stake of a given list of validator addresses.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_sum_voting_power_by_addresses">sum_voting_power_by_addresses</a>(vs: &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, addresses: &vector&lt;<b>address</b>&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_sum_voting_power_by_addresses">sum_voting_power_by_addresses</a>(vs: &vector&lt;Validator&gt;, addresses: &vector&lt;<b>address</b>&gt;): u64 {
    <b>let</b> <b>mut</b> sum = 0;
    addresses.do_ref!(|addr| {
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_ref">get_validator_ref</a>(vs, *addr);
        sum = sum + <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>();
    });
    sum
}
</code></pre>

Function <code>active_validators</code>

Return the active validators in self

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): &vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): &vector&lt;Validator&gt; {
    &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>
}
</code></pre>

Function <code>is_validator_candidate</code>

Returns true if the addr is a validator candidate.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_validator_candidate">is_validator_candidate</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, addr: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_validator_candidate">is_validator_candidate</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, addr: <b>address</b>): bool {
    self.validator_candidates.contains(addr)
}
</code></pre>

Function <code>is_active_validator</code>

Returns true if addr is an active validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator">is_active_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, addr: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_active_validator">is_active_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, addr: <b>address</b>): bool {
    self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>.any!(|v| v.sui_address() == addr)
}
</code></pre>

Function <code>is_inactive_validator</code>

Returns true if the staking pool identified by staking_pool_id is of an inactive validator.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_inactive_validator">is_inactive_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, staking_pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_inactive_validator">is_inactive_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, staking_pool_id: ID): bool {
    self.inactive_validators.contains(staking_pool_id)
}
</code></pre>

Function <code>is_at_risk_validator</code>

Return true if addr is currently an at-risk validator below the minimum stake for removal

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_at_risk_validator">is_at_risk_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>, addr: <b>address</b>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_is_at_risk_validator">is_at_risk_validator</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>, addr: <b>address</b>): bool {
    self.at_risk_validators.contains(&addr)
}
</code></pre>

Function <code>active_validator_addresses</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validator_addresses">active_validator_addresses</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">sui_system::validator_set::ValidatorSet</a>): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validator_addresses">active_validator_addresses</a>(self: &<a href="../sui_sui_system/validator_set#sui_system_validator_set_ValidatorSet">ValidatorSet</a>): vector&lt;<b>address</b>&gt; {
    <b>let</b> vs = &self.<a href="../sui_sui_system/validator_set#sui_system_validator_set_active_validators">active_validators</a>;
    <b>let</b> <b>mut</b> res = vector[];
    vs.do_ref!(|v| res.push_back(v.sui_address()));
    res
}
</code></pre>

Macro function <code>mul_div</code>

<code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>($a: u64, $b: u64, $c: u64): u64
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set_mul_div">mul_div</a>($a: u64, $b: u64, $c: u64): u64 {
    (($a <b>as</b> u128) * ($b <b>as</b> u128) / ($c <b>as</b> u128)) <b>as</b> u64
}
</code></pre>