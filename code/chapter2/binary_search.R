binary_search=function(v,x){
  if (x>v[length(v)]){return(NULL)}
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



