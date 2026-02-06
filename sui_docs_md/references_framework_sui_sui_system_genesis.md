-  [Struct GenesisValidatorMetadata](#sui_system_genesis_GenesisValidatorMetadata)
-  [Struct GenesisChainParameters](#sui_system_genesis_GenesisChainParameters)
-  [Struct TokenDistributionSchedule](#sui_system_genesis_TokenDistributionSchedule)
-  [Struct TokenAllocation](#sui_system_genesis_TokenAllocation)
-  [Constants](#@Constants_0)
-  [Function create](#sui_system_genesis_create)
-  [Function allocate_tokens](#sui_system_genesis_allocate_tokens)

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
<b>use</b> <a href="../sui_sui_system/sui_system#sui_system_sui_system">sui_system::sui_system</a>;
<b>use</b> <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner">sui_system::sui_system_state_inner</a>;
<b>use</b> <a href="../sui_sui_system/validator#sui_system_validator">sui_system::validator</a>;
<b>use</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap">sui_system::validator_cap</a>;
<b>use</b> <a href="../sui_sui_system/validator_set#sui_system_validator_set">sui_system::validator_set</a>;
<b>use</b> <a href="../sui_sui_system/validator_wrapper#sui_system_validator_wrapper">sui_system::validator_wrapper</a>;
<b>use</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">sui_system::voting_power</a>;
</code>

Struct <code>GenesisValidatorMetadata</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/genesis#sui_system_genesis_GenesisValidatorMetadata">GenesisValidatorMetadata</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>name: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>description: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>image_url: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>project_url: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>sui_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>gas_price: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>commission_rate: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>protocol_public_key: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>proof_of_possession: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>network_public_key: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>worker_public_key: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>network_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>p2p_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>primary_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>worker_address: vector&lt;u8&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>GenesisChainParameters</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/genesis#sui_system_genesis_GenesisChainParameters">GenesisChainParameters</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>protocol_version: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>chain_start_timestamp_ms: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>epoch_duration_ms: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake_subsidy_start_epoch: u64</code>
</dt>
<dd>
 Stake Subsidy parameters
</dd>
<dt>
<code>stake_subsidy_initial_distribution_amount: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake_subsidy_period_length: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>stake_subsidy_decrease_rate: u16</code>
</dt>
<dd>
</dd>
<dt>
<code>max_validator_count: u64</code>
</dt>
<dd>
 Validator committee parameters
</dd>
<dt>
<code>min_validator_joining_stake: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_low_stake_threshold: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_very_low_stake_threshold: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>validator_low_stake_grace_period: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenDistributionSchedule</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/genesis#sui_system_genesis_TokenDistributionSchedule">TokenDistributionSchedule</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>stake_subsidy_fund_mist: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>allocations: vector&lt;<a href="../sui_sui_system/genesis#sui_system_genesis_TokenAllocation">sui_system::genesis::TokenAllocation</a>&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenAllocation</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/genesis#sui_system_genesis_TokenAllocation">TokenAllocation</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>recipient_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>amount_mist: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>staked_with_validator: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;</code>
</dt>
<dd>
 Indicates if this allocation should be staked at genesis and with which validator
</dd>
</dl>

Constants

The <a href="../sui_sui_system/genesis#sui_system_genesis_create">create</a> function was called at a non-genesis epoch.

<code><b>const</b> <a href="../sui_sui_system/genesis#sui_system_genesis_ENotCalledAtGenesis">ENotCalledAtGenesis</a>: u64 = 0;
</code>

The <a href="../sui_sui_system/genesis#sui_system_genesis_create">create</a> function was called with duplicate validators.

<code><b>const</b> <a href="../sui_sui_system/genesis#sui_system_genesis_EDuplicateValidator">EDuplicateValidator</a>: u64 = 1;
</code>

Function <code>create</code>

This function will be explicitly called once at genesis.
It will create a singleton SuiSystemState object, which contains
all the information we need in the system.

<code><b>fun</b> <a href="../sui_sui_system/genesis#sui_system_genesis_create">create</a>(sui_system_state_id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>, sui_supply: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, genesis_chain_parameters: <a href="../sui_sui_system/genesis#sui_system_genesis_GenesisChainParameters">sui_system::genesis::GenesisChainParameters</a>, genesis_validators: vector&lt;<a href="../sui_sui_system/genesis#sui_system_genesis_GenesisValidatorMetadata">sui_system::genesis::GenesisValidatorMetadata</a>&gt;, token_distribution_schedule: <a href="../sui_sui_system/genesis#sui_system_genesis_TokenDistributionSchedule">sui_system::genesis::TokenDistributionSchedule</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/genesis#sui_system_genesis_create">create</a>(
    sui_system_state_id: UID,
    <b>mut</b> sui_supply: Balance&lt;SUI&gt;,
    genesis_chain_parameters: <a href="../sui_sui_system/genesis#sui_system_genesis_GenesisChainParameters">GenesisChainParameters</a>,
    genesis_validators: vector&lt;<a href="../sui_sui_system/genesis#sui_system_genesis_GenesisValidatorMetadata">GenesisValidatorMetadata</a>&gt;,
    token_distribution_schedule: <a href="../sui_sui_system/genesis#sui_system_genesis_TokenDistributionSchedule">TokenDistributionSchedule</a>,
    ctx: &<b>mut</b> TxContext,
) {
    // Ensure this is only called at <a href="../sui_sui_system/genesis#sui_system_genesis">genesis</a>
    <b>assert</b>!(ctx.epoch() == 0, <a href="../sui_sui_system/genesis#sui_system_genesis_ENotCalledAtGenesis">ENotCalledAtGenesis</a>);
    // Create all the <span className="code-inline">Validator</span> structs
    <b>let</b> <b>mut</b> validators = vector[];
    genesis_validators.do!(|genesis_validator| {
        <b>let</b> <a href="../sui_sui_system/genesis#sui_system_genesis_GenesisValidatorMetadata">GenesisValidatorMetadata</a> {
            name,
            description,
            image_url,
            project_url,
            sui_address,
            gas_price,
            commission_rate,
            protocol_public_key,
            proof_of_possession,
            network_public_key,
            worker_public_key,
            network_address,
            p2p_address,
            primary_address,
            worker_address,
        } = genesis_validator;
        <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator#sui_system_validator_new">validator::new</a>(
            sui_address,
            protocol_public_key,
            network_public_key,
            worker_public_key,
            proof_of_possession,
            name,
            description,
            image_url,
            project_url,
            network_address,
            p2p_address,
            primary_address,
            worker_address,
            gas_price,
            commission_rate,
            ctx,
        );
        // Ensure that each <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is unique
        <b>assert</b>!(
            !<a href="../sui_sui_system/validator_set#sui_system_validator_set_is_duplicate_validator">validator_set::is_duplicate_validator</a>(&validators, &<a href="../sui_sui_system/validator#sui_system_validator">validator</a>),
            <a href="../sui_sui_system/genesis#sui_system_genesis_EDuplicateValidator">EDuplicateValidator</a>,
        );
        validators.push_back(<a href="../sui_sui_system/validator#sui_system_validator">validator</a>);
    });
    <b>let</b> <a href="../sui_sui_system/genesis#sui_system_genesis_TokenDistributionSchedule">TokenDistributionSchedule</a> {
        stake_subsidy_fund_mist,
        allocations,
    } = token_distribution_schedule;
    <b>let</b> subsidy_fund = sui_supply.split(stake_subsidy_fund_mist);
    <b>let</b> <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">storage_fund</a> = balance::zero();
    // Allocate tokens and staking operations
    <a href="../sui_sui_system/genesis#sui_system_genesis_allocate_tokens">allocate_tokens</a>(sui_supply, allocations, &<b>mut</b> validators, ctx);
    // Activate all validators
    validators.do_mut!(|<a href="../sui_sui_system/validator#sui_system_validator">validator</a>| <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.activate(0));
    <b>let</b> system_parameters = <a href="../sui_sui_system/sui_system_state_inner#sui_system_sui_system_state_inner_create_system_parameters">sui_system_state_inner::create_system_parameters</a>(
        genesis_chain_parameters.epoch_duration_ms,
        genesis_chain_parameters.stake_subsidy_start_epoch,
        // Validator committee parameters
        genesis_chain_parameters.max_validator_count,
        genesis_chain_parameters.min_validator_joining_stake,
        genesis_chain_parameters.validator_low_stake_threshold,
        genesis_chain_parameters.validator_very_low_stake_threshold,
        genesis_chain_parameters.validator_low_stake_grace_period,
        ctx,
    );
    <b>let</b> <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">stake_subsidy</a> = <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy_create">stake_subsidy::create</a>(
        subsidy_fund,
        genesis_chain_parameters.stake_subsidy_initial_distribution_amount,
        genesis_chain_parameters.stake_subsidy_period_length,
        genesis_chain_parameters.stake_subsidy_decrease_rate,
        ctx,
    );
    sui_system::create(
        sui_system_state_id,
        validators,
        <a href="../sui_sui_system/storage_fund#sui_system_storage_fund">storage_fund</a>,
        genesis_chain_parameters.protocol_version,
        genesis_chain_parameters.chain_start_timestamp_ms,
        system_parameters,
        <a href="../sui_sui_system/stake_subsidy#sui_system_stake_subsidy">stake_subsidy</a>,
        ctx,
    );
}
</code></pre>

Function <code>allocate_tokens</code>

<code><b>fun</b> <a href="../sui_sui_system/genesis#sui_system_genesis_allocate_tokens">allocate_tokens</a>(sui_supply: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, allocations: vector&lt;<a href="../sui_sui_system/genesis#sui_system_genesis_TokenAllocation">sui_system::genesis::TokenAllocation</a>&gt;, validators: &<b>mut</b> vector&lt;<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/genesis#sui_system_genesis_allocate_tokens">allocate_tokens</a>(
    <b>mut</b> sui_supply: Balance&lt;SUI&gt;,
    allocations: vector&lt;<a href="../sui_sui_system/genesis#sui_system_genesis_TokenAllocation">TokenAllocation</a>&gt;,
    validators: &<b>mut</b> vector&lt;Validator&gt;,
    ctx: &<b>mut</b> TxContext,
) {
    allocations.destroy!(
        |<a href="../sui_sui_system/genesis#sui_system_genesis_TokenAllocation">TokenAllocation</a> { recipient_address, amount_mist, staked_with_validator }| {
            <b>let</b> allocation_balance = sui_supply.split(amount_mist);
            <b>if</b> (staked_with_validator.is_some()) {
                <b>let</b> validator_address = staked_with_validator.destroy_some();
                <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator">validator</a> = <a href="../sui_sui_system/validator_set#sui_system_validator_set_get_validator_mut">validator_set::get_validator_mut</a>(validators, validator_address);
                <a href="../sui_sui_system/validator#sui_system_validator">validator</a>.request_add_stake_at_genesis(
                    allocation_balance,
                    recipient_address,
                    ctx,
                );
            } <b>else</b> {
                transfer::public_transfer(allocation_balance.into_coin(ctx), recipient_address);
            };
        },
    );
    // should be none left at this point.
    // Provided allocations must fully allocate the sui_supply and there
    sui_supply.destroy_zero();
}
</code></pre>