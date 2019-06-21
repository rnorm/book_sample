import numpy as np
from scipy.optimize import minimize

class LogisticRegression:
    def __init__(self):
        self.coef = None

    # we use '_' as the prefix of the method name to indicate the method is private
    def _sigmoid(self, x):
        return 1.0/(1.0 + np.exp(-x))

    def _log_lik(self, beta, x, y):
        linear = np.dot(x, beta)
        ll = np.sum(linear.dot(y)) - np.sum(np.log(1.0+np.exp(linear)))
        return -ll

    def fit(self, x, y):
        self.coef = minimize(fun=self._log_lik, args=(np.insert(x, 0, 1.0, axis=1),y), method='L-BFGS-B', x0=np.zeros(1+x.shape[1])).x
    
    def predict(self, new_x):
        linear = np.insert(new_x, 0, 1.0, axis=1).dot(self.coef) # add 1 to new_x
        return self._sigmoid(linear)
