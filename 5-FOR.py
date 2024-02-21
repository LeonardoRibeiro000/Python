#Todo for em python é um for each

#percorrer uma lista --------------------------------------------------------------
lista_produtos = ["faca", "garfo", "panela", "frigideira", "flavorstone"]

#para cada produto na lista de produtos: retorna o produto
for produto in lista_produtos:
   print(produto)

#percorrer a lista e colocar as iniciais em maiúsculo
for produto in lista_produtos:
    print(produto.capitalize())

#transformar todos os itens em maiúsculo
for produto in lista_produtos:
    print(produto.upper())


#calcular o imposto de cada produto
valores_produtos = [10, 16, 40, 50, 100]

for valor in valores_produtos:
    imposto = valor * 0.1
    print(imposto)


#percorrendo um dicionário --------------------------------------------------------
produtos = {
    'faca': 10,
    'garfo': 16,
    'panela': 40,
    'frigideira': 50,
    'flavorstone': 100
}


for produto in produtos:
    print(produto)
    print(produtos[produto])
    
    

