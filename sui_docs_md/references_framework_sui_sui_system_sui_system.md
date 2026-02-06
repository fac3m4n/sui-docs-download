Sui System State Type Upgrade Guide
<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a> is a thin wrapper around SuiSystemStateInner that provides a versioned interface.
The <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a> object has a fixed ID 0x5, and the SuiSystemStateInner object is stored as a dynamic field.
There are a few different ways to upgrade the SuiSystemStateInner type:

The simplest and one that doesn't involve a real upgrade is to just add dynamic fields to the extra_fields field
of SuiSystemStateInner or any of its sub type. This is useful when we are in a rush, or making a small change,
or still experimenting a new field.

To properly upgrade the SuiSystemStateInner type, we need to ship a new framework that does the following:
1. Define a new SuiSystemStateInnertype (e.g. SuiSystemStateInnerV2).
2. Define a data migration function that migrates the old SuiSystemStateInner to the new one (i.e. SuiSystemStateInnerV2).
3. Replace all uses of SuiSystemStateInner with SuiSystemStateInnerV2 in both sui_system.move and sui_system_state_inner.move,
with the exception of the <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_create">sui_system_state_inner::create</a> function, which should always return the genesis type.
4. Inside <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_inner_maybe_upgrade">load_inner_maybe_upgrade</a> function, check the current version in the wrapper, and if it's not the latest version,
call the data migration function to upgrade the inner object. Make sure to also update the version in the wrapper.
A detailed example can be found in sui/tests/framework_upgrades/mock_sui_systems/shallow_upgrade.
Along with the Move change, we also need to update the Rust code to support the new type. This includes:
1. Define a new SuiSystemStateInner struct type that matches the new Move type, and implement the SuiSystemStateTrait.
2. Update the <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a> struct to include the new version as a new enum variant.
3. Update the get_sui_system_state function to handle the new version.
To test that the upgrade will be successful, we need to modify sui_system_state_production_upgrade_test test in
protocol_version_tests and trigger a real upgrade using the new framework. We will need to keep this directory as old version,
put the new framework in a new directory, and run the test to exercise the upgrade.

To upgrade Validator type, besides everything above, we also need to:
1. Define a new Validator type (e.g. ValidatorV2).
2. Define a data migration function that migrates the old Validator to the new one (i.e. ValidatorV2).
3. Replace all uses of Validator with ValidatorV2 except the genesis creation function.
4. In validator_wrapper::upgrade_to_latest, check the current version in the wrapper, and if it's not the latest version,
call the data migration function to upgrade it.
In Rust, we also need to add a new case in get_validator_from_table.
Note that it is possible to upgrade SuiSystemStateInner without upgrading Validator, but not the other way around.
And when we only upgrade SuiSystemStateInner, the version of Validator in the wrapper will not be updated, and hence may become
inconsistent with the version of SuiSystemStateInner. This is fine as long as we don't use the Validator version to determine
the SuiSystemStateInner version, or vice versa.

