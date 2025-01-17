"""
Todos métodos e propriedade em pyton são publicos
o programador tem que declarar quando é privado com _

"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject._name = name
    mysillyobject._age = age

  def minhafuncaoPublica(abc):
    print("Hello my name is " + abc._name)

  def _minhafuncaoPrivada(abc):
    print("Hello my name is " + abc._name)

p1 = Person("John", 36)
p1.minhafuncaoPublica()
