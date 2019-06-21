# Fatorial
def fat(n):
    if(n == 0):
        return 1
    return n * fat(n - 1)

'''
Fatorial de 3:

3! = 3 * 2 * 1 = 6

fat(3)
    3 * fat(2)
    fat(2)
        2 * fat(1)
        fat(1)
            1 * fat(0)
            fat(0) = 1
'''
# Fibonacci
'''
A soma do primeiro número com o segundo número é o 
resultado do terceiro número
fibonacci = 1, 1, 2, 3, 5, 8, 13...
'''

def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(6))

# Potencialização
'''
    base, exp
    base = 2
    exp = 10
    2 ** 10 = 1024
'''
def pot(base, exp):
    if(exp == 0):
        return 1
    return base * pot(base, exp - 1)

print(pot(2, 10))