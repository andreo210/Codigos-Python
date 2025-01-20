"""
Escrever em um arquivo existente
Para gravar em um arquivo existente, você deve adicionar um parâmetro à open():

"a"- Acrescentar - será anexado ao final do arquivo
"w"- Escrever - substituirá qualquer conteúdo existente
"""

# Abra o arquivo "demofile2.txt" e anexe conteúdo ao arquivo:
f = open("demofile2.txt", "a")
f.write("to escrvendo no final do arquivo")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# Abra o arquivo "demofile3.txt" e sobrescreva o conteúdo:
f = open("demofile3.txt", "w")
f.write("apguei o que tinha e estou colocando um novo conteudo")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())