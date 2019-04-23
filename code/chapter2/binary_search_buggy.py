def binary_search_buggy(v,x):
  start,end = 0,len(v)-1
  while start<end:
    mid = (start+end)//2  # // is the floor division operator
    if v[mid]>=x:
      end = mid
    else:
      start = mid+1
  return start

v=[1,2,5,10]
print(binary_search_buggy(v,-1))
print(binary_search_buggy(v,5))
print(binary_search_buggy(v,11))

