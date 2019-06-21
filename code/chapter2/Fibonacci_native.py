def Fibonacci_native(n):
    if n==1 or n==2:
        return 1
    return Fibonacci_native(n-1) + Fibonacci_native(n-2)
