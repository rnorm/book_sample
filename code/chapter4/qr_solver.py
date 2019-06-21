import numpy as np

def qr_solver(x,y):
  q,r=np.linalg.qr(x)
  p = np.dot(q.T,y)
  return np.dot(np.linalg.inv(r),p)
