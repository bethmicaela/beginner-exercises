string_one = input("Enter a word: ")
string_two = input("Enter other word: ")
print(string_one + " " + string_two)


# CÓDIGO EJEMPLO: El operador [ ] (corchetes) permite obtener un carácter a partir de un string. La posición del carácter se indica entre los corchetes, ya sea ingresando directamente el número, con una variable que contenga un número o con una operación que de como resultado un número. Siempre, el primer carácter de un string estará ubicado en la posición 0.

# frase = "Estoy programando"
# print(frase[0])
# i = 6  # Variable que guarda la letra ubicada en la posicion 6
# print(frase[i])  # De la frase imprimo la variable i donde tengo guardada la letra posicionada en 6 



# CÓDIGO EJEMPLO 2: Mediante len() podemos obtener la cantidad de caracteres que contiene un string. Este valor siempre será un número entero (tipo int) y puede guardarse en una variable, imprimirse, usarse en una operación aritmética, etc.

# frase = "Estoy programando"
# print(len(frase)) # Cuento los caracteres (letras): 17
# ultimo_caracter = frase[len(frase)-1] 
# print(ultimo_caracter) # Muestra el último caracter