# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/ebf75b738a784d6dad28494e18113b31
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
X = N
for i in range(2, N + 1):
    if X == 1:
        break
    while X % i == 0:
        X //= i
        print(i)
