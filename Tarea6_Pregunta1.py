def contarvocalesconsonantes(palabra):
    vocales = "aeiouAEIOU"
    c_vocales = 0
    c_consonantes = 0

    for letra in palabra:
        if letra.isalpha():  
            if letra in vocales:
                c_vocales = c_consonantes + 1
            else:
                c_consonantes = c_consonantes + 1

    return c_vocales, c_consonantes

def main():
    palabras = []

    while True:
        palabra = input("Ingresa una palabra (enter para finalizar): ")
        if palabra == "":
            break
        palabras.append(palabra)

    for palabra in palabras:
        vocales, consonantes = contarvocalesconsonantes(palabra)
        print(f"Palabra: {palabra}, Vocales: {vocales}, Consonantes: {consonantes}")

if __name__ == "__main__":
    main()
