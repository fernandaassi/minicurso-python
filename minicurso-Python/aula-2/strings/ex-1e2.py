'''
***** Exercício 1 *****
Dada a frase "Python é muito legal", use o fatiamento para dar nome as variáveis
contendo cada palavra.
'''

# Criando a frase dada no enunciado
frase = "Python é muito legal"

# Cada palavra da frase é armazenada em uma variável.
# O fatimaneto é utilizado.
python = frase[0:6]
eh = frase[7:8]
muito = frase[9:14]
legal = frase[15:20]

'''
***** Execício 2 *****
Qual o tamanho dessa frase? E qual o tamanho de cada palavra? Use o artifício da
programação para saber se você estava certo.
'''

# A função len() é usada para saber o tamanho de cada palavra e da frase
# Os resultados são armazenados em novas variáveis
tam_frase = len(frase)
tam_python = len(python)
tam_eh = len(eh)
tam_muito = len(muito)
tam_legal = len(legal)

# Mostra o resultado do exercício na tela
print("Frase original: {}".format(frase))
print()
print("Tamanho de cada palavra na frase:")
print("python = {} letras".format(tam_python))
print("é = {} letras".format(tam_eh))
print("muito = {} letras".format(tam_muito))
print("legal = {} letras".format(tam_legal))
print("Frase inteira = {} letras".format(tam_frase))
