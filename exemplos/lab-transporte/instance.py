import random
import sys

# Fornecedores: m [3, 10]
# Clientes: n [3, 10]
# Estoque: a [3, 20]
# Demanda: b [3, 10]
# Custos: c [1, 5]

m = None
n = None
estoque = None
demanda = None
custos = None

def gera(semente):
    global m, n, estoque, demanda, custos

    random.seed(semente)
    m = random.randint(3, 10)
    n = random.randint(3, 10)
    
    estoque = []
    for i in range(m):
        estoque.append(random.randint(3, 20))

    demanda = []
    for j in range(n):
        demanda.append(random.randint(3, 10))

    custos = []
    for i in range(m):
        custos.append([])
        for j in range(n):
            custos[i].append(random.randint(1, 5))


def mostra():
    print()
    print(f'Fornecedores m = {m}')
    print(f'Clientes n = {n}')
    print()
    print(f'Estoques: {estoque}')
    print(f'Demandas: {demanda}')
    print()
    print(f'Custos:')
    for l in custos:
        print(l)

#gera(1)
#mostra()