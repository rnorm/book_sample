Fibonacci_native = function(n){
  if (n==1 || n==2){
    1
  }else {
    Fibonacci_native(n-1) + Fibonacci_native(n-2)
  }
}
