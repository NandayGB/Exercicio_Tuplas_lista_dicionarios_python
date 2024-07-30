"""Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
"""

contatos = {
    "Alice": "9876-5432",
    "Aurora": "8765-4321",
    "Fernanda": "7654-3210",
    "Eduardo": "6543-2109"
}


nome = input("Digite o nome do contato que deseja procurar: ")


telefone = contatos.get(nome)

if telefone:
    print(f"Telefone de {nome}: {telefone}")
else:
    print(f"Contato {nome} não encontrado.")