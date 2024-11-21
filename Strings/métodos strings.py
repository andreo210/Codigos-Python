print('ola')
print("ola")

w = "Curso de python"
print(w)

"""comentario"""

a = """ola este
eh um curso
de python"""

print(a)


# tudo maiusculo
c = "ola mundo"
print(c.upper())

# tudo minusculo
d = "OLA MUNDO"
print(d.lower())

# Remover Espaço em Branco
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# O replace()método substitui uma string por outra string:
a = "Hello, World!"
print(a.replace("H", "J"))

# split()método divide a string em substrings se encontrar instâncias do separador:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

e = "ola"
f = "mundo"
g = e + " " + f
print(g)
