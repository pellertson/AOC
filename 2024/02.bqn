#!/usr/bin/env bqn
util ← •Import "../util/utils.bqn"
in ← •ParseFloat⚇1 (" "⊸util.Split)¨ •file.Lines "input/02.in"
_btwn ← {1⊸↓𝔽¯1⊸↓}
IncOrDec ← (∧´{𝔽∘<∨(𝔽∘>)})_btwn
Diff ← (∧´{a←|𝕨-𝕩⋄(a≠0)∧(a≤3)})_btwn
BigTest ← IncOrDec∧Diff

# to those who read this, know that test cases are very important
# couldn't have completed this had i not used aoc's test cases
testSafe ← ⟨7‿6‿4‿2‿1,1‿3‿6‿7‿9⟩
testUnsafe ← ⟨1‿2‿7‿8‿9,9‿7‿6‿2‿1,1‿3‿2‿4‿5,8‿6‿4‿4‿1⟩
! ∧´ BigTest¨ testSafe
! ∧´ ¬BigTest¨ testUnsafe
p1 ← +´BigTest¨ in


•Show p1
 
