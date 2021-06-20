# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/85503261a5b5492ca153ccbe74adf43d
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
num = input()
total = 0
for i in num:
    total += int(i)

print(total)
