#Podemos atribuir estrutura de dados a estrutura de dados, como adicionar "Lista" dentro de um "Dicionário"

loja = {'nome': ["Notebook", "TV", "Caixa de som", "Teclado"],
        'precos': [1200, 3500, 500, 250]}

print(loja)

for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)