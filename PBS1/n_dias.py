#programa que calcula el numero de dias entre dos fechas

def calcular_diferencia_dias(dia1, dia2):
    return abs(dia2 - dia1)
dia1 = int (input("Ingrese el primer día: "))
dia2 = int (input("Ingrese el segundo día: "))
dias_diferencia = calcular_diferencia_dias(dia1, dia2)

print(f"La diferencia entre {dia1} y {dia2} es: {dias_diferencia} días.")