# Fibonacci en incremento con limite predeterminado 

# var_1 = 0
# var_2 = 1
# print(var_1)
# print(var_2)

# for i in range(8):
#     var_3 = var_1 + var_2
#     print(var_3) 
#     var_1 = var_2
#     var_2 = var_3



# Fibonacci al revez con limite predeterminado

# var_1 = 55
# var_2 = 34
# print(var_1)
# print(var_2)

# for i in range(8, -1, -1):
#     var_3 = var_1 - var_2
#     print(var_3) 
#     var_1 = var_2
#     var_2 = var_3



#  Fibonacci con limite del usuario y con eleccion de incremento o al revez:

def fibonacci(maximo):
    var_1 = 0
    var_2 = 1
    print(var_1)
    print(var_2)

    for i in range(maximo):
        var_3 = var_1 + var_2
        print(var_3) 
        var_1 = var_2
        var_2 = var_3

def fibonacci_reverse(maximo):
    var_1 = maximo
    var_2 = maximo # FALTA EVALUAR PARA QUE FUNCIONE!!!!!
    print(var_1)
    print(var_2)

    for i in range(maximo, -1, -1):
        var_3 = var_1 - var_2
        print(var_3) 
        var_1 = var_2
        var_2 = var_3


def run():
    option = input("Enter option 1 or 2:")
    max = int(input("Enter a maximum number to know the Fibonacci sequence, from 1 to 15: "))

    if option == "1":
        fibonacci(max)
    elif option == "2" :
        fibonacci_reverse(max)
    else:
        print("Nada")
    
    if max < 0 or max == 0 or max >= 16:
        print("Enter correct numbers please")


if __name__=="__main__":
    run()