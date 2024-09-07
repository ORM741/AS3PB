def mayor(nmayor):
   lista.sort(reverse=True)
   return lista[1]

l = str (input("Ingresa una lista de números separados por espacios: "))
lista = [int (l) for l in l.split()]
print(mayor(lista))