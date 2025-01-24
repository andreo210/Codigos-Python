"""
Datas Python
Uma data em Python não é um tipo de dado próprio, mas podemos importar um módulo chamado datetimepara trabalhar com datas como objetos de data.
"""
import datetime

x = datetime.datetime.now()
print(x)




"""
Saída de data
Quando executamos o código do exemplo acima o resultado será:
2025-01-14 16:44:27.225992
A data contém ano, mês, dia, hora, minuto, segundo e microssegundo.
O datetime módulo tem muitos métodos para retornar informações sobre o objeto de data.
Aqui estão alguns exemplos, você aprenderá mais sobre eles mais adiante neste capítulo:
"""
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))




"""
Criando objetos de data
Para criar uma data, podemos usar a datetime() classe (construtor) do datetimemódulo.
A datetime() classe requer três parâmetros para criar uma data: ano, mês e dia.
"""
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)




"""
O método strftime()
O datetimeobjeto tem um método para formatar objetos de data em strings legíveis.
O método é chamado strftime()e recebe um parâmetro, format, para especificar o formato da string retornada:
"""
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

"""
Uma referência de todos os códigos de formato legal:

Directive	Description	Example	Try it
%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
"""


