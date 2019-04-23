from binary_search import binary_search
from find_pos import find_pos
import timeit
import random

v=list(range(1,10001))

def test_for_loop(n):
  random.seed(2019)
  for _ in range(n):
    find_pos(v,random.randint(1,10000))

def test_bs(n):
  random.seed(2019)
  for _ in range(n):
    binary_search(v,random.randint(1,10000))

# for-loop solution
print(timeit.timeit('test_for_loop(1000)',setup='from __main__ import test_for_loop',number=1))
# binary_search solution
print(timeit.timeit('test_bs(1000)',setup='from __main__ import test_bs',number=1))
