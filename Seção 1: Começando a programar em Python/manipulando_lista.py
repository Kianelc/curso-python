lista = [1, 2, 3, 'Kiane']
lista2 = [6, 9, 10]
lista3 = lista + lista2

# Remove o primeiro elemento
lista.pop(0)

# Remove o ultimo elemento
lista.pop(len(lista) - 1)

# Remove pelo elemento e Pop remove pelo índice
lista2.remove(6)

for i in lista3:
    print(i)

# Tamanho da lista
print(len(lista3))

# Transforma a lista em uma tupla (sabemos que está em uma tupla, pois os números estão entre parênteses)
t_lista = tuple(lista)
print(t_lista)

# Acrescenta elementos ao final da lista
lista.append(11)

# Insere um elemento na lista, o primeiro parâmetro é a posição e o segundo o número
lista.insert(1, 10)

# Insere na ultima posição
lista.insert(len(lista), 5)

# Ordenar uma lista
lista.sort()

# Exibir o ultimo elemento da lista
print(lista[-1])

# Exibir o segundo elemento e o terceiro
print(lista[1:3])

# Exibe todos os número depois do segundo elemento
print(lista[1:])

# Inverter lista
print(lista[::-1])