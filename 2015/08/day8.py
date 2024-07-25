def parse1(file: str) -> int:
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


def parse2(file: str) -> int:
    a = b = 0
    s = '"'
    with open(file) as f:
        while (ch := f.read(1)) != '':
            match ch:
                case '\n':
                    s += '"'
                    a += len(s)
                    b += len(eval(s))
                    s = '"'
                case '"':
                    s += '\\"'
                case '\\':
                    s += '\\\\'
                case _:
                    s += ch
    
    return a - b
    
if __name__ == "__main__":
    assert 12 == parse1("test.txt")
    print(parse1("input.txt"))
    
    assert 19 == parse2("test.txt")
    print(parse2("input.txt"))
