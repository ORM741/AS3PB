#programa que calcule el factorial de un numero
n = int (input ("indique el numero al que obtener su factorial "))
i = 1
while n > 1:
    i = i * n
    n = n - 1
print (i)