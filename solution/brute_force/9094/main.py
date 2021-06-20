# Authored by : gusdn3477
# Co-authored by : tony9402
# Link : http://boj.kr/ea96af96027540dcb1daa3b65e849eab
import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    n,m = map(int, input().split())
    ct = 0
    for a in range(1,n):
        for b in range(a+1,n):
            if (a * a + b * b + m) % (a*b) == 0:
                ct += 1

    print(ct)
