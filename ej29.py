promedio = 0
sumatoria = 0
cantidad = 0

for i in range(6):
    number = int(input("Number: "))

    if number > 0:
        promedio += number
        cantidad += 1
    else:
        sumatoria += number
print(f"Sumatoria de los negativos, {sumatoria}")

if cantidad != 0:
    print(f"El promedio de los positivos es, {promedio / cantidad} ")
