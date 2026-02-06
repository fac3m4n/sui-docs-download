Functions for operating on Move packages from within Move:
- Creating proof-of-publish objects from one-time witnesses
- Administering package upgrades through upgrade policies.

-  [Struct Publisher](#sui_package_Publisher)
-  [Struct UpgradeCap](#sui_package_UpgradeCap)
-  [Struct UpgradeTicket](#sui_package_UpgradeTicket)
-  [Struct UpgradeReceipt](#sui_package_UpgradeReceipt)
-  [Constants](#@Constants_0)
-  [Function claim](#sui_package_claim)
-  [Function claim_and_keep](#sui_package_claim_and_keep)
-  [Function burn_publisher](#sui_package_burn_publisher)
-  [Function from_package](#sui_package_from_package)
-  [Function from_module](#sui_package_from_module)
-  [Function published_module](#sui_package_published_module)
-  [Function published_package](#sui_package_published_package)
-  [Function upgrade_package](#sui_package_upgrade_package)
-  [Function version](#sui_package_version)
-  [Function upgrade_policy](#sui_package_upgrade_policy)
-  [Function ticket_package](#sui_package_ticket_package)
-  [Function ticket_policy](#sui_package_ticket_policy)
-  [Function receipt_cap](#sui_package_receipt_cap)
-  [Function receipt_package](#sui_package_receipt_package)
-  [Function ticket_digest](#sui_package_ticket_digest)
-  [Function compatible_policy](#sui_package_compatible_policy)
-  [Function additive_policy](#sui_package_additive_policy)
-  [Function dep_only_policy](#sui_package_dep_only_policy)
-  [Function only_additive_upgrades](#sui_package_only_additive_upgrades)
-  [Function only_dep_upgrades](#sui_package_only_dep_upgrades)
-  [Function make_immutable](#sui_package_make_immutable)
-  [Function authorize_upgrade](#sui_package_authorize_upgrade)
-  [Function commit_upgrade](#sui_package_commit_upgrade)
-  [Function restrict](#sui_package_restrict)

<code><b>use</b> <a href="../sui_std/address#std_address">std::address</a>;
<b>use</b> <a href="../sui_std/ascii#std_ascii">std::ascii</a>;
<b>use</b> <a href="../sui_std/bcs#std_bcs">std::bcs</a>;
<b>use</b> <a href="../sui_std/option#std_option">std::option</a>;
<b>use</b> <a href="../sui_std/string#std_string">std::string</a>;
<b>use</b> <a href="../sui_std/type_name#std_type_name">std::type_name</a>;
<b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
<b>use</b> <a href="../sui_sui/address#sui_address">sui::address</a>;
<b>use</b> <a href="../sui_sui/hex#sui_hex">sui::hex</a>;
<b>use</b> <a href="../sui_sui/object#sui_object">sui::object</a>;
<b>use</b> <a href="../sui_sui/party#sui_party">sui::party</a>;
<b>use</b> <a href="../sui_sui/transfer#sui_transfer">sui::transfer</a>;
<b>use</b> <a href="../sui_sui/tx_context#sui_tx_context">sui::tx_context</a>;
<b>use</b> <a href="../sui_sui/types#sui_types">sui::types</a>;
<b>use</b> <a href="../sui_sui/vec_map#sui_vec_map">sui::vec_map</a>;
</code>

Struct <code>Publisher</code>

This type can only be created in the transaction that
generates a module, by consuming its one-time witness, so it
can be used to identify the address that published the package
a type originated from.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/package#sui_package_Publisher">Publisher</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/package#sui_package">package</a>: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a></code>
</dt>
<dd>
</dd>
<dt>
<code>module_name: <a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a></code>
</dt>
<dd>
</dd>
</dl>

Struct <code>UpgradeCap</code>

Capability controlling the ability to upgrade a package.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> <b>has</b> key, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>id: <a href="../sui_sui/object#sui_object_UID">sui::object::UID</a></code>
</dt>
<dd>
</dd>
<dt>
<code><a href="../sui_sui/package#sui_package">package</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 (Mutable) ID of the package that can be upgraded.
</dd>
<dt>
<code><a href="../sui_sui/package#sui_package_version">version</a>: u64</code>
</dt>
<dd>
 (Mutable) The number of upgrades that have been applied
 successively to the original package.  Initially 0.
</dd>
<dt>
<code>policy: u8</code>
</dt>
<dd>
 What kind of upgrades are allowed.
</dd>
</dl>

Struct <code>UpgradeTicket</code>

Permission to perform a particular upgrade (for a fixed version of
the package, bytecode to upgrade with and transitive dependencies to
depend against).

An <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> can only issue one ticket at a time, to prevent races
between concurrent updates or a change in its upgrade policy after
issuing a ticket, so the ticket is a "Hot Potato" to preserve forward
progress.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>cap: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 (Immutable) ID of the <code><a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a></code> this originated from.
</dd>
<dt>
<code><a href="../sui_sui/package#sui_package">package</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 (Immutable) ID of the package that can be upgraded.
</dd>
<dt>
<code>policy: u8</code>
</dt>
<dd>
 (Immutable) The policy regarding what kind of upgrade this ticket
 permits.
</dd>
<dt>
<code>digest: vector&lt;u8&gt;</code>
</dt>
<dd>
 (Immutable) SHA256 digest of the bytecode and transitive
 dependencies that will be used in the upgrade.
</dd>
</dl>

Struct <code>UpgradeReceipt</code>

Issued as a result of a successful upgrade, containing the
information to be used to update the <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>.  This is a "Hot
Potato" to ensure that it is used to update its <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> before
the end of the transaction that performed the upgrade.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a>
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>cap: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 (Immutable) ID of the <code><a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a></code> this originated from.
</dd>
<dt>
<code><a href="../sui_sui/package#sui_package">package</a>: <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a></code>
</dt>
<dd>
 (Immutable) ID of the package after it was upgraded.
</dd>
</dl>

Constants

Tried to create a <a href="../sui_sui/package#sui_package_Publisher">Publisher</a> using a type that isn't a
one-time witness.

<code><b>const</b> <a href="../sui_sui/package#sui_package_ENotOneTimeWitness">ENotOneTimeWitness</a>: u64 = 0;
</code>

Tried to set a less restrictive policy than currently in place.

<code><b>const</b> <a href="../sui_sui/package#sui_package_ETooPermissive">ETooPermissive</a>: u64 = 1;
</code>

This <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> has already authorized a pending upgrade.

<code><b>const</b> <a href="../sui_sui/package#sui_package_EAlreadyAuthorized">EAlreadyAuthorized</a>: u64 = 2;
</code>

This <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> has not authorized an upgrade.

<code><b>const</b> <a href="../sui_sui/package#sui_package_ENotAuthorized">ENotAuthorized</a>: u64 = 3;
</code>

Trying to commit an upgrade to the wrong <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>.

<code><b>const</b> <a href="../sui_sui/package#sui_package_EWrongUpgradeCap">EWrongUpgradeCap</a>: u64 = 4;
</code>

Update any part of the package (function implementations, add new
functions or types, change dependencies)

<code><b>const</b> <a href="../sui_sui/package#sui_package_COMPATIBLE">COMPATIBLE</a>: u8 = 0;
</code>

Add new functions or types, or change dependencies, existing
functions can't change.

<code><b>const</b> <a href="../sui_sui/package#sui_package_ADDITIVE">ADDITIVE</a>: u8 = 128;
</code>

Only be able to change dependencies.

<code><b>const</b> <a href="../sui_sui/package#sui_package_DEP_ONLY">DEP_ONLY</a>: u8 = 192;
</code>

Function <code>claim</code>

Claim a Publisher object.
Requires a One-Time-Witness to prove ownership. Due to this
constraint there can be only one Publisher object per module
but multiple per package (!).

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_claim">claim</a>&lt;OTW: drop&gt;(otw: OTW, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>): <a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_claim">claim</a>&lt;OTW: drop&gt;(otw: OTW, ctx: &<b>mut</b> TxContext): <a href="../sui_sui/package#sui_package_Publisher">Publisher</a> {
    <b>assert</b>!(<a href="../sui_sui/types#sui_types_is_one_time_witness">types::is_one_time_witness</a>(&otw), <a href="../sui_sui/package#sui_package_ENotOneTimeWitness">ENotOneTimeWitness</a>);
    <b>let</b> type_name = type_name::with_original_ids&lt;OTW&gt;();
    <a href="../sui_sui/package#sui_package_Publisher">Publisher</a> {
        id: <a href="../sui_sui/object#sui_object_new">object::new</a>(ctx),
        <a href="../sui_sui/package#sui_package">package</a>: type_name.address_string(),
        module_name: type_name.module_string(),
    }
}
</code></pre>

Function <code>claim_and_keep</code>

Claim a Publisher object and send it to transaction sender.
Since this function can only be called in the module initializer,
the sender is the publisher.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_claim_and_keep">claim_and_keep</a>&lt;OTW: drop&gt;(otw: OTW, ctx: &<b>mut</b> <a href="../sui_sui/tx_context#sui_tx_context_TxContext">sui::tx_context::TxContext</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_claim_and_keep">claim_and_keep</a>&lt;OTW: drop&gt;(otw: OTW, ctx: &<b>mut</b> TxContext) {
    <a href="../sui_sui/transfer#sui_transfer_public_transfer">sui::transfer::public_transfer</a>(<a href="../sui_sui/package#sui_package_claim">claim</a>(otw, ctx), ctx.sender())
}
</code></pre>

Function <code>burn_publisher</code>

Destroy a Publisher object effectively removing all privileges
associated with it.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_burn_publisher">burn_publisher</a>(self: <a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_burn_publisher">burn_publisher</a>(self: <a href="../sui_sui/package#sui_package_Publisher">Publisher</a>) {
    <b>let</b> <a href="../sui_sui/package#sui_package_Publisher">Publisher</a> { id, <a href="../sui_sui/package#sui_package">package</a>: _, module_name: _ } = self;
    id.delete();
}
</code></pre>

Function <code>from_package</code>

Check whether type belongs to the same package as the publisher object.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_from_package">from_package</a>&lt;T&gt;(self: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_from_package">from_package</a>&lt;T&gt;(self: &<a href="../sui_sui/package#sui_package_Publisher">Publisher</a>): bool {
    type_name::with_original_ids&lt;T&gt;().address_string() == self.<a href="../sui_sui/package#sui_package">package</a>
}
</code></pre>

Function <code>from_module</code>

Check whether a type belongs to the same module as the publisher object.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_from_module">from_module</a>&lt;T&gt;(self: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_from_module">from_module</a>&lt;T&gt;(self: &<a href="../sui_sui/package#sui_package_Publisher">Publisher</a>): bool {
    <b>let</b> type_name = type_name::with_original_ids&lt;T&gt;();
    (type_name.address_string() == self.<a href="../sui_sui/package#sui_package">package</a>) && (type_name.module_string() == self.module_name)
}
</code></pre>

Function <code>published_module</code>

Read the name of the module.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_published_module">published_module</a>(self: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>): &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_published_module">published_module</a>(self: &<a href="../sui_sui/package#sui_package_Publisher">Publisher</a>): &String {
    &self.module_name
}
</code></pre>

Function <code>published_package</code>

Read the package address string.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_published_package">published_package</a>(self: &<a href="../sui_sui/package#sui_package_Publisher">sui::package::Publisher</a>): &<a href="../sui_std/ascii#std_ascii_String">std::ascii::String</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_published_package">published_package</a>(self: &<a href="../sui_sui/package#sui_package_Publisher">Publisher</a>): &String {
    &self.<a href="../sui_sui/package#sui_package">package</a>
}
</code></pre>

Function <code>upgrade_package</code>

The ID of the package that this cap authorizes upgrades for.
Can be 0x0 if the cap cannot currently authorize an upgrade
because there is already a pending upgrade in the transaction.
Otherwise guaranteed to be the latest version of any given
package.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_upgrade_package">upgrade_package</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_upgrade_package">upgrade_package</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>): ID {
    cap.<a href="../sui_sui/package#sui_package">package</a>
}
</code></pre>

Function <code>version</code>

The most recent version of the package, increments by one for each
successfully applied upgrade.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_version">version</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>): u64
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_version">version</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>): u64 {
    cap.<a href="../sui_sui/package#sui_package_version">version</a>
}
</code></pre>

Function <code>upgrade_policy</code>

The most permissive kind of upgrade currently supported by this
cap.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_upgrade_policy">upgrade_policy</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_upgrade_policy">upgrade_policy</a>(cap: &<a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>): u8 {
    cap.policy
}
</code></pre>

Function <code>ticket_package</code>

The package that this ticket is authorized to upgrade

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_package">ticket_package</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">sui::package::UpgradeTicket</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_package">ticket_package</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a>): ID {
    ticket.<a href="../sui_sui/package#sui_package">package</a>
}
</code></pre>

Function <code>ticket_policy</code>

The kind of upgrade that this ticket authorizes.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_policy">ticket_policy</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">sui::package::UpgradeTicket</a>): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_policy">ticket_policy</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a>): u8 {
    ticket.policy
}
</code></pre>

Function <code>receipt_cap</code>

ID of the <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> that this receipt should be used to
update.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_receipt_cap">receipt_cap</a>(receipt: &<a href="../sui_sui/package#sui_package_UpgradeReceipt">sui::package::UpgradeReceipt</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_receipt_cap">receipt_cap</a>(receipt: &<a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a>): ID {
    receipt.cap
}
</code></pre>

Function <code>receipt_package</code>

ID of the package that was upgraded to: the latest version of
the package, as of the upgrade represented by this receipt.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_receipt_package">receipt_package</a>(receipt: &<a href="../sui_sui/package#sui_package_UpgradeReceipt">sui::package::UpgradeReceipt</a>): <a href="../sui_sui/object#sui_object_ID">sui::object::ID</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_receipt_package">receipt_package</a>(receipt: &<a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a>): ID {
    receipt.<a href="../sui_sui/package#sui_package">package</a>
}
</code></pre>

Function <code>ticket_digest</code>

A hash of the package contents for the new version of the
package.  This ticket only authorizes an upgrade to a package
that matches this digest.  A package's contents are identified
by two things:

- modules: [[u8]]       a list of the package's module contents
- deps:    [[u8; 32]]   a list of 32 byte ObjectIDs of the
package's transitive dependencies

A package's digest is calculated as:

sha3_256(sort(modules ++ deps))

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_digest">ticket_digest</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">sui::package::UpgradeTicket</a>): &vector&lt;u8&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_ticket_digest">ticket_digest</a>(ticket: &<a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a>): &vector&lt;u8&gt; {
    &ticket.digest
}
</code></pre>

Function <code>compatible_policy</code>

Expose the constants representing various upgrade policies

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_compatible_policy">compatible_policy</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_compatible_policy">compatible_policy</a>(): u8 { <a href="../sui_sui/package#sui_package_COMPATIBLE">COMPATIBLE</a> }
</code></pre>

Function <code>additive_policy</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_additive_policy">additive_policy</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_additive_policy">additive_policy</a>(): u8 { <a href="../sui_sui/package#sui_package_ADDITIVE">ADDITIVE</a> }
</code></pre>

Function <code>dep_only_policy</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_dep_only_policy">dep_only_policy</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_dep_only_policy">dep_only_policy</a>(): u8 { <a href="../sui_sui/package#sui_package_DEP_ONLY">DEP_ONLY</a> }
</code></pre>

Function <code>only_additive_upgrades</code>

Restrict upgrades through this upgrade cap to just add code, or
change dependencies.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_only_additive_upgrades">only_additive_upgrades</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_only_additive_upgrades">only_additive_upgrades</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>) {
    cap.<a href="../sui_sui/package#sui_package_restrict">restrict</a>(<a href="../sui_sui/package#sui_package_ADDITIVE">ADDITIVE</a>)
}
</code></pre>

Function <code>only_dep_upgrades</code>

Restrict upgrades through this upgrade cap to just change
dependencies.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_only_dep_upgrades">only_dep_upgrades</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_only_dep_upgrades">only_dep_upgrades</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>) {
    cap.<a href="../sui_sui/package#sui_package_restrict">restrict</a>(<a href="../sui_sui/package#sui_package_DEP_ONLY">DEP_ONLY</a>)
}
</code></pre>

Function <code>make_immutable</code>

Discard the <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> to make a package immutable.

<code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_make_immutable">make_immutable</a>(cap: <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>entry</b> <b>fun</b> <a href="../sui_sui/package#sui_package_make_immutable">make_immutable</a>(cap: <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>) {
    <b>let</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a> { id, <a href="../sui_sui/package#sui_package">package</a>: _, <a href="../sui_sui/package#sui_package_version">version</a>: _, policy: _ } = cap;
    id.delete();
}
</code></pre>

Function <code>authorize_upgrade</code>

Issue a ticket authorizing an upgrade to a particular new bytecode
(identified by its digest).  A ticket will only be issued if one has
not already been issued, and if the policy requested is at least as
restrictive as the policy set out by the cap.

The digest supplied and the policy will both be checked by
validators when running the upgrade.  I.e. the bytecode supplied in
the upgrade must have a matching digest, and the changes relative to
the parent package must be compatible with the policy in the ticket
for the upgrade to succeed.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_authorize_upgrade">authorize_upgrade</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>, policy: u8, digest: vector&lt;u8&gt;): <a href="../sui_sui/package#sui_package_UpgradeTicket">sui::package::UpgradeTicket</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_authorize_upgrade">authorize_upgrade</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>, policy: u8, digest: vector&lt;u8&gt;): <a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a> {
    <b>let</b> id_zero = @0x0.to_id();
    <b>assert</b>!(cap.<a href="../sui_sui/package#sui_package">package</a> != id_zero, <a href="../sui_sui/package#sui_package_EAlreadyAuthorized">EAlreadyAuthorized</a>);
    <b>assert</b>!(policy &gt;= cap.policy, <a href="../sui_sui/package#sui_package_ETooPermissive">ETooPermissive</a>);
    <b>let</b> <a href="../sui_sui/package#sui_package">package</a> = cap.<a href="../sui_sui/package#sui_package">package</a>;
    cap.<a href="../sui_sui/package#sui_package">package</a> = id_zero;
    <a href="../sui_sui/package#sui_package_UpgradeTicket">UpgradeTicket</a> {
        cap: <a href="../sui_sui/object#sui_object_id">object::id</a>(cap),
        <a href="../sui_sui/package#sui_package">package</a>,
        policy,
        digest,
    }
}
</code></pre>

Function <code>commit_upgrade</code>

Consume an <a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a> to update its <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>, finalizing
the upgrade.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_commit_upgrade">commit_upgrade</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>, receipt: <a href="../sui_sui/package#sui_package_UpgradeReceipt">sui::package::UpgradeReceipt</a>)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/package#sui_package_commit_upgrade">commit_upgrade</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>, receipt: <a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a>) {
    <b>let</b> <a href="../sui_sui/package#sui_package_UpgradeReceipt">UpgradeReceipt</a> { cap: cap_id, <a href="../sui_sui/package#sui_package">package</a> } = receipt;
    <b>assert</b>!(<a href="../sui_sui/object#sui_object_id">object::id</a>(cap) == cap_id, <a href="../sui_sui/package#sui_package_EWrongUpgradeCap">EWrongUpgradeCap</a>);
    <b>assert</b>!(cap.<a href="../sui_sui/package#sui_package">package</a>.to_address() == @0x0, <a href="../sui_sui/package#sui_package_ENotAuthorized">ENotAuthorized</a>);
    cap.<a href="../sui_sui/package#sui_package">package</a> = <a href="../sui_sui/package#sui_package">package</a>;
    cap.<a href="../sui_sui/package#sui_package_version">version</a> = cap.<a href="../sui_sui/package#sui_package_version">version</a> + 1;
}
</code></pre>

Function <code>restrict</code>

<code><b>fun</b> <a href="../sui_sui/package#sui_package_restrict">restrict</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">sui::package::UpgradeCap</a>, policy: u8)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/package#sui_package_restrict">restrict</a>(cap: &<b>mut</b> <a href="../sui_sui/package#sui_package_UpgradeCap">UpgradeCap</a>, policy: u8) {
    <b>assert</b>!(cap.policy &lt;= policy, <a href="../sui_sui/package#sui_package_ETooPermissive">ETooPermissive</a>);
    cap.policy = policy;
}
</code></pre>