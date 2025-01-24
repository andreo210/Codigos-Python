"""
Depois que um conjunto é criado, você não pode alterar seus itens,
mas pode adicionar novos itens.
Para adicionar um item a um conjunto, use o add() método.
"""

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


"""
Adicionar conjuntos
Para adicionar itens de outro conjunto ao conjunto atual, 
use o update() método .
"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


"""
Adicionar qualquer iterável
O objeto no update()método não precisa ser um conjunto, 
pode ser qualquer objeto iterável (tuplas, listas, dicionários etc.)
"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)