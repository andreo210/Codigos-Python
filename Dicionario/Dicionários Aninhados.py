
"""
Dicionários Aninhados
Um dicionário pode conter dicionários,
 isso é chamado de dicionários aninhados."""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)


# Crie três dicionários e, em seguida, 
# crie um dicionário que conterá os outros três dicionários:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


"""
Acessar itens em dicionários aninhados
Para acessar itens de um dicionário aninhado, 
use o nome dos dicionários, começando pelo dicionário externo
"""
print(myfamily["child2"]["name"])


"""
Percorrer dicionários aninhados
Você pode percorrer um dicionário usando o items() como este:
"""
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])