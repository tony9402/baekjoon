# Authored by : gusdn3477
# Co-authored by : tony9402
# Link : http://boj.kr/816fdae98bec4a4f95a3fb44fd2f348f
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

def solve(N):
    ret = 4
    for a in range(1, sqrtN + 1):
        if a * a == N:
            ret = 1
        
        if ret == 1:
            break
        for b in range(1, sqrtN + 1):
            if a * a + b * b  > N:
                break
            if a * a + b * b == N:
                ret = 2

            if ret <= 2:
                break
            for c in range(1, sqrtN + 1):
                if a * a + b * b + c * c  > N:
                    break
                if a * a + b * b + c * c == N:
                    ret = 3
                    break

    return ret

N = int(input())
sqrtN = int(sqrt(N))
print(solve(N))
