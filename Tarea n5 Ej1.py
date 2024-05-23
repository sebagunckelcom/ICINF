Preguntas = int(input("¿Cuantas fueron el total de preguntas hechas al entrevistado? "))
Correctas = int(input("¿Cuantas respuestas correctas tuvo el entrevistado? "))

Puntaje = Correctas / Preguntas * 100

if Puntaje >= 95:
    print("El conocimiento del entrevistado es de nivel maximo")
else:
    if Puntaje >= 70:
        print("El conocimiento del entrevistado es de nivel medio")
    else:
        if Puntaje >= 40:
            print("El conocimiento del entrevistado es de nivel regular")
        else:
            print("El conocimiento del entrevistado es de nivel insuficiente")

print("el puntaje de la entrevista es de ", Puntaje)
    
    