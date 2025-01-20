"""
Excluir um arquivo
Para excluir um arquivo, você deve importar o módulo do sistema operacional e executar sua os.remove():
"""

# Remova o arquivo "demofile.txt":
import os
os.remove("demofile.txt")

# Para evitar um erro, você pode verificar se o arquivo existe antes de tentar excluí-lo:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")



"""
Excluir pasta
Para excluir uma pasta inteira, use o os.rmdir():
"""
import os
os.rmdir("myfolder")