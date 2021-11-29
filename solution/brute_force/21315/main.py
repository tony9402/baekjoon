# Authored by : yj2221
# Co-authored by : -
# Link : http://boj.kr/9857ec1183e144acb9d49a7316bdf595

from itertools import permutations
import sys

def input():
    return sys.stdin.readline().rstrip()

def shuffle(card1, card2, card3):
    card = card2 + card1 + card3
    if len(card2) > 1:
        return shuffle(card2[:len(card2)//2] + card1, card2[len(card2)//2:], card3)
    else:
        card = card2 + card1 + card3
        return card

n = int(input())
correct_cards = list(map(int,input().split()))
answer = []
orders = [i for i in range(1, 10)] + [i for i in range(1, 10)]

for perm in permutations(orders, 2):
    if 2 ** max(perm)>=n: 
        continue
    cards = [i for i in range(1, n+1)]
    for k in perm:
        card1 = []
        card2 = cards[n-(2**k):]
        card3 = cards[:n-(2**k)]
        cards = shuffle(card1, card2, card3)
    
    if cards == correct_cards:
        answer = perm
        break

print(' '.join(map(str, answer)))
