Split ← •BQN¨('x'⊸((⊢-˜+`×¬)∘=⊔⊢))
Part1 ← (⌊´+(+´2×⊢))∘(1⊸⌽⊸×)∘Split

•Show Part1 •FLines "input.txt"