"""
O Python tem um conjunto de funções matemáticas integradas, incluindo um extenso módulo matemático, 
que permite executar tarefas matemáticas em números.

Funções matemáticas integradas
As funções min()e max() podem ser usadas para encontrar o menor ou maior valor em um iterável:
"""
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# A abs() função retorna o valor absoluto (positivo) do número especificado:
x = abs(-7.25)
print(x)


# A função pow retorna o valor de x elevado à potência de y (x y )
x = pow(4, 3)
print(x)


"""
O Módulo de Matemática
O Python também tem um módulo integrado chamado math, que amplia a lista de funções matemáticas.
Para usá-lo, você deve importar o mathmódulo:
"""
import math
x = math.sqrt(64)
print(x)



"""
O math.ceil()método arredonda um número para cima, para o inteiro mais próximo, 
e o math.floor() método arredonda um número para baixo, para o inteiro mais próximo, e retorna o resultad
"""
import math
x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1



"""A math.pi constante retorna o valor de PI (3,14...): """
import math
x = math.pi
print(x)