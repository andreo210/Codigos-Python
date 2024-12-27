"""
Adicionando Itens
Adicionar um item ao dicionário é feito usando uma nova chave de índice 
e atribuindo um valor a ela:
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)


"""
Atualizar dicionário
O update()método atualizará o dicionário com os itens de um argumento fornecido.
 Se o item não existir, o item será adicionado.
O argumento deve ser um dicionário ou um objeto iterável com pares chave:valor.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1994
}
thisdict.update({"color": "red"})