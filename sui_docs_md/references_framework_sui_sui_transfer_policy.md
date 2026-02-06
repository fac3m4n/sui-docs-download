Defines the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> type and the logic to approve <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>s.

- TransferPolicy - is a highly customizable primitive, which provides an
interface for the type owner to set custom transfer rules for every
deal performed in the Kiosk or a similar system that integrates with TP.

- Once a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt; is created for and shared (or frozen), the
type T becomes tradable in Kiosks. On every purchase operation, a
<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> is created and needs to be confirmed by the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>
hot potato or transaction will fail.

- Type owner (creator) can set any Rules as long as the ecosystem supports
them. All of the Rules need to be resolved within a single transaction (eg
pay royalty and pay fixed commission). Once required actions are performed,
the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> can be "confirmed" via <a href="../sui_sui/transfer_policy#sui_transfer_policy_confirm_request">confirm_request</a> call.

- <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> aims to be the main interface for creators to control trades
of their types and collect profits if a fee is required on sales. Custom
policies can be removed at any moment, and the change will affect all instances
of the type at once.

-  [Struct TransferRequest](#sui_transfer_policy_TransferRequest)
-  [Struct TransferPolicy](#sui_transfer_policy_TransferPolicy)
-  [Struct TransferPolicyCap](#sui_transfer_policy_TransferPolicyCap)
-  [Struct TransferPolicyCreated](#sui_transfer_policy_TransferPolicyCreated)
-  [Struct TransferPolicyDestroyed](#sui_transfer_policy_TransferPolicyDestroyed)
-  [Struct RuleKey](#sui_transfer_policy_RuleKey)
-  [Constants](#@Constants_0)
-  [Function new_request](#sui_transfer_policy_new_request)
-  [Function new](#sui_transfer_policy_new)
-  [Function default](#sui_transfer_policy_default)
-  [Function withdraw](#sui_transfer_policy_withdraw)
-  [Function destroy_and_withdraw](#sui_transfer_policy_destroy_and_withdraw)
-  [Function confirm_request](#sui_transfer_policy_confirm_request)
-  [Function add_rule](#sui_transfer_policy_add_rule)
-  [Function get_rule](#sui_transfer_policy_get_rule)
-  [Function add_to_balance](#sui_transfer_policy_add_to_balance)
-  [Function add_receipt](#sui_transfer_policy_add_receipt)
-  [Function has_rule](#sui_transfer_policy_has_rule)
-  [Function remove_rule](#sui_transfer_policy_remove_rule)
-  [Function uid](#sui_transfer_policy_uid)
-  [Function uid_mut_as_owner](#sui_transfer_policy_uid_mut_as_owner)
-  [Function rules](#sui_transfer_policy_rules)
-  [Function item](#sui_transfer_policy_item)
-  [Function paid](#sui_transfer_policy_paid)
-  [Function from](#sui_transfer_policy_from)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/internal#std_internal">std::internal</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/u128#std_u128">std::u128</a>;
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
<b>use</b> <a href="../sui_sui/package#sui_package">sui::package</a>;
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

Struct <code>TransferRequest</code>

A "Hot Potato" forcing the buyer to get a transfer permission
from the item type (T) owner on purchase attempt.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;<b>phantom</b> T&gt;
</code>

<summary>Fields</summary>

<dl>
<dt>
<code><a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 The ID of the transferred item. Although the <code>T</code> has no
 constraints, the main use case for this module is to work
 with Objects.
</dd>
<dt>
<code><a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>: u64</code>
</dt>
<dd>
 Amount of SUI paid for the item. Can be used to
 calculate the fee / transfer policy enforcement.
</dd>
<dt>
<code><a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 The ID of the Kiosk / Safe the object is being sold from.
 Can be used by the TransferPolicy implementors.
</dd>
<dt>
<code>receipts: <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;</code>
</dt>
<dd>
 Collected Receipts. Used to verify that all of the rules
 were followed and <code><a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a></code> can be confirmed.
</dd>
</dl>

Struct <code>TransferPolicy</code>

A unique capability that allows the owner of the T to authorize
transfers. Can only be created with the Publisher object. Although
there's no limitation to how many policies can be created, for most
of the cases there's no need to create more than one since any of the
policies can be used to confirm the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;</code>
</dt>
<dd>
 The Balance of the <code><a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a></code> which collects <code>SUI</code>.
 By default, transfer policy does not collect anything , and it's
 a matter of an implementation of a specific rule - whether to add
 to balance and how much.
</dd>
<dt>
<code><a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>: <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;</code>
</dt>
<dd>
 Set of types of attached rules - used to verify <code>receipts</code> when
 a <code><a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a></code> is received in <code><a href="../sui_sui/transfer_policy#sui_transfer_policy_confirm_request">confirm_request</a></code> function.
 Additionally provides a way to look up currently attached Rules.
</dd>
</dl>

Struct <code>TransferPolicyCap</code>

A Capability granting the owner permission to add/remove rules as well
as to <a href="../sui_sui/transfer_policy#sui_transfer_policy_withdraw">withdraw</a> and <a href="../sui_sui/transfer_policy#sui_transfer_policy_destroy_and_withdraw">destroy_and_withdraw</a> the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;<b>phantom</b> T&gt; <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code>policy_id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TransferPolicyCreated</code>

Event that is emitted when a publisher creates a new <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>
making the discoverability and tracking the supported types easier.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCreated">TransferPolicyCreated</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TransferPolicyDestroyed</code>

Event that is emitted when a publisher destroys a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>.
Allows for tracking supported policies.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyDestroyed">TransferPolicyDestroyed</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>RuleKey</code>

Key to store "Rule" configuration for a specific <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_RuleKey">RuleKey</a>&lt;<b>phantom</b> T: drop&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
</dl>

Constants

The number of receipts does not match the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> requirement.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_EPolicyNotSatisfied">EPolicyNotSatisfied</a>: u64 = 0;
</code>

A completed rule is not set in the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_EIllegalRule">EIllegalRule</a>: u64 = 1;
</code>

A Rule is not set.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_EUnknownRequirement">EUnknownRequirement</a>: u64 = 2;
</code>

Attempting to create a Rule that is already set.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_ERuleAlreadySet">ERuleAlreadySet</a>: u64 = 3;
</code>

Trying to <a href="../sui_sui/transfer_policy#sui_transfer_policy_withdraw">withdraw</a> or close_and_withdraw with a wrong Cap.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>: u64 = 4;
</code>

Trying to <a href="../sui_sui/transfer_policy#sui_transfer_policy_withdraw">withdraw</a> more than there is.

<code><b>const</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotEnough">ENotEnough</a>: u64 = 5;
</code>

Function <code>new_request</code>

Construct a new <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> hot potato which requires an
approving action from the creator to be destroyed / resolved. Once
created, it must be confirmed in the <a href="../sui_sui/transfer_policy#sui_transfer_policy_confirm_request">confirm_request</a> call otherwise
the transaction will fail.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_new_request">new_request</a>&lt;T&gt;(<a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>: u64, <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>): <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_new_request">new_request</a>&lt;T&gt;(<a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>: ID, <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>: u64, <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>: ID): <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt; {
    <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> { <a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>, receipts: <a href="../sui_sui/vec_set#sui_vec_set_empty">vec_set::empty</a>() }
}
</code></pre>

Function <code>new</code>

Register a type in the Kiosk system and receive a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> and
a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a> for the type. The <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> is required to
confirm kiosk deals for the T. If there's no <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>
available for use, the type can not be traded in kiosks.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_new">new</a>&lt;T&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_new">new</a>&lt;T&gt;(pub: &Publisher, ctx: &<b>mut</b> TxContext): (<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;, <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;) {
    <b>assert</b>!(<a href="../sui_sui/package#sui_package_from_package">package::from_package</a>&lt;T&gt;(pub), 0);
    <b>let</b> id = <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx);
    <b>let</b> policy_id = id.to_inner();
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCreated">TransferPolicyCreated</a>&lt;T&gt; { id: policy_id });
    (
        <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> { id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>: <a href="../sui_sui/vec_set#sui_vec_set_empty">vec_set::empty</a>(), <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_zero">balance::zero</a>() },
        <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a> { id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx), policy_id },
    )
}
</code></pre>

Function <code>default</code>

Initialize the Transfer Policy in the default scenario: Create and share
the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>, transfer <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a> to the transaction
sender.

<code><b>entry</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_default">default</a>&lt;T&gt;(pub: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>entry</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_default">default</a>&lt;T&gt;(pub: &Publisher, ctx: &<b>mut</b> TxContext) {
    <b>let</b> (policy, cap) = <a href="../sui_sui/transfer_policy#sui_transfer_policy_new">new</a>&lt;T&gt;(pub, ctx);
    <a href="../sui_sui/transfer#sui_transfer_share_object">sui::transfer::share_object</a>(policy);
    <a href="../sui_sui/transfer#sui_transfer_transfer">sui::transfer::transfer</a>(cap, ctx.sender());
}
</code></pre>

Function <code>withdraw</code>

Withdraw some amount of profits from the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>. If amount
is not specified, all profits are withdrawn.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_withdraw">withdraw</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;, amount: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_withdraw">withdraw</a>&lt;T&gt;(
    self: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;,
    amount: Option&lt;u64&gt;,
    ctx: &<b>mut</b> TxContext,
): Coin&lt;SUI&gt; {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.policy_id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>);
    <b>let</b> amount = <b>if</b> (amount.is_some()) {
        <b>let</b> amt = amount.destroy_some();
        <b>assert</b>!(amt &lt;= self.<a href="../sui_sui/balance#sui_balance">balance</a>.value(), <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotEnough">ENotEnough</a>);
        amt
    } <b>else</b> {
        self.<a href="../sui_sui/balance#sui_balance">balance</a>.value()
    };
    <a href="../sui_sui/coin#sui_coin_take">coin::take</a>(&<b>mut</b> self.<a href="../sui_sui/balance#sui_balance">balance</a>, amount, ctx)
}
</code></pre>

Function <code>destroy_and_withdraw</code>

Destroy a TransferPolicyCap.
Can be performed by any party as long as they own it.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_destroy_and_withdraw">destroy_and_withdraw</a>&lt;T&gt;(self: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, cap: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_destroy_and_withdraw">destroy_and_withdraw</a>&lt;T&gt;(
    self: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
    cap: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
): Coin&lt;SUI&gt; {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(&self) == cap.policy_id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>);
    <b>let</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a> { id: cap_id, policy_id } = cap;
    <b>let</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> { id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>: _, <a href="../sui_sui/balance#sui_balance">balance</a> } = self;
    id.delete();
    cap_id.delete();
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyDestroyed">TransferPolicyDestroyed</a>&lt;T&gt; { id: policy_id });
    <a href="../sui_sui/balance#sui_balance">balance</a>.into_coin(ctx)
}
</code></pre>

Function <code>confirm_request</code>

Allow a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> for the type T. The call is protected
by the type constraint, as only the publisher of the T can get
<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;.

Note: unless there's a policy for T to allow transfers,
Kiosk trades will not be possible.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_confirm_request">confirm_request</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, request: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;): (<a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>, u64, <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_confirm_request">confirm_request</a>&lt;T&gt;(
    self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
    request: <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt;,
): (ID, u64, ID) {
    <b>let</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> { <a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>, receipts } = request;
    <b>let</b> <b>mut</b> completed = receipts.into_keys();
    <b>let</b> <b>mut</b> total = completed.length();
    <b>assert</b>!(total == self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>.length(), <a href="../sui_sui/transfer_policy#sui_transfer_policy_EPolicyNotSatisfied">EPolicyNotSatisfied</a>);
    <b>while</b> (total &gt; 0) {
        <b>let</b> rule_type = completed.pop_back();
        <b>assert</b>!(self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>.contains(&rule_type), <a href="../sui_sui/transfer_policy#sui_transfer_policy_EIllegalRule">EIllegalRule</a>);
        total = total - 1;
    };
    (<a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>, <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>)
}
</code></pre>

Function <code>add_rule</code>

Add a custom Rule to the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>. Once set, <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a> must
receive a confirmation of the rule executed so the hot potato can be unpacked.

- T: the type to which TransferPolicy<T> is applied.
- Rule: the witness type for the Custom rule
- Config: a custom configuration for the rule

Config requires drop to allow creators to remove any policy at any moment,
even if graceful unpacking has not been implemented in a "rule module".

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_rule">add_rule</a>&lt;T, Rule: drop, Config: drop, store&gt;(_: Rule, policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;, cfg: Config)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_rule">add_rule</a>&lt;T, Rule: drop, Config: store + drop&gt;(
    _: Rule,
    policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;,
    cfg: Config,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(policy) == cap.policy_id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>);
    <b>assert</b>!(!<a href="../sui_sui/transfer_policy#sui_transfer_policy_has_rule">has_rule</a>&lt;T, Rule&gt;(policy), <a href="../sui_sui/transfer_policy#sui_transfer_policy_ERuleAlreadySet">ERuleAlreadySet</a>);
    df::add(&<b>mut</b> policy.id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_RuleKey">RuleKey</a>&lt;Rule&gt; {}, cfg);
    policy.<a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>.insert(type_name::with_defining_ids&lt;Rule&gt;())
}
</code></pre>

Function <code>get_rule</code>

Get the custom Config for the Rule (can be only one per "Rule" type).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_get_rule">get_rule</a>&lt;T, Rule: drop, Config: drop, store&gt;(_: Rule, policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;): &Config
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_get_rule">get_rule</a>&lt;T, Rule: drop, Config: store + drop&gt;(
    _: Rule,
    policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
): &Config {
    df::borrow(&policy.id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_RuleKey">RuleKey</a>&lt;Rule&gt; {})
}
</code></pre>

Function <code>add_to_balance</code>

Add some SUI to the balance of a <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_to_balance">add_to_balance</a>&lt;T, Rule: drop&gt;(_: Rule, policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;<a href="../sui_sui/sui#sui_sui_SUI">sui::sui::SUI</a>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_to_balance">add_to_balance</a>&lt;T, Rule: drop&gt;(_: Rule, policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;, <a href="../sui_sui/coin#sui_coin">coin</a>: Coin&lt;SUI&gt;) {
    <b>assert</b>!(<a href="../sui_sui/transfer_policy#sui_transfer_policy_has_rule">has_rule</a>&lt;T, Rule&gt;(policy), <a href="../sui_sui/transfer_policy#sui_transfer_policy_EUnknownRequirement">EUnknownRequirement</a>);
    <a href="../sui_sui/coin#sui_coin_put">coin::put</a>(&<b>mut</b> policy.<a href="../sui_sui/balance#sui_balance">balance</a>, <a href="../sui_sui/coin#sui_coin">coin</a>)
}
</code></pre>

Function <code>add_receipt</code>

Adds a Receipt to the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>, unblocking the request and
confirming that the policy requirements are satisfied.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_receipt">add_receipt</a>&lt;T, Rule: drop&gt;(_: Rule, request: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_add_receipt">add_receipt</a>&lt;T, Rule: drop&gt;(_: Rule, request: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt;) {
    request.receipts.insert(type_name::with_defining_ids&lt;Rule&gt;())
}
</code></pre>

Function <code>has_rule</code>

Check whether a custom rule has been added to the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_has_rule">has_rule</a>&lt;T, Rule: drop&gt;(policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_has_rule">has_rule</a>&lt;T, Rule: drop&gt;(policy: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;): bool {
    df::exists_(&policy.id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_RuleKey">RuleKey</a>&lt;Rule&gt; {})
}
</code></pre>

Function <code>remove_rule</code>

Remove the Rule from the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_remove_rule">remove_rule</a>&lt;T, Rule: drop, Config: drop, store&gt;(policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_remove_rule">remove_rule</a>&lt;T, Rule: drop, Config: store + drop&gt;(
    policy: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(policy) == cap.policy_id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>);
    <b>let</b> _: Config = df::remove(&<b>mut</b> policy.id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_RuleKey">RuleKey</a>&lt;Rule&gt; {});
    policy.<a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>.remove(&type_name::with_defining_ids&lt;Rule&gt;());
}
</code></pre>

Function <code>uid</code>

Allows reading custom attachments to the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a> if there are any.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_uid">uid</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;): &<a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_uid">uid</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;): &UID { &self.id }
</code></pre>

Function <code>uid_mut_as_owner</code>

Get a mutable reference to the self.id to enable custom attachments
to the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_uid_mut_as_owner">uid_mut_as_owner</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">sui::transfer_policy::TransferPolicyCap</a>&lt;T&gt;): &<b>mut</b> <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_uid_mut_as_owner">uid_mut_as_owner</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicyCap">TransferPolicyCap</a>&lt;T&gt;): &<b>mut</b> UID {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.policy_id, <a href="../sui_sui/transfer_policy#sui_transfer_policy_ENotOwner">ENotOwner</a>);
    &<b>mut</b> self.id
}
</code></pre>

Function <code>rules</code>

Read the <a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a> field from the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">sui::transfer_policy::TransferPolicy</a>&lt;T&gt;): &<a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferPolicy">TransferPolicy</a>&lt;T&gt;): &VecSet&lt;TypeName&gt; {
    &self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_rules">rules</a>
}
</code></pre>

Function <code>item</code>

Get the <a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a> field of the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt;): ID { self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_item">item</a> }
</code></pre>

Function <code>paid</code>

Get the <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a> field of the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt;): u64 { self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_paid">paid</a> }
</code></pre>

Function <code>from</code>

Get the <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a> field of the <a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">sui::transfer_policy::TransferRequest</a>&lt;T&gt;): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a>&lt;T&gt;(self: &<a href="../sui_sui/transfer_policy#sui_transfer_policy_TransferRequest">TransferRequest</a>&lt;T&gt;): ID { self.<a href="../sui_sui/transfer_policy#sui_transfer_policy_from">from</a> }
</code></pre>