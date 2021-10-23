# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/c3cc5338e8fa49ae8136e4af174221df
from collections import defaultdict
import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
lst = list(map(int, input().split()))
dic = defaultdict(int) # 어떤 값이 기존에 몇 번 나왔는지 저장

for i in range(1, n): lst[i] += lst[i-1] # 누적합 inplace로 만들기

cnt = 0
for num in lst:
    if num == k: cnt += 1 # 1부터 더한 값 중 k 있으면 cnt += 1
    # O(n) 연산 대신 dictionary에서 찾는 것으로 시간 단축
    cnt += dic[num-k] # 이미 본 누적합 값과 num으로 k 만들 수 있으면 추가
    dic[num] += 1 # num 만들 수 있는 개수 +1

print(cnt)