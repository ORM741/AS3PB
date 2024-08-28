#programa para calcular el interes simple

capital = float (input ("indique el capital inical "))
tasa = float (input ("indique la  tasa de interes anual "))
años = float (input ("indique el numero de años "))
interes = capital * tasa * años
monto_total = capital + interes

print ("el momto total es ", monto_total)