#-------------------------- Listas--------------------------------------------------------------------------------

#Armazenam vários elementos em ordem e são delimitados por colchetes [] e os itens são separados por vírgulas
#Pode armazenar qualquer tipo de item, incluindo números, strings, objetos e outras listas.
#Pode armazenar tipos de dados diferentes juntos em uma única lista


lista = ["Fabricio Daniel", 9.5,9.0,8,True] #*criação da lista
print(lista[2]) #*acessando a lista pelo índice
print(lista[4])
print(lista[0])
for elemento in lista: #*percorrendo a lista com for
    print(elemento)


#Podemos acessar uma string como se fosse uma lista
linguagem = "Python"
print(linguagem[0])

#Mas não podemos substituir
'''linguagem[2] = "O"
print(linguagem)'''

#COMO TRANFORMAR UM CONJUNTO DE CARACTERES (STRING) EM LISTA - USANDO O MÉTODO SPLIT()
duvida = "Quem veio antes? o ovo? ou a galinha?"
lista_palavras = duvida.split("?") #----> esse método precisa de uma delimitador
print(lista_palavras)

#Para transformar uma lista em um conjunto de caracteres utilizamos o método join
receita = ["Tomate", "Cebola", "Paprica", "Requeijão", "Arroz"]
unificador = "."
string_receita = unificador.join(receita)
print(string_receita)