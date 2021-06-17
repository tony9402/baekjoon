# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/c540e6d57a39460eb360903623b90eec

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []

for i in range(N):
    arr.append(input())

arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))

for i in arr:
    print(i)