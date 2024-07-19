#!/bin/sh
sed "s/./&\n/g" < input.txt |
		awk '
		/\(/ { floor++ }
		/\)/ { floor-- }
		(floor == -1 && !p2) { pos = NR; p2 = 1}
		END  { print floor "\n" pos }'
