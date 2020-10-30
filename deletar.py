import requests
from functions import deletarCadastrado

f = open('condutores.txt', 'r')
for i in f.readlines():
  # print(i)
  s = deletarCadastrado(i.strip())
  if s.status_code == 200:
    print("Condutor excluido")
  else:
    print(s.content)
f.close()