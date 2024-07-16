# see more here: https://adventofcode.com/2015/day/2
import fileinput
from typing import Iterator, List
from functools import reduce
from operator import mul

Dimensions = List[int]

def parse_input(input_file: str) -> Iterator[Dimensions]:
    for line in fileinput.input(input_file, encoding="utf-8"):
        yield map(int, line.split('x'))

def part1(box: Dimensions) -> int:
    l, w, h = box
    surface_areas = (l * w, w * h, h * l)
    total_surface_areas = sum(map(lambda x: 2 * x, surface_areas))
    smallest_surface_area = min(surface_areas)
    return total_surface_areas + smallest_surface_area

def part2(box: Dimensions) -> int:
    d = sorted(box)[0:2]
    #ribbon = sum(map(lambda x: 2 * x, d))
    ribbon = 2 * sum(d)
    bow = reduce(mul, box, 1)
    #print(ribbon, bow)
    return ribbon + bow

def test1() -> bool:
    tests = (
            ((2,3,4), 58),
            ((1,1,10), 43),
            )
    return all(check == part1(test) for test, check in tests)

def test2() -> bool:
    tests = (
            ((2,3,4), 34),
            ((1,1,10), 14),
            )
    return all(check == part2(test) for test, check in tests)

def main():
    inputf = "input.txt"
    assert test1()
    print(sum(map(part1, parse_input(inputf))))

    assert test2()
    print(sum(map(part2, parse_input(inputf))))

if __name__ == "__main__":
    main()
