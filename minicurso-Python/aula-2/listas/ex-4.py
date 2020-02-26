'''
***** Exercício 4 *****
Leia uma frase e retorne a primeira e a última palavra
'''

# Leitura da frase.
# Colocaremos a frase em uma lista, sendo cada palavra um item da lista
frase = input("Digite uma frase: ").split(" ")

# Usa indexação para pegar a primeira palavra da lista e armazena em uma variável
primeira_palavra = frase[0]
# Usa indexação para pegar a última palavra da lista, neste caso será o índice do
# tamanho da lista - 1. Para saber o tamanho da lista, usa-se a funçaõ len().
ultima_palavra = frase[len(frase) - 1]

# Mostra na tela o resultado da primeira e da última palavra
print("Primeira palavra: {}".format(primeira_palavra))
print("Ultima palavra: {}".format(ultima_palavra))
