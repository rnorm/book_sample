def find_pos(v,x):
  for i in range(len(v)):
    if v[i]>=x:
      return i
v=[1,2,5,10]
print(find_pos(v,-1))
print(find_pos(v,4))
print(find_pos(v,11))

