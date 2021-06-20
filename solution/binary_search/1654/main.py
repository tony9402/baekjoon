# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/5200a798517a4ec09af16f496ad137bd
import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    global ans
    start, end = 1, max(arr)

    while start <= end:
        ct = 0
        mid = (start + end) // 2
        for i in arr:
            ct += i // mid
        if ct < N:
            end = mid - 1
        else:
            start = mid + 1
    ans = end

K,N = map(int, input().split())
arr = []
ans = 0
for i in range(K):
    arr.append(int(input()))
binary_search()
print(ans)
