'''
***** Exercício 4 *****
Pegue o seu nome e transforme todas as letras em maiúsculas, em seguida transforme
todas as letras em minúsculas e por fim, deixe só a primeira letra como maiúscula.
'''

# Armazena o nome em uma variável
nome = "Fernanda"

# Usa a função upper() para transformar todas as letras em maiúsculas e armazena
# a nova string em uma variável, não alterando a string original
maiusculas = nome.upper()
# Usa a função lower() para transformar todas as letras em minúsculas e armazena
# a nova string em uma variável, não alterando a string original
minusculas = maiusculas.lower()
# Usa a função capitalize() para transformar a primeira letra em maiúscula e
#armazena a nova string em uma variável, não alterando a string original
capitalize = nome.capitalize()

# Mostra o resultado do exercício na tela
print("O nome: {}".format(nome))
print("Todas as letras maiúsculas: {}".format(maiusculas))
print("Todas as letras minúsculas: {}".format(minusculas))
print("Somente primeira letra maiúscula: {}".format(capitalize))
