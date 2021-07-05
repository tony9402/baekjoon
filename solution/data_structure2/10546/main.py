# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/bb59bafb8ef04d69a5ab5ade6d7cfeb9
import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
dic = {}
for i in range(N):
    name = input()
    dic[name] = dic.get(name, 0) + 1

for i in range(N-1):
    name = input()
    dic[name] -= 1

dic_list = list(dic.items())
dic_list.sort(key = lambda x : (-x[1], x[0]))
print(dic_list[0][0])
