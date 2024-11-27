valorPagamento = float(input())
codigoPagamento = int(input())

if codigoPagamento == 1: 
    desconto = (valorPagamento * 0.10) 
    print('%.2f' %(valorPagamento - desconto))
    
elif codigoPagamento == 2: 
    desconto = (valorPagamento * 0.05) 
    print('%.2f' %(valorPagamento - desconto))

elif codigoPagamento == 3: 
    print('%.2f' %(valorPagamento / 5))
    
elif codigoPagamento == 4: 
    acrescimo = (valorPagamento * 0.15)
    valorAtualizado = (valorPagamento + acrescimo) / 10
    print('%.2f' %valorAtualizado)
    
