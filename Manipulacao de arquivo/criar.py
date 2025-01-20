"""
Criar um novo arquivo
Para criar um novo arquivo em Python, use o open(), com um dos seguintes parâmetros:

"x"- Criar - criará um arquivo, retornará um erro se o arquivo existir

"a"- Acrescentar - criará um arquivo se o arquivo especificado não existir

"w"- Escrever - criará um arquivo se o arquivo especificado não existir
"""
# Crie um arquivo chamado "myfile.txt":
f = open("myfile.txt", "x")

# Crie um novo arquivo se ele não existir:
f = open("myfile.txt", "w")