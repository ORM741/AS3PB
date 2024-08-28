#programa para saber si un año es bisiesto

año = int (input ("indique el año "))

if (año % 4) == 0 and (año % 100) != 0:
    print ("año bisiesto")
elif (año % 100) == 0 and (año % 400) == 0:
    print ("año bisiesto")
else :
    print ("año no bisiesto")