# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/2b9516c8789c4a42849250efcef845c7
import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(n)])
heap = [lst[0][1]]
for i in range(1, n):
    if heap[0] > lst[i][0]: # 새로운 회의실 필요
        heapq.heappush(heap, lst[i][1])
    else: # 기존 회의실 이어서 사용 가능
        heapq.heappop(heap)
        heapq.heappush(heap, lst[i][1])

print(len(heap))