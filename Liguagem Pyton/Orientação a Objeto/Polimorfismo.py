"""
A palavra "polimorfismo" significa "muitas formas" e, em programação,
refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em muitos objetos ou classes.
"""

"""
Polimorfismo de classe
O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter várias classes com o mesmo nome de método.
Por exemplo, digamos que temos três classes: Car, Boat, e Plane, e todas elas têm um método chamado move():
"""
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()



  """
Polimorfismo de Classe de Herança
E quanto a classes com classes filhas com o mesmo nome? Podemos usar polimorfismo aí?
Sim. Se usarmos o exemplo acima e fizermos uma classe pai chamada Vehicle, e fizermos Car, 
Boat, Plane classes filhas de Vehicle, as classes filhas herdam os Vehicle métodos, mas podem substituí-los:
"""
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()