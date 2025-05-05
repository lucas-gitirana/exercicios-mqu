import random

amount = 100

print('capital,investimentos,rendimentos,minimos,maximos')

for _ in range(amount):
    print(random.randint(1000,40000), end=',')
    n_investments = random.randint(2, 10)
    print(n_investments, end=',')

    print('{', end='')
    for i in range(n_investments):
        print(round(random.random()*0.14+0.01,2), end='')
        if i != n_investments - 1: print(';', end='')
    print('}', end=',')

    print('{', end='')
    for i in range(n_investments):
        print(min(round(random.random()*(1/n_investments-0.01),2),0.3), end='')
        if i != n_investments - 1: print(';', end='')
    print('}', end=',')

    print('{', end='')
    total = 0
    for i in range(n_investments):
        value = round(random.random()*0.4+0.2,2)
        value = max(value, 0.3)
        if i != n_investments - 1:
            total += value
            print(value, end='')
            print(';', end='')
        else:
            value = value if total >= 1 else round(1 - total + 0.2, 2)
            print(value, end='')
    print('}', end='\n')