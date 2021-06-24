# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/685c4c3dc1c24c118d3c89ffdefa6679
import sys
def input():
    return sys.stdin.readline().rstrip()

while True:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        a = input()
        a_lower = a.lower()
        arr.append((a,a_lower))
    arr.sort(key = lambda x : x[1])
    print(arr[0][0])