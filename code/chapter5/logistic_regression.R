library(R6)
LogisticRegression = R6Class(
  "LogisticRegression",
  public = list(
    coef = NULL,
    initialize = function() {
    },
    sigmoid = function(x) {
      1.0/(1.0 + exp(-x))
    },
    log_lik = function(beta, x, y) {
      linear = x %*% beta
      ll = sum(linear * y) - sum(log(1 + exp(linear)))
      return(-ll) # return negative log-likelihood
    },
    fit = function(x, y) {
      if (!is.matrix(x)) x = data.matrix(x)
      self$coef = optim(par=rep(0, 1+ncol(x)), fn=self$log_lik, x=cbind(1, x), y=y, method="L-BFGS-B")$par
    },
    predict = function(new_x) {
      if (!is.matrix(new_x)) new_x = data.matrix(new_x)
      linear = cbind(1, new_x) %*% self$coef
      self$sigmoid(linear)
    }
  )
)
