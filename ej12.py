number = int(input("Enter a whole number: "))
print((number % 2) == 0) # Retorna true or false

# También se puede resolver con condicionales: 

# if number % 2 == 0:
#     print("True")
# else:
#     print("False")




# CÓDIGO EJEMPLO: Primero se calcularán los valores lógicos (True o False) de las dos comparaciones: a > 100 y a != 1000 (lo cual dependerá del número guardado en la variable a). A continuación, se utilizará la tabla de verdad de la operación AND para calcular el resultado.

# a = int(input("Enter an integer from 100 and up: "))
# print(a > 100  and  a != 1000)