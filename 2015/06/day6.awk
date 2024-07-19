{ gsub(",", " ") }

/^turn on/ {
		print "turning on" >> "/dev/stderr"
		for (i = $3; i <= $6; i++) {
				for (j = $4; j <= $7; j++) {
						lights[i,j] = 1
				}
		}
}

/^turn off/ {
		print "turning off" >> "/dev/stderr"
		for (i = $3; i <= $6; i++) {
				for (j = $4; j <= $7; j++) {
						delete lights[i,j]
				}
		}
}

/^toggle/ {
		print "toggling" >> "/dev/stderr"
		for (i = $2; i <= $5; i++) {
				for (j = $3; j <= $6; j++) {
						lights[i,j]
						if (lights[i,j] == 1) {
								delete lights[i,j]
						} else {
								lights[i,j] = 1
						}
				}
		}
}

END { print length(lights) }
