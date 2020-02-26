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
