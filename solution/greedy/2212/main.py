# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/2b4e1797973e4e16a3b38ff778023e3e
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
lst = sorted(list(set(map(int, input().split())))) # 중복 제거 후 정렬
distance = sorted([lst[i]-lst[i-1] for i in range(1, len(lst))]) # 센서 사이 거리 계산 후 정렬
print(sum(distance[:(len(lst)-k)])) # 그리디하게 최장 거리 k개 제외한 게 정답
