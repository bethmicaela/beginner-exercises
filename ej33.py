intro = """
Ingrese numeros positivos e ingrese el numero cero para saber que numero es el mayor"""
print(intro)

bigger_number = -1

number = int(input("Ingrese numero positivo: "))

while number != 0: # Mientras numero sea distinto de cero
    if number > bigger_number: # Si el numero ingresado es mayor a mi variable mayor, eje
        bigger_number = number  # En la variable mayor voy a almacenar el numero mayor que ingreso el usuario
    number = int(input("Ingrese numero positivo: "))
print(f"El mayor numero ingresado es {bigger_number}")

# En cada vuelta del ciclo voy a evaluar si el numero ingresado que es guardado en la variable bigger_number es mayor a