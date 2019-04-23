library(microbenchmark)
source('binary_search.R')
source('find_pos.R')

v=1:10000

# call the find_pos 100 times; 
# each time we randomly select an integer as the target value 

# for-loop solution
set.seed(2019)
print(microbenchmark(find_pos(v,sample(10000,1)),times=1000))
# binary-search solution
set.seed(2019)
print(microbenchmark(binary_search(v,sample(10000,1)),times=1000))
