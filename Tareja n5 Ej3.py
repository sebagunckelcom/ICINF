altura = 0
sumalturas = 0
cont = 0

while altura >= 0:
    altura = float(input("ingrese las alturas de las personas deseadas: "))
    if altura == 0:
        break
    sumalturas= sumalturas + altura
    cont = cont + 1
    
promedio= sumalturas / cont
print("el promedio de estara es de :", promedio)
