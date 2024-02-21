 #*=============================== Lista =====================================================

products = ['piranha', 'coco', 'gigole']

#*exibir valores
print(products)

#*contar quantos valores têm na lista
print(len(products))

#*percorrer uma lista
for prod in products:
    print(prod)


#*percorrer a lista com index
for idx, prod in enumerate(products):
    print(idx, prod)
    
#*adicionar valores na lista
products.append('oculos') #?final da lista
print(products)

products.insert(2, 'pulseira') #?local específico pelo índice
print(products)


#*remover elementos
'''products.remove('oculos') #?remove um valor específico
print(products)

products.pop(1) #?remove pelo índice
print(products)

valor_removido = products.pop(1) #?retorna o valor removido
print(valor_removido)

del products[1]
print(products)'''

 #*Funções e métodos
 
print(len(products))

#*o método min() e max() usado em lsita com strings, usa a quantidade de caracteres da string como refência
#strings
menor_valor = min(products)
print(menor_valor)

maior_valor = max(products)
print(maior_valor)

#numbers
numbers = [1,123,35432,567,32]
menor_valor = min(numbers)
print(menor_valor)

maior_valor = max(numbers)
print(maior_valor)

#*somar valores

soma = sum(numbers)
print(soma)


#*descobrir o índice do elemento
indice = numbers.index(1) #?usa como parâmetro um valor da lista pra identificar o seu índice
print(indice)

#*contar o número de ocorrências na lista
contagem = numbers.count(35432) #? retorna o número de ocorrências do valor
print(contagem)


#*classificar os valores por ordem
numbers.sort() #?ordem crescente
print(numbers)

numbers.sort(reverse=True) #?ordem descrecente
print(numbers)

numbers.reverse() #?inverte a ordem
print(numbers)
