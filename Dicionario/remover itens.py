"""
Removendo Itens
Existem vários métodos para remover itens de um dicionário:
"""

"""Exemplo
O pop() remove o item com o nome de chave especificado:"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


"""O popitem() remove o último item inserido (em versões anteriores à 3.7,
 um item aleatório é removido):"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)


""" del remove o item com o nome de chave especificado:"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)


"""O clear() esvazia o dicionário:"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)