-  [Struct ValidatorMetadata](#sui_system_validator_ValidatorMetadata)
-  [Struct Validator](#sui_system_validator_Validator)
-  [Struct StakingRequestEvent](#sui_system_validator_StakingRequestEvent)
-  [Struct UnstakingRequestEvent](#sui_system_validator_UnstakingRequestEvent)
-  [Struct ConvertingToFungibleStakedSuiEvent](#sui_system_validator_ConvertingToFungibleStakedSuiEvent)
-  [Struct RedeemingFungibleStakedSuiEvent](#sui_system_validator_RedeemingFungibleStakedSuiEvent)
-  [Constants](#@Constants_0)
-  [Function new_metadata](#sui_system_validator_new_metadata)
-  [Function new](#sui_system_validator_new)
-  [Function deactivate](#sui_system_validator_deactivate)
-  [Function activate](#sui_system_validator_activate)
-  [Function adjust_stake_and_gas_price](#sui_system_validator_adjust_stake_and_gas_price)
-  [Function request_add_stake](#sui_system_validator_request_add_stake)
-  [Function convert_to_fungible_staked_sui](#sui_system_validator_convert_to_fungible_staked_sui)
-  [Function redeem_fungible_staked_sui](#sui_system_validator_redeem_fungible_staked_sui)
-  [Function request_add_stake_at_genesis](#sui_system_validator_request_add_stake_at_genesis)
-  [Function request_withdraw_stake](#sui_system_validator_request_withdraw_stake)
-  [Function request_set_gas_price](#sui_system_validator_request_set_gas_price)
-  [Function set_candidate_gas_price](#sui_system_validator_set_candidate_gas_price)
-  [Function request_set_commission_rate](#sui_system_validator_request_set_commission_rate)
-  [Function set_candidate_commission_rate](#sui_system_validator_set_candidate_commission_rate)
-  [Function deposit_stake_rewards](#sui_system_validator_deposit_stake_rewards)
-  [Function process_pending_stakes_and_withdraws](#sui_system_validator_process_pending_stakes_and_withdraws)
-  [Function is_preactive](#sui_system_validator_is_preactive)
-  [Function metadata](#sui_system_validator_metadata)
-  [Function sui_address](#sui_system_validator_sui_address)
-  [Function name](#sui_system_validator_name)
-  [Function description](#sui_system_validator_description)
-  [Function image_url](#sui_system_validator_image_url)
-  [Function project_url](#sui_system_validator_project_url)
-  [Function network_address](#sui_system_validator_network_address)
-  [Function p2p_address](#sui_system_validator_p2p_address)
-  [Function primary_address](#sui_system_validator_primary_address)
-  [Function worker_address](#sui_system_validator_worker_address)
-  [Function protocol_pubkey_bytes](#sui_system_validator_protocol_pubkey_bytes)
-  [Function proof_of_possession](#sui_system_validator_proof_of_possession)
-  [Function network_pubkey_bytes](#sui_system_validator_network_pubkey_bytes)
-  [Function worker_pubkey_bytes](#sui_system_validator_worker_pubkey_bytes)
-  [Function next_epoch_network_address](#sui_system_validator_next_epoch_network_address)
-  [Function next_epoch_p2p_address](#sui_system_validator_next_epoch_p2p_address)
-  [Function next_epoch_primary_address](#sui_system_validator_next_epoch_primary_address)
-  [Function next_epoch_worker_address](#sui_system_validator_next_epoch_worker_address)
-  [Function next_epoch_protocol_pubkey_bytes](#sui_system_validator_next_epoch_protocol_pubkey_bytes)
-  [Function next_epoch_proof_of_possession](#sui_system_validator_next_epoch_proof_of_possession)
-  [Function next_epoch_network_pubkey_bytes](#sui_system_validator_next_epoch_network_pubkey_bytes)
-  [Function next_epoch_worker_pubkey_bytes](#sui_system_validator_next_epoch_worker_pubkey_bytes)
-  [Function operation_cap_id](#sui_system_validator_operation_cap_id)
-  [Function next_epoch_gas_price](#sui_system_validator_next_epoch_gas_price)
-  [Function total_stake_amount](#sui_system_validator_total_stake_amount)
-  [Function stake_amount](#sui_system_validator_stake_amount)
-  [Function total_stake](#sui_system_validator_total_stake)
-  [Function voting_power](#sui_system_validator_voting_power)
-  [Function set_voting_power](#sui_system_validator_set_voting_power)
-  [Function pending_stake_amount](#sui_system_validator_pending_stake_amount)
-  [Function pending_stake_withdraw_amount](#sui_system_validator_pending_stake_withdraw_amount)
-  [Function gas_price](#sui_system_validator_gas_price)
-  [Function commission_rate](#sui_system_validator_commission_rate)
-  [Function pool_token_exchange_rate_at_epoch](#sui_system_validator_pool_token_exchange_rate_at_epoch)
-  [Function staking_pool_id](#sui_system_validator_staking_pool_id)
-  [Function is_duplicate](#sui_system_validator_is_duplicate)
-  [Macro function both_some_and_equal](#sui_system_validator_both_some_and_equal)
-  [Function new_unverified_validator_operation_cap_and_transfer](#sui_system_validator_new_unverified_validator_operation_cap_and_transfer)
-  [Function update_name](#sui_system_validator_update_name)
-  [Function update_description](#sui_system_validator_update_description)
-  [Function update_image_url](#sui_system_validator_update_image_url)
-  [Function update_project_url](#sui_system_validator_update_project_url)
-  [Function update_next_epoch_network_address](#sui_system_validator_update_next_epoch_network_address)
-  [Function update_candidate_network_address](#sui_system_validator_update_candidate_network_address)
-  [Function update_next_epoch_p2p_address](#sui_system_validator_update_next_epoch_p2p_address)
-  [Function update_candidate_p2p_address](#sui_system_validator_update_candidate_p2p_address)
-  [Function update_next_epoch_primary_address](#sui_system_validator_update_next_epoch_primary_address)
-  [Function update_candidate_primary_address](#sui_system_validator_update_candidate_primary_address)
-  [Function update_next_epoch_worker_address](#sui_system_validator_update_next_epoch_worker_address)
-  [Function update_candidate_worker_address](#sui_system_validator_update_candidate_worker_address)
-  [Function update_next_epoch_protocol_pubkey](#sui_system_validator_update_next_epoch_protocol_pubkey)
-  [Function update_candidate_protocol_pubkey](#sui_system_validator_update_candidate_protocol_pubkey)
-  [Function update_next_epoch_network_pubkey](#sui_system_validator_update_next_epoch_network_pubkey)
-  [Function update_candidate_network_pubkey](#sui_system_validator_update_candidate_network_pubkey)
-  [Function update_next_epoch_worker_pubkey](#sui_system_validator_update_next_epoch_worker_pubkey)
-  [Function update_candidate_worker_pubkey](#sui_system_validator_update_candidate_worker_pubkey)
-  [Function effectuate_staged_metadata](#sui_system_validator_effectuate_staged_metadata)
-  [Macro function do_extract](#sui_system_validator_do_extract)
-  [Function validate_metadata](#sui_system_validator_validate_metadata)
-  [Function validate_metadata_bcs](#sui_system_validator_validate_metadata_bcs)
-  [Function get_staking_pool_ref](#sui_system_validator_get_staking_pool_ref)
-  [Function new_from_metadata](#sui_system_validator_new_from_metadata)

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
<b>use</b> <a href="../sui_sui_system/validator_cap#sui_system_validator_cap">sui_system::validator_cap</a>;
</code>

Struct <code>ValidatorMetadata</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>: <b>address</b></code>
</dt>
<dd>
 The Sui Address of the validator. This is the sender that created the Validator object,
 and also the address to send validator/coins to during withdraws.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
 The public key bytes corresponding to the private key that the validator
 holds to sign transactions. For now, this is the same as AuthorityName.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
 The public key bytes corresponding to the private key that the validator
 uses to establish TLS connections
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
 The public key bytes correstponding to the Narwhal Worker
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;</code>
</dt>
<dd>
 This is a proof that the validator has ownership of the private key
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 A unique human-readable name of this validator.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a></code>
</dt>
<dd>
</dd>
<dt>
<code>net_address: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The network address of the validator (could also contain extra info such as port, DNS and etc.).
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The address of the validator used for p2p activities such as state sync (could also contain extra info such as port, DNS and etc.).
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The address of the narwhal primary
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 The address of the narwhal worker
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;</code>
</dt>
<dd>
 "next_epoch" metadata only takes effects in the next epoch.
 If none, current value will stay unchanged.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>next_epoch_net_address: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;</code>
</dt>
<dd>
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
 Any extra fields that's not defined statically.
</dd>
</dl>

Struct <code>Validator</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a> <b>has</b> store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">sui_system::validator::ValidatorMetadata</a></code>
</dt>
<dd>
 Summary of the validator.
</dd>
<dt>
<code><a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: u64</code>
</dt>
<dd>
 The voting power of this validator, which might be different from its
 stake amount.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 The ID of this validator's current valid <code>UnverifiedValidatorOperationCap</code>
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>: u64</code>
</dt>
<dd>
 Gas price quote, updated only at end of epoch.
</dd>
<dt>
<code><a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a></code>
</dt>
<dd>
 Staking pool for this validator.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>: u64</code>
</dt>
<dd>
 Commission rate of the validator, in basis point.
</dd>
<dt>
<code>next_epoch_stake: u64</code>
</dt>
<dd>
 Total amount of stake that would be active in the next epoch.
</dd>
<dt>
<code><a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>: u64</code>
</dt>
<dd>
 This validator's gas price quote for the next epoch.
</dd>
<dt>
<code>next_epoch_commission_rate: u64</code>
</dt>
<dd>
 The commission rate of the validator starting the next epoch, in basis point.
</dd>
<dt>
<code>extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a></code>
</dt>
<dd>
 Any extra fields that's not defined statically.
</dd>
</dl>

Struct <code>StakingRequestEvent</code>

Event emitted when a new stake request is received.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_StakingRequestEvent">StakingRequestEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>staker_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>amount: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>UnstakingRequestEvent</code>

Event emitted when a new unstake request is received.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_UnstakingRequestEvent">UnstakingRequestEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>validator_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>staker_address: <b>address</b></code>
</dt>
<dd>
</dd>
<dt>
<code>stake_activation_epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>unstaking_epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>principal_amount: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>reward_amount: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>ConvertingToFungibleStakedSuiEvent</code>

Event emitted when a staked SUI is converted to a fungible staked SUI.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_ConvertingToFungibleStakedSuiEvent">ConvertingToFungibleStakedSuiEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>stake_activation_epoch: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>staked_sui_principal_amount: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>fungible_staked_sui_amount: u64</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>RedeemingFungibleStakedSuiEvent</code>

Event emitted when a fungible staked SUI is redeemed.

<code><b>public</b> <b>struct</b> <a href="../sui_sui_system/validator#sui_system_validator_RedeemingFungibleStakedSuiEvent">RedeemingFungibleStakedSuiEvent</a> <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>pool_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>fungible_staked_sui_amount: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>sui_amount: u64</code>
</dt>
<dd>
</dd>
</dl>

Constants

Invalid proof_of_possession field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EInvalidProofOfPossession">EInvalidProofOfPossession</a>: u64 = 0;
</code>

Invalid pubkey_bytes field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidPubkey">EMetadataInvalidPubkey</a>: u64 = 1;
</code>

Invalid network_pubkey_bytes field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidNetPubkey">EMetadataInvalidNetPubkey</a>: u64 = 2;
</code>

Invalid worker_pubkey_bytes field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidWorkerPubkey">EMetadataInvalidWorkerPubkey</a>: u64 = 3;
</code>

Invalid net_address field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidNetAddr">EMetadataInvalidNetAddr</a>: u64 = 4;
</code>

Invalid p2p_address field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidP2pAddr">EMetadataInvalidP2pAddr</a>: u64 = 5;
</code>

Invalid primary_address field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidPrimaryAddr">EMetadataInvalidPrimaryAddr</a>: u64 = 6;
</code>

Invalid worker_address field in ValidatorMetadata

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EMetadataInvalidWorkerAddr">EMetadataInvalidWorkerAddr</a>: u64 = 7;
</code>

Commission rate set by the validator is higher than the threshold

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_ECommissionRateTooHigh">ECommissionRateTooHigh</a>: u64 = 8;
</code>

Validator Metadata is too long

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>: u64 = 9;
</code>

Intended validator is not a candidate one.

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>: u64 = 10;
</code>

Stake amount is invalid or wrong.

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EInvalidStakeAmount">EInvalidStakeAmount</a>: u64 = 11;
</code>

Function called during non-genesis times.

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_ECalledDuringNonGenesis">ECalledDuringNonGenesis</a>: u64 = 12;
</code>

New Capability is not created by the validator itself

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_ENewCapNotCreatedByValidatorItself">ENewCapNotCreatedByValidatorItself</a>: u64 = 100;
</code>

Capability code is not valid

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EInvalidCap">EInvalidCap</a>: u64 = 101;
</code>

Validator trying to set gas price higher than threshold.

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_EGasPriceHigherThanThreshold">EGasPriceHigherThanThreshold</a>: u64 = 102;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_MAX_COMMISSION_RATE">MAX_COMMISSION_RATE</a>: u64 = 2000;
</code>

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>: u64 = 256;
</code>

Max gas price a validator can set is 100K MIST.

<code><b>const</b> <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_GAS_PRICE">MAX_VALIDATOR_GAS_PRICE</a>: u64 = 100000;
</code>

Function <code>new_metadata</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_metadata">new_metadata</a>(<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>: <b>address</b>, <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>, <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: <a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>, net_address: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, extra_fields: <a href="../sui_sui/bag#sui_bag_Bag">sui::bag::Bag</a>): <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">sui_system::validator::ValidatorMetadata</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_metadata">new_metadata</a>(
    <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>: <b>address</b>,
    <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: String,
    <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: String,
    <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: Url,
    <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: Url,
    net_address: String,
    <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: String,
    <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: String,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: String,
    extra_fields: Bag,
): <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a> {
    <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a> {
        <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>,
        net_address,
        <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>: option::none(),
        next_epoch_net_address: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>: option::none(),
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>: option::none(),
        extra_fields,
    }
}
</code></pre>

Function <code>new</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new">new</a>(<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>: <b>address</b>, <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: vector&lt;u8&gt;, net_address: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>: u64, <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new">new</a>(
    <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>: <b>address</b>,
    <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: vector&lt;u8&gt;,
    net_address: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>: u64,
    <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>: u64,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a> {
    <b>assert</b>!(
        net_address.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>
            && <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a> &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_COMMISSION_RATE">MAX_COMMISSION_RATE</a>, <a href="../sui_sui_system/validator#sui_system_validator_ECommissionRateTooHigh">ECommissionRateTooHigh</a>);
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a> &lt; <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_GAS_PRICE">MAX_VALIDATOR_GAS_PRICE</a>, <a href="../sui_sui_system/validator#sui_system_validator_EGasPriceHigherThanThreshold">EGasPriceHigherThanThreshold</a>);
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a> = <a href="../sui_sui_system/validator#sui_system_validator_new_metadata">new_metadata</a>(
        <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>.to_ascii_string().to_string(),
        <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>.to_ascii_string().to_string(),
        url::new_unsafe_from_bytes(<a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>),
        url::new_unsafe_from_bytes(<a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>),
        net_address.to_ascii_string().to_string(),
        <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.to_ascii_string().to_string(),
        <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.to_ascii_string().to_string(),
        <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.to_ascii_string().to_string(),
        bag::new(ctx),
    );
    // Checks that the keys & addresses & PoP are valid.
    <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
    <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_new_from_metadata">new_from_metadata</a>(<a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>, <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>, ctx)
}
</code></pre>

Function <code>deactivate</code>

Mark Validator's StakingPool as inactive by setting the deactivation_epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_deactivate">deactivate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, deactivation_epoch: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_deactivate">deactivate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, deactivation_epoch: u64) {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.deactivate_staking_pool(deactivation_epoch)
}
</code></pre>

Function <code>activate</code>

Activate Validator's StakingPool by setting the activation_epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_activate">activate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, activation_epoch: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_activate">activate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, activation_epoch: u64) {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.activate_staking_pool(activation_epoch);
}
</code></pre>

Function <code>adjust_stake_and_gas_price</code>

Process pending stake and pending withdraws, and update the gas price.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_adjust_stake_and_gas_price">adjust_stake_and_gas_price</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>) {
    self.<a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a> = self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a> = self.next_epoch_commission_rate;
}
</code></pre>

Function <code>request_add_stake</code>

Request to add stake to the validator's staking pool, processed at the end of the epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_add_stake">request_add_stake</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, stake: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, staker_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_add_stake">request_add_stake</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    stake: Balance&lt;SUI&gt;,
    staker_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
): StakedSui {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a> = stake.value();
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a> &gt; 0, <a href="../sui_sui_system/validator#sui_system_validator_EInvalidStakeAmount">EInvalidStakeAmount</a>);
    <b>let</b> stake_epoch = ctx.epoch() + 1;
    <b>let</b> staked_sui = self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_request_add_stake">request_add_stake</a>(stake, stake_epoch, ctx);
    // Process stake right away <b>if</b> staking pool is preactive.
    <b>if</b> (self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>()) {
        self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.process_pending_stake();
    };
    self.next_epoch_stake = self.next_epoch_stake + <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>;
    event::emit(<a href="../sui_sui_system/validator#sui_system_validator_StakingRequestEvent">StakingRequestEvent</a> {
        pool_id: self.<a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(),
        validator_address: self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>,
        staker_address,
        epoch: ctx.epoch(),
        amount: <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>,
    });
    staked_sui
}
</code></pre>

Function <code>convert_to_fungible_staked_sui</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    staked_sui: StakedSui,
    ctx: &<b>mut</b> TxContext,
): FungibleStakedSui {
    <b>let</b> stake_activation_epoch = staked_sui.activation_epoch();
    <b>let</b> staked_sui_principal_amount = staked_sui.amount();
    <b>let</b> fungible_staked_sui = self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_convert_to_fungible_staked_sui">convert_to_fungible_staked_sui</a>(staked_sui, ctx);
    event::emit(<a href="../sui_sui_system/validator#sui_system_validator_ConvertingToFungibleStakedSuiEvent">ConvertingToFungibleStakedSuiEvent</a> {
        pool_id: self.<a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(),
        stake_activation_epoch,
        staked_sui_principal_amount,
        fungible_staked_sui_amount: fungible_staked_sui.value(),
    });
    fungible_staked_sui
}
</code></pre>

Function <code>redeem_fungible_staked_sui</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, fungible_staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_FungibleStakedSui">sui_system::staking_pool::FungibleStakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    fungible_staked_sui: FungibleStakedSui,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    <b>let</b> fungible_staked_sui_amount = fungible_staked_sui.value();
    <b>let</b> sui = self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_redeem_fungible_staked_sui">redeem_fungible_staked_sui</a>(fungible_staked_sui, ctx);
    self.next_epoch_stake = self.next_epoch_stake - sui.value();
    event::emit(<a href="../sui_sui_system/validator#sui_system_validator_RedeemingFungibleStakedSuiEvent">RedeemingFungibleStakedSuiEvent</a> {
        pool_id: self.<a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(),
        fungible_staked_sui_amount,
        sui_amount: sui.value(),
    });
    sui
}
</code></pre>

Function <code>request_add_stake_at_genesis</code>

Request to add stake to the validator's staking pool at genesis

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_add_stake_at_genesis">request_add_stake_at_genesis</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, stake: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;, staker_address: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_add_stake_at_genesis">request_add_stake_at_genesis</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    stake: Balance&lt;SUI&gt;,
    staker_address: <b>address</b>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(ctx.epoch() == 0, <a href="../sui_sui_system/validator#sui_system_validator_ECalledDuringNonGenesis">ECalledDuringNonGenesis</a>);
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a> = stake.value();
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a> &gt; 0, <a href="../sui_sui_system/validator#sui_system_validator_EInvalidStakeAmount">EInvalidStakeAmount</a>);
    // 0 = <a href="../sui_sui_system/genesis#sui_system_genesis">genesis</a> epoch
    <b>let</b> staked_sui = self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_request_add_stake">request_add_stake</a>(stake, 0, ctx);
    transfer::public_transfer(staked_sui, staker_address);
    // Process stake right away
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.process_pending_stake();
    self.next_epoch_stake = self.next_epoch_stake + <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>;
}
</code></pre>

Function <code>request_withdraw_stake</code>

Request to withdraw stake from the validator's staking pool, processed at the end of the epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_withdraw_stake">request_withdraw_stake</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, staked_sui: <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakedSui">sui_system::staking_pool::StakedSui</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_withdraw_stake">request_withdraw_stake</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    staked_sui: StakedSui,
    ctx: &TxContext,
): Balance&lt;SUI&gt; {
    <b>let</b> principal_amount = staked_sui.amount();
    <b>let</b> stake_activation_epoch = staked_sui.activation_epoch();
    <b>let</b> withdrawn_stake = self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_request_withdraw_stake">request_withdraw_stake</a>(staked_sui, ctx);
    <b>let</b> withdraw_amount = withdrawn_stake.value();
    <b>let</b> reward_amount = withdraw_amount - principal_amount;
    self.next_epoch_stake = self.next_epoch_stake - withdraw_amount;
    event::emit(<a href="../sui_sui_system/validator#sui_system_validator_UnstakingRequestEvent">UnstakingRequestEvent</a> {
        pool_id: self.<a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(),
        validator_address: self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>,
        staker_address: ctx.sender(),
        stake_activation_epoch,
        unstaking_epoch: ctx.epoch(),
        principal_amount,
        reward_amount,
    });
    withdrawn_stake
}
</code></pre>

Function <code>request_set_gas_price</code>

Request to set new gas price for the next epoch.
Need to present a ValidatorOperationCap.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_set_gas_price">request_set_gas_price</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, verified_cap: <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>, new_price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_set_gas_price">request_set_gas_price</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    verified_cap: ValidatorOperationCap,
    new_price: u64,
) {
    <b>assert</b>!(new_price &lt; <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_GAS_PRICE">MAX_VALIDATOR_GAS_PRICE</a>, <a href="../sui_sui_system/validator#sui_system_validator_EGasPriceHigherThanThreshold">EGasPriceHigherThanThreshold</a>);
    <b>let</b> validator_address = *verified_cap.verified_operation_cap_address();
    <b>assert</b>!(validator_address == self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>, <a href="../sui_sui_system/validator#sui_system_validator_EInvalidCap">EInvalidCap</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a> = new_price;
}
</code></pre>

Function <code>set_candidate_gas_price</code>

Set new gas price for the candidate validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_candidate_gas_price">set_candidate_gas_price</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, verified_cap: <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_ValidatorOperationCap">sui_system::validator_cap::ValidatorOperationCap</a>, new_price: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_candidate_gas_price">set_candidate_gas_price</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    verified_cap: ValidatorOperationCap,
    new_price: u64,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(new_price &lt; <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_GAS_PRICE">MAX_VALIDATOR_GAS_PRICE</a>, <a href="../sui_sui_system/validator#sui_system_validator_EGasPriceHigherThanThreshold">EGasPriceHigherThanThreshold</a>);
    <b>let</b> validator_address = *verified_cap.verified_operation_cap_address();
    <b>assert</b>!(validator_address == self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>, <a href="../sui_sui_system/validator#sui_system_validator_EInvalidCap">EInvalidCap</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a> = new_price;
    self.<a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a> = new_price;
}
</code></pre>

Function <code>request_set_commission_rate</code>

Request to set new commission rate for the next epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_set_commission_rate">request_set_commission_rate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, new_commission_rate: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_request_set_commission_rate">request_set_commission_rate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, new_commission_rate: u64) {
    <b>assert</b>!(new_commission_rate &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_COMMISSION_RATE">MAX_COMMISSION_RATE</a>, <a href="../sui_sui_system/validator#sui_system_validator_ECommissionRateTooHigh">ECommissionRateTooHigh</a>);
    self.next_epoch_commission_rate = new_commission_rate;
}
</code></pre>

Function <code>set_candidate_commission_rate</code>

Set new commission rate for the candidate validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_candidate_commission_rate">set_candidate_commission_rate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, new_commission_rate: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_candidate_commission_rate">set_candidate_commission_rate</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, new_commission_rate: u64) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(new_commission_rate &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_COMMISSION_RATE">MAX_COMMISSION_RATE</a>, <a href="../sui_sui_system/validator#sui_system_validator_ECommissionRateTooHigh">ECommissionRateTooHigh</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a> = new_commission_rate;
}
</code></pre>

Function <code>deposit_stake_rewards</code>

Deposit stakes rewards into the validator's staking pool, called at the end of the epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_deposit_stake_rewards">deposit_stake_rewards</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, reward: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_deposit_stake_rewards">deposit_stake_rewards</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, reward: Balance&lt;SUI&gt;) {
    self.next_epoch_stake = self.next_epoch_stake + reward.value();
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.deposit_rewards(reward);
}
</code></pre>

Function <code>process_pending_stakes_and_withdraws</code>

Process pending stakes and withdraws, called at the end of the epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, ctx: &TxContext) {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_process_pending_stakes_and_withdraws">process_pending_stakes_and_withdraws</a>(ctx);
    // TODO: bring this assertion back when we are ready.
    // <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>(self) == self.next_epoch_stake, <a href="../sui_sui_system/validator#sui_system_validator_EInvalidStakeAmount">EInvalidStakeAmount</a>);
}
</code></pre>

Function <code>is_preactive</code>

Returns true if the validator is preactive.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): bool {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>()
}
</code></pre>

Function <code>metadata</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">sui_system::validator::ValidatorMetadata</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &<a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a> {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>
}
</code></pre>

Function <code>sui_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): <b>address</b> {
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>
}
</code></pre>

Function <code>name</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_name">name</a>
}
</code></pre>

Function <code>description</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_description">description</a>
}
</code></pre>

Function <code>image_url</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Url {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>
}
</code></pre>

Function <code>project_url</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_sui/url#sui_url_Url">sui::url::Url</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Url {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>
}
</code></pre>

Function <code>network_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_network_address">network_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_network_address">network_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.net_address
}
</code></pre>

Function <code>p2p_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>
}
</code></pre>

Function <code>primary_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>
}
</code></pre>

Function <code>worker_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &String {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>
}
</code></pre>

Function <code>protocol_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &vector&lt;u8&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>
}
</code></pre>

Function <code>proof_of_possession</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &vector&lt;u8&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>
}
</code></pre>

Function <code>network_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &vector&lt;u8&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>
}
</code></pre>

Function <code>worker_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &vector&lt;u8&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>
}
</code></pre>

Function <code>next_epoch_network_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_address">next_epoch_network_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_address">next_epoch_network_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;String&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.next_epoch_net_address
}
</code></pre>

Function <code>next_epoch_p2p_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;String&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>
}
</code></pre>

Function <code>next_epoch_primary_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;String&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>
}
</code></pre>

Function <code>next_epoch_worker_address</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;String&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>
}
</code></pre>

Function <code>next_epoch_protocol_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;vector&lt;u8&gt;&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>
}
</code></pre>

Function <code>next_epoch_proof_of_possession</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;vector&lt;u8&gt;&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>
}
</code></pre>

Function <code>next_epoch_network_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;vector&lt;u8&gt;&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>
}
</code></pre>

Function <code>next_epoch_worker_pubkey_bytes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;vector&lt;u8&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &Option&lt;vector&lt;u8&gt;&gt; {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>
}
</code></pre>

Function <code>operation_cap_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &ID {
    &self.<a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a>
}
</code></pre>

Function <code>next_epoch_gas_price</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>
}
</code></pre>

Function <code>total_stake_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_total_stake_amount">total_stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_total_stake_amount">total_stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.sui_balance()
}
</code></pre>

Function <code>stake_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_stake_amount">stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.sui_balance()
}
</code></pre>

Function <code>total_stake</code>

Return the total amount staked with this validator

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_total_stake">total_stake</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_total_stake">total_stake</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.sui_balance()
}
</code></pre>

Function <code>voting_power</code>

Return the voting power of this validator.

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>
}
</code></pre>

Function <code>set_voting_power</code>

Set the voting power of this validator, called only from validator_set.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_voting_power">set_voting_power</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, new_voting_power: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_set_voting_power">set_voting_power</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, new_voting_power: u64) {
    self.<a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a> = new_voting_power;
}
</code></pre>

Function <code>pending_stake_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pending_stake_amount">pending_stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pending_stake_amount">pending_stake_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_pending_stake_amount">pending_stake_amount</a>()
}
</code></pre>

Function <code>pending_stake_withdraw_amount</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pending_stake_withdraw_amount">pending_stake_withdraw_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pending_stake_withdraw_amount">pending_stake_withdraw_amount</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_pending_stake_withdraw_amount">pending_stake_withdraw_amount</a>()
}
</code></pre>

Function <code>gas_price</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>
}
</code></pre>

Function <code>commission_rate</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): u64 {
    self.<a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>
}
</code></pre>

Function <code>pool_token_exchange_rate_at_epoch</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, epoch: u64): <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_PoolTokenExchangeRate">sui_system::staking_pool::PoolTokenExchangeRate</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, epoch: u64): PoolTokenExchangeRate {
    self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>.<a href="../sui_sui_system/validator#sui_system_validator_pool_token_exchange_rate_at_epoch">pool_token_exchange_rate_at_epoch</a>(epoch)
}
</code></pre>

Function <code>staking_pool_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_staking_pool_id">staking_pool_id</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): ID {
    object::id(&self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>)
}
</code></pre>

Function <code>is_duplicate</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_is_duplicate">is_duplicate</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, other: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_is_duplicate">is_duplicate</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, other: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): bool {
    <b>let</b> self = &self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>;
    <b>let</b> other = &other.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_name">name</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_name">name</a>
        || self.net_address == other.net_address
        || self.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>
        || self.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a> == other.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>
        // All next epoch parameters.
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.next_epoch_net_address, other.next_epoch_net_address)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>)
        || <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>!(self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>, other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>)
        // My next epoch parameters with other current epoch parameters.
        || self.next_epoch_net_address.is_some_and!(|v| v == other.net_address)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>)
        || self.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>.is_some_and!(|v| v == other.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>)
        // Other next epoch parameters with my current epoch parameters.
        || other.next_epoch_net_address.is_some_and!(|v| v == self.net_address)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a>)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a>)
        || other.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>.is_some_and!(|v| v == self.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a>)
}
</code></pre>

Macro function <code>both_some_and_equal</code>

<code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>&lt;$T&gt;($a: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $b: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_both_some_and_equal">both_some_and_equal</a>&lt;$T&gt;($a: Option&lt;$T&gt;, $b: Option&lt;$T&gt;): bool {
    <b>let</b> (a, b) = ($a, $b);
    a.is_some_and!(|a| b.is_some_and!(|b| a == b))
}
</code></pre>

Function <code>new_unverified_validator_operation_cap_and_transfer</code>

Create a new UnverifiedValidatorOperationCap, transfer to the validator,
and registers it, thus revoking the previous cap's permission.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_unverified_validator_operation_cap_and_transfer">new_unverified_validator_operation_cap_and_transfer</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_unverified_validator_operation_cap_and_transfer">new_unverified_validator_operation_cap_and_transfer</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    ctx: &<b>mut</b> TxContext,
) {
    <b>let</b> sender = ctx.sender();
    <b>assert</b>!(sender == self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>, <a href="../sui_sui_system/validator#sui_system_validator_ENewCapNotCreatedByValidatorItself">ENewCapNotCreatedByValidatorItself</a>);
    <b>let</b> new_id = <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_new_unverified_validator_operation_cap_and_transfer">validator_cap::new_unverified_validator_operation_cap_and_transfer</a>(sender, ctx);
    self.<a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a> = new_id;
}
</code></pre>

Function <code>update_name</code>

Update name of the validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_name">update_name</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_name">update_name</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(<a href="../sui_sui_system/validator#sui_system_validator_name">name</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>, <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_name">name</a> = <a href="../sui_sui_system/validator#sui_system_validator_name">name</a>.to_ascii_string().to_string();
}
</code></pre>

Function <code>update_description</code>

Update description of the validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_description">update_description</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_description">update_description</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_description">description</a> = <a href="../sui_sui_system/validator#sui_system_validator_description">description</a>.to_ascii_string().to_string();
}
</code></pre>

Function <code>update_image_url</code>

Update image url of the validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_image_url">update_image_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_image_url">update_image_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a> = url::new_unsafe_from_bytes(<a href="../sui_sui_system/validator#sui_system_validator_image_url">image_url</a>);
}
</code></pre>

Function <code>update_project_url</code>

Update project url of the validator.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_project_url">update_project_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_project_url">update_project_url</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a> = url::new_unsafe_from_bytes(<a href="../sui_sui_system/validator#sui_system_validator_project_url">project_url</a>);
}
</code></pre>

Function <code>update_next_epoch_network_address</code>

Update network address of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_network_address">update_next_epoch_network_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, net_address: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_network_address">update_next_epoch_network_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    net_address: vector&lt;u8&gt;,
) {
    <b>assert</b>!(
        net_address.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> net_address = net_address.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.next_epoch_net_address = option::some(net_address);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_network_address</code>

Update network address of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_network_address">update_candidate_network_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, net_address: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_network_address">update_candidate_network_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    net_address: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(
        net_address.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> net_address = net_address.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.net_address = net_address;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_p2p_address</code>

Update p2p address of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_p2p_address">update_next_epoch_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_p2p_address">update_next_epoch_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a> = option::some(<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_p2p_address</code>

Update p2p address of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_p2p_address">update_candidate_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_p2p_address">update_candidate_p2p_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>: vector&lt;u8&gt;) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_primary_address</code>

Update primary address of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_primary_address">update_next_epoch_primary_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_primary_address">update_next_epoch_primary_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;,
) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a> = option::some(<a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_primary_address</code>

Update primary address of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_primary_address">update_candidate_primary_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_primary_address">update_candidate_primary_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_worker_address</code>

Update worker address of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_worker_address">update_next_epoch_worker_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_worker_address">update_next_epoch_worker_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;,
) {
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a> = option::some(<a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_worker_address</code>

Update worker address of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_worker_address">update_candidate_worker_address</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_worker_address">update_candidate_worker_address</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    <b>assert</b>!(
        <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.length() &lt;= <a href="../sui_sui_system/validator#sui_system_validator_MAX_VALIDATOR_METADATA_LENGTH">MAX_VALIDATOR_METADATA_LENGTH</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_EValidatorMetadataExceedingLengthLimit">EValidatorMetadataExceedingLengthLimit</a>,
    );
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>.to_ascii_string().to_string();
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_protocol_pubkey</code>

Update protocol public key of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_protocol_pubkey">update_next_epoch_protocol_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, protocol_pubkey: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_protocol_pubkey">update_next_epoch_protocol_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    protocol_pubkey: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;,
) {
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a> = option::some(protocol_pubkey);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a> = option::some(<a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_protocol_pubkey</code>

Update protocol public key of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_protocol_pubkey">update_candidate_protocol_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, protocol_pubkey: vector&lt;u8&gt;, <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_protocol_pubkey">update_candidate_protocol_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    protocol_pubkey: vector&lt;u8&gt;,
    <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a> = protocol_pubkey;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a> = <a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a>;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_network_pubkey</code>

Update network public key of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_network_pubkey">update_next_epoch_network_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, network_pubkey: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_network_pubkey">update_next_epoch_network_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    network_pubkey: vector&lt;u8&gt;,
) {
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a> = option::some(network_pubkey);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_network_pubkey</code>

Update network public key of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_network_pubkey">update_candidate_network_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, network_pubkey: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_network_pubkey">update_candidate_network_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    network_pubkey: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a> = network_pubkey;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_next_epoch_worker_pubkey</code>

Update Narwhal worker public key of this validator, taking effects from next epoch

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_worker_pubkey">update_next_epoch_worker_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, worker_pubkey: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_next_epoch_worker_pubkey">update_next_epoch_worker_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    worker_pubkey: vector&lt;u8&gt;,
) {
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a> = option::some(worker_pubkey);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>update_candidate_worker_pubkey</code>

Update Narwhal worker public key of this candidate validator

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_worker_pubkey">update_candidate_worker_pubkey</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>, worker_pubkey: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_update_candidate_worker_pubkey">update_candidate_worker_pubkey</a>(
    self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>,
    worker_pubkey: vector&lt;u8&gt;,
) {
    <b>assert</b>!(self.<a href="../sui_sui_system/validator#sui_system_validator_is_preactive">is_preactive</a>(), <a href="../sui_sui_system/validator#sui_system_validator_ENotValidatorCandidate">ENotValidatorCandidate</a>);
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a> = worker_pubkey;
    self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.validate();
}
</code></pre>

Function <code>effectuate_staged_metadata</code>

Effectutate all staged next epoch metadata for this validator.
NOTE: this function SHOULD ONLY be called by validator_set when
advancing an epoch.

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_effectuate_staged_metadata">effectuate_staged_metadata</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_effectuate_staged_metadata">effectuate_staged_metadata</a>(self: &<b>mut</b> <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>) {
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.next_epoch_net_address, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.net_address = v
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_p2p_address">next_epoch_p2p_address</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_p2p_address">p2p_address</a> = v
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_primary_address">next_epoch_primary_address</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_primary_address">primary_address</a> = v
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_address">next_epoch_worker_address</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_address">worker_address</a> = v
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_protocol_pubkey_bytes">next_epoch_protocol_pubkey_bytes</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_protocol_pubkey_bytes">protocol_pubkey_bytes</a> = v;
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_proof_of_possession">proof_of_possession</a> = self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_proof_of_possession">next_epoch_proof_of_possession</a>.extract();
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_network_pubkey_bytes">next_epoch_network_pubkey_bytes</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_network_pubkey_bytes">network_pubkey_bytes</a> = v
    });
    <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>!(&<b>mut</b> self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_next_epoch_worker_pubkey_bytes">next_epoch_worker_pubkey_bytes</a>, |v| {
        self.<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_worker_pubkey_bytes">worker_pubkey_bytes</a> = v
    });
}
</code></pre>

Macro function <code>do_extract</code>

Helper macro which extracts the value from Some and applies $f to it.

<code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>&lt;$T&gt;($o: &<b>mut</b> <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;$T&gt;, $f: |$T| -&gt; ())
</code>

<summary>Implementation</summary>

<pre><code><b>macro</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_do_extract">do_extract</a>&lt;$T&gt;($o: &<b>mut</b> Option&lt;$T&gt;, $f: |$T|) {
    <b>let</b> o = $o;
    <b>if</b> (o.is_some()) {
        $f(o.extract());
    }
}
</code></pre>

Function <code>validate_metadata</code>

Aborts if validator metadata is valid

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_validate_metadata">validate_metadata</a>(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: &<a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">sui_system::validator::ValidatorMetadata</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_validate_metadata">validate_metadata</a>(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: &<a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a>) {
    <a href="../sui_sui_system/validator#sui_system_validator_validate_metadata_bcs">validate_metadata_bcs</a>(bcs::to_bytes(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>));
}
</code></pre>

Function <code>validate_metadata_bcs</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_validate_metadata_bcs">validate_metadata_bcs</a>(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: vector&lt;u8&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>native</b> <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_validate_metadata_bcs">validate_metadata_bcs</a>(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: vector&lt;u8&gt;);
</code></pre>

Function <code>get_staking_pool_ref</code>

<code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_get_staking_pool_ref">get_staking_pool_ref</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>): &<a href="../sui_sui_system/staking_pool#sui_system_staking_pool_StakingPool">sui_system::staking_pool::StakingPool</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b>(package) <b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_get_staking_pool_ref">get_staking_pool_ref</a>(self: &<a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a>): &StakingPool {
    &self.<a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>
}
</code></pre>

Function <code>new_from_metadata</code>

Create a new validator from the given <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a>, called by both <a href="../sui_sui_system/validator#sui_system_validator_new">new</a> and new_for_testing.

<code><b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_from_metadata">new_from_metadata</a>(<a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">sui_system::validator::ValidatorMetadata</a>, <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>: u64, <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui_system/validator#sui_system_validator_Validator">sui_system::validator::Validator</a>
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui_system/validator#sui_system_validator_new_from_metadata">new_from_metadata</a>(
    <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>: <a href="../sui_sui_system/validator#sui_system_validator_ValidatorMetadata">ValidatorMetadata</a>,
    <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>: u64,
    <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>: u64,
    ctx: &<b>mut</b> TxContext,
): <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a> {
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a> = <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>.<a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>;
    <b>let</b> <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a> = <a href="../sui_sui_system/staking_pool#sui_system_staking_pool_new">staking_pool::new</a>(ctx);
    <b>let</b> <a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a> = <a href="../sui_sui_system/validator_cap#sui_system_validator_cap_new_unverified_validator_operation_cap_and_transfer">validator_cap::new_unverified_validator_operation_cap_and_transfer</a>(
        <a href="../sui_sui_system/validator#sui_system_validator_sui_address">sui_address</a>,
        ctx,
    );
    <a href="../sui_sui_system/validator#sui_system_validator_Validator">Validator</a> {
        <a href="../sui_sui_system/validator#sui_system_validator_metadata">metadata</a>,
        // Initialize the voting power to be 0.
        // At the epoch change where this <a href="../sui_sui_system/validator#sui_system_validator">validator</a> is actually added to the
        // active <a href="../sui_sui_system/validator#sui_system_validator">validator</a> set, the voting power will be updated accordingly.
        <a href="../sui_sui_system/voting_power#sui_system_voting_power">voting_power</a>: 0,
        <a href="../sui_sui_system/validator#sui_system_validator_operation_cap_id">operation_cap_id</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>,
        <a href="../sui_sui_system/staking_pool#sui_system_staking_pool">staking_pool</a>,
        <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>,
        next_epoch_stake: 0,
        <a href="../sui_sui_system/validator#sui_system_validator_next_epoch_gas_price">next_epoch_gas_price</a>: <a href="../sui_sui_system/validator#sui_system_validator_gas_price">gas_price</a>,
        next_epoch_commission_rate: <a href="../sui_sui_system/validator#sui_system_validator_commission_rate">commission_rate</a>,
        extra_fields: bag::new(ctx),
    }
}
</code></pre>