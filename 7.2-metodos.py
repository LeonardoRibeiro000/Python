#-------------------Métodos para Dicionários ------------------------------------------------
usuarios = {'user1': "Leonardo", "user2": "Bianca", 'user3': "David", 'user4': "Genivaldo"}
print(usuarios)

#pop() -> remove um item de um dicionário e o retorna
print(usuarios.pop('user2'))


#--------------------Métodos de consulta ----------------------------------------------------
#items() -> retorna uma lista de pares chave-valor do dicionário
print(usuarios.items())

#keys() -> retorna uma lista das chaves do dicionário
print(usuarios.keys()) 

#values() -> retorna os valores 
print(usuarios.values())


#-------------------- Leitura dos dados ------------------------------------------------------
#Chaves
for chaves in usuarios.keys():
    print(usuarios[chaves])

#Valores
for valores in usuarios.values():
    print(valores)


#Chave-valor
for chaves, valores in usuarios.items():
    print(chaves, valores)
