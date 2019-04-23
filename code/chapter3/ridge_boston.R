source('linear_regression_ridge.R')

library(MASS) # load Boston data from this package

# let's try lmabda = 0.5
ridge = LR_Ridge$new(0.5)
ridge$fit(data.matrix(Boston[,-ncol(Boston)]),Boston$medv)
print(ridge$coef)
# let's make prediction on the same data
pred=ridge$predict(data.matrix(Boston[,-ncol(Boston)]))
print(pred[1:5])

