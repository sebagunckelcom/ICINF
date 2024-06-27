paicap = {}

for x in range(5):
    pais = input("Ingrese un país: ")
    capital = input("Ingrese la capital del país ingresado: ")
    paicap[pais] = capital

turista = input("Ingrese el nombre del turista: ")
pais_origen = input("Ingrese el país de procedencia del turista: ")

print("El turista con el nombre",turista,"viene de",pais_origen,"y su capital es",paicap[pais_origen])