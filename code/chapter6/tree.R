library(R6)
Tree = R6Class(
  "Tree",
  public = list(
    left = NULL,
    right = NULL,
    variable_id = NULL,
    break_point = NULL,
    val = NULL,
    initialize = function(left, right, variable_id, break_point, val) {
      self$left = left
      self$right = right
      self$variable_id = variable_id
      self$break_point = break_point
      self$val = val
    },
    is_leaf = function() {
      is.null(self$left) && is.null(self$right)
    },
    depth = function() {
      if (self$is_leaf()) {
        1
      } else if (is.null(self$left)) {
        1 + self$right$depth()
      } else if (is.null(self$right)) {
        1 + self$left$depth()
      } else{
        1 + max(self$left$depth(), self$right$depth())
      }
    },
    predict_single = function(x) {
      # if x is a vector
      if (self$is_leaf()) {
        self$val
      } else{
        if (x[self$variable_id] < self$break_point) {
          self$left$predict_single(x)
        } else{
          self$right$predict_single(x)
        }
      }
    },
    predict = function(x) {
      # if x is an array
      preds = rep(0.0, nrow(x))
      for (i in 1:nrow(x)) {
        preds[i] = self$predict_single(x[i, ])
      }
      preds
    },
    print = function() {
      # we can call print(tree), similar to the magic method in Python
      cat("variable_id:", self$variable_id, "\n")
      cat("break at:", self$break_point, "\n")
      cat("is_leaf:", self$is_leaf(), "\n")
      cat("val:", self$val, "\n")
      cat("depth:", self$depth(), "\n")
      invisible(self)
    }
  )
)

