from pyomo.environ import *

# Criação dos dados
V = 100
A = 0.06
components = {
    'Cerveja A':    {'A': 0.058, 'P': 0.28},
    'Cerveja B':    {'A': 0.037, 'P': 0.25},
    'Água':         {'A': 0.000, 'P': 0.05},
    'Vinho':        {'A': 0.083, 'P': 0.40},
}

C = components.keys()


# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão (uma para cada componente)
model.x = Var(C, domain = NonNegativeReals)

# Usando uma função separada
def objective_function(model):
    result = 0
    for c in C:
        result += model.x[c] * components[c]['P']
    return result

# Função objetivo
# model.obj = Objective(rule = objective_function, sense = maximize)
model.cost = Objective(expr = sum(model.x[c] * components[c]['P'] for c in C))

# Restrições
model.vol = Constraint(expr = sum(model.x[c] for c in C) == V)
model.alc = Constraint(expr = sum(model.x[c] * components[c]['A'] for c in C) == A * V)

# Solução
opt = SolverFactory('glpk', executable= r'C:\ProgramData\chocolatey\bin\glpsol.exe')
opt.solve(model)

print('Misturaótima')
for c in C:
    print('>',c, ':',model.x[c](), 'litros')
print()
print('Volume=',model.vol(), 'litros')
print('Custo=$',model.cost())