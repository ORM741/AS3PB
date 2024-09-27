i=1
sum_pre = 0
while True:
    producto = input("Ingrese un nombre del producto (o escriba 'salir' para terminar): ").lower()
    if producto == 'salir':
        break
    cantidad = input("ingrese la cantidad que desea")
    precio = input("ingrese el precio del producto")
    tupla[i] = (producto,cantidad,precio)
    sum_total = cantidad * precio
    sum_pre = sum_pre + sum_total
    i =+ 1
for j in ragne (1,(i+1)):
    print(tupla[j],"el total es",sum_pre)