"""
Uma RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
O RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado.

Módulo RegEx
O Python tem um pacote integrado chamado re, que pode ser usado para trabalhar com expressões regulares.
Importe o re módulo:
"""
import re

# Pesquise a string para ver se ela começa com "The" e termina com "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


"""
Funções RegEx

O remódulo oferece um conjunto de funções que nos permite procurar uma correspondência em uma string:

Function	         Description
findall	             Returns a list containing all matches
search	             Returns a Match object if there is a match anywhere in the string
split	             Returns a list where the string has been split at each match
sub	                 Replaces one or many matches with a string
"""



"""
A função findall()
A findall() função retorna uma lista contendo todas as correspondências.
"""
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)



"""
A função search()
A search() função procura uma correspondência na string e retorna um objeto Match se houver uma correspondência.
Se houver mais de uma correspondência, somente a primeira ocorrência da correspondência será retornada:
"""
import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# Faça uma pesquisa que não retorne nenhuma correspondência
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



"""
A função split()
A split() função retorna uma lista onde a string foi dividida em cada correspondência:
"""
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
# Você pode controlar o número de ocorrências especificando o maxsplit parâmetro:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



"""
A função sub()
A sub() função substitui as correspondências pelo texto de sua escolha:
"""
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Você pode controlar o número de substituições especificando o count parâmetro:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)



"""
Objeto de correspondência
Um objeto Match é um objeto que contém informações sobre a pesquisa e o resultado.
"""
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object



"""
O objeto Match possui propriedades e métodos usados ​​para recuperar informações sobre a pesquisa e o resultado:

.span()retorna uma tupla contendo as posições inicial e final da correspondência.
.stringretorna a string passada para a função
.group()retorna a parte da string onde houve uma correspondência
"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Imprima a string passada para a função:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


# Imprima a parte da string onde houve uma correspondência.
# A expressão regular procura por qualquer palavra que comece com "S" maiúsculo:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())