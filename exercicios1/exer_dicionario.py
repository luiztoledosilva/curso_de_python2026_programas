pessoas = [
    {"nome": "Ana", "idade": 28, "cidade": "São Paulo"},
    {"nome": "Bruno", "idade": 34, "cidade": "Rio de Janeiro"},
    {"nome": "Carla", "idade": 22, "cidade": "Belo Horizonte"}
]

##print(pessoas[0])
"""
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
"""
##for p in pessoas:
    ##print(f"{p['nome']}, {p['idade']} anos, {p['cidade']}")
###for acima para listar as pessoas, usando o nome da chave do dicionário para acessar os valores

##buscar o nome da pessoa mais velha através da chave idade e printar o nome dela com a idade e cidade 
""""
maior_idade = 0
for pessoa in pessoas:
    print(f"{pessoa['nome']} - {pessoa['idade']} anos")
    if pessoa['idade'] > maior_idade:
        maior_idade = pessoa['idade']

print(f"A maior idade encontrada foi: {maior_idade} anos")
print()
for pessoa in pessoas:
    if pessoa['idade'] == maior_idade:
        print(f"A pessoa mais velha é: {pessoa['nome']} - {pessoa['idade']} anos - {pessoa['cidade']}")
"""
        
#adicionar mais duas pessooas no dicionario
pessoas.append({"nome": "David", "idade": 40, "cidade": "Salvador"})
pessoas.append({"nome": "Elena", "idade": 35, "cidade": "Porto Alegre"})

for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
    
for pessoa in pessoas:
    #print(f"{pessoa['nome']} - mora em {pessoa['cidade']}")
    # 
    print(f"{pessoa['nome']} mora em {pessoa['cidade']}")
    
##adicionar mais 3 pessoas que mora em sao paulo, 2 em salvaor e 1 em porto alegre
pessoas.append({"nome": "Fernanda", "idade": 30, "cidade": "São Paulo"})
pessoas.append({"nome": "Gustavo", "idade": 27, "cidade": "São Paulo"})
pessoas.append({"nome": "Heloisa", "idade": 32, "cidade": "São Paulo"})
pessoas.append({"nome": "Isabela", "idade": 29, "cidade": "Salvador"})
pessoas.append({"nome": "João", "idade": 31, "cidade": "Salvador"})
pessoas.append({"nome": "Karen", "idade": 26, "cidade": "Porto Alegre"})

##pessoas que moram em são paulo
print("Pessoas que moram em São Paulo:") 
maior_idade = 0   
for pessoa in pessoas:
    if pessoa['cidade'] == "São Paulo":
        #print(f"{pessoa['nome']} - {pessoa['idade']} anos")
        print(f"{pessoa['nome']} - {pessoa['idade']} anos - {pessoa['cidade']}")
        if maior_idade == 0 or pessoa['idade'] > maior_idade:
            maior_idade = pessoa['idade']
print(f"A maior idade encontrada entre as pessoas que moram em São Paulo foi: {maior_idade} anos")

##adicionar sexo entre masculino ou feminino para cada pessoa do dicionário
pessoas[0]['sexo'] = 'Feminino'
pessoas[1]['sexo'] = 'Masculino'
pessoas[2]['sexo'] = 'Feminino'
pessoas[3]['sexo'] = 'Masculino'
pessoas[4]['sexo'] = 'Feminino'
pessoas[5]['sexo'] = 'Masculino'
pessoas[6]['sexo'] = 'Feminino'
pessoas[7]['sexo'] = 'Masculino'
pessoas[8]['sexo'] = 'Feminino'
pessoas[9]['sexo'] = 'Masculino'
pessoas[10]['sexo'] = 'Feminino'    


#mostrar quantas pessoas tem no dicionario 
print(f"O número total de pessoas no dicionário é: {len(pessoas)}")

###listar todas as pessoas do dicionario com as suas informaçoes de nome, idade, cidade e sexo
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']} anos, Cidade: {pessoa['cidade']}, Sexo: {pessoa['sexo']}")
    
#Nome: Fernanda, Idade: 30 anos, Cidade: S�o Paulo, Sexo: Masculino

#Nome: Heloisa, Idade: 32 anos, Cidade: S�o Paulo, Sexo: Masculino

