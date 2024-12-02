Split ← •BQN¨('x'⊸((⊢-˜+`×¬)∘=⊔⊢))
Part1 ← +´((⌊´+(+´2×⊢))∘(1⊸⌽⊸×)∘Split)¨
Part2 ← +´((×´+(2×⌊´∘(1⊸⌽⊸+)))∘Split)¨
•Show Part1 •FLines "input.txt"
•Show Part2 •FLines "input.txt"

