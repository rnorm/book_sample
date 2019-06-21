library(parallel)
count_inside_point = function(n){
  m = 0
  for (i in 1:n){
    p_x = runif(1, -1, 1)
    p_y = runif(1, -1, 1)
    if (p_x^2 + p_y^2 <=1){
      m = m+1
    }
  }
  m
}

# now let's use the mcapply for parallelization
generate_points_parallel = function(n){
  # detectCores() returns the number of cores available
  # we assign the task to each core
  unlist(mclapply(X = rep(n %/% detectCores(), detectCores()),FUN=count_inside_point))
}

# now let's use vectorization
generate_points_vectorized = function(n){
  p = array(runif(n*2,-1,1), c(n,2))
  sum((p[,1]^2+p[,2]^2)<=1)
}

pi_naive = function(n) cat('naive: pi -', 4*count_inside_point(n)/n, '\n')

pi_parallel = function(n) cat('parallel: pi -', 4*sum(generate_points_parallel(n))/n, '\n')

pi_vectorized = function(n) cat('vectorized: pi -', 4*sum(generate_points_vectorized(n))/n, '\n')

