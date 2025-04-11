"""
Treinar/Testar é um método para medir a precisão do seu modelo.
É chamado de Treinamento/Teste porque você divide o conjunto de dados em dois conjuntos: um conjunto de treinamento e um conjunto de teste.

80% para treinamento e 20% para testes.

Você treina o modelo usando o conjunto de treinamento.

Você testa o modelo usando o conjunto de testes.

Treinar o modelo significa criar o modelo.

Testar o modelo significa testar a precisão do modelo.

Comece com um conjunto de dados
Comece com um conjunto de dados que você deseja testar.

Nosso conjunto de dados ilustra 100 clientes em uma loja e seus hábitos de compra.
"""
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()





"""
Ajustar o conjunto de dados
Como é o conjunto de dados? Na minha opinião, o melhor ajuste seria uma regressão polinomial , então vamos traçar uma reta de regressão polinomial.
Para desenhar uma linha através dos pontos de dados, usamos o plot() do módulo matplotlib:
"""
# Desenhe uma linha de regressão polinomial através dos pontos de dados:
import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
"""
O resultado corrobora minha sugestão de que o conjunto de dados se ajusta a uma regressão polinomial, 
embora isso nos desse resultados estranhos se tentássemos prever valores fora do conjunto de dados. 
Exemplo: a linha indica que um cliente que passa 6 minutos na loja faria uma compra no valor de 200.
Isso provavelmente é um sinal de sobreajuste.
Mas e quanto à pontuação R-quadrado? A pontuação R-quadrado é um bom indicador de quão bem meu conjunto de dados se ajusta ao modelo.
"""





"""
R2
Lembra do R2, também conhecido como R ao quadrado?
Ele mede a relação entre o eixo x e o eixo y, e o valor varia de 0 a 1, onde 0 significa nenhuma relação e 1 significa totalmente relacionado.
O módulo sklearn tem um método chamado r2_score() que nos ajudará a encontrar esse relacionamento.
Neste caso, gostaríamos de medir a relação entre os minutos que um cliente permanece na loja e quanto dinheiro ele gasta
"""
# Quão bem meus dados de treinamento se ajustam em uma regressão polinomial?
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)




"""
Traga o conjunto de testes
Agora criamos um modelo que está OK, pelo menos quando se trata de dados de treinamento.
Agora queremos testar o modelo com os dados de teste também, para ver se nos dá o mesmo resultado.
"""
# Vamos encontrar a pontuação R2 ao usar dados de teste:
import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(test_y, mymodel(test_x))

print(r2)
"""O resultado 0,809 mostra que o modelo também se ajusta ao conjunto de testes, 
e estamos confiantes de que podemos usar o modelo para prever valores futuros."""




"""
Prever Valores
Agora que estabelecemos que nosso modelo está OK, podemos começar a prever novos valores.
"""
# Quanto dinheiro um cliente gastará se permanecer na loja por 5 minutos?
print(mymodel(5))
# O exemplo previu que o cliente gastaria 22,88 dólares,