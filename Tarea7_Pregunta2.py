palabras = []

while True:
    palabra = input("Ingrese una palabra (o presione Enter para finalizar): ")
    if palabra == "":
        break
    palabras.append(palabra)

def contar_a(palabra):
    return palabra.count('A') + palabra.count('a')

print("Conteo de letras 'A' y 'a' en cada palabra:")
for palabra in palabras:
    cantidad_a = contar_a(palabra)
    print("La palabra ",palabra, "tiene", cantidad_a, "letras 'A' o 'a'.")