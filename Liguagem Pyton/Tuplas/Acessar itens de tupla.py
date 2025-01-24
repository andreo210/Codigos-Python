# Imprima o segundo item na tupla:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Imprima o último item da tupla:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# Faixa de índices

# Retorne o terceiro, quarto e quinto item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


# Este exemplo retorna os itens do início até "kiwi", mas NÃO os inclui:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


# Este exemplo retorna os itens de "cherry" até o final:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


# Faixa de índices negativos
# Este exemplo retorna os itens do índice -4 (incluído) ao índice -1 (excluído)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# Verifique se o item existe
# Verifique se "apple" está presente na tupla:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("sim, 'apple' está na tupla de frutas")