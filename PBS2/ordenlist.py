#programa que ordena los valores de una lista
n = str (input("Ingresa una lista de números separados por espacios: "))
lis_n = [int(n) for n in n.split()]
lis_n.sort()
print (lis_n)