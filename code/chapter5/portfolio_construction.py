from ortools.linear_solver import pywraplp

total = 10000.0
rate_of_return = [0.0, 0.08, 0.12, 0.16, 0.14]
solver=pywraplp.Solver('PortfolioConstruction',pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# create the variables
x=[None]*5
for i in range(5):
    x[i]=solver.NumVar(0.0, solver.infinity(), 'x'+str(i))

# create the constraints
constraints = [None]*2
# set the equality constraint
constraints[0] = solver.Constraint(total, total)
constraints[0].SetCoefficient(x[0], 1.0)
constraints[0].SetCoefficient(x[1], 1.0)
constraints[0].SetCoefficient(x[4], 1.0)
# set the inequality constraint
constraints[1] = solver.Constraint(0.0, solver.infinity())
constraints[1].SetCoefficient(x[0], 1.0)
constraints[1].SetCoefficient(x[1], 1.0+rate_of_return[1])
constraints[1].SetCoefficient(x[2], -1.0)
constraints[1].SetCoefficient(x[3], -1.0)

# set objective function
objective = solver.Objective()
objective.SetCoefficient(x[0], 1.0)
objective.SetCoefficient(x[1], 1.0+rate_of_return[1])
objective.SetCoefficient(x[2], -1.0+(1+rate_of_return[2])**3)
objective.SetCoefficient(x[3], -1.0+(1+rate_of_return[3])**2)
objective.SetCoefficient(x[4], (1+rate_of_return[4])**3)
# we want to maximize the objective function
objective.SetMaximization()
status = solver.Solve()
if status == solver.OPTIMAL:
    sol = [e.solution_value() for e in x]
    print("x: {0}".format(sol))
    print("objective: {0}".format(objective.Value()))

