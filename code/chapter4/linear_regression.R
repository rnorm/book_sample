
library(R6)
LR = R6Class(
  "LR",
  public = list(
    coef = NULL,
    initialize = function() {
      
    },
    fit = function(x, y) {
      self$qr_solver(cbind(1, x), y)
    },
    qr_solver = function(x, y) {
      self$coef = qr.coef(qr(x), y)
    },
    predict = function(new_x) {
      cbind(1, new_x) %*% self$coef
    }
  )
)
