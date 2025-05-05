from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x = Var([1,2], domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = model.x[1] + 25 * model.x[2], sense = maximize)

# Restrições
model.con1 = Constraint(expr = 15 * model.x[1] + 300 * model.x[2] <= 10000)
model.con2 = Constraint(expr = model.x[1] - 2 * model.x[2] >= 0)
model.con3 = Constraint(expr = model.x[1] <= 400)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
results = opt.solve(model)

print('Status:', results.solver.status)
print('Termination criterion:', results.solver.termination_condition)
if results.solver.termination_condition == 'optimal':
    print('Optimal solution cost: ', model.obj.expr())
    print('Optimal solution is x1 =', model.x[1].value, 'and x2 =', model.x[2].value)