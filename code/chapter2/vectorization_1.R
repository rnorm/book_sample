library(microbenchmark)

# generate n standard normal r.v
rnorm_loop = function(n){
x=rep(0,n)
for (i in 1:n) {x[i]=rnorm(1)}
}

rnorm_vec = function(n){
x=rnorm(n)
}

n=100
# for loop
print(microbenchmark(rnorm_loop(n),times=1000))
# vectorize
print(microbenchmark(rnorm_vec(n),times=1000))
