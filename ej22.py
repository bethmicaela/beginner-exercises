anio = int(input("Enter a year to find out if it is a leap year: "))

if anio % 4 == 0:  # Divisible por 4
    if anio % 100 != 0 or anio % 400 == 0: # NO divisible por 100 or Divisible por 400
        print("It's leap year")
    else:
        print("It's not leap year")
else:
    print("It's not leap year")
    