import fileinput

def parse(file: str) -> int:
    a = b = 0
    s = ""
    with open(file) as f:
        while (ch := f.read(1)) != '':
            match ch:
                case '\n':
                    a += len(s)
                    b += len(eval(s))
                    s = ""
                case _:
                    s += ch
    
    return a - b

if __name__ == "__main__":
    assert 12 == parse("test.txt")
    print(parse("input.txt"))
