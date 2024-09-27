diccionario = {}
for i in range (1,8):
    dia = i
    temp = int(input(f"Ingrese la temperatura del dia '{dia}': "))
    diccionario[dia] = temp

suma = sum(diccionario.values())
promedio = suma / 7

print(f"El promedio de las temperaturas es: {promedio}")