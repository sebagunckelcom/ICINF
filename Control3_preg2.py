def convierte_negativo(lista):
    return [-num for num in lista]
lista = []

for x in range(10):
    while True:
            num = int(input("Ingrese 10 numeros positivos: "))
            if num > 0:
                lista.append(num)
                break
            else:
                print("El número debe ser positivo. Intente nuevamente.")

lista_negativa = convierte_negativo(lista)
print("Lista con números negativos:", lista_negativa)   