def mcd(a, b):
    while b != 0:
        a , b = b , a % b
    return a

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print(f"El MCD de {num1} y {num2} es: {mcd(num1, num2)}")