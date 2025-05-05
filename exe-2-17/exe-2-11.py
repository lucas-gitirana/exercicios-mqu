from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.x1 = Var(domain = NonNegativeReals)
model.x2 = Var(domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = 8 * model.x1 + 6 * model.x2, sense = minimize)

# Restrições
model.constraints = ConstraintList()
model.constraints.add(expr = model.x1 >= 5)
model.constraints.add(expr = model.x1 <= 12)
model.constraints.add(expr = model.x2 >= 6)
model.constraints.add(expr = model.x2 <= 10)
model.constraints.add(expr = model.x1 + model.x2 >= 20)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model).write()
print('\n\nOptimalsolution')
print('Study:',model.x1())
print('Fun:',model.x2())
print('Value:',model.obj())