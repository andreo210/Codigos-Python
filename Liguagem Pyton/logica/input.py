"""
Entrada do usuário
Python permite entrada de dados pelo usuário.
Isso significa que podemos pedir informações ao usuário.
O método é um pouco diferente no Python 3.6 do que no Python 2.7.
O Python 3.6 usa o input() método .
O Python 2.7 usa o raw_input() método .
O exemplo a seguir solicita o nome de usuário e, quando você o digita, ele é impresso na tela:
"""
#username = input("Enter username:")
#print("Username is: " + username)

username = raw_input("Enter username:")
print("Username is: " + username)