-  [Struct SuiSystemState](#sui_system_sui_system_SuiSystemState)
-  [Struct AccumulatorStorageCostKey](#sui_system_sui_system_AccumulatorStorageCostKey)
-  [Constants](#@Constants_0)
-  [Function create](#sui_system_sui_system_create)
-  [Function request_add_validator_candidate](#sui_system_sui_system_request_add_validator_candidate)
-  [Function request_remove_validator_candidate](#sui_system_sui_system_request_remove_validator_candidate)
-  [Function request_add_validator](#sui_system_sui_system_request_add_validator)
-  [Function request_remove_validator](#sui_system_sui_system_request_remove_validator)
-  [Function request_set_gas_price](#sui_system_sui_system_request_set_gas_price)
-  [Function set_candidate_validator_gas_price](#sui_system_sui_system_set_candidate_validator_gas_price)
-  [Function request_set_commission_rate](#sui_system_sui_system_request_set_commission_rate)
-  [Function set_candidate_validator_commission_rate](#sui_system_sui_system_set_candidate_validator_commission_rate)
-  [Function request_add_stake](#sui_system_sui_system_request_add_stake)
-  [Function request_add_stake_non_entry](#sui_system_sui_system_request_add_stake_non_entry)
-  [Function request_add_stake_mul_coin](#sui_system_sui_system_request_add_stake_mul_coin)
-  [Function request_withdraw_stake](#sui_system_sui_system_request_withdraw_stake)
-  [Function convert_to_fungible_staked_sui](#sui_system_sui_system_convert_to_fungible_staked_sui)
-  [Function redeem_fungible_staked_sui](#sui_system_sui_system_redeem_fungible_staked_sui)
-  [Function request_withdraw_stake_non_entry](#sui_system_sui_system_request_withdraw_stake_non_entry)
-  [Function report_validator](#sui_system_sui_system_report_validator)
-  [Function undo_report_validator](#sui_system_sui_system_undo_report_validator)
-  [Function rotate_operation_cap](#sui_system_sui_system_rotate_operation_cap)
-  [Function update_validator_name](#sui_system_sui_system_update_validator_name)
-  [Function update_validator_description](#sui_system_sui_system_update_validator_description)
-  [Function update_validator_image_url](#sui_system_sui_system_update_validator_image_url)
-  [Function update_validator_project_url](#sui_system_sui_system_update_validator_project_url)
-  [Function update_validator_next_epoch_network_address](#sui_system_sui_system_update_validator_next_epoch_network_address)
-  [Function update_candidate_validator_network_address](#sui_system_sui_system_update_candidate_validator_network_address)
-  [Function update_validator_next_epoch_p2p_address](#sui_system_sui_system_update_validator_next_epoch_p2p_address)
-  [Function update_candidate_validator_p2p_address](#sui_system_sui_system_update_candidate_validator_p2p_address)
-  [Function update_validator_next_epoch_primary_address](#sui_system_sui_system_update_validator_next_epoch_primary_address)
-  [Function update_candidate_validator_primary_address](#sui_system_sui_system_update_candidate_validator_primary_address)
-  [Function update_validator_next_epoch_worker_address](#sui_system_sui_system_update_validator_next_epoch_worker_address)
-  [Function update_candidate_validator_worker_address](#sui_system_sui_system_update_candidate_validator_worker_address)
-  [Function update_validator_next_epoch_protocol_pubkey](#sui_system_sui_system_update_validator_next_epoch_protocol_pubkey)
-  [Function update_candidate_validator_protocol_pubkey](#sui_system_sui_system_update_candidate_validator_protocol_pubkey)
-  [Function update_validator_next_epoch_worker_pubkey](#sui_system_sui_system_update_validator_next_epoch_worker_pubkey)
-  [Function update_candidate_validator_worker_pubkey](#sui_system_sui_system_update_candidate_validator_worker_pubkey)
-  [Function update_validator_next_epoch_network_pubkey](#sui_system_sui_system_update_validator_next_epoch_network_pubkey)
-  [Function update_candidate_validator_network_pubkey](#sui_system_sui_system_update_candidate_validator_network_pubkey)
-  [Function validator_address_by_pool_id](#sui_system_sui_system_validator_address_by_pool_id)
-  [Function pool_exchange_rates](#sui_system_sui_system_pool_exchange_rates)
-  [Function active_validator_addresses](#sui_system_sui_system_active_validator_addresses)
-  [Function active_validator_addresses_ref](#sui_system_sui_system_active_validator_addresses_ref)
-  [Function active_validator_voting_powers](#sui_system_sui_system_active_validator_voting_powers)
-  [Function calculate_rewards](#sui_system_sui_system_calculate_rewards)
-  [Function advance_epoch](#sui_system_sui_system_advance_epoch)
-  [Function load_system_state](#sui_system_sui_system_load_system_state)
-  [Function load_system_state_mut](#sui_system_sui_system_load_system_state_mut)
-  [Function load_system_state_ref](#sui_system_sui_system_load_system_state_ref)
-  [Function load_inner_maybe_upgrade](#sui_system_sui_system_load_inner_maybe_upgrade)
-  [Function validator_voting_powers](#sui_system_sui_system_validator_voting_powers)
-  [Function store_execution_time_estimates](#sui_system_sui_system_store_execution_time_estimates)
-  [Function store_execution_time_estimates_v2](#sui_system_sui_system_store_execution_time_estimates_v2)
-  [Function get_accumulator_storage_fund_amount](#sui_system_sui_system_get_accumulator_storage_fund_amount)
-  [Function write_accumulator_storage_cost](#sui_system_sui_system_write_accumulator_storage_cost)

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
<b>use</b> <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">sui_system::stake_subsidy</a>;
<b>use</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">sui_system::staking_pool</a>;
<b>use</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">sui_system::storage_fund</a>;
<b>use</b> <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner">sui_system::sui_system_state_inner</a>;
<b>use</b> <a href="../sui_sui_system/validator#sui_system_validator">sui_system::validator</a>;
<b>use</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap">sui_system::validator_cap</a>;
<b>use</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set">sui_system::validator_set</a>;
<b>use</b> <a href="../sui_sui_system/validator_wrapper#sui_system_validator_wrapper">sui_system::validator_wrapper</a>;
<b>use</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">sui_system::voting_power</a>;
</code>

Struct <code>SuiSystemState</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a> <b>has</b> key
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>version: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>AccumulatorStorageCostKey</code>

Key for storing the storage cost for accumulator objects, computed at end of epoch.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_AccumulatorStorageCostKey">AccumulatorStorageCostKey</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

<code><b>const</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_ENotSystemAddress">ENotSystemAddress</a>: u64 = 0;
</code>

<code><b>const</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_EWrongInnerVersion">EWrongInnerVersion</a>: u64 = 1;
</code>

Function <code>create</code>

Create a new SuiSystemState object and make it shared.
This function will be called only once in genesis.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_create">create</a>(id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, validators: vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">storage_fund</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, protocol_version: u64, epoch_start_timestamp_ms: u64, parameters: <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_SystemParameters">sui_system::sui_system_state_inner::SystemParameters</a>, <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">stake_subsidy</a>: <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy_StakeSubsidy">sui_system::stake_subsidy::StakeSubsidy</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_create">create</a>(
    id: UID,
    validators: vector&lt;Validator&gt;,
    <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">storage_fund</a>: Balance&lt;SUI&gt;,
    protocol_version: u64,
    epoch_start_timestamp_ms: u64,
    parameters: SystemParameters,
    <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">stake_subsidy</a>: StakeSubsidy,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> system_state = <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_create">sui_system_state_inner::create</a>(
        validators,
        <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">storage_fund</a>,
        protocol_version,
        epoch_start_timestamp_ms,
        parameters,
        <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">stake_subsidy</a>,
        ctx,
    );
    <b>let</b> version = <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_genesis_system_state_version">sui_system_state_inner::genesis_system_state_version</a>();
    <b>let</b> <b>mut</b> self = <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a> {
        id,
        version,
    };
    dynamic_field::add(&<b>mut</b> self.id, version, system_state);
    transfer::share_object(self);
}
</code></pre>

Function <code>request_add_validator_candidate</code>

Can be called by anyone who wishes to become a validator candidate and starts accruing delegated
stakes in their staking pool. Once they have at least MIN_VALIDATOR_JOINING_STAKE amount of stake they
can call <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator">request_add_validator</a> to officially become an active validator at the next epoch.
Aborts if the caller is already a pending or active validator, or a validator candidate.
Note: proof_of_possession MUST be a valid signature using sui_address and protocol_pubkey_bytes.
To produce a valid PoP, run [fn test_proof_of_possession].

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator_candidate">request_add_validator_candidate</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, pubkey_bytes: vector&lt;u8&gt;, network_pubkey_bytes: vector&lt;u8&gt;, worker_pubkey_bytes: vector&lt;u8&gt;, proof_of_possession: vector&lt;u8&gt;, name: vector&lt;u8&gt;, description: vector&lt;u8&gt;, image_url: vector&lt;u8&gt;, project_url: vector&lt;u8&gt;, net_address: vector&lt;u8&gt;, p2p_address: vector&lt;u8&gt;, primary_address: vector&lt;u8&gt;, worker_address: vector&lt;u8&gt;, gas_price: u64, commission_rate: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator_candidate">request_add_validator_candidate</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    pubkey_bytes: vector&lt;u8&gt;,
    network_pubkey_bytes: vector&lt;u8&gt;,
    worker_pubkey_bytes: vector&lt;u8&gt;,
    proof_of_possession: vector&lt;u8&gt;,
    name: vector&lt;u8&gt;,
    description: vector&lt;u8&gt;,
    image_url: vector&lt;u8&gt;,
    project_url: vector&lt;u8&gt;,
    net_address: vector&lt;u8&gt;,
    p2p_address: vector&lt;u8&gt;,
    primary_address: vector&lt;u8&gt;,
    worker_address: vector&lt;u8&gt;,
    gas_price: u64,
    commission_rate: u64,
    ctx: &<b>mut</b> TxContext,
) {
    wrapper
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator_candidate">request_add_validator_candidate</a>(
            pubkey_bytes,
            network_pubkey_bytes,
            worker_pubkey_bytes,
            proof_of_possession,
            name,
            description,
            image_url,
            project_url,
            net_address,
            p2p_address,
            primary_address,
            worker_address,
            gas_price,
            commission_rate,
            ctx,
        )
}
</code></pre>

Function <code>request_remove_validator_candidate</code>

Called by a validator candidate to remove themselves from the candidacy. After this call
their staking pool becomes deactivate.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator_candidate">request_remove_validator_candidate</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator_candidate">request_remove_validator_candidate</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    ctx: &<b>mut</b> TxContext,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator_candidate">request_remove_validator_candidate</a>(ctx)
}
</code></pre>

Function <code>request_add_validator</code>

Called by a validator candidate to add themselves to the active validator set beginning next epoch.
Aborts if the validator is a duplicate with one of the pending or active validators, or if the amount of
stake the validator has doesn't meet the min threshold, or if the number of new validators for the next
epoch has already reached the maximum.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator">request_add_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator">request_add_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>, ctx: &<b>mut</b> TxContext) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_validator">request_add_validator</a>(ctx)
}
</code></pre>

Function <code>request_remove_validator</code>

A validator can call this function to request a removal in the next epoch.
We use the sender of ctx to look up the validator
(i.e. sender must match the sui_address in the validator).
At the end of the epoch, the <a href="../sui_sui_system/validator#sui_system_validator">validator</a> object will be returned to the sui_address
of the validator.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator">request_remove_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator">request_remove_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>, ctx: &<b>mut</b> TxContext) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_remove_validator">request_remove_validator</a>(ctx)
}
</code></pre>

Function <code>request_set_gas_price</code>

A validator can call this entry function to submit a new gas price quote, to be
used for the reference gas price calculation at the end of the epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_gas_price">request_set_gas_price</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>, new_gas_price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_gas_price">request_set_gas_price</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    cap: &UnverifiedValidatorOperationCap,
    new_gas_price: u64,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_gas_price">request_set_gas_price</a>(cap, new_gas_price)
}
</code></pre>

Function <code>set_candidate_validator_gas_price</code>

This entry function is used to set new gas price for candidate validators

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_gas_price">set_candidate_validator_gas_price</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>, new_gas_price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_gas_price">set_candidate_validator_gas_price</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    cap: &UnverifiedValidatorOperationCap,
    new_gas_price: u64,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_gas_price">set_candidate_validator_gas_price</a>(cap, new_gas_price)
}
</code></pre>

Function <code>request_set_commission_rate</code>

A validator can call this entry function to set a new commission rate, updated at the end of
the epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_commission_rate">request_set_commission_rate</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, new_commission_rate: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_commission_rate">request_set_commission_rate</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    new_commission_rate: u64,
    ctx: &<b>mut</b> TxContext,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_set_commission_rate">request_set_commission_rate</a>(new_commission_rate, ctx)
}
</code></pre>

Function <code>set_candidate_validator_commission_rate</code>

This entry function is used to set new commission rate for candidate validators

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_commission_rate">set_candidate_validator_commission_rate</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, new_commission_rate: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_commission_rate">set_candidate_validator_commission_rate</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    new_commission_rate: u64,
    ctx: &<b>mut</b> TxContext,
) {
    wrapper
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_set_candidate_validator_commission_rate">set_candidate_validator_commission_rate</a>(new_commission_rate, ctx)
}
</code></pre>

Function <code>request_add_stake</code>

Add stake to a validator's staking pool.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake">request_add_stake</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, stake: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, validator_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake">request_add_stake</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    stake: Coin&lt;SUI&gt;,
    validator_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> staked_sui = <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_non_entry">request_add_stake_non_entry</a>(wrapper, stake, validator_address, ctx);
    transfer::public_transfer(staked_sui, ctx.sender());
}
</code></pre>

Function <code>request_add_stake_non_entry</code>

The non-entry version of <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake">request_add_stake</a>, which returns the staked SUI instead of transferring it to the sender.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_non_entry">request_add_stake_non_entry</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, stake: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, validator_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_non_entry">request_add_stake_non_entry</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    stake: Coin&lt;SUI&gt;,
    validator_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
): StakedSui {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake">request_add_stake</a>(stake, validator_address, ctx)
}
</code></pre>

Function <code>request_add_stake_mul_coin</code>

Add stake to a validator's staking pool using multiple coins.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_mul_coin">request_add_stake_mul_coin</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, stakes: vector&lt;<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;&gt;, stake_amount: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;, validator_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_mul_coin">request_add_stake_mul_coin</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    stakes: vector&lt;Coin&lt;SUI&gt;&gt;,
    stake_amount: option::Option&lt;u64&gt;,
    validator_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> staked_sui = wrapper
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_add_stake_mul_coin">request_add_stake_mul_coin</a>(stakes, stake_amount, validator_address, ctx);
    transfer::public_transfer(staked_sui, ctx.sender());
}
</code></pre>

Function <code>request_withdraw_stake</code>

Withdraw stake from a validator's staking pool.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake">request_withdraw_stake</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake">request_withdraw_stake</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    staked_sui: StakedSui,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> withdrawn_stake = wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake_non_entry">request_withdraw_stake_non_entry</a>(staked_sui, ctx);
    transfer::public_transfer(withdrawn_stake.into_coin(ctx), ctx.sender());
}
</code></pre>

Function <code>convert_to_fungible_staked_sui</code>

Convert StakedSui into a FungibleStakedSui object.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    staked_sui: StakedSui,
    ctx: &<b>mut</b> TxContext,
): FungibleStakedSui {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(staked_sui, ctx)
}
</code></pre>

Function <code>redeem_fungible_staked_sui</code>

Convert FungibleStakedSui into a StakedSui object.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, fungible_staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    fungible_staked_sui: FungibleStakedSui,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(fungible_staked_sui, ctx)
}
</code></pre>

Function <code>request_withdraw_stake_non_entry</code>

Non-entry version of <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake">request_withdraw_stake</a> that returns the withdrawn SUI instead of transferring it to the sender.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake_non_entry">request_withdraw_stake_non_entry</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake_non_entry">request_withdraw_stake_non_entry</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    staked_sui: StakedSui,
    ctx: &<b>mut</b> TxContext,
): Balance&lt;SUI&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_request_withdraw_stake">request_withdraw_stake</a>(staked_sui, ctx)
}
</code></pre>

Function <code>report_validator</code>

Report a validator as a bad or non-performant actor in the system.
Succeeds if all the following are satisfied:
1. both the reporter in cap and the input reportee_addr are active validators.
2. reporter and reportee not the same address.
3. the cap object is still valid.
This function is idempotent.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_report_validator">report_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>, reportee_addr: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_report_validator">report_validator</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    cap: &UnverifiedValidatorOperationCap,
    reportee_addr: <b>address</b>,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_report_validator">report_validator</a>(cap, reportee_addr)
}
</code></pre>

Function <code>undo_report_validator</code>

Undo a <a href="../sui_sui_system/sui_system#sui_system_sui_system_report_validator">report_validator</a> action. Aborts if
1. the reportee is not a currently active validator or
2. the sender has not previously reported the reportee_addr, or
3. the cap is not valid

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_undo_report_validator">undo_report_validator</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, cap: &<a href="../sui_sui_system/validator_cap#sui_system_validator_cap_UnverifiedValidatorOperationCap">sui_system::validator_cap::UnverifiedValidatorOperationCap</a>, reportee_addr: <b>address</b>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_undo_report_validator">undo_report_validator</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    cap: &UnverifiedValidatorOperationCap,
    reportee_addr: <b>address</b>,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_undo_report_validator">undo_report_validator</a>(cap, reportee_addr)
}
</code></pre>

Function <code>rotate_operation_cap</code>

Create a new UnverifiedValidatorOperationCap, transfer it to the
validator and registers it. The original object is thus revoked.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_rotate_operation_cap">rotate_operation_cap</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_rotate_operation_cap">rotate_operation_cap</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>, ctx: &<b>mut</b> TxContext) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_rotate_operation_cap">rotate_operation_cap</a>(ctx)
}
</code></pre>

Function <code>update_validator_name</code>

Update a validator's name.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_name">update_validator_name</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, name: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_name">update_validator_name</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    name: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_name">update_validator_name</a>(name, ctx)
}
</code></pre>

Function <code>update_validator_description</code>

Update a validator's description

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_description">update_validator_description</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, description: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_description">update_validator_description</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    description: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_description">update_validator_description</a>(description, ctx)
}
</code></pre>

Function <code>update_validator_image_url</code>

Update a validator's image url

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_image_url">update_validator_image_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, image_url: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_image_url">update_validator_image_url</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    image_url: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_image_url">update_validator_image_url</a>(image_url, ctx)
}
</code></pre>

Function <code>update_validator_project_url</code>

Update a validator's project url

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_project_url">update_validator_project_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, project_url: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_project_url">update_validator_project_url</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    project_url: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_project_url">update_validator_project_url</a>(project_url, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_network_address</code>

Update a validator's network address.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_address">update_validator_next_epoch_network_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, network_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_address">update_validator_next_epoch_network_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    network_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_address">update_validator_next_epoch_network_address</a>(network_address, ctx)
}
</code></pre>

Function <code>update_candidate_validator_network_address</code>

Update candidate validator's network address.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_address">update_candidate_validator_network_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, network_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_address">update_candidate_validator_network_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    network_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_address">update_candidate_validator_network_address</a>(network_address, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_p2p_address</code>

Update a validator's p2p address.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_p2p_address">update_validator_next_epoch_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, p2p_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_p2p_address">update_validator_next_epoch_p2p_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    p2p_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_p2p_address">update_validator_next_epoch_p2p_address</a>(p2p_address, ctx)
}
</code></pre>

Function <code>update_candidate_validator_p2p_address</code>

Update candidate validator's p2p address.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_p2p_address">update_candidate_validator_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, p2p_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_p2p_address">update_candidate_validator_p2p_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    p2p_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_p2p_address">update_candidate_validator_p2p_address</a>(p2p_address, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_primary_address</code>

Update a validator's narwhal primary address.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_primary_address">update_validator_next_epoch_primary_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, primary_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_primary_address">update_validator_next_epoch_primary_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    primary_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_primary_address">update_validator_next_epoch_primary_address</a>(primary_address, ctx)
}
</code></pre>

Function <code>update_candidate_validator_primary_address</code>

Update candidate validator's narwhal primary address.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_primary_address">update_candidate_validator_primary_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, primary_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_primary_address">update_candidate_validator_primary_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    primary_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_primary_address">update_candidate_validator_primary_address</a>(primary_address, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_worker_address</code>

Update a validator's narwhal worker address.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_address">update_validator_next_epoch_worker_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, worker_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_address">update_validator_next_epoch_worker_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    worker_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_address">update_validator_next_epoch_worker_address</a>(worker_address, ctx)
}
</code></pre>

Function <code>update_candidate_validator_worker_address</code>

Update candidate validator's narwhal worker address.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_address">update_candidate_validator_worker_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, worker_address: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_address">update_candidate_validator_worker_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    worker_address: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_address">update_candidate_validator_worker_address</a>(worker_address, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_protocol_pubkey</code>

Update a validator's public key of protocol key and proof of possession.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_protocol_pubkey">update_validator_next_epoch_protocol_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, protocol_pubkey: vector&lt;u8&gt;, proof_of_possession: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_protocol_pubkey">update_validator_next_epoch_protocol_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    protocol_pubkey: vector&lt;u8&gt;,
    proof_of_possession: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_protocol_pubkey">update_validator_next_epoch_protocol_pubkey</a>(protocol_pubkey, proof_of_possession, ctx)
}
</code></pre>

Function <code>update_candidate_validator_protocol_pubkey</code>

Update candidate validator's public key of protocol key and proof of possession.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_protocol_pubkey">update_candidate_validator_protocol_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, protocol_pubkey: vector&lt;u8&gt;, proof_of_possession: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_protocol_pubkey">update_candidate_validator_protocol_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    protocol_pubkey: vector&lt;u8&gt;,
    proof_of_possession: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_protocol_pubkey">update_candidate_validator_protocol_pubkey</a>(protocol_pubkey, proof_of_possession, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_worker_pubkey</code>

Update a validator's public key of worker key.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_pubkey">update_validator_next_epoch_worker_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, worker_pubkey: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_pubkey">update_validator_next_epoch_worker_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    worker_pubkey: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_worker_pubkey">update_validator_next_epoch_worker_pubkey</a>(worker_pubkey, ctx)
}
</code></pre>

Function <code>update_candidate_validator_worker_pubkey</code>

Update candidate validator's public key of worker key.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_pubkey">update_candidate_validator_worker_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, worker_pubkey: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_pubkey">update_candidate_validator_worker_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    worker_pubkey: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_worker_pubkey">update_candidate_validator_worker_pubkey</a>(worker_pubkey, ctx)
}
</code></pre>

Function <code>update_validator_next_epoch_network_pubkey</code>

Update a validator's public key of network key.
The change will only take effects starting from the next epoch.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_pubkey">update_validator_next_epoch_network_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, network_pubkey: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_pubkey">update_validator_next_epoch_network_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    network_pubkey: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_validator_next_epoch_network_pubkey">update_validator_next_epoch_network_pubkey</a>(network_pubkey, ctx)
}
</code></pre>

Function <code>update_candidate_validator_network_pubkey</code>

Update candidate validator's public key of network key.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_pubkey">update_candidate_validator_network_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, network_pubkey: vector&lt;u8&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_pubkey">update_candidate_validator_network_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    network_pubkey: vector&lt;u8&gt;,
    ctx: &TxContext,
) {
    self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_update_candidate_validator_network_pubkey">update_candidate_validator_network_pubkey</a>(network_pubkey, ctx)
}
</code></pre>

Function <code>validator_address_by_pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_validator_address_by_pool_id">validator_address_by_pool_id</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, pool_id: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_validator_address_by_pool_id">validator_address_by_pool_id</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>, pool_id: &ID): <b>address</b> {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_validator_address_by_pool_id">validator_address_by_pool_id</a>(pool_id)
}
</code></pre>

Function <code>pool_exchange_rates</code>

Getter of the pool token exchange rate of a staking pool. Works for both active and inactive pools.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_pool_exchange_rates">pool_exchange_rates</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, pool_id: &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): &<a href="../sui_sui/table#sui_table_Table">sui::table::Table</a>&lt;u64, <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_pool_exchange_rates">pool_exchange_rates</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    pool_id: &ID,
): &Table&lt;u64, PoolTokenExchangeRate&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_pool_exchange_rates">pool_exchange_rates</a>(pool_id)
}
</code></pre>

Function <code>active_validator_addresses</code>

Getter returning addresses of the currently active validators.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses">active_validator_addresses</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses">active_validator_addresses</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): vector&lt;<b>address</b>&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses">active_validator_addresses</a>()
}
</code></pre>

Function <code>active_validator_addresses_ref</code>

Getter returning addresses of the currently active validators by reference.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses_ref">active_validator_addresses_ref</a>(wrapper: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): vector&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses_ref">active_validator_addresses_ref</a>(wrapper: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): vector&lt;<b>address</b>&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_ref">load_system_state_ref</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_addresses">active_validator_addresses</a>()
}
</code></pre>

Function <code>active_validator_voting_powers</code>

Getter returns the voting power of the active validators, values are voting power in the scale of 10000.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_voting_powers">active_validator_voting_powers</a>(wrapper: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_voting_powers">active_validator_voting_powers</a>(wrapper: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): VecMap&lt;<b>address</b>, u64&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_ref">load_system_state_ref</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_voting_powers">active_validator_voting_powers</a>()
}
</code></pre>

Function <code>calculate_rewards</code>

Calculate the rewards for a given staked SUI object.
Used in the package, and can be dev-inspected.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_calculate_rewards">calculate_rewards</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, staked_sui: &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_calculate_rewards">calculate_rewards</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    staked_sui: &StakedSui,
    ctx: &TxContext,
): u64 {
    <b>let</b> system_state = self.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>();
    system_state
        .validators_mut()
        .validator_by_pool_id(&staked_sui.pool_id())
        .get_staking_pool_ref()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_calculate_rewards">calculate_rewards</a>(staked_sui, ctx.epoch())
}
</code></pre>

Function <code>advance_epoch</code>

This function should be called at the end of an epoch, and advances the system to the next epoch.
It does the following things:
1. Add storage charge to the storage fund.
2. Burn the storage rebates from the storage fund. These are already refunded to transaction sender's
gas coins.
3. Distribute computation charge to validator stake.
4. Update all validators.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_advance_epoch">advance_epoch</a>(storage_reward: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, computation_reward: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, new_epoch: u64, next_protocol_version: u64, storage_rebate: u64, non_refundable_storage_fee: u64, storage_fund_reinvest_rate: u64, reward_slashing_rate: u64, epoch_start_timestamp_ms: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_advance_epoch">advance_epoch</a>(
    storage_reward: Balance&lt;SUI&gt;,
    computation_reward: Balance&lt;SUI&gt;,
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    new_epoch: u64,
    next_protocol_version: u64,
    storage_rebate: u64,
    non_refundable_storage_fee: u64,
    storage_fund_reinvest_rate: u64, // share of storage fund's rewards that's reinvested
    // into storage fund, in basis point.
    reward_slashing_rate: u64, // how much rewards are slashed to punish a <a href="../sui_sui_system/validator#sui_system_validator">validator</a>, in bps.
    epoch_start_timestamp_ms: u64, // Timestamp of the epoch start
    ctx: &<b>mut</b> TxContext,
): Balance&lt;SUI&gt; {
    // Validator will make a special system call with sender set <b>as</b> 0x0.
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui_system/sui_system#sui_system_sui_system_ENotSystemAddress">ENotSystemAddress</a>);
    <b>let</b> accumulator_storage_fund_amount = <a href="../sui_sui_system/sui_system#sui_system_sui_system_get_accumulator_storage_fund_amount">get_accumulator_storage_fund_amount</a>(wrapper);
    <b>let</b> storage_rebate = wrapper
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>()
        .<a href="../sui_sui_system/sui_system#sui_system_sui_system_advance_epoch">advance_epoch</a>(
            new_epoch,
            next_protocol_version,
            storage_reward,
            computation_reward,
            storage_rebate,
            non_refundable_storage_fee,
            storage_fund_reinvest_rate,
            reward_slashing_rate,
            epoch_start_timestamp_ms,
            accumulator_storage_fund_amount,
            ctx,
        );
    storage_rebate
}
</code></pre>

Function <code>load_system_state</code>

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state">load_system_state</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): &<a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_SuiSystemStateInnerV2">sui_system::sui_system_state_inner::SuiSystemStateInnerV2</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state">load_system_state</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): &SuiSystemStateInnerV2 {
    <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_inner_maybe_upgrade">load_inner_maybe_upgrade</a>(self)
}
</code></pre>

Function <code>load_system_state_mut</code>

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): &<b>mut</b> <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_SuiSystemStateInnerV2">sui_system::sui_system_state_inner::SuiSystemStateInnerV2</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): &<b>mut</b> SuiSystemStateInnerV2 {
    <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_inner_maybe_upgrade">load_inner_maybe_upgrade</a>(self)
}
</code></pre>

Function <code>load_system_state_ref</code>

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_ref">load_system_state_ref</a>(self: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): &<a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_SuiSystemStateInnerV2">sui_system::sui_system_state_inner::SuiSystemStateInnerV2</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_ref">load_system_state_ref</a>(self: &<a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): &SuiSystemStateInnerV2 {
    <b>let</b> inner: &SuiSystemStateInnerV2 = dynamic_field::borrow(
        &self.id,
        self.version,
    );
    <b>assert</b>!(inner.system_state_version() == self.version, <a href="../sui_sui_system/sui_system#sui_system_sui_system_EWrongInnerVersion">EWrongInnerVersion</a>);
    inner
}
</code></pre>

Function <code>load_inner_maybe_upgrade</code>

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_inner_maybe_upgrade">load_inner_maybe_upgrade</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): &<b>mut</b> <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_SuiSystemStateInnerV2">sui_system::sui_system_state_inner::SuiSystemStateInnerV2</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_load_inner_maybe_upgrade">load_inner_maybe_upgrade</a>(self: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): &<b>mut</b> SuiSystemStateInnerV2 {
    <b>if</b> (self.version == 1) {
        <b>let</b> v1: SuiSystemStateInner = dynamic_field::remove(&<b>mut</b> self.id, self.version);
        <b>let</b> v2 = v1.v1_to_v2();
        self.version = 2;
        dynamic_field::add(&<b>mut</b> self.id, self.version, v2);
    };
    <b>let</b> inner: &<b>mut</b> SuiSystemStateInnerV2 = dynamic_field::borrow_mut(
        &<b>mut</b> self.id,
        self.version,
    );
    <b>assert</b>!(inner.system_state_version() == self.version, <a href="../sui_sui_system/sui_system#sui_system_sui_system_EWrongInnerVersion">EWrongInnerVersion</a>);
    inner
}
</code></pre>

Function <code>validator_voting_powers</code>

Returns the voting power of the active validators, values are voting power in the scale of 10000.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_validator_voting_powers">validator_voting_powers</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<b>address</b>, u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_validator_voting_powers">validator_voting_powers</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): VecMap&lt;<b>address</b>, u64&gt; {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state">load_system_state</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_active_validator_voting_powers">active_validator_voting_powers</a>()
}
</code></pre>

Function <code>store_execution_time_estimates</code>

Saves the given execution time estimate blob to the SuiSystemState object, for system use
at the start of the next epoch.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates">store_execution_time_estimates</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, estimates_bytes: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates">store_execution_time_estimates</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>, estimates_bytes: vector&lt;u8&gt;) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates">store_execution_time_estimates</a>(estimates_bytes)
}
</code></pre>

Function <code>store_execution_time_estimates_v2</code>

Saves the given execution time estimate chunks to the SuiSystemState object, for system use
at the start of the next epoch.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates_v2">store_execution_time_estimates_v2</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, estimate_chunks: vector&lt;vector&lt;u8&gt;&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates_v2">store_execution_time_estimates_v2</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    estimate_chunks: vector&lt;vector&lt;u8&gt;&gt;,
) {
    wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().<a href="../sui_sui_system/sui_system#sui_system_sui_system_store_execution_time_estimates_v2">store_execution_time_estimates_v2</a>(estimate_chunks)
}
</code></pre>

Function <code>get_accumulator_storage_fund_amount</code>

Returns the storage fund amount for accumulator objects stored in extra_fields.
Returns 0 if no value has been stored.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_get_accumulator_storage_fund_amount">get_accumulator_storage_fund_amount</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_get_accumulator_storage_fund_amount">get_accumulator_storage_fund_amount</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>): u64 {
    <b>let</b> extra_fields = wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state">load_system_state</a>().extra_fields();
    <b>let</b> key = <a href="../sui_sui_system/sui_system#sui_system_sui_system_AccumulatorStorageCostKey">AccumulatorStorageCostKey</a>();
    <b>if</b> (extra_fields.contains(key)) {
        *extra_fields.borrow(key)
    } <b>else</b> {
        0
    }
}
</code></pre>

Function <code>write_accumulator_storage_cost</code>

Stores the computed storage cost for accumulator objects.
This is called by an end-of-epoch transaction to record the storage cost
that will be used by advance_epoch.

<code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_write_accumulator_storage_cost">write_accumulator_storage_cost</a>(wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">sui_system::sui_system::SuiSystemState</a>, storage_cost: u64, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_write_accumulator_storage_cost">write_accumulator_storage_cost</a>(
    wrapper: &<b>mut</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system_SuiSystemState">SuiSystemState</a>,
    storage_cost: u64,
    ctx: &TxContext,
) {
    <b>assert</b>!(ctx.sender() == @0x0, <a href="../sui_sui_system/sui_system#sui_system_sui_system_ENotSystemAddress">ENotSystemAddress</a>);
    <b>let</b> extra_fields = wrapper.<a href="../sui_sui_system/sui_system#sui_system_sui_system_load_system_state_mut">load_system_state_mut</a>().extra_fields_mut();
    <b>let</b> key = <a href="../sui_sui_system/sui_system#sui_system_sui_system_AccumulatorStorageCostKey">AccumulatorStorageCostKey</a>();
    <b>if</b> (extra_fields.contains(key)) {
        <b>let</b> existing: &<b>mut</b> u64 = extra_fields.borrow_mut(key);
        *existing = storage_cost;
    } <b>else</b> {
        extra_fields.add(key, storage_cost);
    };
}
</code></pre>