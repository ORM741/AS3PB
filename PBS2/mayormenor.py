#programa que encuentra el numero mayor y el menor de una lista
n = str (input("Ingresa una lista de números separados por espacios: "))
lis_n = [int(n) for n in n.split()]
lis_n.sort()
min = lis_n[0]
lis_n.sort(reverse=True)
max = lis_n[0]
print ("el numero mayor es: ", max , "y el numero menor es: ", min)