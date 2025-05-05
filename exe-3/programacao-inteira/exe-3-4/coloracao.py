from pyomo.environ import *
import sys

C = list(range(30))
graph = []

# Read instance!
instance = open(sys.argv[1], 'r')
for line in instance.readlines():
    if line.startswith('c'):
        continue
    if line.startswith('p'):
        parts = line.strip().split()
        n = int(parts[2])
        graph = [[] for _ in range(n + 1)]  # cria lista de adjacência
        continue
    if line.startswith('e'):
        parts = line.strip().split()
        u = int(parts[1])
        v = int(parts[2])
        graph[u].append(v)
        graph[v].append(u)  # se for grafo não direcionado

#graph = graph[1:]

# Modelage
model = ConcreteModel()
model.y = Var([i for i in range(len(C))], domain = Binary)
model.x = Var([v for v in range(1, len(graph))],[i for i in range(len(C))], domain = Binary)

model.obj = Objective(expr = sum( model.y[i] for i in range(len(C))), sense = minimize)

model.cons = ConstraintList()

for v in range(1, len(graph)):
    model.cons.add(sum(model.x[v,i] for i in range(len(C))) == 1)

for u in range(1, len(graph)):
    for v in graph[u]:
        for i in range(len(C)):
            model.cons.add(model.x[u,i] + model.x[v,i] <= model.y[i])

results = SolverFactory('glpk').solve(model)
print(model.obj())

# Show it!
for v in range(1, len(graph)):
    for i in range(len(C)):
            if (model.x[v,i].value == 1) :
                #print(model.x[v,i].value)
                print(f'O vértice {v} foi colorido com a cor {i}')

#print(graph)