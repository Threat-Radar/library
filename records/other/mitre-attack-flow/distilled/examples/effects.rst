Effects
-------

One of the key ideas behind Attack Flow is understanding how individual adversary
techniques relate to each other. The concept of *effect* is critical for understanding
these relationships between techniques. An effect is the outcome, result, or change in
state that occurs when an adversary executes a technique. Examples of effects include:

1. The attacker modifies the state of an asset, e.g. opening a port on the firewall.
2. The attacker gains some knowledge, e.g. a password.
3. The attacker achieves code execution.

Actions can produce effects, and subsequent actions may *depend* on those effects:

1. The attacker wants to connect to an internal service, which requires opening a port
   on the firewall.
2. The attacker wants to log in remotely, which depends on knowing the password.
3. The attacker wants to run a C2 implant, which depends on having code execution.

While an *action* is being executed, it's effect is an *indeterminate* state, i.e. we
cannot make any statement about the outcome or result. Once the action concludes, then
we can evaluate its effects, whether it succeeded or failed, etc. When one action is
chained to another, the latter depends on the effects of the former, i.e. the second one
can only execute when the first one completes successfully.

A *condition* splits a flow into multiple paths based on evaluating an effect, e.g. if
the action is a privilege escalation exploit, then the condition can test whether the
attacker has obtained elevated privileges (i.e. the exploit succeeded) or still has
regular privileges (i.e. the exploit failed.) A condition always selects one path to
follow, either the ``on_true_refs`` or the ``on_false_refs``.

On the other hand, an *operator* joins multiple attack paths together by aggregating
multiple effects. Conditions and operators can be used to encode complex behavior into
an attack flow that represents how attackers coordinate multiple behaviors to achieve a
desired outcome, as well as how they handle individual technique failure.
