'''
***** Exercício 5 *****
Faça um programa que peça o nome completo de uma pessoa e retorne o primeiro nome.
'''

# Leitura do nome
# Colocaremos o nome completo da pessoa em uma lista, sendo cada nome um item da
# lista.
nome = input("Digite seu nome completo: ").split(" ")

# Usa indexação para pegar o primeiro nome, que é o primeiro item da lista e armazena
# em uma variável
primeiro_nome = nome[0]

# Mostra na tela o primeiro nome da pessoa
print("Primeiro nome: {}".format(primeiro_nome))
