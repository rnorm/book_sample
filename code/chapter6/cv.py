import sys
sys.path.append("..")
from chapter5.lasso import Lasso
from sklearn.model_selection import KFold
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

boston = load_boston()
X, y = boston.data, boston.target

# create the partitions with k=5
k = 5
kf = KFold(n_splits=k)
# create a placeholder for the rmse on each test partition
scores = []

for train_index, test_index in kf.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    # let's train the model on the train partitions
    lr = Lasso(200.0)
    lr.fit(X_train, y_train, max_iter=100)
    # now test on the test partition
    y_hat = lr.predict(X_test)
    # we calculate the root of mean squared error (rmse)
    rmse = mean_squared_error(y_test, y_hat) ** 0.5
    scores.append(rmse)

# average rmse from 5-fold cross-validation
print(sum(scores)/k)
