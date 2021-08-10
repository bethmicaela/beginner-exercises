intro = """
Enter the names of two people to see if they start or end with the same letter.\n"""

print(intro)

name_one = input("Enter a name: ")
name_two = input("Enter other name: ")

if name_one[0] == name_two[0]: 
     print("The initial letters are the same")
elif name_one[-1] == name_two[-1] :
    print("The final letters are the same")
else:
    print("The initial and final letters do not match")