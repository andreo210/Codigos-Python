"""
Variáveis ​​globais
Variáveis ​​que são criadas fora de uma função
 são conhecidas como variáveis ​​globais.

Variáveis ​​globais podem ser usadas por 
qualquer pessoa, tanto dentro quanto fora das funções.
"""

x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()

"""A palavra-chave global
Normalmente, quando você cria uma variável dentro de uma função,
 essa variável é local e só pode ser usada dentro dessa função.
Para criar uma variável global dentro de uma função, 
você pode usar a global palavra-chave.
"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
