#Potencia
def pot2(x):
    return x ** 2

pot2_ = lambda x: x**2

print(pot2_(10))

# Fatorial
def fat(n):
    if(n == 0):
        return 1
    return (n * fat(n - 1))

print(fat(5))

fat_ = lambda n: n * fat_(n -1) if n > 1 else 1

print(fat_(5))

# Map
lista = [1, 2, 3]

m = map(lambda x: x**2, lista)

for i in m:
    print(i)

# Reduce
import functools

print(functools.reduce(lambda x,y: x*y, [1, 2, 3, 4]))

# Filter
f = filter(lambda x: x%2 == 0, range(10))

for i in f:
    print(i)