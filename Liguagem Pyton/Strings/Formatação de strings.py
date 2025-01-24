"""
F-String foi introduzido no Python 3.6 e agora é a maneira preferida de formatar strings.
Antes do Python 3.6, tínhamos que usar o format().

F-string permite formatar partes selecionadas de uma string.
Para especificar uma string como uma f-string, basta colocar um f na frente do literal da string, assim:
"""
txt = f"The price is 49 dollars"
print(txt)



"""
Espaços reservados e modificadores
Para formatar valores em uma f-string, adicione marcadores de posição {}.
Um marcador de posição pode conter variáveis, operações, funções e modificadores para formatar o valor.
"""
price = 59
txt = f"The price is {price} dollars"
print(txt)



"""
Um espaço reservado também pode incluir um modificador para formatar o valor.
Um modificador é incluído adicionando dois pontos :seguidos de um tipo de formatação legal, como .2f o que significa número de ponto fixo com 2 decimais:

Exemplo
Exibir o preço com 2 casas decimais:
"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Você também pode formatar um valor diretamente sem mantê-lo em uma variável:
txt = f"The price is {95:.2f} dollars"
print(txt)



"""
Executar operações em F-Strings
Você pode executar operações Python dentro dos espaços reservados.
Você pode fazer operações matemáticas:
"""
txt = f"The price is {20 * 59} dollars"
print(txt)

# Adicione impostos antes de exibir o preço:
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# Você pode executar if...elseinstruções dentro dos espaços reservados:
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)



"""
Executar funções em F-Strings
Você pode executar funções dentro do espaço reservado:
"""
# Use o método string upper()para converter um valor em letras maiúsculas:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# A função não precisa ser um método interno do Python, você pode criar suas próprias funções e usá-las:
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)




"""
Mais modificadores
No início deste capítulo, explicamos como usar o .2fmodificador para formatar um número em um número de ponto fixo com 2 casas decimais.
Existem vários outros modificadores que podem ser usados ​​para formatar valores:
"""
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)



"""
Formato de string()
Antes do Python 3.6, usávamos o format()método para formatar strings.
O format()método ainda pode ser usado, mas f-strings são mais rápidas e a maneira preferida de formatar strings.
Os próximos exemplos nesta página demonstram como formatar strings com o format()método .
O format()método também usa chaves como marcadores de posição {}, mas a sintaxe é um pouco diferente:
"""
# Adicione um espaço reservado onde você deseja exibir o preço:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Você pode adicionar parâmetros dentro das chaves para especificar como converter o valor:
txt = "The price is {:.2f} dollars"




"""
Valores Múltiplos
Se você quiser usar mais valores, basta adicionar mais valores ao método format():
"""
# E adicione mais marcadores de posição:
quantity = 3
qqqqq = 56
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, qqqqq, price))



"""
Números de índice
Você pode usar números de índice (um número dentro das chaves {0}) para ter certeza de que os valores estão colocados nos espaços reservados corretos:
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Além disso, se você quiser se referir ao mesmo valor mais de uma vez, use o número do índice:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))



"""
Índices Nomeados
Você também pode usar índices nomeados inserindo um nome dentro das chaves {carname},
mas então você deve usar nomes quando passar os valores dos parâmetros txt.format(carname = "Ford"):
"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))