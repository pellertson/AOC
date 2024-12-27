#!/usr/bin/env bqn
# https://adventofcode.com/2024/day/3
test_input ← "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
str ← •Import "../util/bqn-libs/strings.bqn"
P1 ← {𝕊 in:
    lp ← @+41
    # min: mul(X,Y)  max: mul(XXX,YYY)
    •Show m ← ((4≤≠)¨⊸/) •Show "mul(" str.Split in
}
P1 test_input
