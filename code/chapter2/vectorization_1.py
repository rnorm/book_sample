import timeit
import numpy as np

def rnorm_for_loop(n):
  x=[0]*n # create a list with n 0s
  np.random.seed(2019)
  for _ in range(n):
    np.random.normal(0,1,1)

def rnorm_vec(n):
  np.random.seed(2019)
  x = np.random.normal(0,1,n)

print("for loop")
print(f'{timeit.timeit("rnorm_for_loop(100)",setup="from __main__ import rnorm_for_loop",number=1000):.6f} seconds')
print("vectorized")
print(f'{timeit.timeit("rnorm_vec(100)",setup="from __main__ import rnorm_vec",number=1000):.6f} seconds')


