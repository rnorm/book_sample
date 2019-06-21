log_lik = function(theta, x){
  mu = theta[1]
  sigma = theta[2]
  # we return the negative log-likelihood since optim is for minimization
  -(-length(x)*log(sigma) - 0.5/sigma^2*sum((x-mu)^2))
}

normal_mle = function(x){
  # par=c(0,1) as the initial values
  # lower=c(-Inf, 1e-6) for the lower bounds
  optim(par=c(0, 1), fn=log_lik, x=x, lower=c(-Inf, 1e-6), method="L-BFGS-B")$par
}

