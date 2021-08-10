intro = """
Enter two word to know if it is higher or lower\n"""

print(intro)

word_one = input()
word_two = input()

if word_one.isalpha() and word_two.isalpha():
    if word_one < word_two:
        print(word_one, "is less than", word_two)
    elif word_one > word_two:
        print(word_one, "is greater than", word_two)
else:
    print("Write only letters without spaces")

# La funcion isalpha (MÉTODO) nos dice si una cadena tiene sólo carácteres del alfabeto, no importa la longitud de la cadena: validará todos los carácteres, incluso los espacios vacios(los cuáles no entran en el alfabeto y retornará False)