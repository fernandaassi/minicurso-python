# Exercícios Capítulo 4 da apostila

'''
***** Exercício 1 *****
Calcule o resto da divisão de 10 por 3
'''
# cria a variável "resto" e coloca o resto da divisão (módulo) de 10 por 3 dentro dela
resto = 10 % 3

# mostra na tela o resultado calculado.
# os {} são substituídos pelo o que esta dentro de .format(), que no caso é a variável
# "resto".
print("O resto da divião de 10 por 3 é: {}".format(resto))



'''
***** Exercício 2 *****
Calcule a tabuada do 13
'''

# Como neste ponto do curso, nossos conhecimentos ainda estão limitados, a tabuada
# será calculada manualmente.

# Colocamos o texto de desejamos imprimir na tela e as {} são substituídos pelo valor
# da etapa da tabuada que está nos parenteses de .format()
print("1 x 13 = {}".format(1*13))
print("2 x 13 = {}".format(2*13))
print("3 x 13 = {}".format(3*13))
print("4 x 13 = {}".format(4*13))
print("5 x 13 = {}".format(5*13))
print("6 x 13 = {}".format(6*13))
print("7 x 13 = {}".format(7*13))
print("8 x 13 = {}".format(8*13))
print("9 x 13 = {}".format(9*13))
print("10 x 13 = {}".format(10*13))


'''
***** Exercício 3 *****
Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75%
delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana,
durante quatro meses. Ajude o Davinir!
'''

# n_aulas_semana: número de aulas em uma semana
n_aulas_semana = 2
# n_semanas_mes: número de semanas em um mês
n_semanas_mes = 4
# n_aulas_mes: número de aulas em um mes
n_aulas_mes = n_aulas_semana * n_semanas_mes
# n_meses: quantidades de meses do curso
n_meses = 4
# total_aulas: total de aulas do curso
total_aulas = n_aulas_mes * n_meses

# Se ele é obrigado a comparecer a 75% das aulas, isso significa que ele pode faltar
# 25% das aulas. Em decimal isso é 0.25
# total_faltas: numero de faltas que Devanir pode faltar
total_faltas = total_aulas * 0.25

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("O número de faltas que Devanir pode ter é {}".format(total_faltas))


'''
***** Exercício 4 *****
Calcule a área de um círculo de raio r = 2
'''

# raio: raio do círculo
raio = 2
# pi: valor do número pi
pi = 3.14

# area = area do círculo
area = pi * raio**2

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("A área do círculo é: {}".format(area))


'''
***** Exercício 5 *****
Quantos segundos há em 3 horas, 23 minutos e 17 segundos?
'''

# minutos: quantidade de segundos em um minuto (60 segundos)
minutos = 60
#horas: quantidade de segundos em uma hora.
# Uma hora possui 60 minutos, ou seja possui 60 * a quantidade de segundos em
# um minuto
horas = 60 * minutos

# total_segundos: total de segundos em 3 horas, 23 minutos e 17 segundos
total_segundos = 3*horas + 23*minutos + 17

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("Há {} segundos em 3 horas, 23 minutos e 17 segundos".format(total_segundos))


'''
***** Exercício 6 *****
Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua
velocidade média em m/s?
'''

# A velocidade média em metros por segundo (m/s) é calculada pelo divisão do total de
# metros percorridos pelo total de segundos gastos.

# Ou seja, precisamos saber quantos metros existem em 65 kilômetros e quantos segundos
# existem em 3 horas, 23 minutos e 17 segundos (exercício 5)

# Quantos metros existem em 65 kilômetros
# km: quantidade me metros em um kilômetro
km = 1000
# total_metros: total de metros percorridos
total_metros = 65 * km

# Quantos segundos existem em 3 horas, 23 minutos e 17 segundos
# minutos: quantidade de segundos em um minuto (60 segundos)
minutos = 60
#horas: quantidade de segundos em uma hora.
# Uma hora possui 60 minutos, ou seja possui 60 * a quantidade de segundos em
# um minuto
horas = 60 * minutos
# tempo total de segundos em 3 horas, 23 minutos e 17 segundos
total_segundos = 3*horas + 23*minutos + 17

# velocidade_media = velocidade media em metros por segundo
velocidade_media = total_metros / total_segundos

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("A velocidade média é de: {}m/s".format(velocidade_media))


'''
***** Exercício 7 *****
Resolva esta expressão:
(100 - 413 * (20 - 5 * 4)) / 5
'''

# Calculo do numerador
numerador = 100 - 413 * (20 - 5 * 4)
# Calculo do dedominador
dedominador = 5

# Calculo do resultado da divisão
divisao = numerador / dedominador

# Vamos mostrar o resultado do exercício na tela.
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("O resultado da expressao é: {}".format(divisao))


'''
***** Exercício 8 *****
Enivaldo quer ligar três capacitores, de valores:
• C1 = 10μF
• C2 = 22μF
• C3 = 6.8μF
Se ele ligar os três em paralelo, a capacitância resultante é a soma:
Cp = C1 + C2 + C3
Se ele ligar os três em série, a capacitância resultante é:
Cs = 1 / (1/C1 + 1/C2 + 1/C3)
Qual é o valor resultante em cada um desses casos?
'''

# Valores das capacitancias c1, c2 e c3
c1 = 10
c2 = 22
c3 = 6.8

# Valor da capacitancia em paralelo (fórmula dada pela questão)
cp = c1 + c2 + c3

# Valor da capacitancia em serie (fórmula dada pela questão)
cs = 1 / (1/c1 + 1/c2 + 1/c3)

# Vamos mostrar o resultado do exercício na tela.
# Neste caso usaremos dois print(): Um pra capacitancia em paralelo e outro para a
# capacitancia em serie
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("Valor resultante em paralelo: {}".format(cp))
print("Valor resultante em serie: {}".format(cs))


'''
***** Exercício 9 *****
Refaça o exercício anterior, porém para quaisquer valores de capacitores.
'''



# Neste caso precisamos pegar o valor do teclado.
# Para isso usamos a função input().
# Porém é necessário transformar os valores em float, já que a função input()
# por definição lê os valores no formato de string
# A mensagem para o usuário fica dentro dos parênteses do input()
# Pegaremos os valores para o capacitor 1, 2 e 3 (c1, c2 e c3 respectivamente)
c1 = float(input("Informe o valor do capacitor 1: "))
c2 = float(input("Informe o valor do capacitor 2: "))
c3 = float(input("Informe o valor do capacitor 3: "))

# Valor da capacitancia em paralelo (fórmula dada pela questão)
cp = c1 + c2 + c3

# Valor da capacitancia em serie (fórmula dada pela questão)
cs = 1 / (1/c1 + 1/c2 + 1/c3)

# Vamos mostrar o resultado do exercício na tela.
# Neste caso usaremos dois print(): Um pra capacitancia em paralelo e outro para a
# capacitancia em serie
# O que esta entre "" é o texto que vamos mostrar e as {} é substituída pelo o que
# está no parenteses de .format()
print("Valor resultante em paralelo: {}".format(cp))
print("Valor resultante em serie: {}".format(cs))


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
