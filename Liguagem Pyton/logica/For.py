"""
Python para laços
Um loop for é usado para iterar sobre uma sequência
(que pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).

Isso é menos parecido com a palavra-chave for em outras 
linguagens de programação e funciona mais como um método iterador,
como encontrado em outras linguagens de programação orientadas a objetos.

Com o loop for podemos executar um conjunto de instruções,
 uma vez para cada item em uma lista, tupla, conjunto etc.
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


"""
Looping através de uma string
Mesmo as strings sendo objetos iteráveis, 
elas contêm uma sequência de caracteres:"""
for x in "banana":
    print(x)



"""
A declaração break
Com a instrução break podemos parar o loop antes que ele 
tenha percorrido todos os iten
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
# Saia do loop quando xfor "banana", 
# mas desta vez a quebra vem antes da impressão:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


"""
A declaração continue
Com a instrução continue podemos parar a iteração atual do loop e 
continuar com a próxima:
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


"""
A função range()
Para percorrer um conjunto de código um número especificado de vezes,
podemos usar a função range() ,
A função range() retorna uma sequência de números, começando em 0 por padrão,
incrementando em 1 (por padrão) e terminando em um número especificado.
"""
for x in range(6):
    print(x)

# Usando o parâmetro start:
for x in range(2, 6):
    print(x)


"""
Else no loop For
A else em um for loop especifica um bloco de código
a ser executado quando o loop for concluíd
"""
for x in range(6):
    print(x)
else:
    print("Finally finished!")


"""
Loops aninhados
Um loop aninhado é um loop dentro de um loop.
O "loop interno" será executado uma vez para cada iteração do "loop externo":
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


"""
A declaração de passe
for não podem estar vazios, mas se por algum motivo você tiver um for
sem conteúdo, insira-o na pass  para evitar obter um erro
"""
for x in [0, 1, 2]:
    pass