lista_usd= []
clp= 950

for producto in range(10):  
    producto = float(input("Ingrese hasta 10 productos en dolares: "))
    lista_usd.append(producto)

cambio= [producto * clp for producto in lista_usd]
    
print("El cambio a pesos chilenos es de:", cambio) 