puntajes = []

for dia in range(1, 16):
    puntaje = int(input("Ingrese el puntaje del día: "))
    puntajes.append(puntaje)

print("Días con puntaje mayor a 60:")
dia = 1
for puntaje in puntajes:
    if puntaje >= 60:
        print("Día", dia)
    dia += 1

print("Días con puntaje menor a 60:")
dia = 1
for puntaje in puntajes:
    if puntaje < 60:
        print("Día", dia)
    dia += 1