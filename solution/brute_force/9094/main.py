# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/3f137adac3644ed4bae0ff9e21500b54
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    n,m = map(int, input().split())
    ct = 0
    for a in range(1,n):
        for b in range(a+1,n):
            if (a * a + b * b + m) // (a*b) == (a * a + b * b + m) / (a*b):
                ct += 1

    print(ct)
