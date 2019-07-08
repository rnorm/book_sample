library(xgboost)
library(MASS)
library(Metrics)

set.seed(42)
train_index = sample(nrow(Boston), floor(0.8 * nrow(Boston)), replace = FALSE)
Boston = data.matrix(Boston)
target_col = which(colnames(Boston) == 'medv')
X_train = Boston[train_index, -target_col]
y_train = Boston[train_index, target_col]
X_test = Boston[-train_index, -target_col]
y_test = Boston[-train_index, target_col]
# prepare the data for training and testing
dTrain = xgb.DMatrix(X_train, label = y_train)
dTest = xgb.DMatrix(X_test)
params = list(
  "booster" = "gbtree",
  "objective" = "reg:linear",
  "eta" = 0.1,
  "max_depth" = 5,
  "subsample" = 0.6,
  "colsample_bytree" = 0.8,
  "min_child_weight" = 2
)
# run the cross-validation
hist = xgb.cv(
  params = params,
  data = dTrain,
  nrounds = 500,
  early_stopping_rounds = 50,
  metrics = 'rmse',
  nfold = 5,
  verbose = FALSE
)
# since we have the best number of trees from cv, let's train the model with this number of trees
model = xgb.train(params, nrounds = hist$best_iteration, data = dTrain)
pred = predict(model, dTest)

cat(
  "rmse on testing instances is",
  rmse(y_test, pred),
  "with",
  hist$best_iteration,
  "trees"
)

