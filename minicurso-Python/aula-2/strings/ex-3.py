'''
***** Exercício 3 *****
Leia duas strings do teclado e veja se uma contém a outra.
'''

# Le duas strings do teclado, utilizando a função input() e armazena o resultado
# em variáveis
string1 = input("Informe a primeira string: ")
string2 = input("Informe a segunda string: ")

# Utiliza o operador in para saber se uma string está contida na outra
# Armazena o resultado de cada operação em variáveis
s1_in_s2 = string1 in string2
s2_in_s1 = string2 in string1

# Mostra o resultado do exercício na tela
print("A primeira string está contida dentro da segunda string?")
print(s1_in_s2)

print("E a segunda string, está contida dentro da primeira string?")
print(s2_in_s1)
