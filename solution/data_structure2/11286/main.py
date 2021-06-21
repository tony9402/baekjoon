# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/29a558ec778348f589fad5c627187638
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [abs(x), x])