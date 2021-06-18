# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/5540a61d3d364466bbe47e8c62beaedb
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = []

for i in range(N):
    weight, height = map(int, input().split())
    arr.append([weight,height,1])

for i in range(N):
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            arr[i][2] += 1

for i in range(len(arr)):
    print(arr[i][2], end=' ')