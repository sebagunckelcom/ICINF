notas = []
suma_notas = 0

while True:
    nota = float(input("Ingrese las notas deseadas (o 0 para finalizar): "))
    if nota == 0:
        break
    notas.append(nota)
    suma_notas += nota

cont = len(notas)

if cont > 0:
    promedio = suma_notas / cont
    nota_mas_alta = notas[-1]
    nota_mas_baja = notas[0]

print("La cantidad de notas ingresadas es de:", cont)
print("El promedio de las notas es de:", promedio)
print("La nota más alta es de:", nota_mas_alta)
print("La nota más baja es de:", nota_mas_baja)
