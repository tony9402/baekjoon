# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7910ebb7f8ec409ba2e93cb14d047a19
import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if mid < i:
                total += mid
            else:
                total += i
        if total <= M:
            start = mid + 1
        else:
            end = mid - 1
    return end
    
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
print(binary_search())
