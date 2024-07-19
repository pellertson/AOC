function max(a,b) { return (a > b) ? a : b }

{ gsub(",", " ") }

/^turn on/ {
		print "turning on" >> "/dev/stderr"
		for (i = $3; i <= $6; i++) {
				for (j = $4; j <= $7; j++) {
						part1[i,j] = 1
						part2[i,j] += 1
				}
		}
}

/^turn off/ {
		print "turning off" >> "/dev/stderr"
		for (i = $3; i <= $6; i++) {
				for (j = $4; j <= $7; j++) {
						delete part1[i,j]
						part2[i,j] = max(part2[i,j] - 1, 0)
				}
		}
}

/^toggle/ {
		print "toggling" >> "/dev/stderr"
		for (i = $2; i <= $5; i++) {
				for (j = $3; j <= $6; j++) {
						part2[i,j] += 2
						# print i,j,part2[i,j]
						if (part1[i,j] == 1) {
								delete part1[i,j]
						} else {
								part1[i,j] = 1
						}
				}
		}
}

END { 
		print length(part1)
		for (b in part2) s += part2[b]
		print s
}
