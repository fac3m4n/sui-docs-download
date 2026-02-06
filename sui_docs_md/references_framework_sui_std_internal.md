Defines the <a href="../sui_std/internal#std_internal_Permit">Permit</a> type, which can be used to constrain the logic of a
generic function to be authorized only by the module that defines the type
parameter.

```move
module example::use_permit;

public struct MyType { /* ... */ }

public fun test_permit() {
let permit = internal::permit<MyType>();
/* external_module::call_with_permit(permit); */
}
```

To write a function that is guarded by a <a href="../sui_std/internal#std_internal_Permit">Permit</a>, require it as an argument.

```move
// Silly mockup of a type registry where a type can be registered only by
// the module that defines the type.
module example::type_registry;

public fun register_type<T>(_: internal::Permit<T> /* ... */) {
/* ... */
}
```

-  [Struct Permit](#std_internal_Permit)
-  [Function permit](#std_internal_permit)

<code></code>

Struct <code>Permit</code>

A privileged witness of the T type.
Instances can only be created by the module that defines the type T.

<code><b>public</b> <b>struct</b> <a href="../sui_std/internal#std_internal_Permit">Permit</a>&lt;<b>phantom</b> T&gt; <b>has</b> drop
</code>

<summary>Fields</summary>

<dl>
</dl>

Function <code>permit</code>

Construct a new <a href="../sui_std/internal#std_internal_Permit">Permit</a> for the type T.
Can only be called by the module that defines the type T.

<code><b>public</b> <b>fun</b> <a href="../sui_std/internal#std_internal_permit">permit</a>&lt;T&gt;(): <a href="../sui_std/internal#std_internal_Permit">std::internal::Permit</a>&lt;T&gt;
</code>

<summary>Implementation</summary>

<pre><code><b>public</b> <b>fun</b> <a href="../sui_std/internal#std_internal_permit">permit</a>&lt;T&gt;(): <a href="../sui_std/internal#std_internal_Permit">Permit</a>&lt;T&gt; { <a href="../sui_std/internal#std_internal_Permit">Permit</a>() }
</code></pre>