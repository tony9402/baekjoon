# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/f1c91eae2a2245c599c5d1bbc9cde9f5
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = 0
waiting = 0

for i in range(len(arr)):
    total += arr[i] + waiting
    waiting += arr[i]

print(total)