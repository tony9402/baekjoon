# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/cd5989ea170a46c9aba0b049b70f4ee6

import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(len(arr)-1):
    arr[-1] += arr[i] / 2
print(arr[-1])