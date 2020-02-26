'''
***** Exercício 11 *****
Leia o nome do aluno, e a nota das três provas dele. Em seguida, calcule sua média
(média aritmética simples)
'''

# Para ler um nome do teclado vamos usar a função input() e guardar o resultado
# na variável "nome_aluno"
# A mensagem para o usuário fica dentro dos parênteses do input()
nome_aluno = input("Informe o nome do aluno: ")

# Também vamos usar a função input() para ler as 3 notas do aluno, porém é
# necessário transformar os valores em float, já que a função input()
# por definição lê os valores no formato de string
nota1 = float(input("Informe a nota da primeira prova do aluno: "))
nota2 = float(input("Informe a nota da segunda prova do aluno: "))
nota3 = float(input("Informe a nota da terceira prova do aluno: "))

# media: media do aluno das 3 provas (media aritmética simples)
media = (nota1 + nota2 + nota3) / 3


# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format().
print("A média de {} é {}".format(nome_aluno, media))
