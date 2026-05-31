""""
def media(a, b):
    return (a + b) / 2

def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista) 
print(media(10, 20))  # Saída: 15.0
print(media_lista([10, 20, 30]))  # Saída: 20

"""

##funcao que use o for para iterar sobre um dicionário e mostrar o nome e a idade de cada pessoa
"""
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Charlie", "idade": 35}
]

for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
    
"""
    
###coloque dentro de uma funcao a iteração sobre o dicionário e mostre o nome e a idade de cada pessoa

"""
def mostrar_pessoas(pessoas):
    for pessoa in pessoas:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
        
def adicionar_pessoa(pessoas, nome, idade):
    pessoas.append({"nome": nome, "idade": idade})  

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Charlie", "idade": 35}
]

mostrar_pessoas(pessoas)
adicionar_pessoa(pessoas, "David", 28)
print("\nApós adicionar David:")
mostrar_pessoas(pessoas)
    """
##print("Demonstracao")

#adcionar pessoas numa lista de dicionarios com as seguinte estrutura: nome, idade e sexo, com o input atraves de uma funcao 

def adicionar_pessoa(pessoas, nome, idade, sexo):
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})


pessoas = []  # lista inicial fora do loop

while True:
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (m/f): ")
    while sexo.lower() not in ['m', 'f']:
        print("Sexo inválido. Por favor, digite 'm' para masculino ou 'f' para feminino.")
        sexo = input("Digite o sexo da pessoa (m/f): ")

    adicionar_pessoa(pessoas, nome, idade, sexo)

    continuar = input("Deseja adicionar outra pessoa? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nLista de pessoas cadastradas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Sexo: {pessoa['sexo']}")
