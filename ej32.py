# suma = 0
# numero = int(input("Número:"))
# while numero != 0:
#     suma = suma + numero
#     numero = int(input("Número:"))
# print("Suma de todos los números ingresados:", suma)

# CODIGO EJEMPLO: Una repetición while necesita una condición (en este ejemplo: numero != 0), que es un valor lógico para saber si continúa repitiendo el bloque o no. Si el valor es True, se ejecuta el bloque correspondiente al while; si es False, no se ejecuta y continúa el programa con la instrucción siguiente al bloque. El código del ejemplo permite ingresar números y cada uno se acumula sumándolo en la variable suma, para luego pedir al usuario un nuevo número. Cuando se ingresa el 0, el bloque del while no se ejecuta y pasa directamente a la siguiente instrucción, que en este caso es un print que muestra la suma de todos los números ingresados.



# --------------------------------------------------

# numero=int(input("Número:"))
# while numero != 0:  # BUCLE INFINITO
#     print("Tu número es:", numero)


# CODIGO EJEMPLO: La repetición anterior contiene un error y es que, si el número ingresado por el usuario es diferente de cero, se producirá un bucle infinito que mostrará “Tu número es: [número del usuario]” infinitas veces, sin continuar con el resto del programa. Esto es así porque, en las repeticiones while, una vez ejecutado el bloque, se vuelve a evaluar la condición y, si es True, vuelve a ejecutar el bloque y nuevamente a evaluar la condición. En el caso de ingresar un valor distinto de 0 en la variable numero, si no se permite cambiar ese valor la condición siempre comparará el mismo número con el 0 y siempre será True, por lo que nunca dejará de repetir la instrucción print dentro del bloque. Para evitarlo, es necesario permitir cambiar el valor de la variable numero:

# numero = int(input("Número:"))
# while numero != 0: # Imprimo solo el primer numero que ingresa el usuario, si es distinto de cero. 
#     print("Tu número es:", numero)
#     numero = int(input("Número:"))



# --------------------------------------------------



sumatoria = 0
monto = int(input("Ingrese el monto de una venta: "))

while monto != 0:
    sumatoria += monto
    monto = int(input("Ingrese el monto de una venta: "))

    if monto < 0:
        print("Ingrese un monto valido por favor")
        
print(f"El monto de las ventas es: {sumatoria} pesos")
