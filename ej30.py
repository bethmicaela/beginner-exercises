phrase = input("Enter a phrase: ").lower()
character = input("enter the character to be replaced: ")
new = "" # Inicializo una cadena vacia, mediante una variable.

for i in phrase:
    if i == character:
        new = new + "*" # Si los elementos que se encuentran en frase son igual al caracter que pone el usuario, lo remplazo con un asterisco. Tener en cuenta que si pongo una frase en español con acento, el programa no lo tomará.
    else:
        new = new + i # Sino tengo esa letra, lo pongo tal cual es
print(new)



# frase = input("Frase:")
# caracter = input("Carácter:")
# nueva = ""
# for c in frase:
#     if c == caracter:
#         nueva = nueva + "*"
#     else:
#         nueva = nueva + c
# print(nueva)