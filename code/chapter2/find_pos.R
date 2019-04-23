find_pos=function(v,x){
  for (i in 1:length(v)){
    if (v[i]>=x){
      return(i)
    }
  }
}
v=c(1,2,5,10)
print(find_pos(v,-1))
print(find_pos(v,4))
print(find_pos(v,11))
