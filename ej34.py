# CODIGO EJEMPLO: La repetición while ejecutará el bloque siempre que la condición sea True.

# cantidad = 0
# caracter = input("Carácter:")
# while len(caracter) != 1:
#     cantidad += 1
#     caracter = input("Carácter:")

# En este ejemplo se repetirá el bloque mientras los strings ingresados tengan longitud diferente de 1 y la repetición finalizará cuando se ingrese un único carácter.


intro = """
"Bienvenida a la plataforma de calificaciones de alumnos"
"""

print(intro)

regulares = 0
cantidad = 0
total_regulares = 0

calificaciones = input("Desea analizar calificaciones? Responda Si o No: ").lower().strip()

while calificaciones == "si":
    alumno = input("ingrese el nombre del alumno: ")
    calificacion = int(input("ingrese su calificacion: "))

    if calificacion >= 4:
        print("Alumno regular")
        regulares += 1
        total_regulares += calificacion
    else:
        print("Alumno libre")
    
    cantidad += 1
    calificaciones = input("\nDesea analizar mas calificaciones? Responda Si o No: ").lower().strip()
else:
    print("\nA continuacion se muetran los resultados, muchas gracias\n")
    
print(f"Porcentaje de alumnos regulares, {(regulares*100)/cantidad} %")
print(f"Promedio de alumnos regulares, {total_regulares/regulares} %")


