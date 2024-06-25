supermercado = {}

while True:
    producto = input("Ingrese el nombre del producto (o presione Enter para finalizar): ")
    if producto == "":
        break
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    supermercado[producto] = cantidad

x = int(input("Ingrese un valor numérico X para multiplicar las cantidades: "))

print("Productos y sus cantidades multiplicadas por X:")
for producto, cantidad in supermercado.items():
    print(producto,":", cantidad * x)