sueldobajo = sueldoalto = gasto_total = 0

print("Ingrese los sueldos de los empleados mensualmente. (-1 para salir)")
      
sueldo = int(input("ingrese el sueldo del empleado: "))
while sueldo != -1:
    if sueldo <= 900000:
       sueldobajo = sueldobajo + 1
    else:
       sueldoalto = sueldoalto + 1
    gasto_total = gasto_total + sueldo
    sueldo = int(input("ingrese el sueldo del empleado: "))

print("Empleados que cobran hasta $900.000: " + str(sueldoalto))  
print("Empleados que cobran mas de $900.000: " + str(sueldobajo))
print("gasto total en sueldos: $" + str(gasto_total))   