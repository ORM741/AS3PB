#calculo de impuesto sobre una compra

monto = float (input("indique el monto de la compra "))
tasa = float (input("indique el porcentaje de impuestos"))
impuesto = tasa/100 * monto
total = monto + impuesto

print ("el total a pagar es ", total)