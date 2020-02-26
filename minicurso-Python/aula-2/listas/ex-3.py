'''
***** Exercício 3 *****
Dado uma lista de números (deve ser lida do teclado), ordene-a e em seguida inverta a
ordem desta lista.
'''

# Le a lista
lista_numeros = input("Digite uma lista de números sepadados por espaço: ").split(" ")

# Imprime a lista que foi digitada pelo usuário
print("Lista digitada: {}".format(lista_numeros))

# Ordena os elementos da lista.
# Uso da função sort() para fazer a ordenação
lista_numeros.sort()

# Imprime a lista ordenada
print("Lista ordenada: {}".format(lista_numeros))

# Inverte a lista (que está ordenada)
lista_numeros.reverse()

# Imprime a lista invertida
print("Lista invertida: {}".format(lista_numeros))
