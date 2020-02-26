'''
***** Exercício 6 *****
Dada a seguinte lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] imprima somente os números pares
dessa lista.
'''

# Cria a lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Armazena os números pares na lista "pares"
# Para isso é usado a indexação, começando no index 0, indo até o index 10 e pulando
# de dois em dois
pares = lista[1:10:2]

print("Números pares da lista: {}".format(pares))
