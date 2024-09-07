def calcular(lis_n):
    norden = sorted(lis_n)
    a = len(norden)
    if a % 2 == 1:
        mediana = norden[a // 2]
    else:
        # Si es par, la mediana es el promedio de los dos números centrales
        mediana = (norden[a // 2 - 1] + norden[a // 2]) / 2
    return mediana

n = str (input("Ingresa una lista de números separados por espacios: "))
lis_n = [int (n) for n in n.split()]

print ("la mediana es" , calcular(lis_n))