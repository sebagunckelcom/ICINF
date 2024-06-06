lista = []
nombre = 0

for nombre in range(7):
    nombre = input("Ingrese 7 nombres: ")
    lista.append(nombre)

nombres_sin_a = []
for nombre in lista:
    nombre = nombre.strip()
    if len(nombre) == 0 or nombre[-1] != 'a':  
        nombres_sin_a.append(nombre)

print("Lista de nombres que no terminan en 'a':")
print(nombres_sin_a)