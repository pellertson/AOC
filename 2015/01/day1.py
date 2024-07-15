# see more here: https://adventofcode.com/2015/day/1
import operator
import sys
from itertools import accumulate

def part1(parens:str) -> int:
	f = lambda x: 1 if x == '(' else -1
	return sum(map(f, parens))

def part2(parens:str) -> int:
	f = lambda x: 1 if x == '(' else -1
	for i, p in enumerate(accumulate(map(f, parens))):
		if p == -1:
			#print(i)
			return i+1
	return sys.maxint

def test1() -> bool:
	tests = (
		("(())", 0),
		("()()", 0),
		("(((", 3),
		("(()(()(", 3),
		("))(((((", 3),
		("())", -1),
		("))(", -1),
		(")))", -3),
		(")())())", -3),
	)
	
	result = all(check == part1(test) for test, check in tests)
	return result

def test2() -> bool:
	tests = (
		(")", 1),
		("()())", 5),
	)
	
	result = all(check == part2(test) for test, check in tests)
	return result

def main():
	assert test1()
	assert test2()

	with open("input.txt", encoding="utf-8") as i:
		parens = i.read()
		print(part1(parens))
		print(part2(parens))

if __name__ == "__main__":
	main()
