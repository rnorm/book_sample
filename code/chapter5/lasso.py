import numpy as np
from sklearn.preprocessing import StandardScaler

def sto(z, theta):
    return np.sign(z)*np.maximum(np.abs(z)-np.full(len(z),theta), 0.0)

class Lasso:
    def __init__(self, l):
        self.l = l # l is lambda
        self.intercept = 0.0
        self.beta = None
        self.scaler = StandardScaler()
    
    def fit(self, x, y, max_iter=100):
        self.intercept = np.mean(y)
        y_centered = y-self.intercept
        x_transformed = self.scaler.fit_transform(x)
        gamma = 1.0/np.linalg.eig(x_transformed.T.dot(x_transformed))[0].max()
        beta = np.zeros(x_transformed.shape[1])
        for _ in range(max_iter):
            nabla = - np.dot(x_transformed.T, y_centered-np.dot(x_transformed, beta))
            z = beta - 2*gamma*nabla
            beta = sto(z, self.l*gamma)
        self.beta = beta

    def predict(self, new_x):
        new_x_transformed = self.scaler.transform(new_x)
        return np.dot(new_x_transformed, self.beta) + self.intercept


