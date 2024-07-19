#!/usr/bin/env awk
/(ab)|(cd)|(pq)|(xy)/ { next }
/[aeiou].*[aeiou].*[aeiou]/ && 
	/aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz/ { i++ }
END { print i }
