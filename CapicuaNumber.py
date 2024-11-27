def numeroCapicua(numero):
    numeroinvertido=int(str(numero)[::-1])
    if numeroinvertido == numero:
      print('true')
      return(True)
    else:
      print('false')
      return(False)
  

numeroCapicua(132)