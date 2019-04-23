import numpy as np


class LR:
    def __init__(self):
        self.coef = None

    def qr_solver(self, x, y):
        q, r = np.linalg.qr(x)
        p = np.dot(q.T, y)
        return np.dot(np.linalg.inv(r), p)

    def fit(self, x, y):
        self.coef = self.qr_solver(np.hstack((np.ones((x.shape[0], 1)), x)), y)

    def predict(self, x):
        return np.dot(np.hstack((np.ones((x.shape[0], 1)), x)), self.coef)