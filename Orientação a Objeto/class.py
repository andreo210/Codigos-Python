class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)


"""
A função __init__()
Os exemplos acima são classes e objetos em sua forma mais simples e não são realmente úteis em aplicações da vida real.
Para entender o significado das classes, precisamos entender a __init__() função interna.
Todas as classes têm uma função chamada __init__(), que é sempre executada quando a classe está sendo iniciada.
Use a __init__()função para atribuir valores às propriedades do objeto ou outras operações que são necessárias quando o objeto está sendo criado:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)



"""
A função __str__()
A __str__()função controla o que deve ser retornado quando o objeto de classe é representado como uma string.
Se a __str__()função não estiver definida, a representação em string do objeto será retorn
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)
# Exemplo
# A representação em string de um objeto COM a __str__()função:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)



"""
Métodos de Objetos
Objetos também podem conter métodos. Métodos em objetos são funções que pertencem ao objeto.
Vamos criar um método na classe Person:
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



"""
O parâmetro self
O selfparâmetro é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.
Não precisa ter nome self, você pode chamá-lo como quiser, mas precisa ser o primeiro parâmetro de qualquer função na classe
"""
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Modificar propriedades do objeto
# Você pode modificar propriedades em objetos assim:
p1.age = 40

# Excluir propriedades do objeto
# Você pode excluir propriedades em objetos usando a delpalavra-chave:
del p1.age


"""
A declaração de passe
classdefinições não podem estar vazias, mas se por algum motivo você tiver uma classdefinição sem conteúdo, insira-a na passdeclaração para evitar um erro.
"""
class Person:
    pass