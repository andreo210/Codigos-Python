thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Imprima todos os nomes de chaves no dicionário, um por um:
for x in thisdict:
    print(thisdict[x])

# Imprima todos os valores no dicionário, um por um:
for x in thisdict:
    print(x)

# Você também pode usar o values()para retornar valores de um dicionário:
for x in thisdict.values():
    print(x)

# Você pode usar o keys()método para retornar as chaves de um dicionário:
for x in thisdict.keys():
    print(x)