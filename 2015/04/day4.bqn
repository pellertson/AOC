# https://en.wikipedia.org/wiki/MD5#Algorithm
sines ← ⌊(2⋆32)×|∘•math.Sin∘1⊸+ ↕64
shifts ← ⟨
  7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22
  5, 9,14,20,5, 9,14,20,5, 9,14,20,5, 9,14,20
  4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23
  6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21
⟩
HexVal ← {
  # get just the hex val in uppercase string
  a ← (≥⟜'0'∧'9'⊸≥)◶⟨-⟜32⋄⊢⟩¨𝕩

  # convert hex string into digit
  # shout out to BQNCrate
  16⊸×⊸+˜´⌽(∾"0A"+⟜↕¨10‿6)⊐a
}

MD5 ← {
  𝕩
}

!