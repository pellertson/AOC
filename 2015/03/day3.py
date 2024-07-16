def part1(path: str) -> int:
    x = y = 0
    p: dict[str, int] = {}
    p["0,0"] = 1

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

        key = str(x) + ',' + str(y)
        try:
            p[key] += 1
        except KeyError:
            p[key] = 1

    return len(p)

def test1() -> bool:
    tests = (
            (">", 2),
            ("^>v<", 4),
            ("^v^v^v^v^v", 2),
            )
    return all(check == part1(test) for test, check in tests)

def main():
    file = open("input.txt")
    path = file.read()
    file.close()

    assert test1()
    print(part1(path))

if __name__ == "__main__":
    main()
