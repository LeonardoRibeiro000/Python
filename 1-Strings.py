#--------------------------- Strings -----------------------------------------------------
# Conjunto de caracteres que formam um texto
# Criadas com aspas simples e aspas duplas
# Para formatar strings usamos métodos -> nome_objeto.nome_método()
# Existem métodos que não precisam de parênteses

#Principais Métodos-----------------------------------------------------------------------

#str.upper() - converte uma string em maiúsculas
name = "leonardo"
print(name.upper())
 

#str.lower() -> converte uma string para minúsculas
name2 = 'LEONARDO'
print(name2.lower())                             


#str.capitalize() -> Retorna o primeiro caractere em maiúscula e o restante em minúsculo
name3 = "leonardo"
print(name3.capitalize())

#str.strip() -> Remove espaços em branco do inicio e do fim de uma string
teste = " Leonardo"
print(teste.strip())


#str.replace(antigo, novo) -> substitui todas as ocorrências do texto "antigo" na string por "novo"
teste2 = "Le@nardo"
print(teste2.replace("@", "o"))