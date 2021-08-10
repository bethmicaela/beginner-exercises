text = input("Enter a phrase: ")
first_character = text[0]
print("The first character of the phrase is:", first_character)
spaces = text.replace(" ", "")
count = len(spaces)
print("Enter a minor number to", count)
index = int(input(""))
print("The character in that position is: ", spaces[index])



# CODIGO DE EJEMPLO: La instrucción print imprimirá True, ya que el valor contenido en a es diferente del valor contenido en b

# a=10
# b=4
# print(a != b)