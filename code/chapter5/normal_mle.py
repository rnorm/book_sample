from scipy.optimize import minimize
from math import log

def log_lik(theta, x):
  mu = theta[0]
  sigma = theta[1]
  # return the negative log-likelihood for minimization
  return -(-len(x)*log(sigma) - 0.5/sigma**2*sum((e-mu)**2 for e in x))

def normal_mle(x):
  return minimize(fun=lambda e:log_lik(e,x),x0=[0,1],method='L-BFGS-B',bounds=((None,None),(1e-6,None))).x