#trocar o sexo da Fernanda para Feminino
#procurar a Fernanda no dicionário e trocar o sexo dela para Feminino
for pessoa in pessoas:
    if pessoa['nome'] == 'Fernanda':
        pessoa['sexo'] = 'Feminino'
        print(f"O sexo de {pessoa['nome']} foi atualizado para: {pessoa['sexo']}")

for pessoa in pessoas:
    if pessoa['nome'] == 'Heloisa':
        pessoa['sexo'] = 'Feminino'
        print(f"O sexo de {pessoa['nome']} foi atualizado para: {pessoa['sexo']}")
        
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']} anos, Cidade: {pessoa['cidade']}, Sexo: {pessoa['sexo']}")
    
for pessoa in pessoas:
    if pessoa['cidade'] == 'Porto Alegre' and pessoa['sexo'] == 'Feminino':
        print(f"{pessoa['nome']} - {pessoa['idade']} anos - {pessoa['cidade']} - {pessoa['sexo']}")
        
        
#adcionar mais 2 pessoas do sexo feminino que mora em Indaiatuba usando o metodo get para adicionar a chave cidade e sexo
pessoas.append({"nome": "Lara", "idade": 24, "cidade": "Indaiatuba", "sexo": "Feminino"})
pessoas.append({"nome": "Mariana", "idade": 27, "cidade": "Indaiatuba", "sexo": "Feminino"})


##listar todoas as pessoas do dicionario com o metodo
print("Lista de todas as pessoas no dicionário:")
for pessoa in pessoas:
    print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}")
    
##quantas pessoas tem no dicionario no total 
print(f"O número total de pessoas no dicionário é: {len(pessoas)}")

##colocar os estados das pessoas usando o metodo get para adicionar a chave estado
pessoas[0]['estado'] = 'SP'     
pessoas[1]['estado'] = 'RJ'
pessoas[2]['estado'] = 'MG' 
pessoas[3]['estado'] = 'BA'
pessoas[4]['estado'] = 'SP'
pessoas[5]['estado'] = 'SP'
pessoas[6]['estado'] = 'SP'
pessoas[7]['estado'] = 'BA'
pessoas[8]['estado'] = 'BA'
pessoas[9]['estado'] = 'RS'
pessoas[10]['estado'] = 'RS'
pessoas[11]['estado'] = 'SP'
pessoas[12]['estado'] = 'SP'

print("Lista atualizada com o estado de cada pessoa:")
for pessoa in pessoas:
    print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}, Estado: {pessoa.get('estado')}")
##Elena, Idade: 35 anos, Cidade: Porto Alegre, Sexo: Feminino, Estado: SP

#trocar estado da Elena para RS usando o metodo get para atualizar a chave estado
for pessoa in pessoas:
    if pessoa['nome'] == 'Elena':
        pessoa['estado'] = 'RS'
        print(f"O estado de {pessoa['nome']} foi atualizado para: {pessoa['estado']}")
""""      
print("Lista atualizada com o estado de cada pessoa:")
for pessoa in pessoas:
    print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}, Estado: {pessoa.get('estado')}")
    
"""
    
#Heloisa, Idade: 32 anos, Cidade: S�o Paulo, Sexo: Feminino, Estado: BA

for pessoa in pessoas:
    if pessoa['nome'] == 'Heloisa':
        pessoa['estado'] = 'SP'
        print(f"O estado de {pessoa['nome']} foi atualizado para: {pessoa['estado']}")

"""
print("Lista atualizada com o estado de cada pessoa:")
for pessoa in pessoas:
    print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}, Estado: {pessoa.get('estado')})")
    
"""
    
#Jo�o, Idade: 31 anos, Cidade: Salvador, Sexo: Masculino, Estado: RS)

for pessoa in pessoas:
    if pessoa['nome'] == 'João':
        pessoa['estado'] = 'SP'
        print(f"O estado de {pessoa['nome']} foi atualizado para: {pessoa['estado']}")

print("Lista atualizada com o estado de cada pessoa:")
for pessoa in pessoas:
    print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}, Estado: {pessoa.get('estado')})")
    
##pessoas que moram em Indaiatuba nome, idade, cidade, sexo e estado
print("Pessoas que moram em Indaiatuba:"    )
for pessoa in pessoas:
    if pessoa['cidade'] == 'Indaiatuba':
        ###usando o metodo get para acessar as chaves do dicionário
        print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')} anos, Cidade: {pessoa.get('cidade')}, Sexo: {pessoa.get('sexo')}, Estado: {pessoa.get('estado')})")
        
###atualizar o repositorio no github