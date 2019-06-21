import multiprocessing as mp
import numpy as np 
from numpy.random import uniform, seed

# first let's implement without parallelization

def count_inside_point(n):
    m = 0
    # we generate n points
    for _ in range(n):
        p_x = uniform(-1, 1)
        p_y = uniform(-1, 1)
        if p_x ** 2 + p_y ** 2 <= 1:
            m += 1
    return m

# now let's try the parallel approach
# each process uses the same seed, which is not desired
def generate_points_parallel(n):
    pool = mp.Pool()
    # we ask each process to generate n//mp.cpu_count() points
    return pool.map(count_inside_point, [n//mp.cpu_count()]*mp.cpu_count())

# set seed for each process
# first, let's define a helper function
def helper(args):
    n, s = args
    seed(s)
    return count_inside_point(n)
    
def generate_points_parallel_set_seed(n):
    pool = mp.Pool() # we can also specify the number of processes by Pool(number)
    # we ask each process to generate n//mp.cpu_count() points
    return pool.map(helper, list(zip([n//mp.cpu_count()]*mp.cpu_count(),range(mp.cpu_count()))))

# another optimization via vectorization
def generate_points_vectorized(n):
    p = uniform(-1, 1, size=(n,2))
    return np.sum(np.linalg.norm(p, axis=1) <= 1)

def pi_naive(n):
    print(f'pi: {count_inside_point(n)/n*4:.6f}')

def pi_parallel(n):
    print(f'pi: {sum(generate_points_parallel_set_seed(n))/n*4:.6f}')

def pi_vectorized(n):
    print(f'pi: {generate_points_vectorized(n)/n*4:.6f}')
