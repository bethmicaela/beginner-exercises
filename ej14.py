intro = """
Enter a phrase to count the number of letters it has and find out if it is odd or even\n"""

print(intro)

phrase = input()
spaces = phrase.replace(" ", "")  # Saco los espacios basura para contar solo las letras
count = len(spaces)
if count % 2 == 0:  
    print(count, "The number of characters is the result of even numbers") # Pares
else:
    print(count, "The number of characters is the result of odd numbers") # Impares



# CÓDIGO EJEMPLO: Ambas comparaciones arrojan True porque el string “animal” es menor que “piedra” y el string “bailar” es menor que “bebida”. El orden está dado por cómo aparecen las letras en el alfabeto. En el caso de “animal” y “piedra”, la “a” es menor que la “p”. En el caso de “bailar” y “bebida”, como la primera letra es la misma se evalúa la segunda, y en este caso “a” es menor que “e”.

# print("animal" < "piedra")
# print("bailar" < "bebida")