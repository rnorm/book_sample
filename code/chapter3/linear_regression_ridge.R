library(R6)
LR_Ridge = R6Class(
  "LR_Ridge",
  public = list(
    coef = NULL,
    mu = NULL,
    sd = NULL,
    lambda = NULL,
    initialize = function(lambda) {
      self$lambda = lambda
    },
    scale = function(x) {
      self$mu = apply(x, 2, mean)
      self$sd = apply(x, 2, function(e) {
        sqrt((length(e) - 1) / length(e)) * sd(e)
      })
    },
    transform = function(x) {
      return(t((t(x) - self$mu) / self$sd))
    },
    fit = function(x, y) {
      self$scale(x)
      x_transformed = self$transform(x)
      x_lambda = rbind(x_transformed, diag(rep(sqrt(self$lambda), ncol(x))))
      y_lambda = c(y, rep(0, ncol(x)))
      self$qr_solver(cbind(c(rep(1, nrow(
        x
      )), rep(0, ncol(
        x
      ))), x_lambda), y_lambda)
    },
    qr_solver = function(x, y) {
      self$coef = qr.coef(qr(x), y)
    },
    predict = function(new_x) {
      new_x_transformed = self$transform(new_x)
      cbind(rep(1, nrow(new_x)), new_x_transformed) %*% self$coef
    }
  )
)