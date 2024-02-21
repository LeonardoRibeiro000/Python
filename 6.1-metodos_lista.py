
#----- len - Descobrir a quantidade de elementos dentro do conjunto ------
lista = ["Fabricio Daniel", 9.5,9.0,8,True]
print(len(lista))



#------ Partição ----------------------------------------------------



#=------------Append() -> Adiciona um elemento ao final da lista ---
lista.append("Esquerdista")
print(lista)

# ----- Extend() -> Adiciona vários elementos ao final da lista ----
lista.extend([10,8,7])
print(lista)

# ------ remove(), -> Remove um elemento especifico da lista --------
lista.remove(10)
print(lista)


#-------insert() -> insere um elemento em uma determinada posição na lista----- 
#lista.insert(indice, elemento)
lista.insert(9, "Africano")
print(lista)

#----- pop() -> remove um elemento de uma posição especifica -------------------------
lista.pop(8)
print(lista)

#sort-> organiza os elementos em ordem crescente ou descrecente
names = ["Frodo", "Gandalf", "Aragorn", "Boromir", "Sauron", "Legolas", "Sam", "Feremir"]
print(names) 
names.sort()
print(names)