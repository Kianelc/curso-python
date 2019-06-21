lista = [1, 2, 3]
lista2 = (1, 2, 3, 4)

a, b, c = lista

print(a)
print(b)
print(c)

print('-------------')

d, _, e, _ = lista2

print(d)
print(e)

print('-------------')

nome = 'abc'

c1, c2, _ = nome

print(c1)
print(c2)

print('-------------')

def func(x, y = 4):
    return x**2, y**2

print(func(2,3))

r1, r2 = func(2)

print('r1: ', r1)
print('r2: ', r2)