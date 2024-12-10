"""
Descompactando uma Tupla
Quando criamos uma tupla, normalmente atribuímos valores a ela.
Isso é chamado de "empacotamento" de uma tupla:
"""

fruits = ("apple", "banana", "cherry")

(verde, amarelo, vermelho) = fruits

print(verde)
print(amarelo)
print(vermelho)


""""
Usando o Asterisk*
Se o número de variáveis ​​for menor que o número de valores, 
você pode adicionar um *ao nome da variável e os 
valores serão atribuídos à variável como uma lista:
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# Se o asterisco for adicionado a outro nome de variável que não o anterior,
# o Python atribuirá valores à variável até que o número de valores restantes 
# corresponda ao número de variáveis ​​restantes.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)