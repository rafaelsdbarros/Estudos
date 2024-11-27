def adicionar_venda(produtos, vendas):
    for _ in range(5):
        produto = input()
        quantidade = int(input())
        produtos.append(produto)
        vendas.append(quantidade)

def produto_mais_vendido(produtos, vendas):
    indice_maior = vendas.index(max(vendas))
    return produtos[indice_maior], vendas[indice_maior]

def produto_menos_vendido(produtos, vendas):
    indice_menor = vendas.index(min(vendas))
    return produtos[indice_menor], vendas[indice_menor]

def main():
    produtos = []
    vendas = []
    
    adicionar_venda(produtos, vendas)

    mais_vendido, quantidade_mais_vendida = produto_mais_vendido(produtos, vendas)
    menos_vendido, quantidade_menos_vendida = produto_menos_vendido(produtos, vendas)

    print(mais_vendido, quantidade_mais_vendida)
    print(menos_vendido, quantidade_menos_vendida)

main()