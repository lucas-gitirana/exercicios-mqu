from pyomo.environ import *
import sys

graph = []
s = None
t = None
n = None

# Read instance!
instance = open(sys.argv[1], 'r')
for line in instance.readlines():
    if line.startswith('c'): continue
    if line.startswith('p'):
        line = line.strip().split(' ')
        n = int(line[2])
        for _ in range(n):
            graph.append([0] * n)
        continue
    if line.startswith('e'):
        line = line.strip().split(' ')
        graph[int(line[1])][int(line[2])] = int(line[3])
        graph[int(line[2])][int(line[1])] = int(line[3])
    s = 0
    t = n - 1

# Solve it!
model = ConcreteModel()
model.flow = Var([i for i in range(n)], [j for j in range(n)], domain = Binary)

model.obj = Objective(expr = sum(model.flow[i, j] * graph[i][j] for i in range(n) for j in range(n)), sense = minimize)

model.cons = ConstraintList()

for i in range(n):
    b = 1 if i == s else -1 if i == t else 0
    model.cons.add(expr = ((sum(model.flow[i, j] for j in range(n))) - sum(model.flow[j, i] for j in range(n)) == b))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            model.cons.add(expr = model.flow[i, j] == 0)


results = SolverFactory('glpk').solve(model)
#results.write()

# Show it!
current = s
print(f'Shortest path: {current} ', end = '')
while current != t:
    for i in range(n):
        if model.flow[current, i]() == 1:
            print(f'{i} ', end = '')
            current = i
            continue
print(f'\nCost: {model.obj()}')