import numpy as np
from sklearn.preprocessing import StandardScaler
import pdb


class LR_Ridge:
    def __init__(self, l):
        self.l = l
        self.coef = None
        self.scaler = StandardScaler()

    def qr_solver(self, x, y):
        q, r = np.linalg.qr(x)
        p = np.dot(q.T, y)
        return np.dot(np.linalg.inv(r), p)

    def fit(self, x, y):
        x_transformed = self.scaler.fit_transform(x)
        x_lambda = np.vstack(
            (x_transformed, np.diag([self.l**0.5]*x.shape[1])))
        x_lambda = np.hstack(
            (np.vstack((np.ones((x.shape[0], 1)), np.zeros((x.shape[1], 1)))), x_lambda))
        y_lambda = np.hstack((y, np.zeros((x.shape[1],))))
        self.coef = self.qr_solver(x_lambda, y_lambda)

    def predict(self, x):
        new_x_transformed = self.scaler.transform(x)
        new_x_transformed = np.hstack(
            (np.ones((x.shape[0],1)), new_x_transformed)
        )
        return np.dot(new_x_transformed, self.coef)
