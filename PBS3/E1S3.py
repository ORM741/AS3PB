def datos(nombre, edad=18):
    print ("hola" , nombre , "tienes", edad , "años")
edad = input ("indique su edad: ")
if edad == "":
    edad = 18
nombre = input ("indique su nombre: ")

datos(nombre, edad)