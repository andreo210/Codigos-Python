"""
Herança Python
A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
A classe pai é a classe da qual se está herdando, também chamada de classe base.
Classe filha é a classe que herda de outra classe, também chamada de classe derivada.
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()


"""
Criar uma classe filha
Para criar uma classe que herda a funcionalidade de outra classe, envie a classe pai como parâmetro ao criar a classe filha:
"""
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()



"""
Adicione a função __init__()
Até agora, criamos uma classe filha que herda as propriedades e métodos de sua classe pai.
Queremos adicionar a __init__()função à classe filha (em vez da passpalavra-chave).
"""
#class Student(Person):
 #    def __init__(self, fname, lname):
# Quando você adiciona a __init__()função, a classe filha não herdará mais a __init__()função da classe pai.
# Para manter a herança da __init__() função pai, adicione uma chamada à __init__()função pai:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
# Agora adicionamos a __init__()função com sucesso e mantivemos a herança da classe pai, e estamos prontos para adicionar funcionalidade na __init__()função.



"""
Use a função super()
Python também tem uma super()função que fará com que a classe filha herde todos os métodos e propriedades de sua classe pai:
"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


"""Adicionar Propriedades"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# Adicione um yearparâmetro e passe o ano correto ao criar objetos
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)



# Adicionar métodos
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()