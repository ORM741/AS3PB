#programa que genere las tablas de mutiplicar de un numero dado
n = int (input("Ingrese un numero: "))
for i in range (1,11):
    tabla = n*i 
    print (n ,"x", i ,"=", tabla )