produtos = []
quantidades = []

def adicionar_venda(produto, venda): 
        produtos.append(produto)
        quantidades.append(venda)

def produto_mais_vendido(produtos, quantidades):
     i = produtos.index(max(quantidades))
     print(i)

#def produto_menos_vendido(produtos, vendas):
    
def main():
    for _ in range(2):
        adicionar_venda(str(input()), int(input()))

    produto_mais_vendido(produtos, quantidades)


main()
