i = int(input())
par = int()
impar = int()

for n in range(i):
    n = int(input())

    resto = n % 2
    if resto == 0:
        par += 1
    else:
        impar += 1

print(par)
print(impar)

