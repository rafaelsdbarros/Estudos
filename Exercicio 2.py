saldo = 1000.00
while True:
    opcao = int(input())
    if opcao == 1:
        print("%.2f" %saldo)
    elif opcao == 2:
        valor = float(input())
        if (saldo >= valor) and (valor > 0.00):
            saldo -= valor
        print("%.2f" %saldo)
    elif opcao == 3:
        valor = float(input())
        if valor > 0.00:
            saldo += valor
        print("%.2f" %saldo)
    elif opcao == 4:
        break