from pulp import *
import matplotlib.pyplot as pl

prob = LpProblem("The Fitting Problem", LpMinimize)

# Variables
a = LpVariable("a")
c = LpVariable("c")
d = LpVariable("d")

# Objective
prob += d

# Constraints
points = [(1,3),(2,5),(3,7),(5,11),(7,14),(8,15),(10,19)]

for (i,j) in points:
	prob += a*i+j-c >= -d
	prob += a*i+j-c <= d

prob.solve()

# Solution
result = {}
for v in prob.variables():
   print v.name, "=", v.varValue
   result[v.name] = v.varValue

print "objective=", value(prob.objective)

# Plotting
px = [p[0] for p in points]
py = [p[1] for p in points]

lx = range(0,11,1)
ly = [-result['a']*x + result['c'] for x in lx]

fig1,ax1 = pl.subplots()
fonts = 18
ax1.set_title('Solution to Fitting Problem',size=fonts)
ax1.scatter(px,py,color='b',marker='o')
ax1.plot(lx,ly,color='g',linewidth=2)
ax1.set_xlabel('x',size=fonts)
ax1.set_ylabel('y',size=fonts)
ax1.set_xlim(0,10)

pl.show()