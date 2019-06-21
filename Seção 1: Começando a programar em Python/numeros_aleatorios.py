import random

# Retorna um número aleatório entre 0 a 3
print(random.randrange(4))

# Retorna um número aleatório entre 1 e 4
print(random.randint(1,4))

# Retorna um elemento aleatório da lista
lista = [1, 2, 3, 4]
print(random.choice(lista))

# Embaralha os elementos da lista
random.shuffle(lista)
print(lista)

# Pega dois elementos aleatórios da lista
print(random.sample(lista, 2))

# Gera um número flutuante entre 0 e 1
print(random.random())

# Gera um número flutuante entre 1 e 10
print(random.uniform(1, 10))