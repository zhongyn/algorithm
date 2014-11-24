from pulp import *

prob = LpProblem("The Tofu Problem", LpMaximize)

# Variables
x1 = LpVariable("x1", 0)
y1 = LpVariable("y1", 0)
z1 = LpVariable("z1", 0)
x2 = LpVariable("x2", 0)
y2 = LpVariable("y2", 0)
z2 = LpVariable("z2", 0)
x3 = LpVariable("x3", 0)
y3 = LpVariable("y3", 0)
z3 = LpVariable("z3", 0)

# Objective
prob += 4*x1 + 12*x2 + 7*x3 + 8*y1 + 14*y2 + 11*y3 + 4*z1 + 13*z2 + 9*z3

# Constraints
prob += x1+x2+x3 == 400
prob += y1+y2+y3 == 480
prob += z1+z2+z3 == 230
prob += x2+y2+z2 <= 420
prob += x3+y3+z3 <= 250

prob.solve()

# Solution
for v in prob.variables():
   print v.name, "=", v.varValue

print "objective=", value(prob.objective)