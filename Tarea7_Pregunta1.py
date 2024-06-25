numeros = []

for i in range(10):
    numero = int(input("Ingrese 10 numeros: "))
    numeros.append(numero)
numeros.reverse()

print("Los números en orden inverso son:")
for numero in numeros:
    print(numero)