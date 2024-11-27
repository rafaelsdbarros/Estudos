
def main():
    valorProduto = float(input()) 
    precoAtualizado = atualiza_preco(valorProduto)
    precoAtualizadoTaxa = taxa(precoAtualizado)

    print(f"{precoAtualizado:.2f}")
    print(f"{precoAtualizadoTaxa:.2f}")

def atualiza_preco(valor):
    return valor * 0.1

def taxa(valor):
    return valor * 0.025

main()