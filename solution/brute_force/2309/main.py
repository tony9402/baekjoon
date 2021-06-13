# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/be3b4fb036844cb390e1f7a818471cde

import sys

def input():
    return sys.stdin.readline().rstrip()

def findIndex(ans):

    for i in range(9):
        for j in range(i+1,9):
            if arr[i] + arr[j] == ans:
                return (arr[i], arr[j])

arr = []
for i in range(9):
    arr.append(int(input()))

ans = sum(arr) - 100
first, second = findIndex(ans)
arr.remove(first)
arr.remove(second)
arr.sort()

for i in arr:
    print(i)