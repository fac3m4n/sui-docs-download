-  [Struct BridgeRoute](#bridge_chain_ids_BridgeRoute)
-  [Constants](#@Constants_0)
-  [Function sui_mainnet](#bridge_chain_ids_sui_mainnet)
-  [Function sui_testnet](#bridge_chain_ids_sui_testnet)
-  [Function sui_custom](#bridge_chain_ids_sui_custom)
-  [Function eth_mainnet](#bridge_chain_ids_eth_mainnet)
-  [Function eth_sepolia](#bridge_chain_ids_eth_sepolia)
-  [Function eth_custom](#bridge_chain_ids_eth_custom)
-  [Function route_source](#bridge_chain_ids_route_source)
-  [Function route_destination](#bridge_chain_ids_route_destination)
-  [Function assert_valid_chain_id](#bridge_chain_ids_assert_valid_chain_id)
-  [Function valid_routes](#bridge_chain_ids_valid_routes)
-  [Function is_valid_route](#bridge_chain_ids_is_valid_route)
-  [Function get_route](#bridge_chain_ids_get_route)

<code><b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>BridgeRoute</code>

<code><b>public</b> <b>struct</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> <b>has</b> <b>copy</b>, drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>source: u8</code>
</dt>
<dd>
</dd>
<dt>
<code>destination: u8</code>
</dt>
<dd>
</dd>
</dl>

Constants

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_MAINNET">SUI_MAINNET</a>: u8 = 0;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a>: u8 = 1;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a>: u8 = 2;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_MAINNET">ETH_MAINNET</a>: u8 = 10;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a>: u8 = 11;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a>: u8 = 12;
</code>

<code><b>const</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_EInvalidBridgeRoute">EInvalidBridgeRoute</a>: u64 = 0;
</code>

Function <code>sui_mainnet</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_mainnet">sui_mainnet</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_mainnet">sui_mainnet</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_MAINNET">SUI_MAINNET</a> }
</code></pre>

Function <code>sui_testnet</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_testnet">sui_testnet</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_testnet">sui_testnet</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a> }
</code></pre>

Function <code>sui_custom</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_custom">sui_custom</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_sui_custom">sui_custom</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a> }
</code></pre>

Function <code>eth_mainnet</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_mainnet">eth_mainnet</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_mainnet">eth_mainnet</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_MAINNET">ETH_MAINNET</a> }
</code></pre>

Function <code>eth_sepolia</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_sepolia">eth_sepolia</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_sepolia">eth_sepolia</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a> }
</code></pre>

Function <code>eth_custom</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_custom">eth_custom</a>(): u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_eth_custom">eth_custom</a>(): u8 { <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a> }
</code></pre>

Function <code>route_source</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_route_source">route_source</a>(route: &<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">bridge::chain_ids::BridgeRoute</a>): &u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_route_source">route_source</a>(route: &<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a>): &u8 {
    &route.source
}
</code></pre>

Function <code>route_destination</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_route_destination">route_destination</a>(route: &<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">bridge::chain_ids::BridgeRoute</a>): &u8
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_route_destination">route_destination</a>(route: &<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a>): &u8 {
    &route.destination
}
</code></pre>

Function <code>assert_valid_chain_id</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">assert_valid_chain_id</a>(id: u8)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_assert_valid_chain_id">assert_valid_chain_id</a>(id: u8) {
    <b>assert</b>!(
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_MAINNET">SUI_MAINNET</a> ||
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a> ||
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a> ||
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_MAINNET">ETH_MAINNET</a> ||
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a> ||
        id == <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a>,
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_EInvalidBridgeRoute">EInvalidBridgeRoute</a>,
    )
}
</code></pre>

Function <code>valid_routes</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_valid_routes">valid_routes</a>(): vector&lt;<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">bridge::chain_ids::BridgeRoute</a>&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_valid_routes">valid_routes</a>(): vector&lt;<a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a>&gt; {
    vector[
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_MAINNET">SUI_MAINNET</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_MAINNET">ETH_MAINNET</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_MAINNET">ETH_MAINNET</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_MAINNET">SUI_MAINNET</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_SEPOLIA">ETH_SEPOLIA</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_TESTNET">SUI_TESTNET</a> },
        <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source: <a href="../sui_bridge/chain_ids#bridge_chain_ids_ETH_CUSTOM">ETH_CUSTOM</a>, destination: <a href="../sui_bridge/chain_ids#bridge_chain_ids_SUI_CUSTOM">SUI_CUSTOM</a> },
    ]
}
</code></pre>

Function <code>is_valid_route</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_is_valid_route">is_valid_route</a>(source: u8, destination: u8): bool
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_is_valid_route">is_valid_route</a>(source: u8, destination: u8): bool {
    <b>let</b> route = <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source, destination };
    <a href="../sui_bridge/chain_ids#bridge_chain_ids_valid_routes">valid_routes</a>().contains(&route)
}
</code></pre>

Function <code>get_route</code>

<code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_get_route">get_route</a>(source: u8, destination: u8): <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">bridge::chain_ids::BridgeRoute</a>
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_bridge/chain_ids#bridge_chain_ids_get_route">get_route</a>(source: u8, destination: u8): <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> {
    <b>let</b> route = <a href="../sui_bridge/chain_ids#bridge_chain_ids_BridgeRoute">BridgeRoute</a> { source, destination };
    <b>assert</b>!(<a href="../sui_bridge/chain_ids#bridge_chain_ids_valid_routes">valid_routes</a>().contains(&route), <a href="../sui_bridge/chain_ids#bridge_chain_ids_EInvalidBridgeRoute">EInvalidBridgeRoute</a>);
    route
}
</code></pre>