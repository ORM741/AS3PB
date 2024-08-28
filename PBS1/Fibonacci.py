# serie de fibonacci

a = 0 
b = 1 
n = int (input ("indique cuentas veces se realiza el proseso (numero entero) "))

for i in range (0,n):
    print (a)
    c = a + b
    a = b
    b = c