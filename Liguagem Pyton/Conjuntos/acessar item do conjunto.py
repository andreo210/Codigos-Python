"""
Você não pode acessar itens em um conjunto consultando um índice ou uma chave.
Mas você pode percorrer os itens do conjunto usando um for loop, 
ou perguntar se um valor especificado está presente em um conjunto, 
usando a in palavra-chave.
"""

# Percorra o conjunto e imprima os valores:
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# Verifique se "banana" está presente no conjunto:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

# Verifique se "banana" NÃO está presente no conjunto:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

"""Depois que um conjunto é criado, 
você não pode alterar seus itens, mas pode adicionar novos itens."""