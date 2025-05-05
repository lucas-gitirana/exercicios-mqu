from pyomo.environ import *

instances = []
with open('./instances.txt', 'r') as file:
    lines = file.readlines()[1:] 
    for line in lines:
        content = line.strip().split(',')
        capital = int(content[0])
        investimentos = int(content[1])
        rendimentos = [float(x) for x in content[2][1:-1].split(';')]
        minimos = [float(x) for x in content[3][1:-1].split(';')]
        maximos = [float(x) for x in content[4][1:-1].split(';')]
        instances.append({
            'C': capital,
            'n': investimentos,
            'r': rendimentos,
            'm1': minimos,
            'm2': maximos
        })

def solve(instance):
    model = ConcreteModel()
    model.x = Var(range(instance['n']), domain=NonNegativeReals)
    model.obj = Objective(expr=sum(model.x[i] * instance['r'][i] for i in range(instance['n'])), sense=maximize)
    model.constraints = ConstraintList()
    model.constraints.add(sum(model.x[i] for i in range(instance['n'])) == instance['C'])
    for j in range(instance['n']):
        model.constraints.add(model.x[j] >= instance['m1'][j] * sum(model.x[i] for i in range(instance['n'])))
        model.constraints.add(model.x[j] <= instance['m2'][j] * sum(model.x[i] for i in range(instance['n'])))
        
    solver = SolverFactory('glpk')
    results = solver.solve(model)

    print(results.solver.termination_condition, end='')
    if results.solver.termination_condition == 'optimal':
        print(':', end='')
        for i in range(instance['n']):
            print(f'{model.x[i]()},', end='')
        print(model.obj())
    else:
        print()

for instance in instances:
    solve(instance)