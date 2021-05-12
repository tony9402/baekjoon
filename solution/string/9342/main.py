# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/4fcec3ea35e4472bbca8beeebd2fe065
import sys
import re

def input():
    return sys.stdin.readline().rstrip()

regex = re.compile('^[A-F]?A+F+C+[A-F]?$')
N = int(input())
for testcase in range(N):
    line = input()
    print("Infected!" if regex.match(line) else "Good")

