# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/ee8c8ce8f36344348accd5605c2aba66
import sys

def input():
    return sys.stdin.readline().rstrip()

N, L = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in arr:
    if L >= i:
        L += 1
print(L)
