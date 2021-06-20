# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/331c1288d35f4db9b12e371e014dfffd
import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    global ans
    start, end = 0, max(arr)

    while start <= end:
        mid = (start + end) // 2
        total_length = 0
        for i in arr:
            if i - mid >= 0:
                total_length += i - mid

        if total_length < M:
            end = mid - 1
        else:
            start = mid + 1
    ans = end

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
binary_search()
print(ans)
