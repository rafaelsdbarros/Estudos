# -*- coding: utf-8 -*-
def eh_triangulo(a, b, c):
    if (a + b < c) or (a + c < b) or (b + c < a):
        print("Os lados não formam um triângulo")
    else:
        print("Os lados formam um triângulo")
        tipo_triangulo(a, b, c)


def tipo_triangulo(a, b, c):
    #Todos os lados são iguais
    if(a == b) and (a == c):
        print("Equilátero")

    #Dois lados são iguais
    elif(a == b) or (b == c) or (a == c):
        print("Isósceles")

    #Todos os lados são diferentes
    else:
        print("Escaleno")

def main():
    a = int(input())
    b = int(input())
    c = int(input())

    eh_triangulo(a, b, c)

main()



