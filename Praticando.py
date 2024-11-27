def atualiza_preco(valor):
  return valor * 0.1

def taxa(valor_atualizado):
  return valor_atualizado * 0.025

def main():
  valor_produto = float(input("Digite o valor do produto: "))

  valor_com_aumento = atualiza_preco(valor_produto)
  valor_taxa = taxa(valor_com_aumento)

  print(f"Valor atualizado: R$ {valor_com_aumento:.2f}")
  print(f"Valor da taxa: R$ {valor_taxa:.2f}")

if __name__ == "__main__":
  main()