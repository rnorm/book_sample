`%=%` = function(left, right) {
  # we require the RHS to be a list strictly
  stopifnot(is.list(right))
  # dest_env is the desitination environment enclosing the variables on LHS
  dest_env = parent.env(environment())
  left = substitute(left)
  
  recursive_assign = function(left, right, dest_env) {
    if (length(left) == 1) {
      assign(x = deparse(left),
             value = right,
             envir = dest_env)
      return()
    }
    if (length(left) != length(right) + 1) {
      stop("LHS and RHS must have the same shapes")
    }
    
    for (i in 2:length(left)) {
      recursive_assign(left[[i]], right[[i - 1]],  dest_env)
    }
  }
  
  recursive_assign(left, right, dest_env)
}

