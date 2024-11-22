"""
Itens de acesso
Os itens da lista são indexados e você pode 
acessá-los consultando o número do índice:
"""
# Imprima o segundo item da lista:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Indexação negativa significa começar do fim
# -1 refere-se ao último item, -2 refere-se ao penúltimo item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Retorne o terceiro, quarto e quinto item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Este exemplo retorna os itens do início até "kiwi", mas NÃO incluindo:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Este exemplo retorna os itens de "cherry" até o final:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Especifique índices negativos se quiser iniciar a
#  pesquisa a partir do final da lista:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# Verifique se o item existe
thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
