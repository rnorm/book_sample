library(R6)

# soft-thresholding operator
sto = function(z, theta){
  sign(z)*pmax(abs(z)-rep(theta,length(z)), 0.0)
}

Lasso = R6Class(
  "LassoLinearRegression",
  public = list(
    intercept = 0,
    beta = NULL,
    lambda = NULL,
    mu = NULL,
    sd = NULL,
    initialize = function(lambda) {
      self$lambda = lambda
    },
    scale = function(x) {
      self$mu = apply(x, 2, mean)
      self$sd = apply(x, 2, function(e) {
        sqrt((length(e)-1) / length(e))*sd(e)
      })
    },
    transform = function(x) t((t(x) - self$mu) / self$sd),
    fit = function(x, y, max_iter=100) {
      if (!is.matrix(x)) x = data.matrix(x)
      self$scale(x)
      x_transformed = self$transform(x)
      self$intercept = mean(y)
      y_centered = y - self$intercept
      gamma = 1/(eigen(t(x_transformed) %*% x_transformed, only.values=TRUE)$values[1])
      beta = rep(0, ncol(x))
      for (i in 1:max_iter){
        nabla = - t(x_transformed) %*% (y_centered - x_transformed %*% beta)
        z = beta - 2*gamma*nabla
        beta = sto(z, self$lambda*gamma)
      }
      self$beta = beta
    },
    predict = function(new_x) {
      if (!is.matrix(new_x)) new_x = data.matrix(new_x)
      self$transform(new_x) %*% self$beta + self$intercept
    }
  )
)

