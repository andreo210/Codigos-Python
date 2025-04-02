"""
O que é um número aleatório?
Número aleatório NÃO significa um número diferente a cada vez. Aleatório significa algo que não pode ser previsto logicamente.

Pseudo aleatório e verdadeiro aleatório.
Computadores funcionam em programas, e programas são conjuntos definitivos de instruções. Então, significa que deve haver algum algoritmo para gerar 
um número aleatório também.
Se houver um programa para gerar números aleatórios, eles podem ser previstos, portanto não são verdadeiramente aleatórios.
Números aleatórios gerados por meio de um algoritmo de geração são chamados de pseudoaleatórios .
Podemos criar números realmente aleatórios?
Sim. Para gerar um número verdadeiramente aleatório em nossos computadores, precisamos obter os dados aleatórios de alguma fonte externa.
Essa fonte externa geralmente são nossos toques de tecla, movimentos do mouse, dados na rede, etc.
Não precisamos de números verdadeiramente aleatórios, a menos que estejam relacionados à segurança 
(por exemplo, chaves de criptografia) ou a base da aplicação seja a aleatoriedade (por exemplo, roletas digitais).
Neste tutorial usaremos números pseudoaleatórios.
"""


"""
Gerar Número Aleatório
O NumPy oferece o módulo random  para trabalhar com números aleatórios.
"""
# Gere um inteiro aleatório de 0 a 100:
from numpy import random
x = random.randint(100)
print(x)



"""
Gerar Float Aleatório
O método do módulo aleatório rand() retorna um float aleatório entre 0 e 1.
"""
# Gerar um float aleatório de 0 a 1:
from numpy import random
x = random.rand()
print(x)




"""
Gerar matriz aleatória
No NumPy trabalhamos com matrizes, e você pode usar os dois métodos dos exemplos acima para criar matrizes aleatórias.
Inteiros
O método randint() recebe um size parâmetro onde você pode especificar o formato de uma matriz.
"""
# Gere uma matriz 1-D contendo 5 inteiros aleatórios de 0 a 100:
from numpy import random
x=random.randint(100, size=(5))
print(x)

# Gere uma matriz 2-D com 3 linhas, cada linha contendo 5 inteiros aleatórios de 0 a 100:
from numpy import random
x = random.randint(100, size=(3, 5))
print(x)




"""
Flutua
O método rand() também permite que você especifique o formato da matriz.
"""
# Gere uma matriz 1-D contendo 5 floats aleatórios:
from numpy import random
x = random.rand(5)
print(x)

# Gere uma matriz 2-D com 3 linhas, cada linha contendo 5 números aleatórios:
from numpy import random
x = random.rand(3, 5)
print(x)



"""
Gerar número aleatório a partir de matriz
O método choice() permite gerar um valor aleatório com base em uma matriz de valores.
O método choice() recebe um array como parâmetro e retorna aleatoriamente um dos valores.

O choice()método também permite que você retorne uma matriz de valores.
Adicione um sizeparâmetro para especificar o formato da matriz.
"""
# Retorna um dos valores em uma matriz
from numpy import random
x = random.choice([3, 5, 7, 9])
print(x)

# Gere uma matriz 2-D que consiste nos valores no parâmetro da matriz (3, 5, 7 e 9):
from numpy import random
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)