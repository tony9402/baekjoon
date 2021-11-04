# Authored by : cieske
# Co-authored by : -
# Link : http://boj.kr/cfb369b6a5134cfa9c0859eab5464c47
import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
lst = list(map(int, input().split())) # 정렬된 상태로 들어옴
sub = sorted([lst[i+1] - lst[i] for i in range(n-1)]) # 원생 간 키 차이 정렬
print(sum(sub[:(n-k)])) # Greedy하게 n-k개만 선택