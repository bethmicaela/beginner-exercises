user_number = int(input("number: "))

for i in range(1, user_number+1):
    if user_number % i == 0:  # Si {user_number} modulo {i range(1 a user_number+1)}, su resto resulta de cero, imprimo esos numeros:
        print(i)




# CODIGO EJEMPLO : La repetición for utiliza el operador in para recorrer una secuencia. Este operador retorna un valor lógico: True si el primer operando está contenido en el segundo, False si no es así. Es posible utilizar el operador in de forma independiente, para saber, por ejemplo, si un string está contenido dentro de otro: "a" in "hola" dará como resultado True porque el string “a” está dentro de “hola”. Asimismo, se puede negar el valor lógico obtenido por la operación utilizando not: "a" not in "hola" dará como resultado Fase porque no es verdad que el string “a” no esté dentro de “hola”.

# for x in "hola":
#     print(x)