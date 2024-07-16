def deliver(path: str) -> set[str]:
    x = y = 0
    p: dict[str, bool] = {}
    p["0,0"] = True

    for house in path:
        if house == ">":
            x += 1
        elif house == "<":
            x -= 1
        elif house == "v":
            y -= 1
        elif house == "^":
            y += 1
        else:
            # probably don't need this but it's always good to be thorough
            raise Exception("we done screwed up")   

        p[str(x) + ',' + str(y)] = True

    return set(p.keys())

def part1(path: str) -> int:
    return len(deliver(path))

def part2(path:str) -> int:
    a = b = ""
    for i, h in enumerate(path):
        if i % 2 == 0:
            a += h
        else:
            b += h
    #print(deliver(a) + deliver(b))
    return len(deliver(a) | deliver(b))

def test1() -> bool:
    tests = (
            (">", 2),
            ("^>v<", 4),
            ("^v^v^v^v^v", 2),
            )
    return all(check == part1(test) for test, check in tests)

def test2() -> bool:
    tests = (
            ("^v", 3),
            ("^>v<", 3),
            ("^v^v^v^v^v", 11),
            )
    return all(check == part2(test) for test, check in tests)

def main():
    file = open("input.txt")
    path = file.read()
    file.close()

    assert test1()
    print(part1(path))
    assert test2()
    print(part2(path))

if __name__ == "__main__":
    main()
