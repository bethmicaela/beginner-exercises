def mifuncion(value, maximum):
    if value < 10:
        return "0" + str(value)
    elif value <= maximum:
        return value
    else:
        return "error"
    

def run():
    birthday_day = int(input("Enter your birthday date in format DD: "))
    birthday_month = int(input("Enter your birthday date in format MM: "))
    birthday_year = int(input("Enter your birthday date in format YYYY: "))

    print(mifuncion(birthday_day, 31), mifuncion(birthday_month, 12), birthday_year)


if __name__ == "__main__":
    run()


# Otra forma de resolverlo: (confusa)

# fecha = int(input("Fecha en formato DDMMAAAA:"))
# año = fecha % 10000
# dia = fecha // 1000000
# mes = (fecha // 10000) % 100
# print(dia, "/", mes, "/", año)