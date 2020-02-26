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
