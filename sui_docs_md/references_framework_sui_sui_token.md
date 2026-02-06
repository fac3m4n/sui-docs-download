The Token module which implements a Closed Loop Token with a configurable
policy. The policy is defined by a set of rules that must be satisfied for
an action to be performed on the token.

The module is designed to be used with a TreasuryCap to allow for minting
and burning of the <a href="../sui_sui/token#sui_token_Token">Token</a>s. And can act as a replacement / extension or a
companion to existing open-loop (Coin) systems.

```
Module:      sui::balance       sui::coin             sui::token
Main type:   Balance<T>         Coin<T>               Token<T>
Capability:  Supply<T>  <---->  TreasuryCap<T> <----> TreasuryCap<T>
Abilities:   store              key + store           key
```

The Token system allows for fine-grained control over the actions performed
on the token. And hence it is highly suitable for applications that require
control over the currency which a simple open-loop system can't provide.

-  [Struct Token](#sui_token_Token)
-  [Struct TokenPolicyCap](#sui_token_TokenPolicyCap)
-  [Struct TokenPolicy](#sui_token_TokenPolicy)
-  [Struct ActionRequest](#sui_token_ActionRequest)
-  [Struct RuleKey](#sui_token_RuleKey)
-  [Struct TokenPolicyCreated](#sui_token_TokenPolicyCreated)
-  [Constants](#@Constants_0)
-  [Function new_policy](#sui_token_new_policy)
-  [Function share_policy](#sui_token_share_policy)
-  [Function transfer](#sui_token_transfer)
-  [Function spend](#sui_token_spend)
-  [Function to_coin](#sui_token_to_coin)
-  [Function from_coin](#sui_token_from_coin)
-  [Function join](#sui_token_join)
-  [Function split](#sui_token_split)
-  [Function zero](#sui_token_zero)
-  [Function destroy_zero](#sui_token_destroy_zero)
-  [Function keep](#sui_token_keep)
-  [Function new_request](#sui_token_new_request)
-  [Function confirm_request](#sui_token_confirm_request)
-  [Function confirm_request_mut](#sui_token_confirm_request_mut)
-  [Function confirm_with_policy_cap](#sui_token_confirm_with_policy_cap)
-  [Function confirm_with_treasury_cap](#sui_token_confirm_with_treasury_cap)
-  [Function add_approval](#sui_token_add_approval)
-  [Function add_rule_config](#sui_token_add_rule_config)
-  [Function rule_config](#sui_token_rule_config)
-  [Function rule_config_mut](#sui_token_rule_config_mut)
-  [Function remove_rule_config](#sui_token_remove_rule_config)
-  [Function has_rule_config](#sui_token_has_rule_config)
-  [Function has_rule_config_with_type](#sui_token_has_rule_config_with_type)
-  [Function allow](#sui_token_allow)
-  [Function disallow](#sui_token_disallow)
-  [Function add_rule_for_action](#sui_token_add_rule_for_action)
-  [Function remove_rule_for_action](#sui_token_remove_rule_for_action)
-  [Function mint](#sui_token_mint)
-  [Function burn](#sui_token_burn)
-  [Function flush](#sui_token_flush)
-  [Function is_allowed](#sui_token_is_allowed)
-  [Function rules](#sui_token_rules)
-  [Function spent_balance](#sui_token_spent_balance)
-  [Function value](#sui_token_value)
-  [Function transfer_action](#sui_token_transfer_action)
-  [Function spend_action](#sui_token_spend_action)
-  [Function to_coin_action](#sui_token_to_coin_action)
-  [Function from_coin_action](#sui_token_from_coin_action)
-  [Function action](#sui_token_action)
-  [Function amount](#sui_token_amount)
-  [Function sender](#sui_token_sender)
-  [Function recipient](#sui_token_recipient)
-  [Function approvals](#sui_token_approvals)
-  [Function spent](#sui_token_spent)
-  [Function key](#sui_token_key)

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
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/protocol_config#sui_protocol_config">sui::protocol_config</a>;
<b>use</b> <a href="../sui_sui/table#sui_table">sui::table</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/url#sui_url">sui::url</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
<b>use</b> <a href="../sui_sui/vec_set#sui_vec_set">sui::vec_set</a>;
</code>

Struct <code>Token</code>

A single <a href="../sui_sui/token#sui_token_Token">Token</a> with Balance inside. Can only be owned by an address,
and actions performed on it must be confirmed in a matching <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;<b>phantom</b> T&gt; <b>has</b> <a href="../sui_sui/token#sui_token_key">key</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;</code>
</dt>
<dd>
 The Balance of the <code><a href="../sui_sui/token#sui_token_Token">Token</a></code>.
</dd>
</dl>

Struct <code>TokenPolicyCap</code>

A Capability that manages a single <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> specified in the <b>for</b>
field. Created together with <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> in the new function.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;<b>phantom</b> T&gt; <b>has</b> <a href="../sui_sui/token#sui_token_key">key</a>, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><b>for</b>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenPolicy</code>

<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> represents a set of rules that define what actions can be
performed on a <a href="../sui_sui/token#sui_token_Token">Token</a> and which Rules must be satisfied for the
action to succeed.

- For the sake of availability, <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> is a <a href="../sui_sui/token#sui_token_key">key</a>-only object.
- Each <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> is managed by a matching <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>.
- For an action to become available, there needs to be a record in the
<a href="../sui_sui/token#sui_token_rules">rules</a> VecMap. To allow an action to be performed freely, there's an
<a href="../sui_sui/token#sui_token_allow">allow</a> function that can be called by the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> owner.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;<b>phantom</b> T&gt; <b>has</b> <a href="../sui_sui/token#sui_token_key">key</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>: <a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;</code>
</dt>
<dd>
 The balance that is effectively spent by the user on the "spend"
 action. However, actual decrease of the supply can only be done by
 the <code>TreasuryCap</code> owner when <code><a href="../sui_sui/token#sui_token_flush">flush</a></code> is called.
 This balance is effectively spent and cannot be accessed by anyone
 but the <code>TreasuryCap</code> owner.
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_rules">rules</a>: <a href="../sui_sui/vec_map#sui_vec_map_VecMap">sui::vec_map::VecMap</a>&lt;<a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;&gt;</code>
</dt>
<dd>
 The set of rules that define what actions can be performed on the
 token. For each "action" there's a set of Rules that must be
 satisfied for the <code><a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a></code> to be confirmed.
</dd>
</dl>

Struct <code>ActionRequest</code>

A request to perform an "Action" on a token. Stores the information
about the action to be performed and must be consumed by the <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a>
or <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a> functions when the Rules are satisfied.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;<b>phantom</b> T&gt;
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>name: <a href="../sui_std/string#std_string_String">std::string::String</a></code>
</dt>
<dd>
 Name of the Action to look up in the Policy. Name can be one of the
 default actions: <code><a href="../sui_sui/transfer#sui_transfer">transfer</a></code>, <code><a href="../sui_sui/token#sui_token_spend">spend</a></code>, <code><a href="../sui_sui/token#sui_token_to_coin">to_coin</a></code>, <code><a href="../sui_sui/token#sui_token_from_coin">from_coin</a></code> or a
 custom action.
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_amount">amount</a>: u64</code>
</dt>
<dd>
 Amount is present in all of the txs
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_sender">sender</a>: <b>address</b></code>
</dt>
<dd>
 Sender is a permanent field always
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_recipient">recipient</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;</code>
</dt>
<dd>
 Recipient is only available in <code><a href="../sui_sui/transfer#sui_transfer">transfer</a></code> action.
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;&gt;</code>
</dt>
<dd>
 The balance to be "spent" in the <code><a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a></code>, only available
 in the <code><a href="../sui_sui/token#sui_token_spend">spend</a></code> action.
</dd>
<dt>
<code><a href="../sui_sui/token#sui_token_approvals">approvals</a>: <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;</code>
</dt>
<dd>
 Collected approvals (stamps) from completed <code>Rules</code>. They're matched
 against <code><a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.<a href="../sui_sui/token#sui_token_rules">rules</a></code> to determine if the request can be
 confirmed.
</dd>
</dl>

Struct <code>RuleKey</code>

Dynamic field key for the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> to store the Config for a
specific action Rule. There can be only one configuration per
Rule per <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>is_protected: bool</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>TokenPolicyCreated</code>

An event emitted when a <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> is created and shared. Because
<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> can only be shared (and potentially frozen in the future),
we emit this event in the <a href="../sui_sui/token#sui_token_share_policy">share_policy</a> function and mark it as mutable.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/token#sui_token_TokenPolicyCreated">TokenPolicyCreated</a>&lt;<b>phantom</b> T&gt; <b>has</b> <b>copy</b>, drop
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 ID of the <code><a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a></code> that was created.
</dd>
<dt>
<code>is_mutable: bool</code>
</dt>
<dd>
 Whether the <code><a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a></code> is "shared" (mutable) or "frozen"
 (immutable) - TBD.
</dd>
</dl>

Constants

The action is not allowed (defined) in the policy.

<code><b>const</b> <a href="../sui_sui/token#sui_token_EUnknownAction">EUnknownAction</a>: u64 = 0;
</code>

The rule was not approved.

<code><b>const</b> <a href="../sui_sui/token#sui_token_ENotApproved">ENotApproved</a>: u64 = 1;
</code>

Trying to perform an admin action with a wrong cap.

<code><b>const</b> <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>: u64 = 2;
</code>

The balance is too low to perform the action.

<code><b>const</b> <a href="../sui_sui/token#sui_token_EBalanceTooLow">EBalanceTooLow</a>: u64 = 3;
</code>

The balance is not zero.

<code><b>const</b> <a href="../sui_sui/token#sui_token_ENotZero">ENotZero</a>: u64 = 4;
</code>

The balance is not zero when trying to confirm with TransferPolicyCap.

<code><b>const</b> <a href="../sui_sui/token#sui_token_ECantConsumeBalance">ECantConsumeBalance</a>: u64 = 5;
</code>

Rule is trying to access a missing config (with type).

<code><b>const</b> <a href="../sui_sui/token#sui_token_ENoConfig">ENoConfig</a>: u64 = 6;
</code>

Using <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a> without <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>. Immutable version
of the function must be used instead.

<code><b>const</b> <a href="../sui_sui/token#sui_token_EUseImmutableConfirm">EUseImmutableConfirm</a>: u64 = 7;
</code>

A Tag for the <a href="../sui_sui/token#sui_token_spend">spend</a> action.

<code><b>const</b> <a href="../sui_sui/token#sui_token_SPEND">SPEND</a>: vector&lt;u8&gt; = vector[115, 112, 101, 110, 100];
</code>

A Tag for the <a href="../sui_sui/transfer#sui_transfer">transfer</a> action.

<code><b>const</b> <a href="../sui_sui/token#sui_token_TRANSFER">TRANSFER</a>: vector&lt;u8&gt; = vector[116, 114, 97, 110, 115, 102, 101, 114];
</code>

A Tag for the <a href="../sui_sui/token#sui_token_to_coin">to_coin</a> action.

<code><b>const</b> <a href="../sui_sui/token#sui_token_TO_COIN">TO_COIN</a>: vector&lt;u8&gt; = vector[116, 111, 95, 99, 111, 105, 110];
</code>

A Tag for the <a href="../sui_sui/token#sui_token_from_coin">from_coin</a> action.

<code><b>const</b> <a href="../sui_sui/token#sui_token_FROM_COIN">FROM_COIN</a>: vector&lt;u8&gt; = vector[102, 114, 111, 109, 95, 99, 111, 105, 110];
</code>

Function <code>new_policy</code>

Create a new <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> and a matching <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>.
The <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> must then be shared using the <a href="../sui_sui/token#sui_token_share_policy">share_policy</a> method.

TreasuryCap guarantees full ownership over the currency, and is unique,
hence it is safe to use it for authorization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_new_policy">new_policy</a>&lt;T&gt;(_treasury_cap: &<a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_new_policy">new_policy</a>&lt;T&gt;(
    _treasury_cap: &TreasuryCap&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
): (<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;) {
    <b>let</b> policy = <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>: <a href="../sui_sui/balance#sui_balance_zero">balance::zero</a>(),
        <a href="../sui_sui/token#sui_token_rules">rules</a>: <a href="../sui_sui/vec_map#sui_vec_map_empty">vec_map::empty</a>(),
    };
    <b>let</b> cap = <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <span className="code-inline"><b>for</b></span>: <a href="../sui_sui/object#sui_object_id">object::id</a>(&policy),
    };
    (policy, cap)
}
</code></pre>

Function <code>share_policy</code>

Share the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>. Due to <a href="../sui_sui/token#sui_token_key">key</a>-only restriction, it must be
shared after initialization.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_share_policy">share_policy</a>&lt;T&gt;(policy: <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_share_policy">share_policy</a>&lt;T&gt;(policy: <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;) {
    <a href="../sui_sui/event#sui_event_emit">event::emit</a>(<a href="../sui_sui/token#sui_token_TokenPolicyCreated">TokenPolicyCreated</a>&lt;T&gt; {
        id: <a href="../sui_sui/object#sui_object_id">object::id</a>(&policy),
        is_mutable: <b>true</b>,
    });
    <a href="../sui_sui/transfer#sui_transfer_share_object">transfer::share_object</a>(policy)
}
</code></pre>

Function <code>transfer</code>

Transfer a <a href="../sui_sui/token#sui_token_Token">Token</a> to a <a href="../sui_sui/token#sui_token_recipient">recipient</a>. Creates an <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> for the
"transfer" action. The <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> contains the <a href="../sui_sui/token#sui_token_recipient">recipient</a> field
to be used in verification.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_recipient">recipient</a>: <b>address</b>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/transfer#sui_transfer">transfer</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_recipient">recipient</a>: <b>address</b>, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/token#sui_token_amount">amount</a> = t.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>();
    <a href="../sui_sui/transfer#sui_transfer_transfer">transfer::transfer</a>(t, <a href="../sui_sui/token#sui_token_recipient">recipient</a>);
    <a href="../sui_sui/token#sui_token_new_request">new_request</a>(
        <a href="../sui_sui/token#sui_token_transfer_action">transfer_action</a>(),
        <a href="../sui_sui/token#sui_token_amount">amount</a>,
        option::some(<a href="../sui_sui/token#sui_token_recipient">recipient</a>),
        option::none(),
        ctx,
    )
}
</code></pre>

Function <code>spend</code>

Spend a <a href="../sui_sui/token#sui_token_Token">Token</a> by unwrapping it and storing the Balance in the
<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> for the "spend" action. The <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> contains
the <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a> field to be used in verification.

Spend action requires <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a> to be called to confirm the
request and join the spent balance with the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spend">spend</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spend">spend</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/token#sui_token_Token">Token</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = t;
    id.delete();
    <a href="../sui_sui/token#sui_token_new_request">new_request</a>(
        <a href="../sui_sui/token#sui_token_spend_action">spend_action</a>(),
        <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>(),
        option::none(),
        option::some(<a href="../sui_sui/balance#sui_balance">balance</a>),
        ctx,
    )
}
</code></pre>

Function <code>to_coin</code>

Convert <a href="../sui_sui/token#sui_token_Token">Token</a> into an open Coin. Creates an <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> for the
"to_coin" action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_to_coin">to_coin</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_to_coin">to_coin</a>&lt;T&gt;(t: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, ctx: &<b>mut</b> TxContext): (Coin&lt;T&gt;, <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_Token">Token</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = t;
    <b>let</b> <a href="../sui_sui/token#sui_token_amount">amount</a> = <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>();
    id.delete();
    (
        <a href="../sui_sui/balance#sui_balance">balance</a>.into_coin(ctx),
        <a href="../sui_sui/token#sui_token_new_request">new_request</a>(
            <a href="../sui_sui/token#sui_token_to_coin_action">to_coin_action</a>(),
            <a href="../sui_sui/token#sui_token_amount">amount</a>,
            option::none(),
            option::none(),
            ctx,
        ),
    )
}
</code></pre>

Function <code>from_coin</code>

Convert an open Coin into a <a href="../sui_sui/token#sui_token_Token">Token</a>. Creates an <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> for
the "from_coin" action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_from_coin">from_coin</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: <a href="../sui_sui/coin#sui_coin_Coin">sui::coin::Coin</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_from_coin">from_coin</a>&lt;T&gt;(<a href="../sui_sui/coin#sui_coin">coin</a>: Coin&lt;T&gt;, ctx: &<b>mut</b> TxContext): (<a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_amount">amount</a> = <a href="../sui_sui/coin#sui_coin">coin</a>.<a href="../sui_sui/token#sui_token_value">value</a>();
    <b>let</b> <a href="../sui_sui/token#sui_token">token</a> = <a href="../sui_sui/token#sui_token_Token">Token</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/coin#sui_coin">coin</a>.into_balance(),
    };
    (
        <a href="../sui_sui/token#sui_token">token</a>,
        <a href="../sui_sui/token#sui_token_new_request">new_request</a>(
            <a href="../sui_sui/token#sui_token_from_coin_action">from_coin_action</a>(),
            <a href="../sui_sui/token#sui_token_amount">amount</a>,
            option::none(),
            option::none(),
            ctx,
        ),
    )
}
</code></pre>

Function <code>join</code>

Join two <a href="../sui_sui/token#sui_token_Token">Token</a>s into one, always available.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_join">join</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: &<b>mut</b> <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, another: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_join">join</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: &<b>mut</b> <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, another: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_Token">Token</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = another;
    <a href="../sui_sui/token#sui_token">token</a>.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_join">join</a>(<a href="../sui_sui/balance#sui_balance">balance</a>);
    id.delete();
}
</code></pre>

Function <code>split</code>

Split a <a href="../sui_sui/token#sui_token_Token">Token</a> with <a href="../sui_sui/token#sui_token_amount">amount</a>.
Aborts if the <a href="../sui_sui/token#sui_token_Token">Token</a>.<a href="../sui_sui/balance#sui_balance">balance</a> is lower than <a href="../sui_sui/token#sui_token_amount">amount</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_split">split</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: &<b>mut</b> <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_amount">amount</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_split">split</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: &<b>mut</b> <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_amount">amount</a>: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt; {
    <b>assert</b>!(<a href="../sui_sui/token#sui_token">token</a>.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>() &gt;= <a href="../sui_sui/token#sui_token_amount">amount</a>, <a href="../sui_sui/token#sui_token_EBalanceTooLow">EBalanceTooLow</a>);
    <a href="../sui_sui/token#sui_token_Token">Token</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/token#sui_token">token</a>.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_split">split</a>(<a href="../sui_sui/token#sui_token_amount">amount</a>),
    }
}
</code></pre>

Function <code>zero</code>

Create a zero <a href="../sui_sui/token#sui_token_Token">Token</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_zero">zero</a>&lt;T&gt;(ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_zero">zero</a>&lt;T&gt;(ctx: &<b>mut</b> TxContext): <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt; {
    <a href="../sui_sui/token#sui_token_Token">Token</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/balance#sui_balance">balance</a>: <a href="../sui_sui/balance#sui_balance_zero">balance::zero</a>(),
    }
}
</code></pre>

Function <code>destroy_zero</code>

Destroy an empty <a href="../sui_sui/token#sui_token_Token">Token</a>, fails if the balance is non-zero.
Aborts if the <a href="../sui_sui/token#sui_token_Token">Token</a>.<a href="../sui_sui/balance#sui_balance">balance</a> is not zero.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_destroy_zero">destroy_zero</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_destroy_zero">destroy_zero</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_Token">Token</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = <a href="../sui_sui/token#sui_token">token</a>;
    <b>assert</b>!(<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>() == 0, <a href="../sui_sui/token#sui_token_ENotZero">ENotZero</a>);
    <a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_destroy_zero">destroy_zero</a>();
    id.delete();
}
</code></pre>

Function <code>keep</code>

Transfer the <a href="../sui_sui/token#sui_token_Token">Token</a> to the transaction sender.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_keep">keep</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_keep">keep</a>&lt;T&gt;(<a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;, ctx: &<b>mut</b> TxContext) {
    <a href="../sui_sui/transfer#sui_transfer_transfer">transfer::transfer</a>(<a href="../sui_sui/token#sui_token">token</a>, ctx.<a href="../sui_sui/token#sui_token_sender">sender</a>())
}
</code></pre>

Function <code>new_request</code>

Create a new <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.
Publicly available method to allow for custom actions.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_new_request">new_request</a>&lt;T&gt;(name: <a href="../sui_std/string#std_string_String">std::string::String</a>, <a href="../sui_sui/token#sui_token_amount">amount</a>: u64, <a href="../sui_sui/token#sui_token_recipient">recipient</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;, <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>: <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<a href="../sui_sui/balance#sui_balance_Balance">sui::balance::Balance</a>&lt;T&gt;&gt;, ctx: &<a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_new_request">new_request</a>&lt;T&gt;(
    name: String,
    <a href="../sui_sui/token#sui_token_amount">amount</a>: u64,
    <a href="../sui_sui/token#sui_token_recipient">recipient</a>: Option&lt;<b>address</b>&gt;,
    <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>: Option&lt;Balance&lt;T&gt;&gt;,
    ctx: &TxContext,
): <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt; {
    <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> {
        name,
        <a href="../sui_sui/token#sui_token_amount">amount</a>,
        <a href="../sui_sui/token#sui_token_recipient">recipient</a>,
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>,
        <a href="../sui_sui/token#sui_token_sender">sender</a>: ctx.<a href="../sui_sui/token#sui_token_sender">sender</a>(),
        <a href="../sui_sui/token#sui_token_approvals">approvals</a>: <a href="../sui_sui/vec_set#sui_vec_set_empty">vec_set::empty</a>(),
    }
}
</code></pre>

Function <code>confirm_request</code>

Confirm the request against the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> and return the parameters
of the request: (Name, Amount, Sender, Recipient).

Cannot be used for <a href="../sui_sui/token#sui_token_spend">spend</a> and similar actions that deliver <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>
to the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>. For those actions use <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a>.

Aborts if:
- the action is not allowed (missing record in <a href="../sui_sui/token#sui_token_rules">rules</a>)
- action contains <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a> (use <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a>)
- the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> does not meet the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> rules for the action

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a>&lt;T&gt;(policy: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, request: <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_std/string#std_string_String">std::string::String</a>, u64, <b>address</b>, <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a>&lt;T&gt;(
    policy: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    request: <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
): (String, u64, <b>address</b>, Option&lt;<b>address</b>&gt;) {
    <b>assert</b>!(request.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.is_none(), <a href="../sui_sui/token#sui_token_ECantConsumeBalance">ECantConsumeBalance</a>);
    <b>assert</b>!(policy.<a href="../sui_sui/token#sui_token_rules">rules</a>.contains(&request.name), <a href="../sui_sui/token#sui_token_EUnknownAction">EUnknownAction</a>);
    <b>let</b> <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> {
        name,
        <a href="../sui_sui/token#sui_token_approvals">approvals</a>,
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>,
        <a href="../sui_sui/token#sui_token_amount">amount</a>,
        <a href="../sui_sui/token#sui_token_sender">sender</a>,
        <a href="../sui_sui/token#sui_token_recipient">recipient</a>,
    } = request;
    <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.destroy_none();
    <b>let</b> <a href="../sui_sui/token#sui_token_rules">rules</a> = &(*policy.<a href="../sui_sui/token#sui_token_rules">rules</a>.get(&name)).into_keys();
    <b>let</b> rules_len = <a href="../sui_sui/token#sui_token_rules">rules</a>.length();
    <b>let</b> <b>mut</b> i = 0;
    <b>while</b> (i &lt; rules_len) {
        <b>let</b> rule = &<a href="../sui_sui/token#sui_token_rules">rules</a>[i];
        <b>assert</b>!(<a href="../sui_sui/token#sui_token_approvals">approvals</a>.contains(rule), <a href="../sui_sui/token#sui_token_ENotApproved">ENotApproved</a>);
        i = i + 1;
    };
    (name, <a href="../sui_sui/token#sui_token_amount">amount</a>, <a href="../sui_sui/token#sui_token_sender">sender</a>, <a href="../sui_sui/token#sui_token_recipient">recipient</a>)
}
</code></pre>

Function <code>confirm_request_mut</code>

Confirm the request against the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> and return the parameters
of the request: (Name, Amount, Sender, Recipient).

Unlike <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a> this function requires mutable access to the
<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> and must be used on <a href="../sui_sui/token#sui_token_spend">spend</a> action. After dealing with the
spent balance it calls <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a> internally.

See <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a> for the list of abort conditions.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a>&lt;T&gt;(policy: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, request: <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_std/string#std_string_String">std::string::String</a>, u64, <b>address</b>, <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_request_mut">confirm_request_mut</a>&lt;T&gt;(
    policy: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    <b>mut</b> request: <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;,
    ctx: &<b>mut</b> TxContext,
): (String, u64, <b>address</b>, Option&lt;<b>address</b>&gt;) {
    <b>assert</b>!(policy.<a href="../sui_sui/token#sui_token_rules">rules</a>.contains(&request.name), <a href="../sui_sui/token#sui_token_EUnknownAction">EUnknownAction</a>);
    <b>assert</b>!(request.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.is_some(), <a href="../sui_sui/token#sui_token_EUseImmutableConfirm">EUseImmutableConfirm</a>);
    policy.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.<a href="../sui_sui/token#sui_token_join">join</a>(request.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.extract());
    <a href="../sui_sui/token#sui_token_confirm_request">confirm_request</a>(policy, request, ctx)
}
</code></pre>

Function <code>confirm_with_policy_cap</code>

Confirm an <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> as the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> owner. This function
allows <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> owner to perform Capability-gated actions ignoring
the ruleset specified in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

Aborts if request contains <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a> due to inability of the
<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> to decrease supply. For scenarios like this a
TreasuryCap is required (see <a href="../sui_sui/token#sui_token_confirm_with_treasury_cap">confirm_with_treasury_cap</a>).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_with_policy_cap">confirm_with_policy_cap</a>&lt;T&gt;(_policy_cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, request: <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_std/string#std_string_String">std::string::String</a>, u64, <b>address</b>, <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_with_policy_cap">confirm_with_policy_cap</a>&lt;T&gt;(
    _policy_cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    request: <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
): (String, u64, <b>address</b>, Option&lt;<b>address</b>&gt;) {
    <b>assert</b>!(request.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.is_none(), <a href="../sui_sui/token#sui_token_ECantConsumeBalance">ECantConsumeBalance</a>);
    <b>let</b> <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> {
        name,
        <a href="../sui_sui/token#sui_token_amount">amount</a>,
        <a href="../sui_sui/token#sui_token_sender">sender</a>,
        <a href="../sui_sui/token#sui_token_recipient">recipient</a>,
        <a href="../sui_sui/token#sui_token_approvals">approvals</a>: _,
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>,
    } = request;
    <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.destroy_none();
    (name, <a href="../sui_sui/token#sui_token_amount">amount</a>, <a href="../sui_sui/token#sui_token_sender">sender</a>, <a href="../sui_sui/token#sui_token_recipient">recipient</a>)
}
</code></pre>

Function <code>confirm_with_treasury_cap</code>

Confirm an <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> as the TreasuryCap owner. This function
allows TreasuryCap owner to perform Capability-gated actions ignoring
the ruleset specified in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

Unlike <a href="../sui_sui/token#sui_token_confirm_with_policy_cap">confirm_with_policy_cap</a> this function allows <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>
to be consumed, decreasing the total_supply of the <a href="../sui_sui/token#sui_token_Token">Token</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_with_treasury_cap">confirm_with_treasury_cap</a>&lt;T&gt;(treasury_cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, request: <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): (<a href="../sui_std/string#std_string_String">std::string::String</a>, u64, <b>address</b>, <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_confirm_with_treasury_cap">confirm_with_treasury_cap</a>&lt;T&gt;(
    treasury_cap: &<b>mut</b> TreasuryCap&lt;T&gt;,
    request: <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
): (String, u64, <b>address</b>, Option&lt;<b>address</b>&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> {
        name,
        <a href="../sui_sui/token#sui_token_amount">amount</a>,
        <a href="../sui_sui/token#sui_token_sender">sender</a>,
        <a href="../sui_sui/token#sui_token_recipient">recipient</a>,
        <a href="../sui_sui/token#sui_token_approvals">approvals</a>: _,
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>,
    } = request;
    <b>if</b> (<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.is_some()) {
        treasury_cap.supply_mut().decrease_supply(<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.destroy_some());
    } <b>else</b> {
        <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.destroy_none();
    };
    (name, <a href="../sui_sui/token#sui_token_amount">amount</a>, <a href="../sui_sui/token#sui_token_sender">sender</a>, <a href="../sui_sui/token#sui_token_recipient">recipient</a>)
}
</code></pre>

Function <code>add_approval</code>

Add an "approval" to the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a> by providing a Witness.
Intended to be used by Rules to add their own approvals, however, can
be used to add arbitrary approvals to the request (not only the ones
required by the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_approval">add_approval</a>&lt;T, W: drop&gt;(_t: W, request: &<b>mut</b> <a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_approval">add_approval</a>&lt;T, W: drop&gt;(_t: W, request: &<b>mut</b> <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;, _ctx: &<b>mut</b> TxContext) {
    request.<a href="../sui_sui/token#sui_token_approvals">approvals</a>.insert(type_name::with_defining_ids&lt;W&gt;())
}
</code></pre>

Function <code>add_rule_config</code>

Add a Config for a Rule in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>. Rule configuration is
independent from the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.<a href="../sui_sui/token#sui_token_rules">rules</a> and needs to be managed by the
Rule itself. Configuration is stored per Rule and not per Rule per
Action to allow reuse in different actions.

- Rule witness guarantees that the Config is approved by the Rule.
- <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> guarantees that the Config setup is initiated by
the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> owner.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_rule_config">add_rule_config</a>&lt;T, Rule: drop, Config: store&gt;(_rule: Rule, self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, <a href="../sui_sui/config#sui_config">config</a>: Config, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_rule_config">add_rule_config</a>&lt;T, Rule: drop, Config: store&gt;(
    _rule: Rule,
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    <a href="../sui_sui/config#sui_config">config</a>: Config,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    df::add(&<b>mut</b> self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;(), <a href="../sui_sui/config#sui_config">config</a>)
}
</code></pre>

Function <code>rule_config</code>

Get a Config for a Rule in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>. Requires Rule
witness, hence can only be read by the Rule itself. This requirement
guarantees safety of the stored Config and allows for simpler dynamic
field management inside the Rule Config (custom type keys are not needed
for access gating).

Aborts if the Config is not present.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rule_config">rule_config</a>&lt;T, Rule: drop, Config: store&gt;(_rule: Rule, self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;): &Config
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rule_config">rule_config</a>&lt;T, Rule: drop, Config: store&gt;(_rule: Rule, self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;): &Config {
    <b>assert</b>!(<a href="../sui_sui/token#sui_token_has_rule_config_with_type">has_rule_config_with_type</a>&lt;T, Rule, Config&gt;(self), <a href="../sui_sui/token#sui_token_ENoConfig">ENoConfig</a>);
    df::borrow(&self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;())
}
</code></pre>

Function <code>rule_config_mut</code>

Get mutable access to the Config for a Rule in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.
Requires Rule witness, hence can only be read by the Rule itself,
as well as <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> to guarantee that the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> owner
is the one who initiated the Config modification.

Aborts if:
- the Config is not present
- <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rule_config_mut">rule_config_mut</a>&lt;T, Rule: drop, Config: store&gt;(_rule: Rule, self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;): &<b>mut</b> Config
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rule_config_mut">rule_config_mut</a>&lt;T, Rule: drop, Config: store&gt;(
    _rule: Rule,
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
): &<b>mut</b> Config {
    <b>assert</b>!(<a href="../sui_sui/token#sui_token_has_rule_config_with_type">has_rule_config_with_type</a>&lt;T, Rule, Config&gt;(self), <a href="../sui_sui/token#sui_token_ENoConfig">ENoConfig</a>);
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    df::borrow_mut(&<b>mut</b> self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;())
}
</code></pre>

Function <code>remove_rule_config</code>

Remove a Config for a Rule in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.
Unlike the <a href="../sui_sui/token#sui_token_add_rule_config">add_rule_config</a>, this function does not require a Rule
witness, hence can be performed by the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> owner on their own.

Rules need to make sure that the Config is present when performing
verification of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

Aborts if:
- the Config is not present
- <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_remove_rule_config">remove_rule_config</a>&lt;T, Rule, Config: store&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): Config
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_remove_rule_config">remove_rule_config</a>&lt;T, Rule, Config: store&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
): Config {
    <b>assert</b>!(<a href="../sui_sui/token#sui_token_has_rule_config_with_type">has_rule_config_with_type</a>&lt;T, Rule, Config&gt;(self), <a href="../sui_sui/token#sui_token_ENoConfig">ENoConfig</a>);
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    df::remove(&<b>mut</b> self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;())
}
</code></pre>

Function <code>has_rule_config</code>

Check if a config for a Rule is set in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> without
checking the type of the Config.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_has_rule_config">has_rule_config</a>&lt;T, Rule&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_has_rule_config">has_rule_config</a>&lt;T, Rule&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;): bool {
    df::exists_&lt;<a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a>&lt;Rule&gt;&gt;(&self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;())
}
</code></pre>

Function <code>has_rule_config_with_type</code>

Check if a Config for a Rule is set in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a> and that
it matches the type provided.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_has_rule_config_with_type">has_rule_config_with_type</a>&lt;T, Rule, Config: store&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_has_rule_config_with_type">has_rule_config_with_type</a>&lt;T, Rule, Config: store&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;): bool {
    df::exists_with_type&lt;<a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a>&lt;Rule&gt;, Config&gt;(&self.id, <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;())
}
</code></pre>

Function <code>allow</code>

Allows an <a href="../sui_sui/token#sui_token_action">action</a> to be performed on the <a href="../sui_sui/token#sui_token_Token">Token</a> freely by adding an
empty set of Rules for the <a href="../sui_sui/token#sui_token_action">action</a>.

Aborts if the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_allow">allow</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_allow">allow</a>&lt;T&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    <a href="../sui_sui/token#sui_token_action">action</a>: String,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    self.<a href="../sui_sui/token#sui_token_rules">rules</a>.insert(<a href="../sui_sui/token#sui_token_action">action</a>, <a href="../sui_sui/vec_set#sui_vec_set_empty">vec_set::empty</a>());
}
</code></pre>

Function <code>disallow</code>

Completely disallows an <a href="../sui_sui/token#sui_token_action">action</a> on the <a href="../sui_sui/token#sui_token_Token">Token</a> by removing the record
from the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.<a href="../sui_sui/token#sui_token_rules">rules</a>.

Aborts if the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_disallow">disallow</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_disallow">disallow</a>&lt;T&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    <a href="../sui_sui/token#sui_token_action">action</a>: String,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    self.<a href="../sui_sui/token#sui_token_rules">rules</a>.remove(&<a href="../sui_sui/token#sui_token_action">action</a>);
}
</code></pre>

Function <code>add_rule_for_action</code>

Adds a Rule for an action with name in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

Aborts if the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_rule_for_action">add_rule_for_action</a>&lt;T, Rule: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_add_rule_for_action">add_rule_for_action</a>&lt;T, Rule: drop&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    <a href="../sui_sui/token#sui_token_action">action</a>: String,
    ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    <b>if</b> (!self.<a href="../sui_sui/token#sui_token_rules">rules</a>.contains(&<a href="../sui_sui/token#sui_token_action">action</a>)) {
        <a href="../sui_sui/token#sui_token_allow">allow</a>(self, cap, <a href="../sui_sui/token#sui_token_action">action</a>, ctx);
    };
    self.<a href="../sui_sui/token#sui_token_rules">rules</a>.get_mut(&<a href="../sui_sui/token#sui_token_action">action</a>).insert(type_name::with_defining_ids&lt;Rule&gt;())
}
</code></pre>

Function <code>remove_rule_for_action</code>

Removes a rule for an action with name in the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>. Returns
the config object to be handled by the sender (or a Rule itself).

Aborts if the <a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a> is not matching the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_remove_rule_for_action">remove_rule_for_action</a>&lt;T, Rule: drop&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">sui::token::TokenPolicyCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: <a href="../sui_std/string#std_string_String">std::string::String</a>, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_remove_rule_for_action">remove_rule_for_action</a>&lt;T, Rule: drop&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<a href="../sui_sui/token#sui_token_TokenPolicyCap">TokenPolicyCap</a>&lt;T&gt;,
    <a href="../sui_sui/token#sui_token_action">action</a>: String,
    _ctx: &<b>mut</b> TxContext,
) {
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(self) == cap.<span className="code-inline"><b>for</b></span>, <a href="../sui_sui/token#sui_token_ENotAuthorized">ENotAuthorized</a>);
    self.<a href="../sui_sui/token#sui_token_rules">rules</a>.get_mut(&<a href="../sui_sui/token#sui_token_action">action</a>).remove(&type_name::with_defining_ids&lt;Rule&gt;())
}
</code></pre>

Function <code>mint</code>

Mint a <a href="../sui_sui/token#sui_token_Token">Token</a> with a given <a href="../sui_sui/token#sui_token_amount">amount</a> using the TreasuryCap.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_mint">mint</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_amount">amount</a>: u64, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_mint">mint</a>&lt;T&gt;(cap: &<b>mut</b> TreasuryCap&lt;T&gt;, <a href="../sui_sui/token#sui_token_amount">amount</a>: u64, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt; {
    <b>let</b> <a href="../sui_sui/balance#sui_balance">balance</a> = cap.supply_mut().increase_supply(<a href="../sui_sui/token#sui_token_amount">amount</a>);
    <a href="../sui_sui/token#sui_token_Token">Token</a> { id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx), <a href="../sui_sui/balance#sui_balance">balance</a> }
}
</code></pre>

Function <code>burn</code>

Burn a <a href="../sui_sui/token#sui_token_Token">Token</a> using the TreasuryCap.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_burn">burn</a>&lt;T&gt;(cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_burn">burn</a>&lt;T&gt;(cap: &<b>mut</b> TreasuryCap&lt;T&gt;, <a href="../sui_sui/token#sui_token">token</a>: <a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;) {
    <b>let</b> <a href="../sui_sui/token#sui_token_Token">Token</a> { id, <a href="../sui_sui/balance#sui_balance">balance</a> } = <a href="../sui_sui/token#sui_token">token</a>;
    cap.supply_mut().decrease_supply(<a href="../sui_sui/balance#sui_balance">balance</a>);
    id.delete();
}
</code></pre>

Function <code>flush</code>

Flush the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a> into the TreasuryCap. This
action is only available to the TreasuryCap owner.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_flush">flush</a>&lt;T&gt;(self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, cap: &<b>mut</b> <a href="../sui_sui/coin#sui_coin_TreasuryCap">sui::coin::TreasuryCap</a>&lt;T&gt;, _ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_flush">flush</a>&lt;T&gt;(
    self: &<b>mut</b> <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;,
    cap: &<b>mut</b> TreasuryCap&lt;T&gt;,
    _ctx: &<b>mut</b> TxContext,
): u64 {
    <b>let</b> <a href="../sui_sui/token#sui_token_amount">amount</a> = self.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>();
    <b>let</b> <a href="../sui_sui/balance#sui_balance">balance</a> = self.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.<a href="../sui_sui/token#sui_token_split">split</a>(<a href="../sui_sui/token#sui_token_amount">amount</a>);
    cap.supply_mut().decrease_supply(<a href="../sui_sui/balance#sui_balance">balance</a>)
}
</code></pre>

Function <code>is_allowed</code>

Check whether an action is present in the rules VecMap.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_is_allowed">is_allowed</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: &<a href="../sui_std/string#std_string_String">std::string::String</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_is_allowed">is_allowed</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: &String): bool {
    self.<a href="../sui_sui/token#sui_token_rules">rules</a>.contains(<a href="../sui_sui/token#sui_token_action">action</a>)
}
</code></pre>

Function <code>rules</code>

Returns the rules required for a specific action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rules">rules</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: &<a href="../sui_std/string#std_string_String">std::string::String</a>): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_rules">rules</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;, <a href="../sui_sui/token#sui_token_action">action</a>: &String): VecSet&lt;TypeName&gt; {
    *self.<a href="../sui_sui/token#sui_token_rules">rules</a>.get(<a href="../sui_sui/token#sui_token_action">action</a>)
}
</code></pre>

Function <code>spent_balance</code>

Returns the <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a> of the <a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">sui::token::TokenPolicy</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_TokenPolicy">TokenPolicy</a>&lt;T&gt;): u64 {
    self.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>()
}
</code></pre>

Function <code>value</code>

Returns the <a href="../sui_sui/balance#sui_balance">balance</a> of the <a href="../sui_sui/token#sui_token_Token">Token</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_value">value</a>&lt;T&gt;(t: &<a href="../sui_sui/token#sui_token_Token">sui::token::Token</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_value">value</a>&lt;T&gt;(t: &<a href="../sui_sui/token#sui_token_Token">Token</a>&lt;T&gt;): u64 {
    t.<a href="../sui_sui/balance#sui_balance">balance</a>.<a href="../sui_sui/token#sui_token_value">value</a>()
}
</code></pre>

Function <code>transfer_action</code>

Name of the Transfer action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_transfer_action">transfer_action</a>(): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_transfer_action">transfer_action</a>(): String {
    <b>let</b> transfer_str = <a href="../sui_sui/token#sui_token_TRANSFER">TRANSFER</a>;
    transfer_str.to_string()
}
</code></pre>

Function <code>spend_action</code>

Name of the Spend action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spend_action">spend_action</a>(): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spend_action">spend_action</a>(): String {
    <b>let</b> spend_str = <a href="../sui_sui/token#sui_token_SPEND">SPEND</a>;
    spend_str.to_string()
}
</code></pre>

Function <code>to_coin_action</code>

Name of the ToCoin action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_to_coin_action">to_coin_action</a>(): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_to_coin_action">to_coin_action</a>(): String {
    <b>let</b> to_coin_str = <a href="../sui_sui/token#sui_token_TO_COIN">TO_COIN</a>;
    to_coin_str.to_string()
}
</code></pre>

Function <code>from_coin_action</code>

Name of the FromCoin action.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_from_coin_action">from_coin_action</a>(): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_from_coin_action">from_coin_action</a>(): String {
    <b>let</b> from_coin_str = <a href="../sui_sui/token#sui_token_FROM_COIN">FROM_COIN</a>;
    from_coin_str.to_string()
}
</code></pre>

Function <code>action</code>

The Action in the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_action">action</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): <a href="../sui_std/string#std_string_String">std::string::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_action">action</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): String { self.name }
</code></pre>

Function <code>amount</code>

Amount of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_amount">amount</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_amount">amount</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): u64 { self.<a href="../sui_sui/token#sui_token_amount">amount</a> }
</code></pre>

Function <code>sender</code>

Sender of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_sender">sender</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): <b>address</b>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_sender">sender</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): <b>address</b> { self.<a href="../sui_sui/token#sui_token_sender">sender</a> }
</code></pre>

Function <code>recipient</code>

Recipient of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_recipient">recipient</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;<b>address</b>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_recipient">recipient</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): Option&lt;<b>address</b>&gt; {
    self.<a href="../sui_sui/token#sui_token_recipient">recipient</a>
}
</code></pre>

Function <code>approvals</code>

Approvals of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_approvals">approvals</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): <a href="../sui_sui/vec_set#sui_vec_set_VecSet">sui::vec_set::VecSet</a>&lt;<a href="../sui_std/type_name#std_type_name_TypeName">std::type_name::TypeName</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_approvals">approvals</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): VecSet&lt;TypeName&gt; {
    self.<a href="../sui_sui/token#sui_token_approvals">approvals</a>
}
</code></pre>

Function <code>spent</code>

Burned balance of the <a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spent">spent</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">sui::token::ActionRequest</a>&lt;T&gt;): <a href="../sui_std/option#std_option_Option">std::option::Option</a>&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/token#sui_token_spent">spent</a>&lt;T&gt;(self: &<a href="../sui_sui/token#sui_token_ActionRequest">ActionRequest</a>&lt;T&gt;): Option&lt;u64&gt; {
    <b>if</b> (self.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.is_some()) {
        option::some(self.<a href="../sui_sui/token#sui_token_spent_balance">spent_balance</a>.<a href="../sui_sui/borrow#sui_borrow">borrow</a>().<a href="../sui_sui/token#sui_token_value">value</a>())
    } <b>else</b> {
        option::none()
    }
}
</code></pre>

Function <code>key</code>

Create a new <a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a> for a Rule. The is_protected field is kept
for potential future use, if Rules were to have a freely modifiable
storage as addition / replacement for the Config system.

The goal of is_protected is to potentially allow Rules store a mutable
version of their configuration and mutate state on user action.

<code><b>fun</b> <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;(): <a href="../sui_sui/token#sui_token_RuleKey">sui::token::RuleKey</a>&lt;Rule&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/token#sui_token_key">key</a>&lt;Rule&gt;(): <a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a>&lt;Rule&gt; { <a href="../sui_sui/token#sui_token_RuleKey">RuleKey</a> { is_protected: <b>true</b> } }
</code></pre>