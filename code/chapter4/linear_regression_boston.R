source('linear_regression.R')

library(MASS) # load Boston data from this package

lr = LR$new()
# -i means excluding the ith column from the data.frame
lr$fit(data.matrix(Boston[,-ncol(Boston)]),Boston$medv)
print(lr$coef)
# let's make prediction on the same data
pred=lr$predict(data.matrix(Boston[,-ncol(Boston)]))
print(pred[1:5])

# compare it with the R built-in linear regression model
rlm = lm(medv ~ ., data=Boston)
print(rlm$coef)
print(rlm$fitted[1:5])
