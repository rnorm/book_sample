library(lpSolve)

total = 10000.0
rate_of_return = c(0, 0.08, 0.12, 0.16, 0.14)
# define the objective function
f.obj = c(1, 1+rate_of_return[2], -1+(1+rate_of_return[3])^3, -1+(1+rate_of_return[4])^2, (1+rate_of_return[5])^3)
# define the constraints
f.con = t(array(c(1, 1, 0, 0, 1, 1, 1+rate_of_return[2], -1, -1, 0), c(5, 2)))
# define the direction in the constraints
f.dir = c("=", ">=")
# define the right hand side of the constraints
f.rhs = c(total, 0)

solution = lp("max", f.obj, f.con, f.dir, f.rhs)
cat('x:', solution$solution, '\n')
cat('obj:', solution$objval, '\n')
