from sklearn.datasets import load_boston
from linear_regression_ridge import LR_Ridge
boston = load_boston()
X, y = boston.data, boston.target
# first, let's run our own linear regression
ridge = LR_Ridge(0.5)
ridge.fit(X, y)
print(ridge.coef)
print(ridge.predict(X)[:5])
