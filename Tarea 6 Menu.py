def mostrar_menu():
    opciones = [
        "1. Ingresar un elemento a la lista",
        "2. Modificar un elemento de la lista según el índice",
        "3. Eliminar un elemento de la lista según el índice",
        "4. Eliminar el último elemento de la lista",
        "5. Buscar un elemento de la lista según el dato (devuelve el índice)",
        "6. Mostrar todos los elementos de la lista",
        "7. Salir"
    ]
    print("\nMenú de opciones:")
    for opcion in opciones:
        print(opcion)

def ingresar_elemento(lista):
    lista.append(input("Ingrese el elemento a agregar: "))

def modificar_elemento(lista):
    try:
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        lista[indice] = input("Ingrese el nuevo valor del elemento: ")
    except (ValueError, IndexError):
        print("Índice inválido.")

def eliminar_elemento(lista):
    try:
        print(f"Elemento '{lista.pop(int(input('Ingrese el índice del elemento a eliminar: ')))}' eliminado.")
    except (ValueError, IndexError):
        print("Índice inválido.")

def eliminar_ultimo_elemento(lista):
    print(f"Último elemento '{lista.pop()}' eliminado." if lista else "La lista está vacía.")

def buscar_elemento(lista):
    elemento = input("Ingrese el elemento a buscar: ")
    print(f"El elemento '{elemento}' está en el índice {lista.index(elemento)}." if elemento in lista else f"El elemento '{elemento}' no se encuentra en la lista.")

def mostrar_lista(lista):
    print("Elementos de la lista:")
    for i, elemento in enumerate(lista):
        print(f"{i}: {elemento}")

def main():
    lista = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ingresar_elemento(lista)
        elif opcion == '2':
            modificar_elemento(lista)
        elif opcion == '3':
            eliminar_elemento(lista)
        elif opcion == '4':
            eliminar_ultimo_elemento(lista)
        elif opcion == '5':
            buscar_elemento(lista)
        elif opcion == '6':
            mostrar_lista(lista)
        elif opcion == '7':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()