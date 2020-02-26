'''
***** Exercício 12 *****
Leia o nome de uma pessoa, a sua idade, altura, sexo, peso e se é fumante ou não. Em
seguida, imprima uma fixa desta pessoa com essas informações.
'''

# Para ler um as informações vamos usar a função input() e guardar o resultado
# nas respectivas variáveis
# Para as informações que não são strings precisaremos colocar o tipo do dado (int
# ou float) antes do input()
# A mensagem para o usuário fica dentro dos parênteses do input()
nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo: ")
peso = float(input("Informe seu peso: "))
fumante = input("Informe se é fumante: ")

# Vamos mostrar o resultado do exercício na tela.
# Neste caso usaremos dois print(): Um para cada informação dada
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()

print("Nome: {}".format(nome))
print("Idade: {} anos".format(idade))
print("Altura: {} metros".format(altura))
print("Sexo: {}".format(sexo))
print("Peso: {}kg".format(peso))
print("Fumante: {}".format(fumante))
