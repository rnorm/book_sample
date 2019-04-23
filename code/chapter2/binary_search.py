def binary_search(v,x):
  if x>v[-1]: return
  start,end = 0,len(v)-1
  while start<end:
    mid = (start+end)//2
    if v[mid]>=x:
      end = mid
    else:
      start = mid+1
  return start
