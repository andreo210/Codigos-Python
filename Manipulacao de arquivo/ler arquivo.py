"""
Para abrir o arquivo, use a função integrada open().
A open() retorna um objeto de arquivo, que possui um read() para ler o conteúdo do arquivo:
"""
f = open("demofile.txt", "r")
print(f.read())



"""
Ler somente partes do arquivo
Por padrão, o read() retorna o texto inteiro, mas você também pode especificar quantos caracteres deseja retornar:
"""
# Retorna os 5 primeiros caracteres do arquivo:
f = open("demofile.txt", "r")
print(f.read(5))



"""
Ler linhas
Você pode retornar uma linha usando o readline():
"""
# Leia uma linha do arquivo:
f = open("demofile.txt", "r")
print(f.readline())

# Chamando readline()duas vezes, você pode ler as duas primeiras linhas:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

# Ao percorrer as linhas do arquivo, você pode ler o arquivo inteiro, linha por linha:
f = open("demofile.txt", "r")
for x in f:
  print(x)


"""
Fechar arquivos
É uma boa prática sempre fechar o arquivo quando terminar de usá-lo.
"""
f = open("demofile.txt", "r")
print(f.readline())
f.close()