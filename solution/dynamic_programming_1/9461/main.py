# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/369118cac2b14c75866029d361c95152
import sys

def input():
    return sys.stdin.readline().rstrip()

def recursion(x):
    if x == 1 or x == 2 or x == 3:
        return 1
    if dp[x] == 0:
        dp[x] = recursion(x-2) + recursion(x-3)
    return dp[x]

T = int(input())
dp = [0] * 101
for i in range(T):
    N = int(input())
    print(recursion(N))