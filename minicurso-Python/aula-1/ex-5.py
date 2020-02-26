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
