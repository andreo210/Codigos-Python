"""
Âmbito local
Uma variável criada dentro de uma função pertence ao escopo local dessa função e só pode ser usada dentro dela.
"""
# Uma variável criada dentro de uma função está disponível dentro dessa função:
def myfunc():
  x = 300
  print(x)
myfunc()



"""
Função dentro da função
Conforme explicado no exemplo acima, a variável xnão está disponível fora da função, mas está disponível para qualquer função dentro da função:
"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()




"""
Âmbito global
Uma variável criada no corpo principal do código Python é uma variável global e pertence ao escopo global.
Variáveis ​​globais estão disponíveis em qualquer escopo, global e local.
"""
x = 300

def myfunc():
  print(x)

myfunc()

print(x)





"""
Nomeando Variáveis
Se você operar com o mesmo nome de variável dentro e fora de uma função, 
o Python as tratará como duas variáveis ​​separadas, uma disponível no escopo global (fora da função)
e outra disponível no escopo local (dentro da função):
"""
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)



"""
Palavra-chave global
Se você precisar criar uma variável global, mas estiver preso no escopo local, você pode usar a global palavra-chave .
A global palavra-chave torna a variável global.
"""
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Além disso, use a globalpalavra-chave se quiser fazer uma alteração em uma variável global dentro de uma função.
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)




"""
Palavra-chave não local
A nonlocalpalavra-chave é usada para trabalhar com variáveis ​​dentro de funções aninhadas.
A nonlocalpalavra-chave faz com que a variável pertença à função externa.
"""
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())