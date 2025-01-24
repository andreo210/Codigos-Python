"""
Copiar um dicionário
Você não pode copiar um dicionário simplesmente digitando dict2 = dict1,
porque: dict2será apenas uma referência a dict1, e as alterações feitas
em dict1serão feitas automaticamente também em dict2.
Há maneiras de fazer uma cópia, uma delas é usar o método Dictionary integrado copy().
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)


# Outra maneira de fazer uma cópia é usar a função interna dict().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)