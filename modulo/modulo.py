"""
O que é um módulo?
Considere um módulo como sendo o mesmo que uma biblioteca de código.
Um arquivo contendo um conjunto de funções que você deseja incluir em seu aplicativo.
"""
# def greeting(name):
# print("Hello, " + name)

import myModule

myModule.greeting("Jonathan")

a = myModule.person1["age"]
print(a)


"""
Nomeando um módulo
Você pode nomear o arquivo do módulo como quiser, mas ele deve ter a extensão de arquivo .py
Renomeando um módulo
Você pode criar um alias ao importar um módulo, usando a aspalavra-chave:
"""
import myModule as mx
a = mx.person1["age"]
print(a)




"""
Módulos Integrados
Existem vários módulos integrados no Python, que você pode importar quando quiser.
"""
import platform
x = platform.system()
print(x)



"""
Usando a função dir()
Há uma função interna para listar todos os nomes de funções (ou nomes de variáveis) em um módulo. A dir()função:
"""
import platform
x = dir(platform)
print(x)




"""
Importar do módulo
Você pode escolher importar apenas partes de um módulo usando a frompalavra-chave.
"""
from myModule import person1
print (person1["age"])