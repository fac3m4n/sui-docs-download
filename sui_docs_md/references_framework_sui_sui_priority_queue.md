Priority queue implemented using a max heap.

-  [Struct PriorityQueue](#sui_priority_queue_PriorityQueue)
-  [Struct Entry](#sui_priority_queue_Entry)
-  [Constants](#@Constants_0)
-  [Function new](#sui_priority_queue_new)
-  [Function pop_max](#sui_priority_queue_pop_max)
-  [Function insert](#sui_priority_queue_insert)
-  [Function new_entry](#sui_priority_queue_new_entry)
-  [Function create_entries](#sui_priority_queue_create_entries)
-  [Function restore_heap_recursive](#sui_priority_queue_restore_heap_recursive)
-  [Function max_heapify_recursive](#sui_priority_queue_max_heapify_recursive)
-  [Function priorities](#sui_priority_queue_priorities)

<code><b>use</b> <a href="../sui_std/vector#std_vector">std::vector</a>;
</code>

Struct <code>PriorityQueue</code>

Struct representing a priority queue. The entries vector represents a max
heap structure, where entries[0] is the root, entries[1] and entries[2] are the
left child and right child of the root, etc. More generally, the children of
entries[i] are at i * 2 + 1 and i * 2 + 2. The max heap should have the invariant
that the parent node's priority is always higher than its child nodes' priorities.

<code><b>public</b> <b>struct</b> <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a>&lt;T: drop&gt; <b>has</b> drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>entries: vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;&gt;</code>
</dt>
<dd>
</dd>
</dl>

Struct <code>Entry</code>

<code><b>public</b> <b>struct</b> <a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T: drop&gt; <b>has</b> drop, store
</code>

<summary>Fields</summary>

<dl>
<dt>
<code>priority: u64</code>
</dt>
<dd>
</dd>
<dt>
<code>value: T</code>
</dt>
<dd>
</dd>
</dl>

Constants

For when heap is empty and there's no data to pop.

<code><b>const</b> <a href="../sui_sui/priority_queue#sui_priority_queue_EPopFromEmptyHeap">EPopFromEmptyHeap</a>: u64 = 0;
</code>

For when the value vector and priority vector have mismatched lengths

<code><b>const</b> <a href="../sui_sui/priority_queue#sui_priority_queue_ELengthMismatch">ELengthMismatch</a>: u64 = 1;
</code>

For when access a node of a priority_queue at an invalid index

<code><b>const</b> <a href="../sui_sui/priority_queue#sui_priority_queue_EIndexOutOfBounds">EIndexOutOfBounds</a>: u64 = 2;
</code>

Function <code>new</code>

Create a new priority queue from the input entry vectors.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_new">new</a>&lt;T: drop&gt;(entries: vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;&gt;): <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">sui::priority_queue::PriorityQueue</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_new">new</a>&lt;T: drop&gt;(<b>mut</b> entries: vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T&gt;&gt;): <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a>&lt;T&gt; {
    <b>let</b> len = entries.length();
    <b>let</b> <b>mut</b> i = len / 2;
    // Max heapify from the first node that is a parent (node at len / 2).
    <b>while</b> (i &gt; 0) {
        i = i - 1;
        <a href="../sui_sui/priority_queue#sui_priority_queue_max_heapify_recursive">max_heapify_recursive</a>(&<b>mut</b> entries, len, i);
    };
    <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a> { entries }
}
</code></pre>

Function <code>pop_max</code>

Pop the entry with the highest priority value.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_pop_max">pop_max</a>&lt;T: drop&gt;(pq: &<b>mut</b> <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">sui::priority_queue::PriorityQueue</a>&lt;T&gt;): (u64, T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_pop_max">pop_max</a>&lt;T: drop&gt;(pq: &<b>mut</b> <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a>&lt;T&gt;): (u64, T) {
    <b>let</b> len = pq.entries.length();
    <b>assert</b>!(len &gt; 0, <a href="../sui_sui/priority_queue#sui_priority_queue_EPopFromEmptyHeap">EPopFromEmptyHeap</a>);
    // Swap the max element with the last element in the entries and remove the max element.
    <b>let</b> <a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a> { priority, value } = pq.entries.swap_remove(0);
    // Now the max heap property <b>has</b> been violated at the root node, but nowhere <b>else</b>
    // so we call max heapify on the root node.
    <a href="../sui_sui/priority_queue#sui_priority_queue_max_heapify_recursive">max_heapify_recursive</a>(&<b>mut</b> pq.entries, len - 1, 0);
    (priority, value)
}
</code></pre>

Function <code>insert</code>

Insert a new entry into the queue.

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_insert">insert</a>&lt;T: drop&gt;(pq: &<b>mut</b> <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">sui::priority_queue::PriorityQueue</a>&lt;T&gt;, priority: u64, value: T)
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_insert">insert</a>&lt;T: drop&gt;(pq: &<b>mut</b> <a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a>&lt;T&gt;, priority: u64, value: T) {
    pq.entries.push_back(<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a> { priority, value });
    <b>let</b> index = pq.entries.length() - 1;
    <a href="../sui_sui/priority_queue#sui_priority_queue_restore_heap_recursive">restore_heap_recursive</a>(&<b>mut</b> pq.entries, index);
}
</code></pre>

Function <code>new_entry</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_new_entry">new_entry</a>&lt;T: drop&gt;(priority: u64, value: T): <a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_new_entry">new_entry</a>&lt;T: drop&gt;(priority: u64, value: T): <a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T&gt; {
    <a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a> { priority, value }
}
</code></pre>

Function <code>create_entries</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_create_entries">create_entries</a>&lt;T: drop&gt;(p: vector&lt;u64&gt;, v: vector&lt;T&gt;): vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_create_entries">create_entries</a>&lt;T: drop&gt;(p: vector&lt;u64&gt;, v: vector&lt;T&gt;): vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T&gt;&gt; {
    <b>assert</b>!(v.length() == p.length(), <a href="../sui_sui/priority_queue#sui_priority_queue_ELengthMismatch">ELengthMismatch</a>);
    <b>let</b> <b>mut</b> res = vector[];
    p.zip_do_reverse!(v, |priority, value| res.push_back(<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a> { priority, value }));
    res.reverse();
    res
}
</code></pre>

Function <code>restore_heap_recursive</code>

<code><b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_restore_heap_recursive">restore_heap_recursive</a>&lt;T: drop&gt;(v: &<b>mut</b> vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;&gt;, i: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_restore_heap_recursive">restore_heap_recursive</a>&lt;T: drop&gt;(v: &<b>mut</b> vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T&gt;&gt;, i: u64) {
    <b>if</b> (i == 0) {
        <b>return</b>
    };
    <b>let</b> parent = (i - 1) / 2;
    // If <a href="../sui_sui/priority_queue#sui_priority_queue_new">new</a> elem is greater than its parent, swap them and recursively
    // do the restoration upwards.
    <b>if</b> (*&v[i].priority &gt; *&v[parent].priority) {
        v.swap(i, parent);
        <a href="../sui_sui/priority_queue#sui_priority_queue_restore_heap_recursive">restore_heap_recursive</a>(v, parent);
    }
}
</code></pre>

Function <code>max_heapify_recursive</code>

Max heapify the subtree whose root is at index i. That means after this function
finishes, the subtree should have the property that the parent node has higher priority
than both child nodes.
This function assumes that all the other nodes in the subtree (nodes other than the root)
do satisfy the max heap property.

<code><b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_max_heapify_recursive">max_heapify_recursive</a>&lt;T: drop&gt;(v: &<b>mut</b> vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">sui::priority_queue::Entry</a>&lt;T&gt;&gt;, len: u64, i: u64)
</code>

<summary>Implementation</summary>

<pre><code><b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_max_heapify_recursive">max_heapify_recursive</a>&lt;T: drop&gt;(v: &<b>mut</b> vector&lt;<a href="../sui_sui/priority_queue#sui_priority_queue_Entry">Entry</a>&lt;T&gt;&gt;, len: u64, i: u64) {
    <b>if</b> (len == 0) {
        <b>return</b>
    };
    <b>assert</b>!(i &lt; len, <a href="../sui_sui/priority_queue#sui_priority_queue_EIndexOutOfBounds">EIndexOutOfBounds</a>);
    <b>let</b> left = i * 2 + 1;
    <b>let</b> right = left + 1;
    <b>let</b> <b>mut</b> max = i;
    // Find the node with highest priority among node <span className="code-inline">i</span> and its two children.
    <b>if</b> (left &lt; len && *&v[left].priority &gt; *&v[max].priority) {
        max = left;
    };
    <b>if</b> (right &lt; len && *&v[right].priority &gt; *&v[max].priority) {
        max = right;
    };
    // If the parent node (node <span className="code-inline">i</span>) doesn't have the highest priority, we swap the parent with the
    // max priority node.
    <b>if</b> (max != i) {
        v.swap(max, i);
        // After the swap, we have restored the property at node <span className="code-inline">i</span> but now the max heap property
        // may be violated at node <span className="code-inline">max</span> since this node now <b>has</b> a <a href="../sui_sui/priority_queue#sui_priority_queue_new">new</a> value. So we need to now
        // max heapify the subtree rooted at node <span className="code-inline">max</span>.
        <a href="../sui_sui/priority_queue#sui_priority_queue_max_heapify_recursive">max_heapify_recursive</a>(v, len, max);
    }
}
</code></pre>

Function <code>priorities</code>

<code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_priorities">priorities</a>&lt;T: drop&gt;(pq: &<a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">sui::priority_queue::PriorityQueue</a>&lt;T&gt;): vector&lt;u64&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_sui/priority_queue#sui_priority_queue_priorities">priorities</a>&lt;T: drop&gt;(pq: &<a href="../sui_sui/priority_queue#sui_priority_queue_PriorityQueue">PriorityQueue</a>&lt;T&gt;): vector&lt;u64&gt; {
    pq.entries.map_ref!(|e| e.priority)
}
</code></pre>