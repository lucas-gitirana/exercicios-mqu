from pyomo.environ import *
import instance
import sys

semente = int(sys.argv[1])

def mostra_solucao(model):
    print()
    print(f'Instância (semente): {semente}')
    
    print('    ', end = '')
    for j in range(instance.n):
        print(f' {j+1:5} ', end = '')
    print()
    print('  ' + '-' * (instance.n * 7 + 1))
    
    for i in range(instance.m):
        print(f'{i+1} | ', end = '')
        for j in range(instance.n):
            print(f' {model.x[i,j]():5} ', end = '')
        print()
    print()
    print('Custo total:', model.obj())


def resolve():
    instance.gera(semente)

    # Criação do modelo
    model = ConcreteModel()

    # Variáveis de decisão: para cada par depósito x cliente
    model.x = Var([i for i in range(instance.m)], [j for j in range(instance.n)], domain = NonNegativeReals)

    def objective_function(model):
        result = 0
        for i in range(instance.m):
            for j in range(instance.n):
                result += model.x[i,j] * instance.custos[i][j]
        return result

    # Função objetivo
    #model.obj = Objective(expr = sum(model.x[i,j]*instance.custos[i][j] for i in range(instance.m) for j in range(instance.n)))
    model.obj = Objective(rule = objective_function)

    # Restrições
    model.cons = ConstraintList()

    for i in range(instance.m):
        model.cons.add(expr = sum(model.x[i,j] for j in range(instance.n)) <= instance.estoque[i])

    for j in range(instance.n):
        model.cons.add(expr = sum(model.x[i,j] for i in range(instance.m)) == instance.demanda[j])

    # Solução
    solver = SolverFactory('glpk')
    #solver.solve(model).write()
    results = solver.solve(model)

    if results.solver.termination_condition == 'optimal':
        mostra_solucao(model)    
    else:
        #instance.mostra()
        print('Solução ótima não encontrada!')
    

resolve()