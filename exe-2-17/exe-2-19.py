from pyomo.environ import *

# Criação dos dados
m=10
T=28
V=83
D=[1.3,0.7, 1.8, 1.1, 1.0, 1.5,0.9,0.8,1.0,1.2]
Q=[10, 12, 40,21,5,5,8,17,6, 9]
R=[5, 3,2.2,4,1.8,4.1,3.7,1.9,6,2]

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão (uma para cada componente)
model.x = Var(range(m), domain = NonNegativeReals)

# Função objetivo
model.obj = Objective(expr = sum(model.x[i] * R[i] for i in range(m)), sense = maximize)

# Restrições
model.vol = Constraint(expr = sum(model.x[i] for i in range(m)) <= V)
model.ton = Constraint(expr = sum(model.x[i] * D[i] for i in range(m)) <= T)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model)

print('Funçãoobjetivo:',model.obj())
for i in range(m):
    print(f'Grão {i+1}: {model.x[i]()} m3.')