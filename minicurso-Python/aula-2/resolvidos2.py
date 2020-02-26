'''
***************************************************************************
************************** EXERCÍCIOS CAPITULO 5 **************************
***************************************************************************
'''

'''
***** Exercício 1 *****
Crie uma lista com o nome de 3 pessoas.
'''

# Cria uma variável chamada "nome_pessoas" e dentro dela é colocado uma lista
# com o nome de 3 pessoas. Os nomes estão entre "" pois são strings
nome_pessoas = ["Fernanda", "João", "Amanda"]

# Imprime o resutado do exercício na tela
print("Lista com o nome de 3 pessoas: {}".format(nome_pessoas))


'''
***** Exercício 2 *****
Crie três listas, uma lista de cada coisa a seguir:
• frutas
• docinhos de festas (não se esqueça dos brigadeiros)
• ingredientes de feijoada
Lembre-se de salvá-las em alguma variável!
(a) Agora crie uma lista que contenha essas três listas (uma lista de lista, vamos
chamar de listona).
(b) Você consegue acessar o elemento brigadeiro?
(c) Adicione mais brigadeiros à segunda lista de listona.
'''

# Cria três listas diferentes
frutas = ["maça", "banana", "laranja"]
docinhos_festa = ["bolo", "beijinho", "brigadeiro"]
feijoada = ["arroz", "feijão preto", "couve"]

# Coloca as três listas criadas em uma única lista. Uma lista de listas.
listona = [frutas, docinhos_festa, feijoada]

# Imprime a listona.
# Resposta do item a)
print("a) Lista que contém as 3 listas: {}".format(listona))

# Acessa o elemento brigadeiro na listona
# Para fazer isto, ele tem que acessar o terceiro elemento (ou seja, elemento de
# indice 2 de docinhos_festa) da segunda lista (elemento de índice 1 de listona).
# Desta forma, ele acessa primeiro a segunda lista de listona, e em seguida acessa
# o terceiro elemento de docinhos_festa
# Resposta do item b)
print("b) {}".format(listona[1][2]))

# Para adicionar mais brigadeiros na segunda lista de listona usaremos a função
# append().
# Primeiro, precisamos acessar a segunda lista de listona (lista com indice 1), para
# então, usar a função append() para adicionar mais brigadeiros.
listona[1].append("brigadeiro")
listona[1].append("brigadeiro")

# Imprime a listona após inserção de mais brigadeiros
# Resposta do item c)
print("c) Listona após inserção de mais brigadeiros: {}".format(listona))


'''
***** Exercício 3 *****
Dado uma lista de números (deve ser lida do teclado), ordene-a e em seguida inverta a
ordem desta lista.
'''

# Le a lista
lista_numeros = input("Digite uma lista de números sepadados por espaço: ").split(" ")

# Imprime a lista que foi digitada pelo usuário
print("Lista digitada: {}".format(lista_numeros))

# Ordena os elementos da lista.
# Uso da função sort() para fazer a ordenação
lista_numeros.sort()

# Imprime a lista ordenada
print("Lista ordenada: {}".format(lista_numeros))

# Inverte a lista (que está ordenada)
lista_numeros.reverse()

# Imprime a lista invertida
print("Lista invertida: {}".format(lista_numeros))


'''
***** Exercício 4 *****
Leia uma frase e retorne a primeira e a última palavra
'''

# Leitura da frase.
# Colocaremos a frase em uma lista, sendo cada palavra um item da lista
frase = input("Digite uma frase: ").split(" ")

# Usa indexação para pegar a primeira palavra da lista e armazena em uma variável
primeira_palavra = frase[0]
# Usa indexação para pegar a última palavra da lista, neste caso será o índice do
# tamanho da lista - 1. Para saber o tamanho da lista, usa-se a funçaõ len().
ultima_palavra = frase[len(frase) - 1]

# Mostra na tela o resultado da primeira e da última palavra
print("Primeira palavra: {}".format(primeira_palavra))
print("Ultima palavra: {}".format(ultima_palavra))


'''
***** Exercício 5 *****
Faça um programa que peça o nome completo de uma pessoa e retorne o primeiro nome.
'''

# Leitura do nome
# Colocaremos o nome completo da pessoa em uma lista, sendo cada nome um item da
# lista.
nome = input("Digite seu nome completo: ").split(" ")

# Usa indexação para pegar o primeiro nome, que é o primeiro item da lista e armazena
# em uma variável
primeiro_nome = nome[0]

# Mostra na tela o primeiro nome da pessoa
print("Primeiro nome: {}".format(primeiro_nome))


'''
***** Exercício 6 *****
Dada a seguinte lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] imprima somente os números pares
dessa lista.
'''

# Cria a lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Armazena os números pares na lista "pares"
# Para isso é usado a indexação, começando no index 0, indo até o index 10 e pulando
# de dois em dois
pares = lista[1:10:2]

print("Números pares da lista: {}".format(pares))



'''
***************************************************************************
************************** EXERCÍCIOS CAPITULO 6 **************************
***************************************************************************
'''


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


'''
***** Exercício 5 *****
Leia uma string do teclado e faça ela se repetir 10 vezes.
'''

# Le a string do teclado e armazena o resultado em uma variável
string = input("Digite uma string: ")

# Usa o operador * para fazer a string se repetir 10 vezes e armazena o resultado
# em uma nova variável
string_x_10 = string * 10


# Mostra o resultado do exercício na tela
print("String repetida 10 vezes: {}".format(string_x_10))
