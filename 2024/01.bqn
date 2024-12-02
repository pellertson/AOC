#!/usr/bin/env bqn

input ← ⍉>•ParseFloat{𝔽∘(5⊸↑)⋈𝔽∘(8⊸↓)}¨ •file.Lines "input/01.in"
p1 ← +´(|∘-)˝∧˘ input
p2 ← {+´𝕨×+˝⍉𝕨=⌜>𝕩}˝ input

•Show p1‿p2
