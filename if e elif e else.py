a = 33
b = 200
if b > a:
    print("b é maior que a")


# A palavra-chave elif é a maneira do Python dizer "se as condições anteriores
#  não forem verdadeiras, então tente esta condição"

if b > a:
    print("b é maior que a")
elif a == b:
    print("a e b são iguais")


# palavra-chave else captura qualquer coisa que não 
# seja capturada pelas condições anteriores.
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


# Declaração if de uma linha:
if a > b: print("a is greater than b")


# Declaração if else de uma linha:
print("A") if a > b else print("B")


# Declaração if else de uma linha, com 3 condições:
print("A") if a > b else print("=") if a == b else print("B")


# Você pode ter ifinstruções dentro ifde instruções, 
# o que é chamado de instruções aninhadas if .
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# if As instruções não podem estar vazias, 
# mas se por algum motivo você tiver uma if sem conteúdo,
#  insira pass-a para evitar um erro.
a = 33
b = 200

if b > a:
    pass