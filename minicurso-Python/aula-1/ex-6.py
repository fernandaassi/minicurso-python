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
