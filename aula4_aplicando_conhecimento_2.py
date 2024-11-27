import math

tipoInvestimento = int(input())
valorInicial = float(input())
prazoInvestimento = int(input())

#Poupança
if tipoInvestimento == 1:
    taxaDeJuros = 0.5 / 100
    valorFuturo = (valorInicial * math.pow((1 + taxaDeJuros), prazoInvestimento))
    print('%.2f' %valorFuturo)

#CDB    
elif tipoInvestimento == 2:
    taxaDeJuros = 0.8 / 100
    valorFuturo = (valorInicial * math.pow((1 + taxaDeJuros), prazoInvestimento))
    print('%.2f' %valorFuturo)

#Tesouro Direto  
elif tipoInvestimento == 3:
    taxaDeJuros = 1 / 100
    valorFuturo = (valorInicial * math.pow((1 + taxaDeJuros), prazoInvestimento))
    print('%.2f' %valorFuturo)    