#----------------DICIONÁRIO------------------------

cadastro = {'matricula': 2001335669,
            'dia_cadastro': 25,
            'mes_cadastro': 10,
            'turma': '2E'
            }

print(cadastro)

#------- ACESSAR UMA CHAVE ESPECIFICA --------------
print(cadastro['matricula'])


#------- ALTERAR UM VALOR --------------------------
cadastro['turma'] = '2G'
print(cadastro)


#------- ADICIONAR CHAVE/VALOR ---------------------
cadastro['modalidade'] = 'EAD'
print(cadastro)