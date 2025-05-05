from pyomo.environ import *

#Criação do modelo
model = ConcreteModel()

n = 20
v = [4, 5, 1, 2, 7, 8, 6, 4, 2, 3, 8, 6, 4, 5, 2, 1, 3, 6, 7, 9]
p = [5, 2, 1, 4, 8, 7, 9, 5, 4, 1, 6, 7, 4, 8, 9, 4, 3, 2, 6, 8]
P = 35

#Variáveis de decisão
model.x = Var(range(n), domain = Boolean)

#Função objetivo
model.obj = Objective(expr = sum([model.x[i] * v[i] for i in range(n)]), sense = maximize)

#Restrições
model.const1 = Constraint(expr = sum([p[i] * model.x[i] for i in range(n)]) <= P)

#Solução
# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model, timelimit = 10).write()
for i in range(n):
    print(model.x[i]())
print()
print(model.obj.expr())