from sklearn.datasets import load_boston
from linear_regression import LR
boston = load_boston()
X, y = boston.data, boston.target
# first, let's run our own linear regression
lr = LR()
lr.fit(X, y)
print(lr.coef)
print(lr.predict(X)[:5])

# now, use sklearn's linear regression model
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X, y)
print(reg.coef_)
print(reg.predict(X)[:5])
