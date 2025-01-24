"""
Remover item
Para remover um item de um conjunto, use remove() ou discard().
"""
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) 
# se o item a ser removido não existir,
#  remove() será gerado um erro.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


"""
Você também pode usar o pop() para remover um item,
mas esse método removerá um item aleatório, 
então você não pode ter certeza de qual item será removido.
O valor de retorno do pop() é o item removido
"""
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)




"""
O clear() método esvazia o conjunto:
"""
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


"""
del excluirá o conjunto completamente:
"""
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)