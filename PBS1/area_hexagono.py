#programa para calcular el area de un hexagono

L = int (input ("indique un lado del hexagono "))
area = round ((3 * (3**(1/2))/2) * L**2 , 3)

print ("el area del hexagono es ", area)