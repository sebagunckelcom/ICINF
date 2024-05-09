num = int(input("ingrese una contraseña de 4 digitos: "))

if num >= 1 and num < 10:
    print("El numero es de un solo digito")
if num > 10 and num <= 99:
    print("El numero es de dos digitos")
if num >= 100 and num <= 999:
    print("El numero es de tres digitos")
if num >= 1000 and num <= 9999:
    print("El numero es de cuatro digitos")