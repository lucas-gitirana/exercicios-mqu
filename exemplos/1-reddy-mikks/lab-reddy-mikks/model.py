from pyomo.environ import *

def solve(data):
    model = ConcreteModel()
    model.x = Var([1,2], domain = NonNegativeReals)

    model.obj = Objective(expr = data['lucro'][0] * model.x[1] + data['lucro'][1] * model.x[2], sense = maximize)
    
    model.con1 = Constraint(expr = data['uso_m1'][0] * model.x[1] + data['uso_m1'][1] * model.x[2] <= data['estoque'][0])
    model.con2 = Constraint(expr = data['uso_m2'][0] * model.x[1] + data['uso_m2'][1] * model.x[2] <= data['estoque'][1])
    model.con3 = Constraint(expr = -model.x[1] + model.x[2] <= 1)
    model.con4 = Constraint(expr = model.x[2] <= data['limite'][1])
    model.con5 = Constraint(expr = model.x[1] <= data['limite'][0])

    opt = SolverFactory('glpk')
    results = opt.solve(model)

    tc = results.solver.termination_condition
    if tc == 'optimal':
        return model.x[1].value, model.x[2].value, model.obj.expr()
    else:
        return tc