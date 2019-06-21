#!python
#cython: language_level=3

cdef int Fibonacci_c(int n):
    if n==1 or n==2:
        return 1
    return Fibonacci_c(n-1) + Fibonacci_c(n-2)

def Fibonacci_static(n):
    return Fibonacci_c(n)

def Fibonacci(n):
    if n==1 or n==2:
        return 1
    return Fibonacci(n-1) + Fibonacci(n-2)
