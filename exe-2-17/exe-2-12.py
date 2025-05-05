from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = model.x1 + model.x2, sense = minimize)

# Restrições
model.constraints = ConstraintList()
model.constraints.add(expr = 0.2 * model.x1 + 0.1 * model.x2 >= 14)
model.constraints.add(expr = 0.25 * model.x1 + 0.6 * model.x2 >= 30)
model.constraints.add(expr = 0.1 * model.x1 + 0.15 * model.x2 >= 10)
model.constraints.add(expr = 0.15 * model.x1 + 0.1 * model.x2 >= 8)
model.constraints.add(expr = 0.6 * model.x1 - 0.4 * model.x2 >= 0)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model).write()
print('\n\nOptimalsolution')
print('X1:',model.x1())
print('X2:',model.x2())
print('Value:',model.obj())