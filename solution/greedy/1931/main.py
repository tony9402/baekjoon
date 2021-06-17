# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/7150be3ff485402ebb4c5011fa88ac7d
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []
total = 1

for i in range(N):
    a,b = map(int, input().split())
    arr.append((a,b))

arr.sort(key = lambda x : (x[1],x[0]))
end_time = arr[0][1]

for i in range(1,N):
    if arr[i][0] >= end_time:
        end_time = arr[i][1]
        total += 1

print(total)