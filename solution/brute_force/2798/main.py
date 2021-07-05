# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/29a558ec778348f589fad5c627187638
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
MAX = 0
arr = list(map(int, input().split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for z in range(j+1,len(arr)):
            if arr[i] + arr[j] + arr[z] <= M:
                MAX = max(MAX, arr[i] + arr[j] + arr[z])
print(MAX)