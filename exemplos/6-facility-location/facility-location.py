f = [15,13,3,14,5]
C = [[0,2,8,4,7],
     [1,0,3,6,5],
     [1,7,0,4,3],
     [1,8,4,0,5],
     [5,3,9,4,0]]
n = len(C)
k = 2

from pyomo.environ import *

model = ConcreteModel()

model.y = Var([j for j in range(n)], domain=Binary)

model.x = Var([i for i in range(n)], [j for j in range(n)], domain=Binary)

def objective_function(model):
    installation_cost = 0
    attending_cost = 0
    for j in range(n):
        installation_cost += model.y[j] * f[j]
        for i in range(n):
            attending_cost += model.x[i,j] * C[i][j]
    return installation_cost + attending_cost

model.obj = Objective(rule=objective_function, sense=minimize)

model.cons = ConstraintList()

model.cons.add(sum(model.y[j] for j in range(n)) <= k)

for i in range(n):  
    model.cons.add(sum(model.x[i,j] for j in range(n)) == 1)

for i in range(n):
    for j in range(n):
        model.cons.add(model.x[i,j] <= model.y[j])

solver = SolverFactory('glpk')
solver.solve(model).write()

print('Custo total:', model.obj())
for j in range(n):
    for i in range(n):
        if model.x[i,j]() == 0: continue
        print(f'Cidade {i + 1} é atendida pela cidade {j + 1}')
