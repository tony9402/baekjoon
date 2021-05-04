import sys
import re

def ri():
    return sys.stdin.readline().strip()

regex = re.compile('^[A-F]?A+F+C+[A-F]?$')
N = int(ri())
for testcase in range(N):
    line = ri()
    print("Infected!" if regex.match(line) else "Good")

