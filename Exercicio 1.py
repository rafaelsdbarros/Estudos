total_compra = 0.0
    
while True:
    nome_produto = input().lower()
    
    if nome_produto == 'fim':
        break

    quantidade = float(input())
    valor_unitario = float(input())
    
    total_produto = quantidade * valor_unitario
    print(f"{total_produto:.2f}")
    total_compra += total_produto

print(f"resultado = {total_compra:.2f}")
print(f"{total_compra}")