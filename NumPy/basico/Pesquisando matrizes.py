"""
Pesquisando matrizes
Você pode pesquisar um determinado valor em uma matriz e retornar os índices que obtiverem uma correspondência.
Para pesquisar uma matriz, use o where().
"""
# Encontre os índices onde o valor é 4
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Encontre os índices onde os valores são pares:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# Encontre os índices onde os valores são ímpares:
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)







"""
Pesquisa ordenada
Existe um método chamado searchsorted() que realiza uma busca binária na matriz e
retorna o índice onde o valor especificado seria inserido para manter a ordem da busca.

Presume-se que o searchsorted() seja usado em matrizes classificadas.
"""
# Encontre os índices onde o valor 7 deve ser inserido:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
"""
Exemplo explicado: O número 7 deve ser inserido no índice 1 para manter a ordem de classificação.
O método inicia a busca pela esquerda e retorna o primeiro índice onde o número 7 não é mais maior que o próximo valor.
"""







"""
Pesquisar do lado direito
Por padrão, o índice mais à esquerda é retornado, mas podemos side='right' retornar o índice mais à direita.
"""
# Encontre os índices onde o valor 7 deve ser inserido, começando pela direita:
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
"""
Exemplo explicado: O número 7 deve ser inserido no índice 2 para manter a ordem de classificação.
O método inicia a busca pela direita e retorna o primeiro índice onde o número 7 não é mais menor que o próximo valor.
"""




"""
Valores Múltiplos
Para pesquisar mais de um valor, use uma matriz com os valores especificados.
"""
# Encontre os índices onde os valores 2, 4 e 6 devem ser inseridos:
import numpy as np
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
"""
O valor de retorno é uma matriz: [1 2 3]contendo os três índices onde 2, 4, 6 seriam inseridos na matriz original para manter a ordem.
"""