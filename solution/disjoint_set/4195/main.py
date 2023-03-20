# Authored by : fineman999
# Co-authored by : -
# Link : http://boj.kr/3add8bbe6c624a9f97020c569f0feabe


import sys
from collections import defaultdict

import sys

def input():
    return sys.stdin.readline().rstrip()

# 루트 노드 찾기(union-find)
def find_parents(hash_friends, friend):
    start = friend
    while hash_friends[friend] != friend:
        friend = hash_friends[friend]
    hash_friends[start] = friend
    return friend

def solution(N, friends):
    tmp = set() # 2. 중복 제거
    for A, B in friends:
        tmp.add(A)
        tmp.add(B)
    # 3. 초기 값 세팅
    hash_friends = {value: value for value in tmp}
    hash_cnt = {value: 1 for value in tmp}
    answer = []
    # 4. A와 B가 연결되어 있지 않으면 A와 B의 수를 합 한 후, A와 B를 연결
    for A, B in friends:
        if find_parents(hash_friends, A) != find_parents(hash_friends, B):
            check_b = hash_cnt[find_parents(hash_friends, B)]
            hash_cnt[find_parents(hash_friends, A)] += check_b
            hash_friends[find_parents(hash_friends, B)] = find_parents(hash_friends, A)
        # 5. A에 포함된 친구 수 배열에 추가
        answer.append(hash_cnt[find_parents(hash_friends, A)])
        
    # 6. 배열에 추가된 친구 수 출력
    for ele in answer:
        print(ele)

# 1. 실행
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        friends = []
        for _ in range(N):
            friends.append(list(input().split()))
        solution(N, friends)

if __name__ == '__main__':
    main()