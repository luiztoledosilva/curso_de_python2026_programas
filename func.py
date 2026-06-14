def adicionar_pessoas(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
        
###colocar nome, idade, profisao e sexo 
def adicionar_dados(nome, idade, profissao, sexo):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Profissão: {profissao}")
    print(f"Sexo: {sexo}")
###for para percorrer a lista de pessoas e imprimir os dados
def imprimir_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Profissão: {pessoa['profissao']}")
        print(f"Sexo: {pessoa['sexo']}")
        print("-" * 20)
#teste das funções
"""
pessoas = [
    {"nome": "João", "idade": 30, "profissao": "Engenheiro", "sexo": "Masculino"},
    {"nome": "Maria", "idade": 25, "profissao": "Médica", "sexo": "Feminino"},
    {"nome": "Carlos", "idade": 40, "profissao": "Professor", "sexo": "Masculino"}
]   
pessoas=imprimir_pessoas(pessoas)

"""
###funcao para fazer append dos dados num arquivo
def adicionar_dados_arquivo(nome, idade, profissao, sexo):
    with open("dados_pessoas.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Idade: {idade}\n")
        arquivo.write(f"Profissão: {profissao}\n")
        arquivo.write(f"Sexo: {sexo}\n")
        arquivo.write("-" * 20 + "\n")
        ###fazer o for para ler o arquivo e imprimir os dados
def ler_dados_arquivo():
    with open("dados_pessoas.txt", "r") as arquivo:
        dados = arquivo.read()
        print(dados)
        for linha in arquivo:
            print(linha)
            
#teste das funções


 

