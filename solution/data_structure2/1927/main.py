# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/5d73f6bad59b42a58688435c855b9580
import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,x)
