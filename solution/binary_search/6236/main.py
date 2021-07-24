# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/2fe2f6f8da4f448a8b1b2e6a4da13627
import sys

def input():
    return sys.stdin.readline().rstrip()

def binary_search():
    global K
    start, end = max(arr), sum(arr)
    while start <= end:
        mid = (start + end) // 2
        have,ct = 0,0
        for i in arr:
            if have < i:
                have = mid - i
                ct += 1
            else:
                have = have - i
        if ct > M:
            start = mid + 1
        else:
            end = mid - 1
            K = mid
        
N, M = map(int, input().split())
arr = []
K = 0
for i in range(N):
    arr.append(int(input()))
binary_search()
print(K)
