import numpy as np

class LR_GD:
    """
    linear regression with vanilla gradient descent
    """

    def __init__(self, x, y, learning_rate=0.005, seed=42):
        # we put 1s in the first column of x
        self.x = np.hstack((np.ones((x.shape[0], 1)), x))
        self.y = y[:, None]
        self.seed = seed
        np.random.seed(self.seed)
        self.coef = np.random.uniform(size=(self.x.shape[1], 1))
        self.learning_rate = learning_rate

    def predict(self, new_x):
        # let's use @ for matrix multiplication
        return new_x @ self.coef

    def gradient(self):
        y_hat = self.predict(self.x)
        return -2.0*self.x.T @ (self.y-y_hat)/self.x.shape[0]

    def update(self):
        self.coef -= self.learning_rate*self.gradient()

    def fit(self, max_iteration=1000):
        for _ in range(max_iteration):
            self.update()