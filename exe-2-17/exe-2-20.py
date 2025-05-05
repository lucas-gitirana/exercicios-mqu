from pyomo.environ import *

# Criação dos dados
m=3 #fornecedores
n=3 #clientes
a=[5, 7,3] #estoques
b=[7, 3,5] #demandas
c=[[3, 1, 100], #custos
   [4,2,4],
   [100,3,3]]

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão (uma para cada componente)
model.x = Var([i for i in range(m)],[j for j in range(n)], domain = NonNegativeReals)

# Função objetivo
def objective_function(model):
    sum = 0
    for i in range(m):
        for j in range(n):
            sum += c[i][j] * model.x[i, j]
    return sum

model.obj = Objective(rule = objective_function, sense = minimize)

# Restrições
model.cons = ConstraintList()

for i in range(m):
    model.cons.add(expr = sum(model.x[i,j] for j in range(n)) <= a[i])

for j in range(n):
    model.cons.add(expr = sum(model.x[i,j] for i in range(m)) == b[j])

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model).write()

print('Custototal:',model.obj())
for i in range(m):
    for j in range(n):
        print(i+1, '-->',j+ 1, ':',model.x[i,j]())