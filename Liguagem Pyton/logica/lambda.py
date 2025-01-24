"""
Uma função lambda é uma pequena função anônima.
Uma função lambda pode receber qualquer número de argumentos,
mas só pode ter uma expressão.
"""
x=lambda a : a + 10
print(x(5))

# Multiplique argumento apor argumento be retorne o resultado:
x = lambda a, b : a * b
print(x(5, 6))

# Resuma o argumento a, b, e ce retorne o resultado
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

"""
Por que usar funções Lambda?
O poder do lambda é melhor demonstrado quando você o usa como uma
função anônima dentro de outra função.
Digamos que você tenha uma definição de função que recebe um argumento,
e esse argumento será multiplicado por um número desconhecido:
"""
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))