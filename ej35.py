# cantidad = 0
# n = int(input("Número:"))
# while n > 0 and n % 10 != 0:
#     cantidad += 1
#     n = int(input("Número:"))


# CODIGO EJEMPLO: Una condición tiene que ser un valor lógico, sin importar qué tipo de operación se deba realizar para obtenerlo. En el ejemplo anterior, se ejecutará el bloque mientras los números ingresados sean positivos (mayores que 0) y no sean múltiplos de 10. Cuando el usuario ingrese un número que incumpla alguna de las dos condiciones (un número negativo ó un número múltiplo de 10) el bloque deja de ejecutarse.



string = "" # Se me va a ir sumando cada caracter en esta cadena vacia
letra_a = 0
caracter = input("Escribí un caracter: ").strip()

while (len(caracter)) == 1 and caracter != "0":
    string += caracter
    if caracter == "a":
        letra_a += 1
    caracter = input("Escribí un caracter: ").strip()

print(f"El string completo es: {string}")
print(f"Porcentaje de letras 'a' es: {(letra_a * 100) / len(string)}") # Multiplico a la cantidad de letras 'a' que hay por 100 y lo divido por la cantidad de letras que ingreso el usuario 
