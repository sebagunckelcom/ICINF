num1 = float(input("ingrese la primera nota: "))
num2 = float(input("ingrese la segunda nota: "))
num3 = float(input("ingrese la tercera nota: "))
num4 = float(input("ingrese la cuarta nota: "))

prom = (num1+num2+num3+num4) / 4
if prom >= 4.0:
    print("pasaste el ramo con un promedio de: ", prom)
else:
    print("te echaste el ramo papito: ", prom)