# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/93afacc450454aedbd2b0d6667914846
import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search(t):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == t:
            return 1
        elif arr[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return 0

T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    arr.sort()
    for j in arr2:
        print(binary_search(j))