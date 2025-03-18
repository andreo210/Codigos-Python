"""
Tipos de dados em Python
Por padrão, o Python tem estes tipos de dados:

strings- usado para representar dados de texto, o texto é fornecido entre aspas. por exemplo "ABCD"
integer- usado para representar números inteiros. por exemplo -1, -2, -3
float- usado para representar números reais. por exemplo 1,2, 42,42
boolean- usado para representar Verdadeiro ou Falso.
complex- usado para representar números complexos. por exemplo 1,0 + 2,0j, 1,5 + 2,5j

Tipos de dados em NumPy
O NumPy tem alguns tipos de dados extras e se refere a tipos de dados com um caractere, como ipara inteiros, upara inteiros sem sinal, etc.

Abaixo está uma lista de todos os tipos de dados no NumPy e os caracteres usados ​​para representá-los.

i- inteiro
b- booleano
u- inteiro sem sinal
f- flutuar
c- flutuação complexa
m- delta de tempo
M- data e hora
O- objeto
S- corda
U- sequência unicode
V- pedaço fixo de memória para outro tipo ( void )
"""


"""
Verificando o tipo de dados de uma matriz
O objeto array NumPy tem uma propriedade chamada dtype que retorna o tipo de dados do array:
"""
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Obtenha o tipo de dados de uma matriz contendo strings:
import numpy as np
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)



"""
Criando matrizes com um tipo de dados definido
Usamos a array() para criar matrizes, esta função pode receber um argumento opcional: dtype que nos permite definir o tipo de dado esperado dos elementos da matriz:
Para i, u, f, S e U podemos definir tamanho também.
"""
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Crie uma matriz com tipo de dados inteiro de 4 bytes:
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)




"""
Convertendo Tipo de Dados em Arrays Existentes
A melhor maneira de alterar o tipo de dados de um array existente é fazer uma cópia do array com o astype()
A astype() cria uma cópia do array e permite que você especifique o tipo de dado como um parâmetro.
O tipo de dado pode ser especificado usando uma string, como 'f'para float, 'i'para integer etc. ou você pode usar o tipo de dado diretamente, como floatpara float e intpara integer.
"""
# Altere o tipo de dados de float para inteiro usando 'i'como valor de parâmetro:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# Altere o tipo de dados de float para inteiro usando intcomo valor de parâmetro:
import numpy as np
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# Alterar o tipo de dados de inteiro para booleano:
import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)