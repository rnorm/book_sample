source('../chapter5/lasso.R')

library(caret)
library(MASS)
library(Metrics) # we use the rmse function from this package
k = 5

set.seed(42)
# if we set returnTrain = TRUE, we get the indices for train partition
test_indices = createFolds(Boston$medv, k = k, list = TRUE, returnTrain = FALSE)
scores = rep(NA, k)

for (i in 1:k){
  lr = Lasso$new(200)
  # we exclude the indices for test partition and train the model
  lr$fit(data.matrix(Boston[-test_indices[[i]], -ncol(Boston)]), Boston$medv[-test_indices[[i]]], 100)
  y_hat = lr$predict(data.matrix(Boston[test_indices[[i]], -ncol(Boston)]))
  scores[i] = rmse(Boston$medv[test_indices[[i]]], y_hat)
}
print(mean(scores))
