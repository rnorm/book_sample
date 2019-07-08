import xgboost as xgb
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.metrics import mean_squared_error
import numpy as np

seed = 42
boston = datasets.load_boston()
X, y = shuffle(boston.data, boston.target, random_state=seed)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.8)
X_train, y_train = X[:offset], y[:offset]
X_test, y_test = X[offset:], y[offset:]

params = {'booster': 'gbtree', 'objective': 'reg:linear', 'learning_rate': 0.1,
          'max_depth': 5, 'subsample': 0.6, 'colsample_bytree': 0.8, 'min_child_weight': 2}

# prepare the data for training and testing
dtrain = xgb.DMatrix(data=X_train, label=y_train, missing=None)
dtest = xgb.DMatrix(X_test)

# run 5-fold cross-validation with maximum 1000 trees, and try to minimize the metric rmse
# early stopping 50 trees
hist = xgb.cv(params, dtrain=dtrain, nfold=5,
              metrics=['rmse'], num_boost_round=1000, maximize=False, early_stopping_rounds=50)

# find the best number of trees from the cross-validation history
best_number_trees = hist['test-rmse-mean'].idxmin()

# since we have the best number of trees from cv, let's train the model with this number of trees
model = xgb.train(params, dtrain, num_boost_round=best_number_trees)
pred = model.predict(dtest)
print(
    f"rmse on testing instances is {mean_squared_error(pred, y_test)**0.5:.6f} with {best_number_trees} trees")

