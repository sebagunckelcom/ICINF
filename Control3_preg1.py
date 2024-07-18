números=("1234567890")

def solo_numeros(var):
    for x in var:
        if x in números:
            n=True
        else:
            n=False
            break
    return n

var=input("Ingrese un numero o letra: ")
print(solo_numeros(var))