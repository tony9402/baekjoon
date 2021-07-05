# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/6cd0f036ab1d40eaad68c57ee4eb6ff4
import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
num  = [ int(str(N * i)[::-1]) for i in range(1, K + 1) ]
print(max(num))
