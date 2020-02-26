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
