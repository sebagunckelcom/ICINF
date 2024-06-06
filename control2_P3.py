lista= []
palabra = 0

while palabra != "":
   palabra= input("ingrese palabra (enter para finalizar): ")
   lista.append(palabra)

if lista:
   palabraxl= max(lista)
   caracteres= len(palabraxl)

   print("La palabra con mas caracteres es", palabraxl,", con", caracteres, "caracteres")
else:
   print("No se ingresaron palabras")
   

    