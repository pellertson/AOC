import fileinput
import textwrap
import re
import logging
from enum import Enum

logging.basicConfig(level=logging.INFO)

class Gates:
    def __init__(self):
        self.gates: dict[str, int] = {}
    
    def _assign(self, id: str, signal: int):
        logging.info(f"Assigning {signal} to {id}")
        self.gates[id] = signal
    
    def _and(self, a: str, b: str, to: str):
        logging.info(f"Putting ({a} & {b}) into {to}")
        self.gates[to] = self.gates[a] & self.gates[b]
    
    def _or(self, a: str, b: str, to: str):
        logging.info(f"Putting ({a} | {b}) into {to}")
        self.gates[to] = self.gates[a] | self.gates[b]
        
    def _not(self, a: str, to: str):
        logging.info(f"Putting (~{a}) into {to}")
        #self.gates[to] = ~ self.gates[a]
        self.gates[to] = (2 ** 16) - self.gates[a] - 1
        
    def _lshift(self, a: str, places: int, to: str):
        logging.info(f"Putting ({a} << {places}) into {to}")
        self.gates[to] = self.gates[a] << places
    
    def _rshift(self, a: str, places: int, to: str):
        logging.info(f"Putting ({a} >> {places}) into {to}")
        self.gates[to] = self.gates[a] >> places
        
    def parse_instructions(self, instructions: list[str]):
        logging.info("Parsing instructions")
        assign_r = re.compile("[0-9]+ -> [a-z]+")
        and_r = re.compile("[a-z]+ AND [a-z]+ -> [a-z]+")
        or_r = re.compile("[a-z]+ OR [a-z]+ -> [a-z]+")
        lshift_r = re.compile("[a-z]+ LSHIFT [0-9]+ -> [a-z]")
        rshift_r = re.compile("[a-z]+ RSHIFT [0-9]+ -> [a-z]")
        not_r = re.compile("NOT [a-z]+ -> [a-z]+")
        
        for inst in instructions:
            p = inst.split(' ')
            
            if assign_r.match(inst):
                self._assign(p[2], int(p[0]))
            elif and_r.match(inst):
                self._and(p[0], p[2], p[4])
            elif or_r.match(inst):
                self._or(p[0], p[2], p[4])
            elif lshift_r.match(inst):
                self._lshift(p[0], int(p[2]), p[4])
            elif rshift_r.match(inst):
                self._rshift(p[0], int(p[2]), p[4])
            elif not_r.match(inst):
                self._not(p[1], p[3])
            else:
                raise RuntimeError(f"Could not parse instruction: \"{inst}\"")
        
        logging.info("Finished parsing!")
    
def test1() -> bool:
    ex = """\
    123 -> x
    456 -> y
    x AND y -> d
    x OR y -> e
    x LSHIFT 2 -> f
    y RSHIFT 2 -> g
    NOT x -> h
    NOT y -> i"""
    
    check = {
        'd': 72,
        'e': 507,
        'f': 492,
        'g': 114,
        'h': 65412,
        'i': 65079,
        'x': 123,
        'y': 456
    }
    
    g = Gates()
    g.parse_instructions(textwrap.dedent(ex).split("\n"))
    
    #print(g.gates)
    #print(check)
    
    return g.gates == check
    

def main():
    assert test1()
    t1 = Gates()
    t1.parse_instructions(fileinput.input(files="input.txt"))
    print(t1[a])
    
    
if __name__ == "__main__":
    main()
