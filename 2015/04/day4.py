# see more here: https://adventofcode.com/2015/day/4
import hashlib
import itertools

def part1(key: str) -> int:
    for i in itertools.count(1):
        test = f"{key}{i}"
        lead_digest = hashlib.md5(test.encode()).hexdigest()[:5]
        if lead_digest == "00000":
            return i

def part2(key: str) -> int:
    for i in itertools.count(1):
        test = f"{key}{i}"
        lead_digest = hashlib.md5(test.encode()).hexdigest()[:6]
        if lead_digest == "000000":
            return i
        
def main():
    with open("input.txt") as key:
        key_str = key.read()
        print(part1(key_str))
        print(part2(key_str))

if __name__ == "__main__":
    main()


