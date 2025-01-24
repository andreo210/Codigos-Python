"""
Acessando Itens
Você pode acessar os itens de um dicionário consultando seu nome de chave, dentro de colchetes:
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# ou
x = thisdict.get("model")
print(x)



"""
Obter chaves
O keys() retornará uma lista de todas as chaves no dicionário.
"""
x = thisdict.keys()

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) # antes
car["color"] = "white"
print(x) # depois


"""
Obter valores
O values() retornará uma lista de todos os valores no dicionário.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


"""
Obter itens
O items() retornará cada item em um dicionário, como tuplas em uma lista.
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


"""
Verifique se a chave existe
Para determinar se uma chave especificada está presente em um dicionário, use  in:
"""
thisdict = {
     "brand": "Ford",
     "model": "Mustang",
     "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")