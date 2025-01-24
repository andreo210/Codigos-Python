# Para alterar o valor de um item específico, consulte o número do índice:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Para alterar o valor dos itens dentro 
# de um intervalo específico, defina uma lista com os novos valores e 
# consulte o intervalo de números de índice onde deseja inserir
#  os novos valores
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Se você inserir mais itens do que substituir,
#  os novos itens serão inseridos onde você especificou,
#  e os itens restantes serão movidos de acordo:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# Altere o segundo e o terceiro valor substituindo-os por um valor:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)