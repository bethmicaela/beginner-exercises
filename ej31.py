user_phrase = input("Enter a phrase to see it backwards: ")
# slice = user_phrase[::-1]
# print(slice)

# for i in user_phrase:
#     for i in range(-1, 0, -1):
#         print(i)

new = ""

count = len(user_phrase)-1

while count >= 0:
    new = new + user_phrase[count]
    count -= 1 # No entiendo el funcionamiento
print(new)
