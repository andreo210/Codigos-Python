"""
O que é PIP?
PIP é um gerenciador de pacotes Python, ou módulos, se preferir.

O que é um pacote?
Um pacote contém todos os arquivos necessários para um módulo.
Módulos são bibliotecas de código Python que você pode incluir em seu projeto.

Verifique a versão do PIP:
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip --version

Baixe um pacote
Baixar um pacote é muito fácil.
Abra a interface de linha de comando e diga ao PIP para baixar o pacote desejado.
Navegue na linha de comando até o local do diretório de script do Python e digite o seguinte:
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase

Encontre Pacotes
Encontre mais pacotes em https://pypi.org/ .

Remover pacote
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

Listar Pacotes
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list
"""

# usando um pacote
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))