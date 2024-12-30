"""
O loop while
Com o loop while podemos executar um conjunto de instruções
desde que uma condição seja verdadeira.
"""
i = 1
while i < 6:
    print(i)
    i += 1


"""
A declaração break
Com a instrução break podemos parar o loop
mesmo se a condição while for verdadeira:
"""
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
i += 1


"""
A declaração continue
Com a instrução continue podemos parar a iteração atual
e continuar com a próxima:
"""
i = 0
while i < 6:
    i += 1
    if i == 3:
      continue
print(i)


"""
A declaração else
Com a instrução else podemos executar um bloco de código uma vez quando a
condição não for mais verdadeira:
"""
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")