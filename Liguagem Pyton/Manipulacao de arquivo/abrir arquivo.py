"""
Manipulação de arquivos
A função principal para trabalhar com arquivos em Python é a open().
A open() recebe dois parâmetros: nome do arquivo e modo.

Existem quatro métodos (modos) diferentes para abrir um arquivo:

"r"- Ler - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir

"a"- Acrescentar - Abre um arquivo para anexar, cria o arquivo se ele não existir

"w"- Escrever - Abre um arquivo para escrita, cria o arquivo se ele não existir

"x"- Criar - Cria o arquivo especificado, retorna um erro se o arquivo existir

Além disso, você pode especificar se o arquivo deve ser tratado como modo binário ou texto

"t"- Texto - Valor padrão. Modo de texto

"b"- Binário - Modo binário (por exemplo, imagens)
"""

f = open("demofile.txt")

# O código acima é o mesmo que:
f = open("demofile.txt", "rt")
