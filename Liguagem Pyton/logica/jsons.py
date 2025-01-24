"""
JSON é uma sintaxe para armazenar e trocar dados.
JSON é texto escrito com notação de objeto JavaScript.

O Python tem um pacote integrado chamado json, 
que pode ser usado para trabalhar com dados JSON.
"""
import json 


"""
Analisar JSON - Converter de JSON para Python
Se você tiver uma string JSON, poderá analisá-la usando o json.loads()método .
"""
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])


"""
Converter de Python para JSON
Se você tiver um objeto Python, poderá convertê-lo 
em uma string JSON usando o json.dumps()método .
"""
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Converta um objeto Python contendo todos os tipos de dados legais:
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


"""
Formatar o resultado
O exemplo acima imprime uma string JSON, mas não é muito fácil de ler,
sem recuos e quebras de linha.
O json.dumps()método possui parâmetros para facilitar a leitura do resultado:
"""
# Use o indent parâmetro para definir o número de recuos:
print(json.dumps(x, indent=4))

# Você também pode definir os separadores, o valor padrão é (", ", ": "),
#  o que significa usar uma vírgula e um espaço para separar cada objeto,
#  e dois pontos e um espaço para separar chaves de valores:
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# Use o sort_keys parâmetro para especificar se o resultado deve ser classificado ou não
print(json.dumps(x, indent=4, sort_keys=True))