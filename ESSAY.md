# Why Complexity Is Rare

**What We Learned From the Simplest Possible Worlds**

---

At first glance, our work looks technical and abstract. It involves artificial "worlds" governed by simple rules, where patterns form, move, collide, or disappear. But the question behind it is a very human one:

> *What does it take for something to persist, to carry information, and to compute, when it is interrupted, disturbed, or only partially observed?*

We did not begin with a grand theory. Instead, we began by breaking things.

---

## Interrupting Worlds on Purpose

The central tool in this work is something called *temporal filtering*. Rather than letting a system run smoothly, we interrupt it. We skip updates. We sample only some moments in time. We ask a harsh question:

**Which patterns still make sense when you don't see every step?**

This turns out to be extremely revealing. Many systems that look rich and complex when you watch every frame collapse as soon as you miss a few. Others survive effortlessly.

That observation triggered the entire project.

---

## The First Surprise: Survival Isn't About Complexity

Some highly chaotic systems survived interruption perfectly. Others that looked orderly fell apart.

So we tested the obvious explanations.

- Maybe survival depends on how "closed" a structure is.
- Maybe it depends on timing or resonance.
- Maybe surrounding stable structures can protect fragile ones.
- Maybe there's a critical rhythm that must be matched.

One by one, these ideas failed.

Structures survived not because they were clever, timed just right, or supported by neighbors—but because they could *repair themselves*. If a disturbance knocked them slightly off track, they were drawn back.

This property is called a **basin of attraction**. It is not about motion. It is not about beauty. It is about recovery.

That led to a clean result:

> **To survive interruption, a structure must be able to heal itself.**

*— See [Paper 5: Structural Invariants](https://github.com/RobinNixon/Invariants)*

---

## The Second Surprise: Survival Is Not the Same as Visibility

Something unexpected happened next.

Some patterns survived interruption perfectly, but became *unreadable*. They were still "there," but no longer distinguishable. Information had quietly vanished.

This forced a separation that most people never make:

- **Survival** means a structure continues to exist.
- **Visibility** means you can still tell one state from another.

They are not the same thing.

We discovered that visibility depends on how information is layered onto a background. In some systems, the background itself oscillates. When sampling aligns exactly with that oscillation, differences can cancel out. The system survives, but information becomes harder to see.

This phenomenon is called **anti-resonance**. Surprisingly, being "perfectly in sync" can destroy contrast.

From this came a second principle:

> **To preserve information, you must avoid synchronizing with the carrier that holds it.**
>
> **Survival and visibility are independent dimensions of robustness.**

*— See [Paper 6: Anti-Resonance](https://github.com/RobinNixon/Anti-Resonance)*

---

## Why One Rule Keeps Appearing

Throughout this work, one particular system kept reappearing: a simple rule known as **Rule 110**.

Rule 110 has long been famous because it can, in principle, compute anything. But that fame often sounded mystical. *Why this rule?*

Our framework answers that cleanly.

In the simplest possible rule space, you are balancing several incompatible requirements:

- You need **repair**, or everything collapses.
- You need **motion**, or nothing computes.
- You must avoid **chaos**, or information dissolves.
- You must avoid **rigid order**, or nothing moves.

Most rules give up one requirement to satisfy the others. Rule 110 is the only one that satisfies all of them at once—even precariously.

That does not make it magical. It makes it *inevitable*.

If no such rule existed, computation would be impossible in that universe.

> **Rule 110 is not special because it computes.**
> **It is special because if it didn't exist, nothing else that simple could.**

*— See [Paper 1: The Five-Bit Threshold](https://github.com/RobinNixon/UCT)*

---

## What This Work Really Shows

Across six experimental papers and one final synthesis, we arrived at a simple, hard-earned conclusion:

- **Persistence requires repair.**
- **Information requires contrast.**
- **Motion without repair is fragile.**
- **Repair without motion is inert.**
- **Synchrony can silently erase meaning.**

We did not discover this by proposing a theory. We discovered it by systematically eliminating every explanation that did not survive contact with experiments.

The final framework was not invented. It was what remained.

*— See [Paper 7: The Orthogonal Robustness Framework](https://github.com/RobinNixon/Robustness)*

---

## Why This Matters Beyond Cellular Automata

Although we studied simple artificial worlds, the principles apply widely.

Any system that updates intermittently, loses data, or operates asynchronously faces the same tradeoffs. This includes:

- Distributed computing systems
- Learning algorithms
- Biological processes
- Communication channels
- Simulations and models

The lesson is not *how* to build a specific thing.
The lesson is *what kinds of things are even possible* under interruption.

That is why this project ends here.

Once the structure is clear, more experiments stop adding insight. What follows are applications.

---

## A Calm Ending

This work did not seek everything. It sought what was unavoidable.

And once that was found, stopping was the honest move.

---

### The Complete Research Series

| # | Paper | Repository |
|---|-------|------------|
| 1 | The Five-Bit Threshold | [UCT](https://github.com/RobinNixon/UCT) |
| 2 | Stickiness and Control | [Stickiness](https://github.com/RobinNixon/Stickiness) |
| 3 | Self-Maintenance | [Self-Maintenance](https://github.com/RobinNixon/Self-Maintenance) |
| 4 | Substrate Leakiness | [Leakiness](https://github.com/RobinNixon/Leakiness) |
| 5 | Structural Invariants | [Invariants](https://github.com/RobinNixon/Invariants) |
| 6 | Anti-Resonance | [Anti-Resonance](https://github.com/RobinNixon/Anti-Resonance) |
| 7 | Orthogonal Robustness | [Robustness](https://github.com/RobinNixon/Robustness) |

---

*Robin Nixon et al, 2026*
