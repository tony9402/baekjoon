# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/3bcac4799e584285b9df8be8d69ab79a
import sys
from bisect import bisect_left, bisect_right
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr.sort()
for i in arr2:
    idx_left = bisect_left(arr,i)
    idx_right = bisect_right(arr,i)
    print(idx_right - idx_left, end=' ')