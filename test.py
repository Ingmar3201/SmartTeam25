from itertools import permutations
from itertools import combinations


n = 11
target = (0, 1, 3, 4, 6, 7, 8, 10, 2, 5, 9)

for i in permutations(range(n), n):
    if i == target:
        print(i)
        break

