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
