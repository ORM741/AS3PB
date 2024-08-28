#programa para determinar el tipo de triangulo

l1 = int (input("indique el lado 1 del triangulo "))
l2 = int (input("indique el lado 2 del triangulo "))
l3 = int (input("indique el lado 3 del triangulo "))

if l1 == l2 == l3:
    print ("triangulo equilatero")
elif l1 == l2 != l3 or l1 == l3 != l2 or l1 != l3 == l2:
    print ("triangulo isoceles")
else:
    print ("triangulo escaleno")