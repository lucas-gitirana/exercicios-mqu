from pyomo.environ import *
import sys
import instance

semente = int(sys.argv[1])
instance.gera(semente)

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
    # Criação do modelo
    model = ConcreteModel()

    # Variáveis de decisão (uma para cada componente)
    model.x = Var([i for i in range(instance.m)],[j for j in range(instance.n)], domain = NonNegativeReals)

    # Função objetivo
    def objective_function(model):
        sum = 0
        for i in range(instance.m):
            for j in range(instance.n):
                sum += instance.custos[i][j] * model.x[i, j]
        return sum

    model.obj = Objective(rule = objective_function, sense = minimize)

    # Restrições
    model.cons = ConstraintList()

    for i in range(instance.m):
        model.cons.add(expr = sum(model.x[i,j] for j in range(instance.n)) <= instance.estoque[i])

    for j in range(instance.n):
        model.cons.add(expr = sum(model.x[i,j] for i in range(instance.m)) == instance.demanda[j])

    # Solução
    opt = SolverFactory('glpk', executable=r'C:\ProgramData\chocolatey\bin\glpsol.exe')
    resultado = opt.solve(model)

    if resultado.solver.termination_condition == TerminationCondition.optimal:
        mostra_solucao(model)
    else:
        print('Solução ótima não encontrada!')

resolve()