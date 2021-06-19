# Authored by : gusdn3477
# Co-authored by : -
# Link : http://boj.kr/986f23862eab4f97b7df8bd16177ac70
import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()

def find_1(N):
    for a in range(int(sqrt(N))+1, 0, -1):
        if a ** 2 == N:
            return 1
    return 0

def find_2(N):
    for a in range(int(sqrt(N))+1, 0, -1):
        for b in range(int(sqrt(N))+1, 0, -1):
            if a ** 2 + b ** 2 > N:
                continue
            if a ** 2 + b ** 2 == N:
                return 2
    return 0
                    
def find_3(N):
    for a in range(int(sqrt(N))+1, 0, -1):
        for b in range(int(sqrt(N))+1, 0, -1):
            if a ** 2 + b ** 2 > N:
                continue
            for c in range(int(sqrt(N))+1, 0, -1):
                if a ** 2 + b ** 2 + c ** 2> N:
                    continue
                if a ** 2 + b ** 2 + c ** 2 == N:
                    return 3
    return 0
                    
def find_4(N):
    for a in range(int(sqrt(N))+1, 0, -1):
        for b in range(int(sqrt(N))+1, 0, -1):
            if a ** 2 + b ** 2 > N:
                continue
            for c in range(int(sqrt(N))+1, 0, -1):
                if a ** 2 + b ** 2 + c ** 2> N:
                    continue
                for d in range(int(sqrt(N))+1, 0, -1):
                    if a ** 2 + b ** 2 + c ** 2 + d ** 2 > N:
                        continue
                    if a ** 2 + b ** 2 + c ** 2 + d ** 2 == N:
                        return 4
    return 0


N = int(input())
ans = find_1(N) or find_2(N) or find_3(N) or find_4(N)
print(ans)