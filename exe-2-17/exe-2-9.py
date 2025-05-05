from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.e = Var(domain = NonNegativeReals)
model.d = Var(domain = NonNegativeReals)

# Usando uma função separada
def objective_function(model):
    return model.e + 2 * model.d

# Função objetivo
model.obj = Objective(rule = objective_function, sense = maximize)

# Usando funções para as restrições
def con1(model):
    return model.e + model.d <= 10

def con2(model):
    return model.e - model.d >= 0

def con3(model):
    return model.d <= 4


# Restrições
model.con1 = Constraint(rule = con1)
model.con2 = Constraint(rule = con2)
model.con3 = Constraint(rule = con3)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model).write()
print('\n\nOptimalsolution')
print('Study:',model.e())
print('Fun:',model.d())
print('Value:',model.obj())