#include <Rcpp.h>
using namespace Rcpp;

// [[Rcpp::export]]
int Fibonacci(int n) {
  if (n==1 or n==2){
    return 1;
  } 
  return Fibonacci(n-1)+Fibonacci(n-2);
}

