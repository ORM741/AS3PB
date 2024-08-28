#programa para determinar cual es el numero primo 
n = int (input ("indique un numero "))

if n == 2 :
    print("numero primo")
elif (n % 2) != 0:
    print ("numero primo")
else :
    print ("numero natural")