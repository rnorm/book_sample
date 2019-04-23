binary_search_buggy=function(v,x){
  start = 1
  end = length(v)
  while (start<end){
    mid = (start+end) %/% 2 # %/% is the floor division operator
    if (v[mid]>=x){
      end = mid
    }else{
      start = mid+1
    }
  }
  return(start)
}
v=c(1,2,5,10)
print(binary_search_buggy(v,-1))
print(binary_search_buggy(v,5))
print(binary_search_buggy(v,11))



