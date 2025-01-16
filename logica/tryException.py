"""
O try permite que você teste um bloco de código em busca de erros.
O except permite que você lide com o erro.
O else permite que você execute código quando não há erro.
O finally permite que você execute código, independentemente do resultado dos blocos try e except.
"""

"""
Tratamento de exceções
Quando ocorre um erro, ou uma exceção, como chamamos, o Python normalmente para e gera uma mensagem de erro.
Essas exceções podem ser tratadas usando a tryinstrução:
"""
try:
  print(x)
except:
  print("uma exception ocorreu")



"""
Muitas exceções
Você pode definir quantos blocos de exceção quiser, por exemplo, 
se quiser executar um bloco especial de código para um tipo especial de erro:
"""
try:
  print(x)
except NameError:
  print("variavel x nao definida")
except:
  print("Something else went wrong")


"""
ELSE
Você pode usar a else para definir um bloco de código a ser executado se nenhum erro for gerado:
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("testando else")



"""
FINALLY
O finally, se especificado, será executado independentemente se o bloco try gerar um erro ou não.
"""
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Isso pode ser útil para fechar objetos e limpar recursos:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")



"""
Gerar exeção
Como desenvolvedor Python, você pode escolher lançar uma exceção se uma condição ocorrer.
Para lançar (ou levantar) uma exceção, use a raisepalavra-chave.
"""
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



"""
A raise é usada para gerar uma exceção.
Você pode definir que tipo de erro gerar e o texto a ser impresso para o usuário.
"""
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")