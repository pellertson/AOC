#!/usr/bin/env bqn
in ← •file.Lines "input/02.in"

# run a function "in between" every element.
_btwn ← {1⊸↓𝔽¯1⊸↓} 
IncOrDec ← (<∨>)_btwn
Lvl ← {a←|𝕨-𝕩⋄(a≠0)∧(a≤3)}_btwn
p1 ← +´{0=+´(Lvl ∧ IncOrDec) 𝕩}¨ in

•Show p1
