from itertools import permutations
from itertools import combinations
import time


n = 60

startTime = time.time()
print(startTime)

for i in permutations(range(n), n):
    pass
    #print(time.time() - startTime,i)

print(time.time() - startTime)



