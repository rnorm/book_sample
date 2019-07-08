from gbm import GBM
import numpy as np
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error


def rmse(actual, pred):
    return (mean_squared_error(actual, pred))**0.5


def get_boston_data(seed=42):
    boston = datasets.load_boston()
    X, y = shuffle(boston.data, boston.target, random_state=seed)
    X = X.astype(np.float32)
    offset = int(X.shape[0] * 0.8)
    X_train, y_train = X[:offset], y[:offset]
    X_test, y_test = X[offset:], y[offset:]
    return X_train, y_train, X_test, y_test
    
if __name__ == "__main__":
    X_train, y_train, X_test, y_test = get_boston_data(42)
    gbm = GBM(X_train, y_train, depth=6, eta=0.05, lam=1.0,
              gamma=1, sub_sample=0.5, sub_feature=0.7)
    gbm.set_test_data(X_test, y_test)
    gbm.fit(max_tree=200)

