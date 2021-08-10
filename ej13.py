intro = """
Welcome to online ticket sales to travel to Bariloche 
The price of each ticket is $1200\n"""

print(intro)

age = int(input("Enter your age: "))
if age < 18:
    print("Sorry, you are a minor and cannot purchase these tickets")
elif age >= 18:
    tickets = int(input("Enter the number of tickets you want: ")) 
    print("The total price is: ", 1200 * tickets)
    print("Thanks for your purchase")
else:
    print("Please enter valid numbers")
    
    