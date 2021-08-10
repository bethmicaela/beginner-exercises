number_one = int(input("Number one: "))
number_two = int(input("Number two: "))
number_three = int(input("Number three: "))

if number_one > number_two and number_one > number_three:
    print(f"{number_one} it's bigger than {number_two} and {number_three}")
elif number_two > number_one and number_two > number_three:
    print(f"{number_two} it's bigger than {number_one} and {number_three}")
else:
    print(f"{number_three} it's bigger than {number_one} and {number_two}")