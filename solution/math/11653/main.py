# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/ebf75b738a784d6dad28494e18113b31
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
while True:
    if N == 1:
        break
    for i in range(2,N+1):
        if N % i == 0:
            print(i)
            N = N // i
            break