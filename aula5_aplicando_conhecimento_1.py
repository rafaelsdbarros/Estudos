while True: 
    nomeProduto = str(input()).lower
    qtdProduto = int(input())
    valorUnitario = float(input())
    precoFinal = float()

    precoTotal =+ valorUnitario * qtdProduto

    if nomeProduto == 'fim':
        totalCompra = precoTotal
        print("%.2f" %totalCompra)
        break


