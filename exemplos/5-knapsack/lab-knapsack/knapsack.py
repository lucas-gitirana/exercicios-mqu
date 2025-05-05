from pyomo.environ import *
import sys

n = None
P = None
values = None
weights = None

def read_instance(instance):
    global n, P, values, weights
    values = []
    weights = []
    file = open(instance, 'r')
    first = True
    for line in file.readlines():
        if first:
            n = int(line.split(' ')[0])
            P = int(line.split(' ')[1])
            first = False
            continue
        values.append(float(line.split(' ')[0]))
        weights.append(float(line.split(' ')[1]))
    
def solve():
    # Criação do modelo
    model = ConcreteModel()

    # Variáveis de decisão
    model.x = Var(range(n), domain = Boolean)

    # Função objetivo
    model.obj = Objective(expr = sum([values[i] * model.x[i] for i in range(n)]), sense = maximize)

    # Restrições
    model.con1 = Constraint(expr = sum([weights[i] * model.x[i] for i in range(n)]) <= P)

    # Solução
    opt = SolverFactory('glpk')
    #opt.solve(model).write()
    opt.solve(model)
    #for i in range(n):
    #    print(model.x[i]())
    return model.obj.expr()

#instance = sys.argv[1]
#read_instance(instance)
#print(solve())

from glob import glob
for instance in glob('./instances/low-dimensional/*'):
    read_instance(instance)
    print(instance[instance.rindex('/') + 1:] + ': ', end = '')
    print(solve())
