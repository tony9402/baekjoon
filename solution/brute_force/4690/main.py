# Authored by : chj3748
# Co-authored by : -
# Link : http://boj.kr/fb355cbf95324465b430f4423567a2c4
for a in range(2, 100 + 1):
    for b in range(2, a):
        for c in range(b, a):
            for d in range(c, a):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')