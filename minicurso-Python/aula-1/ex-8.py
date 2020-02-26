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
