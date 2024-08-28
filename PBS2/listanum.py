#suma de elementos en una lista
n = str (input("Ingresa una lista de números separados por espacios: "))
lis_n = [int(n) for n in n.split()]
suma = sum(lis_n)
print ("el total es ",suma)