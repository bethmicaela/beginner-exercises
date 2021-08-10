phrase = input("Enter a phrase: ").lower()
vowels = ["a", "e", "i", "o", "u"]
count = 0


for i in phrase:
    if i in vowels:
        count = count+1
print("Vowels:", count)


