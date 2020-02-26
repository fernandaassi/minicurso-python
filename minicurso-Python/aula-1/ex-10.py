'''
***** Exercício 10 *****
Leia um nome pelo teclado e imprima "Olá, <nome lido>!"
'''

# Para ler um nome do teclado vamos usar a função input() e guardar o resultado
# na variável "nome"
# A mensagem para o usuário fica dentro dos parênteses do input()
nome = input("Informe seu nome: ")

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("Olá, {}".format(nome))
