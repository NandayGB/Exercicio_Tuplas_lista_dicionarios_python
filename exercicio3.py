"""Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra."""

def adicionar_item(carrinho, produto, quantidade):
    if produto in carrinho:
        carrinho[produto] += quantidade
    else:
        carrinho[produto] = quantidade

def calcular_total(carrinho, precos):
    total = 0
    for produto, quantidade in carrinho.items():
        total += precos.get(produto, 0) * quantidade  
    return total

carrinho = {}

adicionar_item(carrinho, "maçã", 2)
adicionar_item(carrinho, "banana", 3)
adicionar_item(carrinho, "laranja", 1)

precos = {
    "maçã": 15.00,
    "banana": 9.75,
    "laranja": 8.90,
}
total = calcular_total(carrinho, precos)

print("Seu carrinho:")
for produto, quantidade in carrinho.items():
    preco = precos.get(produto, 0)
    print(f"- {quantidade} {produto}(s) - R$ {preco:.2f} cada")
print(f"Total: R$ {total:.2f}")